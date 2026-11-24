"""Deterministic validators, Google Sites embed bundler, and run logger."""

from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from .prompts import PROJECT_ROOT

SCHEMA_PATH = PROJECT_ROOT / "schema.json"
LOGS_PATH = PROJECT_ROOT / "logs" / "runs.jsonl"


def load_schema() -> dict[str, Any]:
    """Load the official content.json JSON Schema."""
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _check_balanced_delimiters(code: str) -> str | None:
    """Check balanced braces and parentheses outside string/char literals."""
    cleaned = re.sub(r'"(?:\\.|[^"\\])*"', '""', code)
    cleaned = re.sub(r"'(?:\\.|[^'\\])*'", "''", cleaned)
    if cleaned.count("{") != cleaned.count("}"):
        return "chaves '{' e '}' desbalanceadas"
    if cleaned.count("(") != cleaned.count(")"):
        return "parenteses '(' e ')' desbalanceados"
    return None


def validate_content_data(data: dict[str, Any]) -> list[str]:
    """Validate content.json against schema.json and semantic rules."""
    errors: list[str] = []
    validator = Draft202012Validator(load_schema())
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in err.path) or "root"
        errors.append(f"Schema ({loc}): {err.message}")

    for idx, q in enumerate(data.get("certo_errado", []), start=1):
        steps = q.get("explicacao_passos", [])
        if len(steps) < 2:
            errors.append(f"Certo/Errado #{idx}: precisa de ao menos 2 passos numerados.")

    for idx, sec in enumerate(data.get("secoes_estudo", []), start=1):
        code = sec.get("codigo_c", "")
        if not any(tok in code for tok in (";", "{", "#include", "struct", "*")):
            errors.append(f"Secao #{idx}: codigo_c nao parece codigo C valido.")
        delim_err = _check_balanced_delimiters(code)
        if delim_err:
            errors.append(f"Secao #{idx} codigo_c: {delim_err}.")

    for idx, sim in enumerate(data.get("simulado", []), start=1):
        opt_code = sim.get("codigo_opcional", "")
        if opt_code.strip():
            delim_err = _check_balanced_delimiters(opt_code)
            if delim_err:
                errors.append(f"Simulado #{idx} codigo_opcional: {delim_err}.")

    return errors


def build_google_sites_embed(output_dir: Path) -> Path:
    """Bundle index.html + styles.css + app.js + content.json into a single iframe-safe HTML file."""
    html_text = (output_dir / "index.html").read_text(encoding="utf-8")
    css_text = (output_dir / "styles.css").read_text(encoding="utf-8")
    js_text = (output_dir / "app.js").read_text(encoding="utf-8")
    content_text = (output_dir / "content.json").read_text(encoding="utf-8")

    # Inline stylesheet
    bundled = re.sub(
        r'<link\s+rel="stylesheet"\s+href="styles\.css"\s*/?>',
        lambda _: f"<style>\n{css_text}\n</style>",
        html_text,
    )
    # Inject content JSON fallback + inline script
    data_script = f"<script>\nwindow.__STUDY_DATA__ = {content_text};\n</script>"
    bundled = re.sub(
        r'<script\s+src="app\.js"\s*></script>',
        lambda _: f"{data_script}\n<script>\n{js_text}\n</script>",
        bundled,
    )

    embed_path = output_dir / "embed-google-sites.html"
    embed_path.write_text(bundled, encoding="utf-8")
    return embed_path


def validate_output_bundle(output_dir: Path) -> dict[str, Any]:
    """Check all required node artifacts in an output folder and score structural completeness."""
    required_files = [
        "briefing.md",
        "dossie.md",
        "content.json",
        "index.html",
        "styles.css",
        "app.js",
    ]
    missing = [name for name in required_files if not (output_dir / name).is_file()]
    errors: list[str] = [f"Arquivo ausente: {name}" for name in missing]

    content_data: dict[str, Any] = {}
    content_path = output_dir / "content.json"
    if content_path.is_file():
        try:
            content_data = json.loads(content_path.read_text(encoding="utf-8"))
            errors.extend(validate_content_data(content_data))
        except json.JSONDecodeError as exc:
            errors.append(f"content.json invalido: {exc}")

    dossie_path = output_dir / "dossie.md"
    if dossie_path.is_file():
        dossie_text = dossie_path.read_text(encoding="utf-8")
        urls = re.findall(r"https?://[^\s\)\]>\"']+", dossie_text)
        if len(urls) < 3:
            errors.append(f"dossie.md tem apenas {len(urls)} URL(s); minimo esperado = 3.")

    embed_path: str | None = None
    if not missing and not errors:
        embed_file = build_google_sites_embed(output_dir)
        embed_path = str(embed_file)

    return {
        "ok": len(errors) == 0,
        "output_dir": str(output_dir),
        "missing_files": missing,
        "errors": errors,
        "gcc_available": shutil.which("gcc") is not None,
        "counts": {
            "secoes_estudo": len(content_data.get("secoes_estudo", [])),
            "certo_errado": len(content_data.get("certo_errado", [])),
            "simulado": len(content_data.get("simulado", [])),
            "referencias": len(content_data.get("referencias", [])),
        },
        "embed_google_sites": embed_path,
    }


def append_run_log(record: dict[str, Any]) -> Path:
    """Append a structured run record to logs/runs.jsonl."""
    LOGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **record,
    }
    with LOGS_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return LOGS_PATH
