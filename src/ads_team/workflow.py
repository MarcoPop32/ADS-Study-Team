"""Google ADK 2.x graph workflow for the ADS Study Team (no deprecated agents)."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field

from google.adk import Agent, Workflow
from google.adk.apps.app import App, ResumabilityConfig
from google.adk.events import RequestInput
from google.adk.workflow import JoinNode, START, node

from .prompts import build_instruction, read_memory, read_schema_text
from .tools import append_run_log, validate_content_data

MODEL_ID = os.environ.get("ADK_MODEL", "gemini-4-neon")
MAX_QUALITY_ROUNDS = 2


class TeamWorkflowState(BaseModel):
    """Shared state across the ADS Study Team graph."""

    topic: str = ""
    round_number: int = 1
    max_rounds: int = MAX_QUALITY_ROUNDS
    briefing: str = ""
    dossie: str = ""
    content_json_text: str = ""
    ui_bundle_text: str = ""
    audit_status: Literal["APROVADO", "REPROVADO"] = "REPROVADO"
    audit_score: int = 0
    weakest_agent: Literal["pesquisador", "conteudista", "construtor", "none"] = "none"
    fix_instructions: str = ""
    human_decision: str = ""


def _create_agents() -> dict[str, Agent]:
    """Instantiate all ADK LLM Agents using MODEL_ID and Skill prompts."""
    memory_text = read_memory()
    schema_text = read_schema_text()

    lead_agent = Agent(
        name="lead",
        model=MODEL_ID,
        description="Coordenador do time ADS; cria briefing, le memoria e consolida pacote.",
        instruction=build_instruction(
            "ads-lead",
            f"MEMORIA DO TIME (leia antes de agir):\n{memory_text}",
        ),
        output_key="briefing",
    )

    pesquisador_agent = Agent(
        name="pesquisador",
        model=MODEL_ID,
        description="Curador de referencias tecnicas de ADS.",
        instruction=build_instruction("ads-pesquisador"),
        output_key="dossie",
    )

    conteudista_agent = Agent(
        name="conteudista",
        model=MODEL_ID,
        description="Escritor didatico e gerador de Certo/Errado + Simulado em JSON.",
        instruction=build_instruction(
            "ads-conteudista",
            f"SCHEMA OFICIAL (content.json deve obedecer 100%):\n{schema_text}",
        ),
        output_key="content_json_text",
    )

    construtor_agent = Agent(
        name="construtor",
        model=MODEL_ID,
        description="Construtor de interface interativa HTML/CSS/JS para GitHub Pages e Google Sites.",
        instruction=build_instruction(
            "ads-construtor",
            f"CONTRATO DE DADOS QUE A UI CONSOME:\n{schema_text}",
        ),
        output_key="ui_bundle_text",
    )

    verificador_agent = Agent(
        name="verificador",
        model=MODEL_ID,
        description="Auditor de qualidade; pontua 0-100 e aponta correcoes cirurgicas.",
        instruction=build_instruction(
            "ads-verificador",
            (
                "Responda SEMPRE em JSON puro com as chaves: "
                "status ('APROVADO' ou 'REPROVADO'), nota (0-100), "
                "agente_responsavel ('pesquisador'|'conteudista'|'construtor'|'none'), "
                "correcoes (lista de strings)."
            ),
        ),
    )

    return {
        "lead": lead_agent,
        "pesquisador": pesquisador_agent,
        "conteudista": conteudista_agent,
        "construtor": construtor_agent,
        "verificador": verificador_agent,
    }


def _extract_json_block(text: str) -> dict[str, Any] | None:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        cleaned = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    try:
        parsed = json.loads(cleaned)
        return parsed if isinstance(parsed, dict) else None
    except Exception:
        return None


def build_workflow() -> Workflow:
    """Build the ADK 2.x graph workflow with fan-out, JoinNode, quality loop (cap 2), and HITL pause."""
    agents = _create_agents()
    join_pacote = JoinNode(
        name="join_pacote",
        description="Sincroniza os ramos paralelos Conteudista e Construtor antes da auditoria.",
    )

    @node
    def quality_router(node_input: Any, ctx: Any) -> str:
        """Route to human approval or back to the specific agent needing fixes (max 2 rounds)."""
        raw_text = str(node_input or "")
        audit = _extract_json_block(raw_text) or {}
        nota = int(audit.get("nota", 0) or 0)
        status = str(audit.get("status", "REPROVADO")).upper()
        responsavel = str(audit.get("agente_responsavel", "conteudista")).lower()

        # Deterministic schema sanity check when JSON content exists in state
        content_raw = ctx.state.get("content_json_text", "") if hasattr(ctx, "state") else ""
        if content_raw:
            parsed_content = _extract_json_block(str(content_raw))
            if parsed_content is None or validate_content_data(parsed_content):
                status = "REPROVADO"
                responsavel = "conteudista"

        current_round = int(ctx.state.get("round_number", 1)) if hasattr(ctx, "state") else 1
        if status == "APROVADO" and nota >= 85:
            return "aprovado"
        if current_round >= MAX_QUALITY_ROUNDS:
            return "limite_rodadas"

        if hasattr(ctx, "state"):
            ctx.state["round_number"] = current_round + 1
            ctx.state["audit_score"] = nota
            ctx.state["weakest_agent"] = responsavel

        if responsavel in {"pesquisador", "conteudista", "construtor"}:
            return f"fix_{responsavel}"
        return "fix_conteudista"

    def aprovacao_humana(node_input: Any):
        """Human-in-the-loop pause before exporting/publishing."""
        yield RequestInput(
            message=(
                "Pacote pronto para revisao humana. Digite 'aprovado' para finalizar "
                "e registrar no log, ou informe ajustes desejados."
            ),
            payload={"audit_summary": str(node_input)[:1500]},
        )

    def registrar_execucao(node_input: Any, ctx: Any) -> dict[str, Any]:
        """Persist final run summary to logs/runs.jsonl after human decision."""
        state = getattr(ctx, "state", {}) if ctx else {}
        record = {
            "topic": state.get("topic", "CLI ADK Run"),
            "mode": "adk-python-graph",
            "model": MODEL_ID,
            "rounds": state.get("round_number", 1),
            "score": state.get("audit_score", 0),
            "weakest_agent": state.get("weakest_agent", "none"),
            "human_decision": str(node_input),
        }
        log_file = append_run_log(record)
        return {"logged_to": str(log_file), **record}

    return Workflow(
        name="ads_study_team_graph",
        description="Grafo ADS: Lead -> Pesquisador -> [Conteudista || Construtor] -> Join -> Verificador (max 2x) -> Aprovacao Humana.",
        state_schema=TeamWorkflowState,
        edges=[
            (START, agents["lead"]),
            (agents["lead"], agents["pesquisador"]),
            # Parallel fan-out
            (agents["pesquisador"], agents["conteudista"]),
            (agents["pesquisador"], agents["construtor"]),
            # Join barrier
            (agents["conteudista"], join_pacote),
            (agents["construtor"], join_pacote),
            # Checker + conditional loop (max 2 rounds)
            (join_pacote, agents["verificador"]),
            (agents["verificador"], quality_router),
            (
                quality_router,
                {
                    "aprovado": aprovacao_humana,
                    "limite_rodadas": aprovacao_humana,
                    "fix_pesquisador": agents["pesquisador"],
                    "fix_conteudista": agents["conteudista"],
                    "fix_construtor": agents["construtor"],
                },
            ),
            # Post-HITL logging
            (aprovacao_humana, registrar_execucao),
        ],
    )


def build_app() -> App:
    """Wrap the workflow in a resumable ADK 2.x App for HITL pause/resume."""
    workflow = build_workflow()
    return App(
        name="ads_study_team_app",
        root_agent=workflow,
        resumability_config=ResumabilityConfig(is_resumable=True),
    )


def describe_graph() -> dict[str, Any]:
    """Return structured metadata about the compiled ADK 2.x graph."""
    wf = build_workflow()

    def _fmt(item: Any) -> Any:
        if isinstance(item, dict):
            return {k: _fmt(v) for k, v in item.items()}
        if isinstance(item, tuple):
            return [_fmt(x) for x in item]
        return getattr(item, "name", str(item))

    formatted_edges = []
    for edge in wf.edges:
        if hasattr(edge, "from_node") and hasattr(edge, "to_node"):
            formatted_edges.append(
                {
                    "from": _fmt(edge.from_node),
                    "to": _fmt(edge.to_node),
                    "route": edge.route,
                }
            )
        elif isinstance(edge, tuple) and len(edge) >= 2:
            formatted_edges.append({"from": _fmt(edge[0]), "to": _fmt(edge[1])})
        else:
            formatted_edges.append({"edge": _fmt(edge)})

    return {
        "workflow_name": wf.name,
        "model_id": MODEL_ID,
        "max_quality_rounds": MAX_QUALITY_ROUNDS,
        "edges_count": len(wf.edges),
        "edges": formatted_edges,
    }
