"""Validation specification and schema checks for ADS Study Team v4.0."""
from __future__ import annotations

import re
from typing import Any


EXPECTED_COUNTS = {
    "topics_ponteiros": 18,
    "topics_structs": 18,
    "topics_arquivos": 17,
    "mcq_per_cat": 30,
    "ce_per_cat": 10,
    "classical_per_cat": 2,
    "simulados": 3,
    "simulado_questions": 14,
    "cheatsheet_panels": 4,
}


def check_balanced_c_delimiters(code: str, label: str, errors: list[str]) -> None:
    """Verify balanced (), {}, [] in C code ignoring strings, chars, and comments."""
    if not isinstance(code, str):
        errors.append(f"{label}: code is not str")
        return
    stack: list[tuple[str, int]] = []
    pairs = {")": "(", "}": "{", "]": "["}
    i = 0
    n = len(code)
    line = 1
    while i < n:
        ch = code[i]
        if ch == "\n":
            line += 1
            i += 1
            continue
        if ch == "/" and i + 1 < n and code[i + 1] == "/":
            nl = code.find("\n", i)
            i = n if nl == -1 else nl
            continue
        if ch == "/" and i + 1 < n and code[i + 1] == "*":
            end = code.find("*/", i + 2)
            if end == -1:
                errors.append(f"{label}: unclosed block comment at line {line}")
                return
            line += code[i:end + 2].count("\n")
            i = end + 2
            continue
        if ch in ('"', "'"):
            quote = ch
            i += 1
            while i < n:
                if code[i] == "\\":
                    i += 2
                    continue
                if code[i] == quote:
                    i += 1
                    break
                if code[i] == "\n":
                    line += 1
                i += 1
            continue
        if ch in ("(", "{", "["):
            stack.append((ch, line))
        elif ch in pairs:
            if not stack or stack[-1][0] != pairs[ch]:
                errors.append(f"{label}: unmatched '{ch}' at line {line}")
                return
            stack.pop()
        i += 1
    if stack:
        ch, ln = stack[-1]
        errors.append(f"{label}: unclosed '{ch}' opened at line {ln}")


def _require_nonempty_str(obj: dict[str, Any], key: str, label: str, errors: list[str]) -> None:
    val = obj.get(key)
    if not isinstance(val, str) or not val.strip():
        errors.append(f"{label}: missing/empty string '{key}'")


def _validate_tracer(tracer: dict[str, Any], label: str, errors: list[str]) -> None:
    for key in ("id", "tabLabel", "badge", "title", "desc", "kind"):
        _require_nonempty_str(tracer, key, label, errors)
    kind = tracer.get("kind")
    if kind not in ("1d", "2d"):
        errors.append(f"{label}: tracer kind must be '1d' or '2d', got {kind!r}")
    code_lines = tracer.get("codeLines")
    if not isinstance(code_lines, list) or not code_lines:
        errors.append(f"{label}: codeLines must be non-empty list")
        code_lines = []
    steps = tracer.get("steps")
    if not isinstance(steps, list) or not steps:
        errors.append(f"{label}: steps must be non-empty list")
        return
    for idx, st in enumerate(steps):
        s_label = f"{label}.step[{idx}]"
        if not isinstance(st, dict):
            errors.append(f"{s_label}: step must be dict")
            continue
        ln = st.get("line")
        if not isinstance(ln, int) or (code_lines and not (0 <= ln < len(code_lines))):
            errors.append(f"{s_label}: invalid line index {ln} for {len(code_lines)} lines")
        if not isinstance(st.get("vars"), dict):
            errors.append(f"{s_label}: 'vars' must be dict")
        _require_nonempty_str(st, "note", s_label, errors)
        if kind == "1d" and not isinstance(st.get("cells"), list):
            errors.append(f"{s_label}: 1d tracer requires 'cells' list")
        if kind == "2d" and not isinstance(st.get("grid"), list):
            errors.append(f"{s_label}: 2d tracer requires 'grid' 2D list")


def validate_topics(topics: list[dict[str, Any]], expected_count: int, prefix: str, errors: list[str]) -> None:
    if len(topics) != expected_count:
        errors.append(f"{prefix}: expected {expected_count} topics, got {len(topics)}")
    seen_ids: set[str] = set()
    for i, t in enumerate(topics):
        label = f"{prefix}[{i}]({t.get('id', '?')})"
        for k in ("id", "num", "title", "pdfRef", "summary", "conceptHtml", "code", "pitfall"):
            _require_nonempty_str(t, k, label, errors)
        tid = t.get("id", "")
        if tid in seen_ids:
            errors.append(f"{label}: duplicate topic id '{tid}'")
        seen_ids.add(tid)
        check_balanced_c_delimiters(t.get("code", ""), f"{label}.code", errors)
        ls = t.get("logicSteps")
        if not isinstance(ls, list) or len(ls) < 2:
            errors.append(f"{label}: logicSteps must have >= 2 items")
        tracers = t.get("tracers")
        if not isinstance(tracers, list) or not tracers:
            errors.append(f"{label}: must have at least 1 tracer")
        else:
            for ti, tr in enumerate(tracers):
                _validate_tracer(tr, f"{label}.tracer[{ti}]", errors)


def validate_mcqs(mcqs: list[dict[str, Any]], category: str, expected_count: int, errors: list[str]) -> None:
    if len(mcqs) != expected_count:
        errors.append(f"mcq[{category}]: expected {expected_count}, got {len(mcqs)}")
    seen_ids: set[str] = set()
    for i, q in enumerate(mcqs):
        label = f"mcq[{category}][{i}]({q.get('id', '?')})"
        for k in ("id", "category", "subtopic", "level", "title", "stem", "gabaritoResumo", "solutionCode"):
            _require_nonempty_str(q, k, label, errors)
        if q.get("category") != category:
            errors.append(f"{label}: category mismatch ({q.get('category')} != {category})")
        if q.get("id") in seen_ids:
            errors.append(f"{label}: duplicate id")
        seen_ids.add(q.get("id", ""))
        opts = q.get("options")
        exps = q.get("optionExplanations")
        if not isinstance(opts, list) or len(opts) != 5 or not all(isinstance(o, str) and o.strip() for o in opts):
            errors.append(f"{label}: options must be 5 non-empty strings")
        if not isinstance(exps, list) or len(exps) != 5 or not all(isinstance(e, str) and e.strip() for e in exps):
            errors.append(f"{label}: optionExplanations must be 5 non-empty strings")
        corr = q.get("correct")
        if not isinstance(corr, int) or not (0 <= corr <= 4):
            errors.append(f"{label}: correct must be int in 0..4")
        steps = q.get("steps")
        if not isinstance(steps, list) or len(steps) < 2:
            errors.append(f"{label}: steps must have >= 2 entries")
        if q.get("code"):
            check_balanced_c_delimiters(q["code"], f"{label}.code", errors)
        check_balanced_c_delimiters(q.get("solutionCode", ""), f"{label}.solutionCode", errors)


def validate_ce(items: list[dict[str, Any]], category: str, expected_count: int, errors: list[str]) -> None:
    if len(items) != expected_count:
        errors.append(f"ce[{category}]: expected {expected_count}, got {len(items)}")
    seen: set[str] = set()
    for i, item in enumerate(items):
        label = f"ce[{category}][{i}]({item.get('id', '?')})"
        for k in ("id", "category", "subtopic", "statement", "keyPoint"):
            _require_nonempty_str(item, k, label, errors)
        if item.get("id") in seen:
            errors.append(f"{label}: duplicate id")
        seen.add(item.get("id", ""))
        if item.get("category") != category:
            errors.append(f"{label}: category mismatch")
        if not isinstance(item.get("answer"), bool):
            errors.append(f"{label}: answer must be bool")
        steps = item.get("steps")
        if not isinstance(steps, list) or not steps:
            errors.append(f"{label}: steps must be non-empty list")


def validate_classical(items: list[dict[str, Any]], module_name: str, expected_count: int, errors: list[str]) -> None:
    if len(items) != expected_count:
        errors.append(f"classical[{module_name}]: expected {expected_count}, got {len(items)}")
    for i, item in enumerate(items):
        label = f"classical[{module_name}][{i}]"
        for k in ("id", "module", "source", "title", "problem", "idea", "code", "trace"):
            _require_nonempty_str(item, k, label, errors)
        check_balanced_c_delimiters(item.get("code", ""), f"{label}.code", errors)


def validate_simulados(simulados: list[dict[str, Any]], errors: list[str]) -> None:
    if len(simulados) != EXPECTED_COUNTS["simulados"]:
        errors.append(f"simulados: expected {EXPECTED_COUNTS['simulados']}, got {len(simulados)}")
    for si, sim in enumerate(simulados):
        label = f"sim[{si}]({sim.get('id', '?')})"
        for k in ("id", "title", "subtitle"):
            _require_nonempty_str(sim, k, label, errors)
        qs = sim.get("questions", [])
        if len(qs) != EXPECTED_COUNTS["simulado_questions"]:
            errors.append(f"{label}: expected 14 questions, got {len(qs)}")
            continue
        total_pts = sum(float(q.get("points", 0)) for q in qs)
        if abs(total_pts - 10.0) > 1e-6:
            errors.append(f"{label}: total points = {total_pts}, expected 10.0")
        for qi, q in enumerate(qs):
            ql = f"{label}.q[{qi}]"
            qtype = q.get("type")
            if qtype == "mcq":
                opts = q.get("options", [])
                exps = q.get("explanations", [])
                if len(opts) != 5 or len(exps) != 5:
                    errors.append(f"{ql}: mcq requires 5 options & 5 explanations")
                if not isinstance(q.get("correct"), int) or not (0 <= q["correct"] <= 4):
                    errors.append(f"{ql}: invalid correct index")
                if q.get("code"):
                    check_balanced_c_delimiters(q["code"], f"{ql}.code", errors)
            elif qtype == "trace":
                _require_nonempty_str(q, "code", ql, errors)
                _require_nonempty_str(q, "expectedOutput", ql, errors)
                _require_nonempty_str(q, "partBModel", ql, errors)
                check_balanced_c_delimiters(q.get("code", ""), f"{ql}.code", errors)
                if not isinstance(q.get("traceSteps"), list) or not q["traceSteps"]:
                    errors.append(f"{ql}: traceSteps required")
            elif qtype == "bughunt":
                nc = q.get("numberedCode")
                bugs = q.get("bugs")
                if not isinstance(nc, list) or not nc:
                    errors.append(f"{ql}: numberedCode required")
                if not isinstance(bugs, list) or len(bugs) != 4:
                    errors.append(f"{ql}: bughunt requires 4 bugs")
                else:
                    for bi, b in enumerate(bugs):
                        if not isinstance(b.get("line"), int) or not (1 <= b["line"] <= len(nc or [])):
                            errors.append(f"{ql}.bug[{bi}]: invalid line number")
            elif qtype in ("step_code", "code"):
                for fld in ("starter", "modelCode", "solutionNote"):
                    _require_nonempty_str(q, fld, ql, errors)
                check_balanced_c_delimiters(q.get("modelCode", ""), f"{ql}.modelCode", errors)
                tests = q.get("tests")
                if not isinstance(tests, list) or len(tests) < 2:
                    errors.append(f"{ql}: requires >= 2 tests")
                if qtype == "step_code":
                    _require_nonempty_str(q, "partAModel", ql, errors)
                    if not isinstance(q.get("partAKeywords"), list) or not q["partAKeywords"]:
                        errors.append(f"{ql}: partAKeywords required")
            else:
                errors.append(f"{ql}: unknown question type {qtype!r}")


def validate_all(data: dict[str, Any]) -> list[str]:
    """Validate complete DATA payload and return list of error strings."""
    errors: list[str] = []
    validate_topics(data.get("topicsPonteiros", []), EXPECTED_COUNTS["topics_ponteiros"], "topicsPonteiros", errors)
    validate_topics(data.get("topicsStructs", []), EXPECTED_COUNTS["topics_structs"], "topicsStructs", errors)
    validate_topics(data.get("topicsArquivos", []), EXPECTED_COUNTS["topics_arquivos"], "topicsArquivos", errors)

    mcqs = data.get("mcqs", [])
    validate_mcqs([m for m in mcqs if m.get("category") == "ponteiros"], "ponteiros", EXPECTED_COUNTS["mcq_per_cat"], errors)
    validate_mcqs([m for m in mcqs if m.get("category") == "structs"], "structs", EXPECTED_COUNTS["mcq_per_cat"], errors)
    validate_mcqs([m for m in mcqs if m.get("category") == "arquivos"], "arquivos", EXPECTED_COUNTS["mcq_per_cat"], errors)

    ces = data.get("certoErrado", [])
    validate_ce([c for c in ces if c.get("category") == "ponteiros"], "ponteiros", EXPECTED_COUNTS["ce_per_cat"], errors)
    validate_ce([c for c in ces if c.get("category") == "structs"], "structs", EXPECTED_COUNTS["ce_per_cat"], errors)
    validate_ce([c for c in ces if c.get("category") == "arquivos"], "arquivos", EXPECTED_COUNTS["ce_per_cat"], errors)

    classical = data.get("classical", [])
    validate_classical([x for x in classical if x.get("module") == "Ponteiros"], "Ponteiros", EXPECTED_COUNTS["classical_per_cat"], errors)
    validate_classical([x for x in classical if x.get("module") == "Structs"], "Structs", EXPECTED_COUNTS["classical_per_cat"], errors)
    validate_classical([x for x in classical if x.get("module") == "Arquivos"], "Arquivos", EXPECTED_COUNTS["classical_per_cat"], errors)

    validate_simulados(data.get("simulados", []), errors)

    cs = data.get("cheatsheet", [])
    if not isinstance(cs, list) or len(cs) != EXPECTED_COUNTS["cheatsheet_panels"]:
        errors.append(f"cheatsheet: expected {EXPECTED_COUNTS['cheatsheet_panels']} panels")

    return errors
