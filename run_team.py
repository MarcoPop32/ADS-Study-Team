"""Single-command entrypoint for the ADS Study Team (Google ADK 2.x)."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import google.adk as adk  # noqa: E402
from google.adk.runners import Runner  # noqa: E402
from google.adk.sessions.in_memory_session_service import InMemorySessionService  # noqa: E402
from google.genai import types  # noqa: E402

from ads_team.tools import validate_output_bundle  # noqa: E402
from ads_team.workflow import MODEL_ID, build_app, describe_graph  # noqa: E402


async def run_live_topic(topic: str) -> None:
    """Execute the ADK 2.x graph workflow via Runner using GEMINI_API_KEY/GOOGLE_API_KEY."""
    if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
        raise SystemExit(
            "Erro: defina a variavel de ambiente GEMINI_API_KEY (ou GOOGLE_API_KEY) antes de rodar.\n"
            "Exemplo PowerShell:\n"
            "  $env:GEMINI_API_KEY = 'SUA_CHAVE_AQUI'\n"
            "  .\\.venv\\Scripts\\python.exe run_team.py --topic \"Ponteiros, Struct e Arquivo em C\""
        )

    app = build_app()
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=app.name, user_id="ads_student")
    runner = Runner(app=app, session_service=session_service)

    print(f"Iniciando ADK {adk.version.__version__} | Modelo: {MODEL_ID} | Tema: {topic}")
    user_msg = types.Content(role="user", parts=[types.Part.from_text(text=topic)])
    async for event in runner.run_async(
        user_id="ads_student",
        session_id=session.id,
        new_message=user_msg,
    ):
        author = getattr(event, "author", "system")
        print(f"[{author}] -> {type(event).__name__}")
        if getattr(event, "content", None):
            print(event.content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Time de Agentes ADS no Google ADK 2.x")
    parser.add_argument("--validate-graph", action="store_true", help="Compila e valida o grafo ADK 2.x")
    parser.add_argument("--validate-output", type=Path, help="Valida um pacote gerado em outputs/<pasta>")
    parser.add_argument("--topic", type=str, help="Executa o grafo ADK 2.x para um tema de aula")
    args = parser.parse_args()

    if args.validate_graph:
        info = describe_graph()
        info["adk_version"] = adk.version.__version__
        print(json.dumps(info, ensure_ascii=False, indent=2))
        return 0

    if args.validate_output:
        report = validate_output_bundle(args.validate_output)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["ok"] else 1

    if args.topic:
        asyncio.run(run_live_topic(args.topic))
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
