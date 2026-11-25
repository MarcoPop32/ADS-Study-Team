"""Master builder for ADS Study Team v4.0 — Guia Mestre Interativo em C."""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILDER_DIR = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(BUILDER_DIR))

import spec
import mod_ponteiros
import mod_structs
import mod_arquivos
import ex_ponteiros
import ex_structs
import ex_arquivos
import simulados_atp
import ui_template


def build_data() -> dict:
    """Assemble and validate the full DATA object for the v4.0 interactive web app."""
    all_mcqs = (
        list(ex_ponteiros.MCQ_PONTEIROS)
        + list(ex_structs.MCQ_STRUCTS)
        + list(ex_arquivos.MCQ_ARQUIVOS)
    )
    all_ce = (
        list(ex_ponteiros.CE_PONTEIROS)
        + list(ex_structs.CE_STRUCTS)
        + list(ex_arquivos.CE_ARQUIVOS)
    )
    all_classical = (
        list(ex_ponteiros.CLASSICAL_PONTEIROS)
        + list(ex_structs.CLASSICAL_STRUCTS)
        + list(ex_arquivos.CLASSICAL_ARQUIVOS)
    )

    payload = {
        "ponteiros": list(mod_ponteiros.TOPICS_PONTEIROS),
        "structs": list(mod_structs.TOPICS_STRUCTS),
        "arquivos": list(mod_arquivos.TOPICS_ARQUIVOS),
        "categoryExercises": {
            "ponteiros": list(ex_ponteiros.MCQ_PONTEIROS),
            "structs": list(ex_structs.MCQ_STRUCTS),
            "arquivos": list(ex_arquivos.MCQ_ARQUIVOS),
        },
        "certoErrado": all_ce,
        "classical": all_classical,
        "simulados": list(simulados_atp.SIMULADOS),
        "cheatsheet": list(simulados_atp.CHEATSHEET_DATA),
        # Also provide flat views for validator
        "topicsPonteiros": list(mod_ponteiros.TOPICS_PONTEIROS),
        "topicsStructs": list(mod_structs.TOPICS_STRUCTS),
        "topicsArquivos": list(mod_arquivos.TOPICS_ARQUIVOS),
        "mcqs": all_mcqs,
    }

    errors = spec.validate_all(payload)
    if errors:
        raise ValueError(f"Validation failed ({len(errors)} errors):\n" + "\n".join(errors[:25]))

    # Remove duplicate validation-only keys before embedding in HTML
    for k in ("topicsPonteiros", "topicsStructs", "topicsArquivos", "mcqs"):
        payload.pop(k, None)
    return payload


def main() -> int:
    data = build_data()
    # Escape '</script>' safely inside embedded JSON
    data_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = ui_template.render_html(data_json)

    out_dir = ROOT / "outputs" / "v4-guia-mestre-ponteiros-structs-arquivos"
    out_dir.mkdir(parents=True, exist_ok=True)
    docs_dir = ROOT / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    targets = [
        out_dir / "index.html",
        docs_dir / "index.html",
        docs_dir / "embed-google-sites.html",
    ]
    for path in targets:
        path.write_text(html, encoding="utf-8")
        print(f"Wrote {path} ({len(html):,} chars)")

    n_ptr = len(data["ponteiros"])
    n_strc = len(data["structs"])
    n_arq = len(data["arquivos"])
    n_mcq = sum(len(v) for v in data["categoryExercises"].values())
    n_ce = len(data["certoErrado"])
    n_cl = len(data["classical"])
    n_sim = len(data["simulados"])
    print(
        f"SUMMARY OK: topics={n_ptr}+{n_strc}+{n_arq}={n_ptr+n_strc+n_arq}, "
        f"mcq={n_mcq}, ce={n_ce}, classical={n_cl}, simulados={n_sim}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
