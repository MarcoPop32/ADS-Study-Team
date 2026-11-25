"""HTML5 / CSS3 / JS Design System 4.0 template for ADS Study Team v4.0."""
from __future__ import annotations


def render_html(data_json: str) -> str:
    """Inject serialized DATA JSON into the complete self-contained HTML template."""
    return HTML_TEMPLATE.replace("__DATA_JSON__", data_json)


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Guia Mestre Interativo em C — Ponteiros, Structs e Arquivos (v4.0)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
    --bg: #f8fafc;
    --surface: #ffffff;
    --surface-alt: #f1f5f9;
    --border: #e2e8f0;
    --border-strong: #cbd5e1;
    --text: #0f172a;
    --text-muted: #475569;
    --text-soft: #64748b;

    --ptr: #2563eb;
    --ptr-bg: #eff6ff;
    --ptr-border: #bfdbfe;

    --strc: #0d9488;
    --strc-bg: #f0fdfa;
    --strc-border: #99f6e4;

    --arq: #d97706;
    --arq-bg: #fffbeb;
    --arq-border: #fde68a;

    --lab: #7c3aed;
    --lab-bg: #f5f3ff;
    --lab-border: #ddd6fe;

    --danger: #dc2626;
    --danger-bg: #fef2f2;
    --danger-border: #fecaca;

    --ok: #16a34a;
    --ok-bg: #f0fdf4;
    --ok-border: #bbf7d0;

    --code-bg: #0f172a;
    --code-fg: #e2e8f0;
    --radius: 12px;
    --shadow: 0 1px 3px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15, 23, 42, 0.04);
    --shadow-lg: 0 12px 28px rgba(15, 23, 42, 0.10);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.65;
    font-size: 15px;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
}

code, pre, .mono {
    font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

p code, li code, td code {
    background: #eef2ff;
    color: #1e3a8a;
    padding: 1px 6px;
    border-radius: 5px;
    font-size: 0.88em;
    border: 1px solid #e0e7ff;
    word-break: break-word;
}

/* Scrollbar elegante */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-strong); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-soft); }

/* Animacoes Design System 4.0 */
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes popCell {
    0% { transform: scale(0.95); }
    60% { transform: scale(1.04); }
    100% { transform: scale(1); }
}
@keyframes pulseRing {
    0%, 100% { box-shadow: 0 0 0 0 rgba(225, 29, 72, 0.35); }
    50% { box-shadow: 0 0 0 6px rgba(225, 29, 72, 0); }
}

/* Topbar + Barra de Progresso de Leitura */
.topbar {
    position: sticky;
    top: 0;
    z-index: 60;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
}

.scroll-progress-track {
    position: relative;
    width: 100%;
    height: 3px;
    background: transparent;
}
.scroll-progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, var(--ptr), var(--strc), var(--arq), var(--lab));
    transition: width 0.1s linear;
}

.topbar-inner {
    max-width: 1280px;
    margin: 0 auto;
    padding: 9px 16px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0;
}

.brand-badge {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: linear-gradient(135deg, #2563eb, #0d9488);
    color: #fff;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.28);
}

.brand-title {
    font-weight: 800;
    font-size: 15.5px;
    line-height: 1.2;
    letter-spacing: -0.01em;
}
.brand-sub {
    font-size: 11.5px;
    color: var(--text-soft);
}

.top-actions {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}

/* Busca + Atalho '/' */
.search-wrap {
    position: relative;
    display: flex;
    align-items: center;
}
.search-input {
    width: 240px;
    padding: 7px 34px 7px 12px;
    border-radius: 999px;
    border: 1px solid var(--border-strong);
    background: var(--surface-alt);
    color: var(--text);
    font-size: 13px;
    outline: none;
    transition: all 0.2s;
}
.search-input:focus {
    background: var(--surface);
    border-color: var(--ptr);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.14);
}
.kbd-hint {
    position: absolute;
    right: 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 5px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-soft);
    pointer-events: none;
}
.search-dropdown {
    position: absolute;
    top: calc(100% + 6px);
    left: 0;
    right: 0;
    min-width: 310px;
    max-height: 390px;
    overflow-y: auto;
    background: var(--surface);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
    box-shadow: var(--shadow-lg);
    padding: 6px;
    display: none;
    z-index: 100;
}
.search-dropdown.open { display: block; animation: fadeSlideUp 0.16s ease; }
.search-item {
    display: flex;
    flex-direction: column;
    gap: 2px;
    width: 100%;
    text-align: left;
    border: none;
    background: transparent;
    padding: 8px 10px;
    border-radius: 8px;
    cursor: pointer;
    color: var(--text);
}
.search-item:hover { background: var(--surface-alt); }
.search-item-title { font-size: 13px; font-weight: 700; }
.search-item-meta { font-size: 11.5px; color: var(--text-soft); }

/* Botoes Topbar */
.playground-open-btn, .pomodoro-pill, .theme-toggle-btn, .search-toggle-btn, .font-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    border-radius: 999px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    font-size: 12.5px;
    font-weight: 700;
    padding: 6px 11px;
    cursor: pointer;
    transition: all 0.16s ease;
    white-space: nowrap;
}
.playground-open-btn {
    background: linear-gradient(135deg, #6d28d9, #4f46e5);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 2px 8px rgba(109, 40, 217, 0.25);
}
.playground-open-btn:hover { transform: translateY(-1px); filter: brightness(1.07); }

.pomodoro-pill.pomo-active {
    background: #fff1f2;
    border-color: #fda4af;
    color: #be123c;
    animation: pulseRing 2.2s infinite;
}
.pomodoro-pill.pomo-break {
    background: var(--ok-bg);
    border-color: var(--ok-border);
    color: var(--ok);
}

.font-size-controls {
    display: inline-flex;
    border: 1px solid var(--border-strong);
    border-radius: 999px;
    overflow: hidden;
}
.font-btn {
    border: none;
    border-radius: 0;
    padding: 6px 9px;
    font-size: 12px;
}
.font-btn + .font-btn { border-left: 1px solid var(--border); }
.font-btn:hover, .theme-toggle-btn:hover { background: var(--surface-alt); }
.search-toggle-btn { display: none; }

.progress-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 5px 11px;
    border-radius: 999px;
    background: var(--surface-alt);
    border: 1px solid var(--border);
    font-size: 12px;
    font-weight: 700;
    color: var(--text-muted);
}
.progress-bar-mini {
    width: 60px;
    height: 7px;
    border-radius: 999px;
    background: var(--border-strong);
    overflow: hidden;
}
.progress-bar-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, var(--ptr), var(--strc));
    transition: width 0.25s ease;
}

/* Primary Nav Tabs */
.nav-bar {
    border-top: 1px solid var(--border);
    background: var(--surface);
}
.nav-tabs {
    max-width: 1280px;
    margin: 0 auto;
    padding: 6px 16px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 5px;
}
.nav-sep { width: 1px; height: 20px; background: var(--border-strong); flex-shrink: 0; margin: 0 2px; }
.nav-tab {
    border: 1px solid transparent;
    background: transparent;
    color: var(--text-muted);
    font-size: 12.4px;
    font-weight: 700;
    padding: 5px 9px;
    border-radius: 9px;
    cursor: pointer;
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    transition: all 0.16s ease;
}
.nav-tab:hover { background: var(--surface-alt); color: var(--text); }
.nav-tab.active {
    background: #0f172a;
    color: #fff;
}
.nav-tab.active[data-view="ponteiros"], .nav-tab.active[data-view="ex-ponteiros"] { background: var(--ptr); }
.nav-tab.active[data-view="structs"], .nav-tab.active[data-view="ex-structs"] { background: var(--strc); }
.nav-tab.active[data-view="arquivos"], .nav-tab.active[data-view="ex-arquivos"] { background: var(--arq); }
.nav-tab.active[data-view="pratica"] { background: var(--lab); }
.nav-tab.active[data-view="simulados"] { background: #be123c; }

.tab-pill-cnt {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    padding: 1px 6px;
    border-radius: 999px;
    background: rgba(15, 23, 42, 0.08);
    color: inherit;
}
.nav-tab.active .tab-pill-cnt { background: rgba(255, 255, 255, 0.22); }

/* Mobile Bottom Nav */
.mobile-bottom-nav { display: none; }

/* Main Container */
.container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 20px 16px 48px;
}

.view-panel { display: none; }
.view-panel.active {
    display: block;
    animation: fadeSlideUp 0.24s ease-out;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #0f172a 100%);
    color: #f8fafc;
    border-radius: 18px;
    padding: 28px 26px;
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
}
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image: radial-gradient(rgba(148, 163, 184, 0.16) 1px, transparent 1px);
    background-size: 22px 22px;
    pointer-events: none;
}
.hero > * { position: relative; z-index: 1; }
.hero-kicker {
    display: inline-block;
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 999px;
    background: rgba(56, 189, 248, 0.18);
    color: #7dd3fc;
    border: 1px solid rgba(125, 211, 252, 0.3);
    margin-bottom: 10px;
}
.hero h1 {
    font-size: clamp(22px, 3vw, 31px);
    line-height: 1.2;
    font-weight: 800;
    margin-bottom: 10px;
}
.hero p {
    font-size: 14.5px;
    color: #cbd5e1;
    max-width: 820px;
    margin-bottom: 18px;
}
.hero-btns {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 20px;
}
.hero-kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 12px;
}
.hero-kpi {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    padding: 12px 14px;
}
.hero-kpi-lbl { font-size: 11.5px; color: #94a3b8; font-weight: 600; }
.hero-kpi-val { font-size: 21px; font-weight: 800; font-family: 'JetBrains Mono', monospace; color: #fff; margin: 2px 0; }
.hero-kpi-sub { font-size: 11.5px; color: #cbd5e1; }

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    border: 1px solid transparent;
    border-radius: 10px;
    padding: 9px 15px;
    font-size: 13.5px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.16s ease;
    text-decoration: none;
}
.btn:hover { transform: translateY(-1px); }
.btn-primary { background: var(--ptr); color: #fff; }
.btn-primary:hover { filter: brightness(1.08); }
.btn-lab { background: var(--lab); color: #fff; }
.btn-lab:hover { filter: brightness(1.08); }
.btn-outline { background: var(--surface); color: var(--text); border-color: var(--border-strong); }
.btn-outline:hover { background: var(--surface-alt); }
.btn-ghost-light {
    background: rgba(255, 255, 255, 0.10);
    color: #fff;
    border-color: rgba(255, 255, 255, 0.24);
}
.btn-ghost-light:hover { background: rgba(255, 255, 255, 0.18); }

/* Resume Banner */
.resume-banner {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    background: linear-gradient(135deg, #eff6ff, #f0fdfa);
    border: 1px solid var(--ptr-border);
    border-left: 5px solid var(--ptr);
    border-radius: 14px;
    padding: 13px 16px;
    margin-bottom: 18px;
}

/* Module Grid */
.module-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
    margin-bottom: 20px;
}
.mod-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px;
    box-shadow: var(--shadow);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 14px;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.mod-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); }
.mod-card.ptr { border-top: 4px solid var(--ptr); }
.mod-card.strc { border-top: 4px solid var(--strc); }
.mod-card.arq { border-top: 4px solid var(--arq); }
.mod-card.lab { border-top: 4px solid var(--lab); }

.mod-card-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 8px; }
.mod-badge {
    display: inline-block;
    font-size: 11.5px;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 999px;
    background: var(--surface-alt);
    color: var(--text-muted);
}
.mod-card.ptr .mod-badge { background: var(--ptr-bg); color: var(--ptr); }
.mod-card.strc .mod-badge { background: var(--strc-bg); color: var(--strc); }
.mod-card.arq .mod-badge { background: var(--arq-bg); color: var(--arq); }
.mod-card.lab .mod-badge { background: var(--lab-bg); color: var(--lab); }
.mod-icon { font-size: 18px; font-weight: 800; opacity: 0.7; }
.mod-card h3 { font-size: 18px; margin-bottom: 6px; }
.mod-card p { font-size: 13.5px; color: var(--text-muted); }

.mod-prog-row { margin-top: 12px; }
.mod-prog-meta { display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; color: var(--text-muted); margin-bottom: 4px; }
.cat-progress-track {
    width: 100%;
    height: 8px;
    background: var(--border);
    border-radius: 999px;
    overflow: hidden;
}
.cat-progress-fill { height: 100%; border-radius: 999px; transition: width 0.3s ease; }

.mod-actions-dual { display: grid; grid-template-columns: 1fr auto; gap: 8px; }

/* Cheat Sheet */
.cheatsheet-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 20px;
    box-shadow: var(--shadow);
}
.cs-head {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 14px;
}
.cs-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}
.cs-mini-card {
    background: var(--surface-alt);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 14px;
    font-size: 13px;
}
.cs-mini-card h4 { font-size: 14px; margin-bottom: 6px; }
.cs-mini-card pre {
    background: var(--code-bg);
    color: var(--code-fg);
    padding: 8px 10px;
    border-radius: 8px;
    font-size: 12px;
    overflow-x: auto;
    margin-top: 6px;
}

.module-header-banner {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 5px solid var(--ptr);
    border-radius: 14px;
    padding: 16px 20px;
    margin-bottom: 18px;
    box-shadow: var(--shadow);
}
.strc-theme .module-header-banner { border-left-color: var(--strc); }
.arq-theme .module-header-banner { border-left-color: var(--arq); }
.module-header-banner h2 { font-size: 20px; margin-bottom: 4px; }
.module-header-banner p { font-size: 13.8px; color: var(--text-muted); }

/* Module Layout + Sticky TOC */
.module-layout {
    display: grid;
    grid-template-columns: 270px minmax(0, 1fr);
    gap: 20px;
    align-items: start;
}
.module-layout > * { min-width: 0; }
.sandbox-box, .topic-card, .module-header-banner, .ex-card, .sim-q-card {
    min-width: 0;
    max-width: 100%;
    overflow-wrap: break-word;
}
.mem-strip { max-width: 100%; overflow-x: auto; padding-bottom: 4px; }
.sim-prompt-html p { margin-bottom: 6px; }
.sim-prompt-html ol, .sim-prompt-html ul { padding-left: 20px; margin-bottom: 6px; }
.toc-sidebar {
    position: sticky;
    top: 108px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 14px;
    max-height: calc(100vh - 124px);
    overflow-y: auto;
    box-shadow: var(--shadow);
}
.toc-title { font-size: 13px; font-weight: 800; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.04em; color: var(--text-soft); }
.toc-mobile-toggle { display: none; }
.toc-prog-box {
    background: var(--surface-alt);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 9px 10px;
    margin-bottom: 10px;
}
.toc-filter-row { display: flex; gap: 5px; margin-top: 8px; }
.toc-flt-btn {
    flex: 1;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 700;
    padding: 4px 6px;
    border-radius: 7px;
    cursor: pointer;
}
.toc-flt-btn.active { background: #0f172a; color: #fff; border-color: #0f172a; }

.toc-btn {
    width: 100%;
    text-align: left;
    border: 1px solid transparent;
    background: transparent;
    padding: 7px 9px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
    cursor: pointer;
    font-size: 12.6px;
    color: var(--text-muted);
    margin-bottom: 3px;
    transition: background 0.14s;
}
.toc-btn:hover { background: var(--surface-alt); color: var(--text); }
.toc-btn.toc-active { background: var(--ptr-bg); color: var(--ptr); font-weight: 700; border-color: var(--ptr-border); }
.strc-theme .toc-btn.toc-active { background: var(--strc-bg); color: var(--strc); border-color: var(--strc-border); }
.arq-theme .toc-btn.toc-active { background: var(--arq-bg); color: var(--arq); border-color: var(--arq-border); }
.toc-btn.done .toc-check { color: var(--ok); font-weight: 800; }
.toc-left { display: flex; align-items: center; gap: 6px; min-width: 0; }
.toc-num { font-size: 11px; font-weight: 700; opacity: 0.75; flex-shrink: 0; }
.toc-title-txt { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.toc-top-btn {
    width: 100%;
    margin-top: 8px;
    padding: 7px;
    border: 1px dashed var(--border-strong);
    background: var(--surface-alt);
    color: var(--text-muted);
    border-radius: 8px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
}

/* Topic Cards */
.topic-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: var(--shadow);
    scroll-margin-top: 115px;
}
.topic-top {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 12px;
}
.topic-num {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 7px;
    background: var(--ptr-bg);
    color: var(--ptr);
    margin-right: 8px;
}
.strc-theme .topic-num { background: var(--strc-bg); color: var(--strc); }
.arq-theme .topic-num { background: var(--arq-bg); color: var(--arq); }
.pdf-ref { display: inline-block; font-size: 12px; color: var(--text-soft); margin-top: 4px; }

.done-toggle {
    border: 1px solid var(--border-strong);
    background: var(--surface-alt);
    color: var(--text-muted);
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 12.5px;
    font-weight: 700;
    cursor: pointer;
    flex-shrink: 0;
    transition: all 0.15s;
}
.done-toggle.completed {
    background: var(--ok-bg);
    border-color: var(--ok);
    color: var(--ok);
}

.topic-summary {
    background: var(--surface-alt);
    border-left: 4px solid var(--ptr);
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 14px;
}
.strc-theme .topic-summary { border-left-color: var(--strc); }
.arq-theme .topic-summary { border-left-color: var(--arq); }

.concept-body p { margin-bottom: 10px; }
.concept-body ul, .concept-body ol { padding-left: 22px; margin-bottom: 10px; }
.concept-body li { margin-bottom: 5px; }

.callout {
    padding: 11px 14px;
    border-radius: 10px;
    border: 1px solid var(--ptr-border);
    background: var(--ptr-bg);
    font-size: 13.5px;
    margin: 12px 0;
}
.callout-danger {
    border-color: var(--danger-border);
    background: var(--danger-bg);
    color: #991b1b;
}
.callout-info {
    border-color: var(--ptr-border);
    background: var(--ptr-bg);
}
.callout-ok {
    border-color: var(--ok-border);
    background: var(--ok-bg);
    color: #166534;
}

/* Memory Diagram */
.mem-box {
    background: var(--surface-alt);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px 14px;
    margin: 14px 0;
}
.mem-caption { font-size: 12.5px; font-weight: 700; color: var(--text-muted); margin-bottom: 8px; }
.mem-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: flex-start;
}
.mem-cell, .ram-cell-live {
    min-width: 78px;
    background: var(--surface);
    border: 1px solid var(--border-strong);
    border-radius: 10px;
    padding: 7px 9px;
    text-align: center;
    transition: all 0.2s ease;
}
.ram-cell-live.active-cell {
    border-color: var(--lab);
    background: var(--lab-bg);
    box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.16);
    animation: popCell 0.22s ease;
}
.mem-cell.null-byte, .ram-cell-live.null-byte {
    border-color: #f59e0b;
    background: #fffbeb;
}
.mem-idx { font-size: 10.5px; color: var(--text-soft); font-weight: 700; }
.mem-val { font-size: 14.5px; font-weight: 800; color: var(--text); margin: 2px 0; }
.mem-tag { font-size: 10px; color: var(--ptr); font-weight: 700; }
.mem-addr { font-size: 10px; color: var(--text-soft); }
.ptr-badge {
    display: inline-block;
    margin-top: 4px;
    padding: 1px 7px;
    border-radius: 999px;
    background: #7c3aed;
    color: #fff;
    font-size: 10.5px;
    font-weight: 700;
}

/* Code Panel IDE Style */
.code-panel {
    background: var(--code-bg);
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
    border: 1px solid #1e293b;
}
.code-header {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    padding: 8px 12px;
    background: #1e293b;
    color: #cbd5e1;
    font-size: 12px;
    font-weight: 600;
}
.code-title-wrap { display: inline-flex; align-items: center; gap: 8px; }
.mac-dots { display: inline-flex; gap: 5px; }
.mac-dots i { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
.mac-dots i:nth-child(1) { background: #ef4444; }
.mac-dots i:nth-child(2) { background: #f59e0b; }
.mac-dots i:nth-child(3) { background: #22c55e; }
.code-actions { display: inline-flex; align-items: center; gap: 6px; }
.copy-btn, .run-pg-btn {
    border: 1px solid rgba(148, 163, 184, 0.35);
    background: rgba(15, 23, 42, 0.45);
    color: #e2e8f0;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.15s;
}
.copy-btn:hover { background: #334155; }
.run-pg-btn {
    background: rgba(124, 58, 237, 0.28);
    border-color: rgba(167, 139, 250, 0.48);
    color: #ddd6fe;
}
.run-pg-btn:hover { background: #7c3aed; color: #fff; }
.code-pre {
    padding: 13px 14px;
    color: var(--code-fg);
    font-size: 13px;
    line-height: 1.55;
    overflow-x: auto;
    margin: 0;
}
.tok-kw { color: #93c5fd; font-weight: 600; }
.tok-type { color: #5eead4; font-weight: 600; }
.tok-pp { color: #c4b5fd; }
.tok-str { color: #fde68a; }
.tok-num { color: #fca5a5; }
.tok-cmt { color: #94a3b8; font-style: italic; }

/* Inline Tracer */
.inline-tracer-host {
    margin: 14px 0;
    border: 1px solid var(--lab-border);
    background: linear-gradient(180deg, rgba(124, 58, 237, 0.04), transparent);
    border-radius: 12px;
    padding: 14px;
}
.inline-tr-head {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}
.inline-tr-algo-pills, .filter-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 10px;
}
.pill-btn {
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-muted);
    padding: 5px 11px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.14s;
}
.pill-btn.active { background: var(--ptr); border-color: var(--ptr); color: #fff; }
.pill-btn.lab-pill.active { background: var(--lab); border-color: var(--lab); color: #fff; }

.itr-controls {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 7px;
    margin: 8px 0;
}
.itr-btn {
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    padding: 5px 10px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
}
.itr-btn.primary { background: var(--lab); border-color: var(--lab); color: #fff; }
.itr-speed-sel {
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    padding: 5px 8px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
}
.itr-progress-track { width: 100%; height: 5px; background: var(--border); border-radius: 999px; overflow: hidden; margin: 4px 0 12px; }
.itr-progress-fill { height: 100%; background: linear-gradient(90deg, #7c3aed, #3b82f6); transition: width 0.2s ease; }

.itr-split {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr);
    gap: 12px;
    align-items: start;
}
.itr-code-box {
    background: var(--code-bg);
    color: var(--code-fg);
    border-radius: 10px;
    padding: 10px 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.2px;
    overflow-x: auto;
}
.code-line { display: flex; gap: 8px; padding: 2px 6px; border-radius: 5px; white-space: pre; }
.code-line.active-line { background: rgba(124, 58, 237, 0.38); color: #fff; font-weight: 700; }
.line-no { color: #64748b; min-width: 20px; text-align: right; user-select: none; }

.step-dots { display: flex; flex-wrap: wrap; gap: 4px; margin: 8px 0; }
.step-dot {
    min-width: 26px;
    height: 24px;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    cursor: pointer;
}
.step-dot.current { background: var(--lab); border-color: var(--lab); color: #fff; }

.vars-row { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
.var-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 9px;
    border-radius: 8px;
    background: var(--surface);
    border: 1px solid var(--border-strong);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
}
.var-chip.var-changed {
    border-color: var(--lab);
    background: var(--lab-bg);
    box-shadow: 0 0 0 2px rgba(124, 58, 237, 0.16);
}
.itr-note {
    margin-top: 10px;
    padding: 9px 12px;
    border-radius: 9px;
    background: var(--surface);
    border: 1px solid var(--border-strong);
    font-size: 13px;
}

.trace-table-wrap { margin-top: 10px; overflow-x: auto; }
.trace-table { width: 100%; border-collapse: collapse; font-size: 12px; font-family: 'JetBrains Mono', monospace; }
.trace-table th, .trace-table td { border: 1px solid var(--border); padding: 5px 8px; text-align: left; }
.trace-table th { background: var(--surface-alt); }
.trace-table tr { cursor: pointer; }
.trace-table tr.cur-row { background: var(--lab-bg); font-weight: 700; }

.sub-heading { font-size: 14px; font-weight: 800; margin: 14px 0 8px; color: var(--text); }
.logic-list { padding-left: 20px; font-size: 13.8px; }
.logic-list li { margin-bottom: 6px; }
.topic-nav-footer {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    margin-top: 16px;
    padding-top: 14px;
    border-top: 1px dashed var(--border-strong);
}

/* Micro-Sandboxes */
.sandbox-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 4px solid var(--ptr);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 20px;
    box-shadow: var(--shadow);
}
.sandbox-box.strc-sb { border-top-color: var(--strc); }
.sandbox-box.arq-sb { border-top-color: var(--arq); }
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 8px;
    margin-top: 10px;
}
.stat-mini {
    background: var(--surface-alt);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 8px 10px;
    font-size: 12px;
}
.stat-mini strong { display: block; font-size: 14px; font-family: 'JetBrains Mono', monospace; margin-top: 2px; }

/* Hub e Exercícios */
.cat-hub-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
    margin-bottom: 22px;
}
.cat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 14px;
    box-shadow: var(--shadow);
}
.cat-card.cat-ptr { border-top: 4px solid var(--ptr); }
.cat-card.cat-strc { border-top: 4px solid var(--strc); }
.cat-card.cat-arq { border-top: 4px solid var(--arq); }
.cat-topics-chips { display: flex; flex-wrap: wrap; gap: 5px; }
.cat-chip { font-size: 11px; padding: 2px 8px; border-radius: 999px; background: var(--surface-alt); border: 1px solid var(--border); }

.ex-global-bar, .cat-controls-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 16px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}

.q-minimap-wrap { width: 100%; margin-top: 10px; padding-top: 10px; border-top: 1px dashed var(--border); }
.q-minimap-lbl { font-size: 11.5px; font-weight: 700; color: var(--text-soft); margin-bottom: 7px; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px; }
.q-minimap-grid { display: flex; flex-wrap: wrap; gap: 5px; }
.q-map-btn {
    position: relative;
    width: 31px;
    height: 29px;
    border-radius: 7px;
    border: 1px solid var(--border-strong);
    background: var(--surface-alt);
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11.5px;
    font-weight: 700;
    cursor: pointer;
}
.q-map-btn.map-ok { background: var(--ok-bg); border-color: var(--ok); color: var(--ok); }
.q-map-btn.map-err { background: var(--danger-bg); border-color: var(--danger); color: var(--danger); }
.q-map-btn.map-fav::after { content: "★"; position: absolute; top: -4px; right: -3px; font-size: 9px; color: #f59e0b; }

.ex-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: var(--shadow);
    scroll-margin-top: 115px;
}
.ex-card-head { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 8px; margin-bottom: 10px; }
.lvl-badge { font-size: 11.5px; font-weight: 700; padding: 3px 9px; border-radius: 999px; }
.lvl-facil { background: var(--ok-bg); color: var(--ok); }
.lvl-medio { background: var(--arq-bg); color: var(--arq); }
.lvl-dificil { background: var(--danger-bg); color: var(--danger); }

.fav-q-btn {
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text-muted);
    border-radius: 999px;
    padding: 3px 10px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
}
.fav-q-btn.is-fav { background: rgba(245, 158, 11, 0.16); border-color: #f59e0b; color: #d97706; }

.cat-search-input {
    padding: 7px 12px;
    border-radius: 999px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    font-size: 12.8px;
    min-width: 220px;
    outline: none;
}

.ex-options-list { display: flex; flex-direction: column; gap: 8px; margin-top: 10px; }
.quiz-opt {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    width: 100%;
    text-align: left;
    padding: 10px 13px;
    border-radius: 10px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    font-size: 13.5px;
    cursor: pointer;
    transition: all 0.15s;
}
.quiz-opt:hover:not(:disabled) { background: var(--surface-alt); border-color: var(--ptr); }
.quiz-opt.selected { border-color: var(--ptr); background: var(--ptr-bg); }
.quiz-opt.correct { border-color: var(--ok); background: var(--ok-bg); color: #14532d; }
.quiz-opt.wrong { border-color: var(--danger); background: var(--danger-bg); color: #7f1d1d; }
.opt-letter {
    flex-shrink: 0;
    width: 24px;
    height: 24px;
    border-radius: 7px;
    background: var(--surface-alt);
    border: 1px solid var(--border-strong);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 800;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
.quiz-opt.correct .opt-letter { background: var(--ok); border-color: var(--ok); color: #fff; }
.quiz-opt.wrong .opt-letter { background: var(--danger); border-color: var(--danger); color: #fff; }

.gabarito-box {
    margin-top: 12px;
    border-top: 1px dashed var(--border-strong);
    padding-top: 12px;
    font-size: 13.5px;
}

/* Certo / Errado Trainer */
.ce-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
    margin-bottom: 20px;
}
.ce-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 15px;
    box-shadow: var(--shadow);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 10px;
}
.ce-actions { display: flex; gap: 8px; }
.ce-btn {
    flex: 1;
    padding: 8px 10px;
    border-radius: 9px;
    border: 1px solid var(--border-strong);
    background: var(--surface-alt);
    font-weight: 800;
    font-size: 13px;
    cursor: pointer;
}
.ce-btn.ce-true-sel { background: var(--ok-bg); border-color: var(--ok); color: var(--ok); }
.ce-btn.ce-false-sel { background: var(--danger-bg); border-color: var(--danger); color: var(--danger); }

/* Simulados ATP */
.sim-header-bar {
    position: sticky;
    top: 105px;
    z-index: 40;
    background: var(--surface);
    border: 1px solid var(--border-strong);
    border-radius: 14px;
    padding: 12px 16px;
    margin-bottom: 16px;
    box-shadow: var(--shadow-lg);
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}
.sim-timer {
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    font-weight: 800;
    padding: 5px 12px;
    border-radius: 10px;
    background: var(--surface-alt);
    border: 1px solid var(--border-strong);
}
.sim-timer.urgent { background: var(--danger-bg); color: var(--danger); border-color: var(--danger); }
.sim-nav-strip { width: 100%; display: flex; flex-wrap: wrap; align-items: center; gap: 5px; padding-top: 8px; border-top: 1px dashed var(--border); }
.sim-q-pill {
    padding: 3px 8px;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--surface-alt);
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    cursor: pointer;
}
.sim-q-pill.answered { background: var(--ptr-bg); border-color: var(--ptr); color: var(--ptr); }
.sim-q-pill.graded-ok { background: var(--ok-bg); border-color: var(--ok); color: var(--ok); }
.sim-q-pill.graded-err { background: var(--danger-bg); border-color: var(--danger); color: var(--danger); }

.sim-confirm-box {
    width: 100%;
    padding: 10px 12px;
    border-radius: 10px;
    background: #fff1f2;
    border: 1px solid #fecdd3;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}
.sim-q-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 16px;
    scroll-margin-top: 175px;
    box-shadow: var(--shadow);
}
.sim-sub-label { font-size: 13px; font-weight: 700; margin: 10px 0 5px; }
.sim-io-box {
    background: var(--surface-alt);
    border: 1px solid var(--border-strong);
    border-radius: 9px;
    padding: 9px 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.2px;
    white-space: pre-wrap;
    margin-bottom: 8px;
}
.sim-text-area, .sim-code-area {
    width: 100%;
    border: 1px solid var(--border-strong);
    border-radius: 10px;
    padding: 10px 12px;
    background: var(--surface);
    color: var(--text);
    font-size: 13px;
    outline: none;
    resize: vertical;
}
.sim-code-area {
    min-height: 185px;
    font-family: 'JetBrains Mono', monospace;
    background: #0b1120;
    color: #e2e8f0;
    border-color: #334155;
}
.sim-text-area { min-height: 76px; }
.c-keybar { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 6px; }
.c-key-btn {
    padding: 3px 8px;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--surface-alt);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11.5px;
    font-weight: 700;
    cursor: pointer;
}
.bug-row { display: grid; grid-template-columns: 76px 1fr 1fr; gap: 8px; margin-bottom: 8px; }
.bug-inp {
    padding: 7px 9px;
    border-radius: 8px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    font-size: 12.5px;
}
.sim-test-row { padding: 8px 10px; border-radius: 8px; font-size: 12.3px; margin-bottom: 6px; font-family: 'JetBrains Mono', monospace; }
.sim-test-row.pass { background: var(--ok-bg); border: 1px solid var(--ok-border); color: #166534; }
.sim-test-row.fail { background: var(--danger-bg); border: 1px solid var(--danger-border); color: #991b1b; }
.sim-kicker-badge { background: #fff1f2; color: #be123c; border: 1px solid #fecdd3; }

/* Playground Modal */
.pg-modal-backdrop {
    position: fixed;
    inset: 0;
    z-index: 120;
    background: rgba(2, 6, 23, 0.68);
    backdrop-filter: blur(6px);
    display: none;
    align-items: center;
    justify-content: center;
    padding: 14px;
}
.pg-modal-backdrop.open { display: flex; animation: fadeSlideUp 0.16s ease; }
.pg-modal {
    width: min(980px, 100%);
    max-height: 92vh;
    background: var(--surface);
    border: 1px solid var(--border-strong);
    border-radius: 16px;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.45);
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
.pg-header {
    flex-shrink: 0;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    padding: 13px 18px;
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
    color: #fff;
    border-bottom: 1px solid #334155;
}
.pg-body { flex: 1 1 auto; min-height: 0; padding: 16px 18px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; }
.pg-io-grid { display: grid; grid-template-columns: 1fr 1.2fr; gap: 12px; }
.pg-console {
    background: #090d16;
    color: #e2e8f0;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 11px 13px;
    min-height: 96px;
    max-height: 190px;
    overflow-y: auto;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
    white-space: pre-wrap;
}
.pg-console.err { border-color: #ef4444; color: #fca5a5; }
.field-label { display: block; font-size: 12px; font-weight: 700; color: var(--text-muted); margin-bottom: 4px; }
.text-input {
    width: 100%;
    padding: 7px 11px;
    border-radius: 8px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    font-size: 13.5px;
}

.fab-top {
    position: fixed;
    right: 18px;
    bottom: 20px;
    z-index: 55;
    width: 42px;
    height: 42px;
    border-radius: 50%;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    font-size: 17px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: var(--shadow-lg);
    display: none;
}
.fab-top.visible { display: flex; align-items: center; justify-content: center; }

.toast {
    position: fixed;
    left: 50%;
    bottom: 24px;
    transform: translate(-50%, 16px);
    background: #0f172a;
    color: #fff;
    padding: 9px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    opacity: 0;
    pointer-events: none;
    transition: all 0.2s ease;
    z-index: 150;
}
.toast.show { opacity: 1; transform: translate(-50%, 0); }

/* ==================== DARK MODE ==================== */
body.dark-mode {
    --bg: #020617;
    --surface: #0f172a;
    --surface-alt: #1e293b;
    --border: #1e293b;
    --border-strong: #334155;
    --text: #f1f5f9;
    --text-muted: #cbd5e1;
    --text-soft: #94a3b8;
    --ptr-bg: rgba(37, 99, 235, 0.16);
    --ptr-border: rgba(59, 130, 246, 0.42);
    --strc-bg: rgba(13, 148, 136, 0.16);
    --strc-border: rgba(45, 212, 191, 0.36);
    --arq-bg: rgba(217, 119, 6, 0.18);
    --arq-border: rgba(251, 191, 36, 0.36);
    --lab-bg: rgba(124, 58, 237, 0.18);
    --lab-border: rgba(167, 139, 250, 0.38);
    --ok-bg: rgba(22, 163, 74, 0.18);
    --ok-border: rgba(74, 222, 128, 0.38);
    --danger-bg: rgba(220, 38, 38, 0.18);
    --danger-border: rgba(248, 113, 113, 0.40);
}
body.dark-mode .topbar { background: rgba(15, 23, 42, 0.92); }
body.dark-mode p code, body.dark-mode li code, body.dark-mode td code {
    background: #1e293b;
    color: #93c5fd;
    border-color: #334155;
}
body.dark-mode .callout-danger { color: #fecaca; }
body.dark-mode .callout-ok { color: #bbf7d0; }
body.dark-mode .resume-banner { background: linear-gradient(135deg, rgba(37,99,235,0.16), rgba(13,148,136,0.14)); }
body.dark-mode .quiz-opt.correct { color: #bbf7d0; }
body.dark-mode .quiz-opt.wrong { color: #fecaca; }
body.dark-mode .sim-confirm-box { background: rgba(190, 18, 60, 0.22); border-color: rgba(251, 113, 133, 0.4); }
body.dark-mode .sim-test-row.pass { color: #bbf7d0; }
body.dark-mode .sim-test-row.fail { color: #fecaca; }
body.dark-mode .sim-kicker-badge { background: rgba(225, 29, 72, 0.2); color: #fda4af; border-color: rgba(251, 113, 133, 0.38); }
body.dark-mode .mem-cell.null-byte, body.dark-mode .ram-cell-live.null-byte { background: rgba(217, 119, 6, 0.24); border-color: #f59e0b; }

/* ==================== RESPONSIVO & GOOGLE SITES (<= 700px) ==================== */
@media (max-width: 960px) {
    .module-layout { grid-template-columns: 1fr; }
    .toc-sidebar { position: relative; top: 0; max-height: none; }
    .toc-mobile-toggle {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid var(--border-strong);
        background: var(--surface-alt);
        color: var(--text);
        padding: 9px 12px;
        border-radius: 10px;
        font-weight: 700;
        cursor: pointer;
    }
    .toc-title { display: none; }
    .toc-list-wrap { display: none; margin-top: 10px; }
    .toc-sidebar.toc-open .toc-list-wrap { display: block; }
    .cat-hub-grid { grid-template-columns: 1fr; }
    .hero-kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .itr-split { grid-template-columns: 1fr; }
}

@media (max-width: 760px) {
    .container { padding: 14px 10px 44px; }
    .stats-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .search-wrap { display: none; }
    .search-wrap.mobile-open {
        display: flex;
        width: 100%;
        order: 10;
    }
    .search-wrap.mobile-open .search-input { width: 100%; }
    .search-toggle-btn { display: inline-flex; }
    .module-grid, .cs-grid, .ce-grid, .pg-io-grid { grid-template-columns: 1fr; }
    .bug-row { grid-template-columns: 1fr; }
    .nav-bar { display: none; }
    .mobile-bottom-nav {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 2px;
        border-top: 1px solid var(--border);
        background: var(--surface);
        padding: 4px 6px;
    }
    .mbn-btn {
        border: none;
        background: transparent;
        color: var(--text-muted);
        font-size: 10.5px;
        font-weight: 700;
        padding: 5px 2px;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1px;
        cursor: pointer;
    }
    .mbn-btn.active { background: var(--ptr-bg); color: var(--ptr); }
    .mbn-icon { font-size: 14px; }
    .playground-open-btn .pg-lbl-txt, #theme-label, .kbd-hint { display: none; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.001ms !important;
        transition-duration: 0.001ms !important;
        scroll-behavior: auto !important;
    }
}
</style>
</head>
<body>

<header class="topbar">
    <div class="scroll-progress-track" aria-hidden="true"><div id="scroll-progress-line" class="scroll-progress-bar"></div></div>
    <div class="topbar-inner">
        <div class="brand">
            <div class="brand-badge">{C*}</div>
            <div>
                <div class="brand-title">Guia Mestre Interativo em C (v4.0)</div>
                <div class="brand-sub">Ponteiros • Structs &amp; Unions • Arquivos &amp; FILE* • 90 Qs + 30 C/E + 3 Provas ATP</div>
            </div>
        </div>
        <div class="top-actions">
            <div class="search-wrap" id="search-wrap">
                <input type="search" id="global-search" class="search-input" placeholder="Buscar tópico, malloc, ->, fseek..." aria-label="Buscar tópico">
                <kbd class="kbd-hint" aria-hidden="true">/</kbd>
                <div id="search-results" class="search-dropdown"></div>
            </div>
            <button type="button" id="btn-pomodoro" class="pomodoro-pill" title="Timer Pomodoro para estudo focado (Clique: iniciar/pausar, Duplo clique: reiniciar)">
                <span>🍅</span><span id="pomo-clock" class="mono">25:00</span>
            </button>
            <button type="button" id="btn-open-playground" class="playground-open-btn" title="Abrir Compilador / Playground C Interativo">
                <span>⚡</span><span class="pg-lbl-txt">Playground C</span>
            </button>
            <div class="progress-pill" title="Tópicos marcados como concluídos">
                <span id="progress-text">0 / 53 estudados</span>
                <div class="progress-bar-mini"><div id="progress-fill" class="progress-bar-fill"></div></div>
            </div>
            <div class="font-size-controls" role="group" aria-label="Tamanho da fonte">
                <button type="button" id="btn-font-dec" class="font-btn" aria-label="Diminuir texto">A−</button>
                <button type="button" id="btn-font-inc" class="font-btn" aria-label="Aumentar texto">A+</button>
            </div>
            <button type="button" id="btn-search-toggle" class="search-toggle-btn" aria-expanded="false" aria-label="Buscar">🔍</button>
            <button type="button" id="btn-theme-toggle" class="theme-toggle-btn" aria-pressed="false" title="Alternar tema">
                <span id="theme-icon">🌙</span>
                <span id="theme-label">Escuro</span>
            </button>
        </div>
    </div>
    <nav class="nav-bar" aria-label="Módulos de Estudo">
        <div class="nav-tabs" id="nav-tabs">
            <button type="button" class="nav-tab active" data-view="home">Visão Geral</button>
            <span class="nav-sep" aria-hidden="true"></span>
            <button type="button" class="nav-tab" data-view="ponteiros">1. Ponteiros <span class="tab-pill-cnt" id="tab-cnt-ptr">0/18</span></button>
            <button type="button" class="nav-tab" data-view="structs">2. Structs <span class="tab-pill-cnt" id="tab-cnt-strc">0/18</span></button>
            <button type="button" class="nav-tab" data-view="arquivos">3. Arquivos <span class="tab-pill-cnt" id="tab-cnt-arq">0/17</span></button>
            <span class="nav-sep" aria-hidden="true"></span>
            <button type="button" class="nav-tab" data-view="pratica">Central Prática <span class="tab-pill-cnt" id="tab-cnt-prat">0/90</span></button>
            <button type="button" class="nav-tab" data-view="ex-ponteiros">Ex. Ponteiros <span class="tab-pill-cnt">30+10</span></button>
            <button type="button" class="nav-tab" data-view="ex-structs">Ex. Structs <span class="tab-pill-cnt">30+10</span></button>
            <button type="button" class="nav-tab" data-view="ex-arquivos">Ex. Arquivos <span class="tab-pill-cnt">30+10</span></button>
            <span class="nav-sep" aria-hidden="true"></span>
            <button type="button" class="nav-tab" data-view="simulados">Simulados ATP <span class="tab-pill-cnt">3</span></button>
        </div>
    </nav>
    <nav class="mobile-bottom-nav" aria-label="Navegação Mobile">
        <button type="button" class="mbn-btn active" data-view="home"><span class="mbn-icon">🏠</span><span>Início</span></button>
        <button type="button" class="mbn-btn" data-view="ponteiros"><span class="mbn-icon">🎯</span><span>Ponteiros</span></button>
        <button type="button" class="mbn-btn" data-view="structs"><span class="mbn-icon">🧱</span><span>Structs</span></button>
        <button type="button" class="mbn-btn" data-view="arquivos"><span class="mbn-icon">💾</span><span>Arquivos</span></button>
        <button type="button" class="mbn-btn" data-view="pratica"><span class="mbn-icon">✎</span><span>Prática</span></button>
        <button type="button" class="mbn-btn" data-view="simulados"><span class="mbn-icon">⏱</span><span>ATP</span></button>
    </nav>
</header>

<main class="container">
    <!-- HOME -->
    <section id="view-home" class="view-panel active">
        <div class="hero">
            <span class="hero-kicker">ATP • Deitel 6ª Ed. (Caps. 7, 10, 11) • C Completo e Total &amp; Lista IFAM</span>
            <h1>Domine Ponteiros, Structs e Arquivos em C com Rastreio na RAM</h1>
            <p>Explore todos os <strong>53 tópicos completos</strong> com explicação visual de endereços, <em>padding</em> e fluxos <code>FILE *</code>, <strong>rastreios passo a passo interativos</strong>, <strong>3 laboratórios ao vivo</strong>, <strong>90 questões A–E + 30 Certo/Errado + 6 clássicos</strong> e <strong>Playground C com structs e arquivos virtuais</strong>.</p>
            <div class="hero-btns">
                <button type="button" class="btn btn-primary" data-goto-view="ponteiros">Começar por Ponteiros →</button>
                <button type="button" class="btn btn-ghost-light" data-goto-view="pratica">Central Prática (120 Itens)</button>
                <button type="button" class="btn btn-ghost-light" id="btn-hero-playground">⚡ Abrir Playground C</button>
                <button type="button" class="btn btn-primary" style="background:#be123c;" data-goto-view="simulados">Simulados ATP (2h)</button>
            </div>
            <div class="hero-kpi-grid">
                <div class="hero-kpi">
                    <div class="hero-kpi-lbl">Tópicos Estudados</div>
                    <div class="hero-kpi-val" id="kpi-topics-val">0 / 53</div>
                    <div class="hero-kpi-sub" id="kpi-topics-sub">0% da teoria concluída</div>
                </div>
                <div class="hero-kpi">
                    <div class="hero-kpi-lbl">Questões Praticadas</div>
                    <div class="hero-kpi-val" id="kpi-quest-val">0 / 90</div>
                    <div class="hero-kpi-sub" id="kpi-quest-sub">+ 30 Certo/Errado &amp; 6 Clássicos</div>
                </div>
                <div class="hero-kpi">
                    <div class="hero-kpi-lbl">Taxa de Acerto</div>
                    <div class="hero-kpi-val" id="kpi-acc-val">—</div>
                    <div class="hero-kpi-sub" id="kpi-acc-sub">Responda questões para medir</div>
                </div>
                <div class="hero-kpi">
                    <div class="hero-kpi-lbl">Rastreios &amp; Provas</div>
                    <div class="hero-kpi-val" id="kpi-sim-val">53+ &amp; 3 ATP</div>
                    <div class="hero-kpi-sub">Playground C com VFS + Pomodoro</div>
                </div>
            </div>
        </div>

        <div id="home-resume-host"></div>

        <div class="module-grid">
            <div class="mod-card ptr">
                <div>
                    <div class="mod-card-head">
                        <span class="mod-badge">Módulo 1 • 18 Tópicos</span>
                        <span class="mod-icon mono">*p / &amp;x</span>
                    </div>
                    <h3>Ponteiros e Memória Dinâmica</h3>
                    <p>Endereços, <code>&amp;</code> e <code>*</code>, <code>NULL</code>, <code>%p</code>, aritmética escalada, vetores/matrizes/strings, referência, <code>int **</code>, <code>malloc</code>/<code>calloc</code>/<code>realloc</code>/<code>free</code>, <em>leaks</em>, callbacks <code>qsort</code>, <code>void *</code>, <code>const</code> e Valgrind/ASan.</p>
                    <div class="mod-prog-row">
                        <div class="mod-prog-meta"><span id="home-prog-txt-ptr">0 / 18 estudados</span><span id="home-prog-pct-ptr" class="mono">0%</span></div>
                        <div class="cat-progress-track"><div id="home-prog-bar-ptr" class="cat-progress-fill" style="width:0%; background:var(--ptr);"></div></div>
                    </div>
                </div>
                <div class="mod-actions-dual">
                    <button type="button" class="btn btn-primary" style="background:var(--ptr);" data-goto-view="ponteiros">Estudar Teoria →</button>
                    <button type="button" class="btn btn-outline" data-goto-view="ex-ponteiros">Ex. Ponteiros (30)</button>
                </div>
            </div>

            <div class="mod-card strc">
                <div>
                    <div class="mod-card-head">
                        <span class="mod-badge">Módulo 2 • 18 Tópicos</span>
                        <span class="mod-icon mono">. / -&gt;</span>
                    </div>
                    <h3>Structs, Unions e Enums</h3>
                    <p>Registros heterogêneos, <code>typedef</code>, <code>.</code> vs <code>-&gt;</code>, inicialização designada, leitura segura com <code>fgets</code>, vetores/ordenação de structs, aninhamento, <code>union</code>, <code>enum</code>, <em>bit fields</em>, <em>padding</em> e listas encadeadas.</p>
                    <div class="mod-prog-row">
                        <div class="mod-prog-meta"><span id="home-prog-txt-strc">0 / 18 estudados</span><span id="home-prog-pct-strc" class="mono">0%</span></div>
                        <div class="cat-progress-track"><div id="home-prog-bar-strc" class="cat-progress-fill" style="width:0%; background:var(--strc);"></div></div>
                    </div>
                </div>
                <div class="mod-actions-dual">
                    <button type="button" class="btn btn-primary" style="background:var(--strc);" data-goto-view="structs">Estudar Teoria →</button>
                    <button type="button" class="btn btn-outline" data-goto-view="ex-structs">Ex. Structs (30)</button>
                </div>
            </div>

            <div class="mod-card arq">
                <div>
                    <div class="mod-card-head">
                        <span class="mod-badge">Módulo 3 • 17 Tópicos</span>
                        <span class="mod-icon mono">FILE *</span>
                    </div>
                    <h3>Arquivos em C (Texto e Binário)</h3>
                    <p>Persistência, <code>fopen</code>/<code>fclose</code>, modos <code>r/w/a/+</code> e binário, <code>fprintf</code>/<code>fscanf</code>/<code>fgets</code>, armadilha <code>while(!feof())</code>, <code>fwrite</code>/<code>fread</code>, <code>fseek</code>/<code>ftell</code>, <code>errno</code>, <code>fflush</code>, <code>argc/argv</code>, CSV e CRUD.</p>
                    <div class="mod-prog-row">
                        <div class="mod-prog-meta"><span id="home-prog-txt-arq">0 / 17 estudados</span><span id="home-prog-pct-arq" class="mono">0%</span></div>
                        <div class="cat-progress-track"><div id="home-prog-bar-arq" class="cat-progress-fill" style="width:0%; background:var(--arq);"></div></div>
                    </div>
                </div>
                <div class="mod-actions-dual">
                    <button type="button" class="btn btn-primary" style="background:var(--arq);" data-goto-view="arquivos">Estudar Teoria →</button>
                    <button type="button" class="btn btn-outline" data-goto-view="ex-arquivos">Ex. Arquivos (30)</button>
                </div>
            </div>

            <div class="mod-card lab">
                <div>
                    <div class="mod-card-head">
                        <span class="mod-badge">Prática Integrada &amp; Provas ATP</span>
                        <span class="mod-icon">★</span>
                    </div>
                    <h3>90 A–E + 30 Certo/Errado + 3 Provas</h3>
                    <p>Banco categorizado com mapa rápido 1..30, filtro por dificuldade, busca interna, favoritos (★), treino rápido de Certo/Errado e <strong>3 simulados cronometrados de 2h</strong> com corretor automático C + arquivos virtuais.</p>
                </div>
                <div style="display:flex; flex-wrap:wrap; gap:8px;">
                    <button type="button" class="btn btn-lab" style="flex:1 1 100%;" data-goto-view="pratica">Central Prática (90 + 30) →</button>
                    <button type="button" class="btn btn-outline" style="flex:1;" data-goto-view="simulados">3 Simulados ATP</button>
                </div>
            </div>
        </div>

        <div class="cheatsheet-card">
            <div class="cs-head">
                <div>
                    <span class="mod-badge" style="background:var(--lab-bg); color:var(--lab); margin-bottom:4px;">Consulta Rápida Pré-Prova</span>
                    <h2 style="font-size:19px;">Guia Rápido de Bolso — Ponteiros, Structs e Arquivos</h2>
                </div>
                <div class="filter-pills" id="cs-tabs" style="margin:0;"></div>
            </div>
            <div id="cs-body"></div>
        </div>

        <div class="module-header-banner">
            <h2>Estratégia de Estudo Eficiente para ATP</h2>
            <p><strong>1. Veja a RAM antes do código:</strong> use os 3 simuladores ao vivo (Stack/Heap de Ponteiros, Layout/Padding de Structs e Buffer/Seek de Arquivos) e avance os rastreios passo a passo.<br>
            <strong>2. Teste no Playground C:</strong> clique em <em>⚡ Testar Código</em> em qualquer exemplo — agora com suporte a <code>struct</code>, <code>-&gt;</code>, <code>malloc</code> e sistema de arquivos virtual (<code>FILE *</code>)!<br>
            <strong>3. Ative o Timer Pomodoro (🍅):</strong> estude em ciclos de 25 min e use <code>/</code> (ou <code>Ctrl+K</code>) para pesquisar qualquer subtópico instantaneamente.</p>
        </div>
    </section>

    <!-- MÓDULO 1: PONTEIROS -->
    <section id="view-ponteiros" class="view-panel">
        <div class="module-layout">
            <aside class="toc-sidebar" id="sidebar-ponteiros">
                <div class="toc-title">Roteiro — Ponteiros (18)</div>
                <button type="button" class="toc-mobile-toggle" data-toggle-toc="sidebar-ponteiros" aria-expanded="false">
                    <span>☰ Roteiro — Ponteiros (18)</span>
                    <span class="toc-arrow">▾</span>
                </button>
                <div class="toc-list-wrap" id="toc-ponteiros"></div>
            </aside>
            <div>
                <div class="module-header-banner">
                    <h2>Módulo 1 — Ponteiros e Alocação Dinâmica em C</h2>
                    <p>Cobre todos os 18 subtópicos de ATP baseados em <em>Deitel 6ª Ed. Cap. 7</em> e <em>C Completo e Total</em>.</p>
                </div>

                <!-- Micro-Sandbox 1: Stack/Heap Ponteiros -->
                <div class="sandbox-box">
                    <h3 style="font-size:16px; margin-bottom:4px;">Laboratório Interativo: Endereços, Aritmética de Ponteiros e Heap</h3>
                    <p style="font-size:13px; color:var(--text-muted);">Alterne o tipo base e clique nas ações para ver <code>p + k</code> avançar exatamente <code>k * sizeof(tipo)</code> bytes na memória RAM:</p>
                    <div class="filter-pills" id="ptr-sb-controls">
                        <button type="button" class="pill-btn active" data-ptr-type="int">Tipo int (4 bytes)</button>
                        <button type="button" class="pill-btn" data-ptr-type="char">Tipo char (1 byte)</button>
                        <button type="button" class="pill-btn" data-ptr-type="double">Tipo double (8 bytes)</button>
                        <button type="button" class="pill-btn lab-pill" data-ptr-act="prev">← p--</button>
                        <button type="button" class="pill-btn lab-pill" data-ptr-act="next">p++ →</button>
                        <button type="button" class="pill-btn lab-pill" data-ptr-act="incval">(*p) += 10</button>
                        <button type="button" class="pill-btn" data-ptr-act="reset">Reiniciar (&amp;v[0])</button>
                    </div>
                    <div id="ptr-sb-mem" class="mem-strip"></div>
                    <div id="ptr-sb-stats" class="stats-grid"></div>
                </div>

                <div id="content-ponteiros"></div>
            </div>
        </div>
    </section>

    <!-- MÓDULO 2: STRUCTS -->
    <section id="view-structs" class="view-panel strc-theme">
        <div class="module-layout">
            <aside class="toc-sidebar" id="sidebar-structs">
                <div class="toc-title">Roteiro — Structs (18)</div>
                <button type="button" class="toc-mobile-toggle" data-toggle-toc="sidebar-structs" aria-expanded="false">
                    <span>☰ Roteiro — Structs (18)</span>
                    <span class="toc-arrow">▾</span>
                </button>
                <div class="toc-list-wrap" id="toc-structs"></div>
            </aside>
            <div>
                <div class="module-header-banner">
                    <h2>Módulo 2 — Structs, Unions, Enums e Estruturas</h2>
                    <p>Baseado em <em>Deitel 6ª Ed. Cap. 10</em> e nos 54 exercícios de <em>Exercicios_Estruturas_Unioes_Enumeracoes.pdf</em>.</p>
                </div>

                <!-- Micro-Sandbox 2: Layout, Padding & Union -->
                <div class="sandbox-box strc-sb">
                    <h3 style="font-size:16px; margin-bottom:4px;">Laboratório Interativo: Memória <code>struct</code> (Padding) vs <code>union</code> &amp; Operadores <code>.</code> / <code>-&gt;</code></h3>
                    <p style="font-size:13px; color:var(--text-muted);">Compare como a ordem dos campos muda os bytes de preenchimento (<em>padding</em>) em arquiteturas de 32/64 bits e como <code>union</code> compartilha o mesmo endereço:</p>
                    <div class="filter-pills" id="strc-sb-controls">
                        <button type="button" class="pill-btn active" data-strc-mode="unaligned">struct { char a; int b; char c; } (12 B)</button>
                        <button type="button" class="pill-btn" data-strc-mode="packed">struct { int b; char a; char c; } (8 B)</button>
                        <button type="button" class="pill-btn" data-strc-mode="union">union { int b; char a; } (4 B)</button>
                    </div>
                    <div id="strc-sb-mem" class="mem-strip"></div>
                    <div id="strc-sb-stats" class="stats-grid"></div>
                </div>

                <div id="content-structs"></div>
            </div>
        </div>
    </section>

    <!-- MÓDULO 3: ARQUIVOS -->
    <section id="view-arquivos" class="view-panel arq-theme">
        <div class="module-layout">
            <aside class="toc-sidebar" id="sidebar-arquivos">
                <div class="toc-title">Roteiro — Arquivos (17)</div>
                <button type="button" class="toc-mobile-toggle" data-toggle-toc="sidebar-arquivos" aria-expanded="false">
                    <span>☰ Roteiro — Arquivos (17)</span>
                    <span class="toc-arrow">▾</span>
                </button>
                <div class="toc-list-wrap" id="toc-arquivos"></div>
            </aside>
            <div>
                <div class="module-header-banner">
                    <h2>Módulo 3 — Processamento de Arquivos em C (<code>FILE *</code>)</h2>
                    <p>Baseado em <em>Deitel 6ª Ed. Cap. 11</em>: fluxos de texto, acesso direto/binário, erros, buffer e CRUD.</p>
                </div>

                <!-- Micro-Sandbox 3: Modos fopen, Buffer e fseek -->
                <div class="sandbox-box arq-sb">
                    <h3 style="font-size:16px; margin-bottom:4px;">Simulador ao Vivo: Modos <code>fopen</code>, Buffer em RAM e Cursor <code>fseek</code> / <code>ftell</code></h3>
                    <p style="font-size:13px; color:var(--text-muted);">Escolha um modo de abertura e execute operações de E/S para visualizar o cursor de leitura/escrita e a diferença entre buffer na RAM e disco:</p>
                    <div class="filter-pills" id="arq-sb-controls">
                        <button type="button" class="pill-btn active" data-arq-mode="r">Modo "r"</button>
                        <button type="button" class="pill-btn" data-arq-mode="w">Modo "w" (trunca!)</button>
                        <button type="button" class="pill-btn" data-arq-mode="a">Modo "a" (append)</button>
                        <button type="button" class="pill-btn" data-arq-mode="r+">Modo "r+" (R/W)</button>
                        <button type="button" class="pill-btn lab-pill" data-arq-act="read1">fgetc(fp)</button>
                        <button type="button" class="pill-btn lab-pill" data-arq-act="writeX">fputc('X', fp)</button>
                        <button type="button" class="pill-btn lab-pill" data-arq-act="rewind">rewind(fp)</button>
                        <button type="button" class="pill-btn lab-pill" data-arq-act="end">fseek(SEEK_END)</button>
                        <button type="button" class="pill-btn lab-pill" data-arq-act="flush">fflush / fclose</button>
                    </div>
                    <div id="arq-sb-mem" class="mem-strip"></div>
                    <div id="arq-sb-stats" class="stats-grid"></div>
                </div>

                <div id="content-arquivos"></div>
            </div>
        </div>
    </section>

    <!-- CENTRAL PRÁTICA & CERTO/ERRADO -->
    <section id="view-pratica" class="view-panel">
        <div id="pratica-hub-root"></div>
    </section>

    <section id="view-ex-ponteiros" class="view-panel">
        <div id="ex-cat-root-ponteiros"></div>
    </section>

    <section id="view-ex-structs" class="view-panel">
        <div id="ex-cat-root-structs"></div>
    </section>

    <section id="view-ex-arquivos" class="view-panel">
        <div id="ex-cat-root-arquivos"></div>
    </section>

    <section id="view-simulados" class="view-panel">
        <div id="sim-root"></div>
    </section>
</main>

<!-- PLAYGROUND C MODAL -->
<div id="c-playground-modal" class="pg-modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="pg-modal-title">
    <div class="pg-modal">
        <div class="pg-header">
            <div>
                <div style="font-size:11px; font-weight:700; color:#a5b4fc; text-transform:uppercase; letter-spacing:0.06em;">Ambiente Interativo C • Ponteiros + Structs + Arquivos Virtuais (VFS)</div>
                <h3 id="pg-modal-title" style="font-size:16.5px; margin:2px 0 0;">⚡ Playground &amp; Testador de Código C</h3>
            </div>
            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <select id="pg-template-sel" class="itr-speed-sel" style="background:#1e293b; color:#f8fafc; border-color:#475569;" aria-label="Carregar exemplo">
                    <option value="">Carregar exemplo pronto...</option>
                    <option value="ptr">Exemplo 1: Ponteiros + troca(&amp;a, &amp;b) + malloc</option>
                    <option value="strc">Exemplo 2: Struct Aluno + Ponteiro -&gt;</option>
                    <option value="arq">Exemplo 3: Arquivo Virtual (fopen/fprintf/fscanf)</option>
                    <option value="clean">Exemplo 4: Rascunho Limpo (main)</option>
                </select>
                <button type="button" class="btn btn-outline" id="btn-pg-close" style="background:rgba(255,255,255,0.1); color:#fff; border-color:rgba(255,255,255,0.25); padding:6px 12px;">✕ Fechar (Esc)</button>
            </div>
        </div>
        <div class="pg-body">
            <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px; flex-wrap:wrap; gap:6px;">
                    <label class="field-label" for="code-area-pg" style="margin:0;">Código-Fonte em C (edite livremente):</label>
                    <button type="button" class="copy-btn" id="btn-pg-copy">Copiar Código</button>
                </div>
                <div class="c-keybar" aria-label="Atalhos rápidos C">
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="{ }">{ }</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="-&gt;">-&gt;</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="&amp;">&amp;</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="*">*</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val=";">;</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="NULL">NULL</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="sizeof()">sizeof()</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="FILE *fp = fopen(&quot;dados.txt&quot;, &quot;w&quot;);">fopen</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="printf(&quot;%d\n&quot;, );">printf</button>
                    <button type="button" class="c-key-btn" data-ins-target="pg" data-ins-val="scanf(&quot;%d&quot;, &amp;);">scanf</button>
                </div>
                <textarea id="code-area-pg" class="sim-code-area" style="min-height:210px;" spellcheck="false" autocorrect="off" autocapitalize="off"></textarea>
            </div>
            <div class="pg-io-grid">
                <div>
                    <label class="field-label" for="pg-stdin">Entrada Padrão (stdin):</label>
                    <textarea id="pg-stdin" class="sim-text-area mono" style="min-height:105px;" placeholder="Opcional: valores de entrada separados por espaço ou linha..."></textarea>
                </div>
                <div>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                        <span class="field-label" style="margin:0;">Saída do Terminal (stdout):</span>
                        <span id="pg-exec-meta" class="mono" style="font-size:11px; color:var(--text-soft);">Pronto</span>
                    </div>
                    <pre id="pg-stdout" class="pg-console">Clique em "▶ Executar Código C" (ou Ctrl+Enter).</pre>
                </div>
            </div>
            <div id="pg-vfs-wrap" style="display:none;">
                <div class="field-label" style="margin-bottom:4px;">Sistema de Arquivos Virtual (arquivos criados/alterados em memória):</div>
                <pre id="pg-vfs-out" class="pg-console" style="max-height:120px;"></pre>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <span style="font-size:12px; color:var(--text-soft);">Suporta <code>struct</code>, <code>typedef</code>, <code>enum</code>, <code>.</code>/<code>-&gt;</code>, <code>&amp;</code>/<code>*</code>, <code>malloc/calloc/free</code>, <code>&lt;string.h&gt;</code> e <code>FILE *</code> virtual (<code>fopen</code>/<code>fprintf</code>/<code>fscanf</code>/<code>fgets</code>/<code>fwrite</code>/<code>fread</code>/<code>fseek</code>/<code>ftell</code>).</span>
                <button type="button" class="btn btn-lab" id="btn-pg-run" style="padding:9px 20px; font-size:13.5px;">▶ Executar Código C (Ctrl+Enter)</button>
            </div>
        </div>
    </div>
</div>

<button type="button" id="btn-fab-top" class="fab-top" title="Voltar ao topo" aria-label="Voltar ao topo">↑</button>
<div id="toast" class="toast" role="status" aria-live="polite"></div>

<script>
const DATA = __DATA_JSON__;

(function() {
    "use strict";

    const STORAGE_KEY = "ads_c_v4_done_topics";
    const CAT_ANS_KEY = "ads_c_v4_cat_answers";
    const CE_ANS_KEY = "ads_c_v4_ce_answers";
    const FAV_Q_KEY = "ads_c_v4_fav_q";
    const LAST_LOC_KEY = "ads_c_v4_last_loc";
    const THEME_KEY = "ads_c_v4_theme";
    const FONT_KEY = "ads_c_v4_font_size";

    const topicById = {};
    const codeRegistry = {};
    let inlineStates = {};
    let inlineTimers = {};
    let tocOnlyPending = {};
    let catAnswers = {};
    let ceAnswers = {};
    let favQuestions = new Set();
    let catFilters = { ponteiros: "Todas", structs: "Todas", arquivos: "Todas" };
    let catSearchTerms = { ponteiros: "", structs: "", arquivos: "" };
    let openQGabaritos = new Set();
    let ceFilterCat = "todas";
    let curCsTab = DATA.cheatsheet && DATA.cheatsheet[0] ? DATA.cheatsheet[0].id : "cs-ptr";

    // Micro-Sandbox states
    let ptrSbType = "int";
    let ptrSbIdx = 0;
    let ptrSbVals = [10, 20, 30, 40, 50];
    let strcSbMode = "unaligned";
    let arqSbMode = "r";
    let arqSbOpen = true;
    let arqSbBytes = ["A", "T", "P", "-", "C", "\\n"];
    let arqSbCursor = 0;
    let arqSbDirty = false;
    let arqSbEof = false;

    // Pomodoro state
    let pomoSec = 25 * 60;
    let pomoRunning = false;
    let pomoBreak = false;
    let pomoTimer = null;

    function updatePomoUI() {
        const btn = document.getElementById("btn-pomodoro");
        const clk = document.getElementById("pomo-clock");
        if (!btn || !clk) return;
        const m = Math.floor(pomoSec / 60);
        const s = pomoSec % 60;
        clk.textContent = String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0");
        btn.classList.toggle("pomo-active", pomoRunning && !pomoBreak);
        btn.classList.toggle("pomo-break", pomoBreak);
    }

    function togglePomodoro() {
        if (pomoRunning) {
            clearInterval(pomoTimer);
            pomoTimer = null;
            pomoRunning = false;
            updatePomoUI();
            showToast("Pomodoro pausado.");
            return;
        }
        pomoRunning = true;
        updatePomoUI();
        pomoTimer = setInterval(function() {
            if (pomoSec > 0) {
                pomoSec--;
            } else {
                pomoBreak = !pomoBreak;
                pomoSec = pomoBreak ? 5 * 60 : 25 * 60;
                showToast(pomoBreak ? "☕ Ciclo de 25m concluído! Pausa de 5 min." : "🍅 Hora de voltar aos estudos!");
            }
            updatePomoUI();
        }, 1000);
    }

    function resetPomodoro() {
        if (pomoTimer) { clearInterval(pomoTimer); pomoTimer = null; }
        pomoRunning = false;
        pomoBreak = false;
        pomoSec = 25 * 60;
        updatePomoUI();
        showToast("Timer Pomodoro reiniciado (25:00).");
    }

    /* ==================== ENGINE C -> JS v4.1 (PONTEIROS + STRUCTS + VFS FILE *) ==================== */
    function runCProgram(sourceCode, stdinStr) {
        let __stdoutBuf = "";
        let stdinPos = 0;
        const stdinRaw = String(stdinStr || "").replace(/\r\n/g, "\n");
        const __vfs = Object.create(null);
        const __openHandles = [];
        const stdin = { __std: "in" };
        const stdout = { __std: "out" };
        const stderr = { __std: "err" };
        let errno = 0;

        function toCStrArr(str) {
            const arr = [];
            for (let i = 0; i < str.length; i++) arr.push(str.charCodeAt(i));
            arr.push(0);
            arr.__elemSz = 1;
            return arr;
        }

        function fromCStr(val) {
            if (val === null || val === undefined) return "";
            if (typeof val === "string") return val;
            if (val && val.__ptr) {
                let out = "";
                for (let i = val.idx; i < val.base.length; i++) {
                    const ch = val.base[i];
                    if (!ch) break;
                    out += typeof ch === "number" ? String.fromCharCode(ch) : String(ch);
                }
                return out;
            }
            if (Array.isArray(val)) {
                let out = "";
                for (let i = 0; i < val.length; i++) {
                    if (!val[i]) break;
                    out += String.fromCharCode(val[i]);
                }
                return out;
            }
            return String(val);
        }

        function writeIntoArr(dest, str) {
            const target = (dest && dest.__ptr) ? dest.base : dest;
            const start = (dest && dest.__ptr) ? dest.idx : 0;
            for (let i = 0; i < str.length; i++) target[start + i] = str.charCodeAt(i);
            target[start + str.length] = 0;
            return dest;
        }

        function __mkPtr(base, idx) {
            const raw = { __ptr: true, base: base, idx: idx || 0 };
            return new Proxy(raw, {
                get: function(target, prop) {
                    if (prop === "__ptr" || prop === "base" || prop === "idx") return target[prop];
                    if (prop === "valueOf") return function() { return target.idx; };
                    if (typeof prop === "string" && /^\d+$/.test(prop)) {
                        return target.base[target.idx + Number(prop)];
                    }
                    const cur = target.base[target.idx];
                    if (cur && typeof cur === "object" && prop in cur) return cur[prop];
                    return target[prop];
                },
                set: function(target, prop, val) {
                    if (prop === "idx" || prop === "base") { target[prop] = val; return true; }
                    if (typeof prop === "string" && /^\d+$/.test(prop)) {
                        target.base[target.idx + Number(prop)] = val;
                        return true;
                    }
                    const cur = target.base[target.idx];
                    if (cur && typeof cur === "object") { cur[prop] = val; return true; }
                    target[prop] = val;
                    return true;
                }
            });
        }

        function __derefGet(p) {
            if (p && p.__ptr) return p.base[p.idx];
            if (Array.isArray(p)) return p[0];
            return p;
        }
        function __derefSet(p, v) {
            if (p && p.__ptr) { p.base[p.idx] = v; return v; }
            if (Array.isArray(p)) { p[0] = v; return v; }
            return v;
        }
        function __ptrAdd(p, k) {
            if (p && p.__ptr) return __mkPtr(p.base, p.idx + k);
            if (Array.isArray(p)) return __mkPtr(p, k);
            return p + k;
        }
        function __ptrDiff(a, b) {
            const ai = (a && a.__ptr) ? a.idx : (Array.isArray(a) ? 0 : null);
            const bi = (b && b.__ptr) ? b.idx : (Array.isArray(b) ? 0 : null);
            if (ai !== null && bi !== null) return ai - bi;
            return a - b;
        }
        function __ptrStep(p, delta) {
            if (p && p.__ptr) return __mkPtr(p.base, p.idx + delta);
            if (Array.isArray(p)) return __mkPtr(p, delta);
            return Number(p) + delta;
        }
        function __sizeof(v) {
            if (v === null || v === undefined) return 4;
            if (typeof v === "number") return 4;
            if (typeof v === "string") return v.length + 1;
            if (v && v.__ptr) return 8;
            if (Array.isArray(v)) return v.length * (v.__elemSz || 4);
            if (typeof v === "object") return 512;
            return 4;
        }
        function __applyStructInit(obj, meta, initVal) {
            if (!initVal) return obj;
            if (Array.isArray(initVal)) {
                for (let i = 0; i < meta.length && i < initVal.length; i++) {
                    const f = meta[i], v = initVal[i];
                    if (f.arr && f.isChar && typeof v === "string") writeIntoArr(obj[f.name], v);
                    else if (f.subFn && typeof v === "object") obj[f.name] = f.subFn(v);
                    else obj[f.name] = v;
                }
            } else if (typeof initVal === "object") {
                const keys = Object.keys(initVal);
                for (let k = 0; k < keys.length; k++) {
                    const key = keys[k], v = initVal[key];
                    const f = meta.find(function(x) { return x.name === key; });
                    if (f && f.arr && f.isChar && typeof v === "string") writeIntoArr(obj[key], v);
                    else if (f && f.subFn && typeof v === "object") obj[key] = f.subFn(v);
                    else obj[key] = v;
                }
            }
            return obj;
        }

        function readTokenFromStr(src, posObj) {
            while (posObj.pos < src.length && /\s/.test(src[posObj.pos])) posObj.pos++;
            if (posObj.pos >= src.length) return null;
            const start = posObj.pos;
            while (posObj.pos < src.length && !/\s/.test(src[posObj.pos])) posObj.pos++;
            return src.slice(start, posObj.pos);
        }

        function readToken() {
            const p = { pos: stdinPos };
            const tok = readTokenFromStr(stdinRaw, p);
            stdinPos = p.pos;
            return tok;
        }

        function __readInt() { const t = readToken(); return t === null ? 0 : parseInt(t, 10); }
        function __readFloat() { const t = readToken(); return t === null ? 0 : parseFloat(t); }
        function __readChar(skipWs) {
            if (skipWs) while (stdinPos < stdinRaw.length && /\s/.test(stdinRaw[stdinPos])) stdinPos++;
            if (stdinPos >= stdinRaw.length) return 0;
            return stdinRaw.charCodeAt(stdinPos++);
        }
        function __readStr(dest) {
            const tok = readToken();
            writeIntoArr(dest, tok === null ? "" : tok);
            return tok === null ? 0 : 1;
        }

        // Virtual File System helpers
        function fopen(nameRaw, modeRaw) {
            const name = fromCStr(nameRaw);
            const mode = fromCStr(modeRaw);
            const exists = Object.prototype.hasOwnProperty.call(__vfs, name);
            if (mode[0] === "r" && !exists) { errno = 2; return null; }
            if (mode[0] === "w") __vfs[name] = { bytes: [] };
            else if (!exists) __vfs[name] = { bytes: [] };
            const f = __vfs[name];
            const pos = (mode[0] === "a") ? f.bytes.length : 0;
            const fp = { __file: true, name: name, mode: mode, file: f, pos: pos, eof: false, err: false, closed: false };
            __openHandles.push(fp);
            return fp;
        }
        function fclose(fp) {
            if (!fp || fp.closed) return -1;
            fp.closed = true;
            return 0;
        }
        function fflush(fp) { return 0; }
        function setvbuf() { return 0; }
        function strerror(e) { return e ? "Arquivo nao encontrado" : "Sucesso"; }
        function feof(fp) { return (!fp || fp.eof) ? 1 : 0; }
        function ferror(fp) { return (!fp || fp.err) ? 1 : 0; }
        function clearerr(fp) { if (fp) { fp.eof = false; fp.err = false; } }
        function rewind(fp) { if (fp) { fp.pos = 0; fp.eof = false; fp.err = false; } }
        function ftell(fp) { return fp ? fp.pos : -1; }
        function fseek(fp, offset, origin) {
            if (!fp) return -1;
            let base = 0;
            if (origin === 1) base = fp.pos;
            else if (origin === 2) base = fp.file.bytes.length;
            const np = base + offset;
            if (np < 0) return -1;
            fp.pos = np;
            fp.eof = false;
            return 0;
        }
        function removeFile(nameRaw) {
            const n = fromCStr(nameRaw);
            if (Object.prototype.hasOwnProperty.call(__vfs, n)) { delete __vfs[n]; return 0; }
            return -1;
        }
        function renameFile(oldRaw, newRaw) {
            const o = fromCStr(oldRaw), n = fromCStr(newRaw);
            if (!Object.prototype.hasOwnProperty.call(__vfs, o)) return -1;
            __vfs[n] = __vfs[o];
            delete __vfs[o];
            return 0;
        }
        function tmpfile() {
            const tmpName = "__tmp_" + Math.random().toString(36).slice(2, 8);
            return fopen(tmpName, "w+b");
        }
        function fputc(ch, fp) {
            const code = typeof ch === "number" ? (ch & 255) : String(ch).charCodeAt(0);
            if (fp && (fp.__std === "out" || fp.__std === "err")) { __stdoutBuf += String.fromCharCode(code); return code; }
            if (!fp || !fp.file) return -1;
            fp.file.bytes[fp.pos++] = code;
            return code;
        }
        function fputs(s, fp) {
            const txt = fromCStr(s);
            if (fp && (fp.__std === "out" || fp.__std === "err")) { __stdoutBuf += txt; return 0; }
            for (let i = 0; i < txt.length; i++) fputc(txt.charCodeAt(i), fp);
            return 0;
        }
        function fgetc(fp) {
            if (fp && fp.__std === "in") return getchar();
            if (!fp || !fp.file || fp.pos >= fp.file.bytes.length) {
                if (fp) fp.eof = true;
                return -1;
            }
            return fp.file.bytes[fp.pos++];
        }
        function __formatPrintf(f, args, startIdx) {
            let argIdx = startIdx;
            let res = "";
            for (let i = 0; i < f.length; i++) {
                if (f[i] === "%" && i + 1 < f.length) {
                    if (f[i + 1] === "%") { res += "%"; i++; continue; }
                    const m = f.slice(i).match(/^%(-?\d+)?(?:\.(\d+))?(?:ll|hh|l|h|z|t|j)?([dfsxcupigeXo])/);
                    if (m) {
                        const width = m[1] ? parseInt(m[1], 10) : 0;
                        const prec = m[2] !== undefined ? parseInt(m[2], 10) : null;
                        const spec = m[3];
                        const v = args[argIdx++];
                        let s = "";
                        if (spec === "d" || spec === "i" || spec === "u") s = String(Math.trunc(Number(v) || 0));
                        else if (spec === "f" || spec === "g" || spec === "e") s = (Number(v) || 0).toFixed(prec !== null ? prec : (spec === "g" ? 2 : 6));
                        else if (spec === "s") s = fromCStr(v);
                        else if (spec === "c") s = String.fromCharCode(typeof v === "number" ? v : String(v).charCodeAt(0));
                        else if (spec === "x") s = (Math.trunc(Number(v) || 0) >>> 0).toString(16);
                        else if (spec === "X") s = (Math.trunc(Number(v) || 0) >>> 0).toString(16).toUpperCase();
                        else if (spec === "o") s = (Math.trunc(Number(v) || 0) >>> 0).toString(8);
                        else if (spec === "p") s = (v === null || v === undefined) ? "0x0" : ("0x" + (0x1000 + ((v.__ptr ? v.idx * 4 : 0))).toString(16).toUpperCase());
                        if (width > 0 && s.length < width) s = " ".repeat(width - s.length) + s;
                        else if (width < 0 && s.length < -width) s = s + " ".repeat(-width - s.length);
                        res += s;
                        i += m[0].length - 1;
                        continue;
                    }
                }
                res += f[i];
            }
            return res;
        }
        function printf(fmt) { __stdoutBuf += __formatPrintf(fromCStr(fmt), arguments, 1); }
        function fprintf(fp, fmt) {
            const text = __formatPrintf(fromCStr(fmt), arguments, 2);
            if (fp && (fp.__std === "out" || fp.__std === "err")) { __stdoutBuf += text; return text.length; }
            for (let i = 0; i < text.length; i++) fputc(text.charCodeAt(i), fp);
            return text.length;
        }
        function sprintf(dest, fmt) {
            const text = __formatPrintf(fromCStr(fmt), arguments, 2);
            writeIntoArr(dest, text);
            return text.length;
        }
        function snprintf(dest, maxN, fmt) {
            const text = __formatPrintf(fromCStr(fmt), arguments, 3);
            writeIntoArr(dest, text.slice(0, Math.max(0, (maxN || 100) - 1)));
            return text.length;
        }
        function fgets(dest, maxN, stream) {
            if (stream && stream.__file) {
                if (stream.pos >= stream.file.bytes.length) { stream.eof = true; return null; }
                let out = "";
                const limit = Math.max(0, (maxN || 100) - 1);
                while (stream.pos < stream.file.bytes.length && out.length < limit) {
                    const ch = String.fromCharCode(stream.file.bytes[stream.pos++]);
                    out += ch;
                    if (ch === "\n") break;
                }
                writeIntoArr(dest, out);
                return dest;
            }
            if (stdinPos >= stdinRaw.length) return null;
            let out = "";
            const limit = Math.max(0, (maxN || 100) - 1);
            while (stdinPos < stdinRaw.length && out.length < limit) {
                const ch = stdinRaw[stdinPos++];
                out += ch;
                if (ch === "\n") break;
            }
            writeIntoArr(dest, out);
            return dest;
        }
        function getchar() { return stdinPos >= stdinRaw.length ? -1 : stdinRaw.charCodeAt(stdinPos++); }
        function putchar(c) { __stdoutBuf += String.fromCharCode(typeof c === "number" ? c : String(c).charCodeAt(0)); }
        function puts(s) { __stdoutBuf += fromCStr(s) + "\n"; }
        function perror(msg) { __stdoutBuf += fromCStr(msg) + ": " + strerror(errno || 2) + "\n"; }

        // Binary serialization helper for structs/arrays into VFS bytes
        function __serializeItem(val, elemSize) {
            const rawStr = JSON.stringify(val);
            const out = new Array(elemSize).fill(0);
            for (let i = 0; i < rawStr.length && i < elemSize; i++) out[i] = rawStr.charCodeAt(i);
            return out;
        }
        function __deserializeItem(bytesSlice) {
            let s = "";
            for (let i = 0; i < bytesSlice.length; i++) {
                if (bytesSlice[i] === 0) break;
                s += String.fromCharCode(bytesSlice[i]);
            }
            return JSON.parse(s);
        }
        function fwrite(ptr, size, count, fp) {
            if (!fp || fp.closed) return 0;
            const elemSize = Math.max(size || 64, 64);
            let written = 0;
            for (let i = 0; i < count; i++) {
                const item = ptr && ptr.__ptr ? ptr.base[ptr.idx + i] : (Array.isArray(ptr) ? ptr[i] : ptr);
                const chunk = __serializeItem(item, elemSize);
                for (let b = 0; b < chunk.length; b++) fp.file.bytes[fp.pos++] = chunk[b];
                written++;
            }
            return written;
        }
        function fread(ptr, size, count, fp) {
            if (!fp || fp.closed) return 0;
            const elemSize = Math.max(size || 64, 64);
            let readCnt = 0;
            for (let i = 0; i < count; i++) {
                if (fp.pos + elemSize > fp.file.bytes.length) { fp.eof = true; break; }
                const slice = fp.file.bytes.slice(fp.pos, fp.pos + elemSize);
                fp.pos += elemSize;
                const val = __deserializeItem(slice);
                if (ptr && ptr.__ptr) {
                    const dst = ptr.base[ptr.idx + i];
                    if (dst && typeof dst === "object" && !Array.isArray(dst) && typeof val === "object") Object.assign(dst, val);
                    else ptr.base[ptr.idx + i] = val;
                } else if (Array.isArray(ptr)) {
                    ptr[i] = val;
                } else if (ptr && typeof ptr === "object" && typeof val === "object") {
                    Object.assign(ptr, val);
                }
                readCnt++;
            }
            return readCnt;
        }

        // <string.h> & <ctype.h> & <stdlib.h>
        function strlen(s) { return fromCStr(s).length; }
        function strcpy(d, o) { return writeIntoArr(d, fromCStr(o)); }
        function strncpy(d, o, n) {
            const src = fromCStr(o);
            const target = (d && d.__ptr) ? d.base : d;
            const st = (d && d.__ptr) ? d.idx : 0;
            for (let i = 0; i < n; i++) target[st + i] = i < src.length ? src.charCodeAt(i) : 0;
            return d;
        }
        function strcat(d, o) { return writeIntoArr(d, fromCStr(d) + fromCStr(o)); }
        function strcmp(a, b) { const sa = fromCStr(a), sb = fromCStr(b); return sa === sb ? 0 : (sa < sb ? -1 : 1); }
        function strncmp(a, b, n) { const sa = fromCStr(a).slice(0, n), sb = fromCStr(b).slice(0, n); return sa === sb ? 0 : (sa < sb ? -1 : 1); }
        function strcspn(s, rej) {
            const ss = fromCStr(s), rr = fromCStr(rej);
            for (let i = 0; i < ss.length; i++) if (rr.indexOf(ss[i]) !== -1) return i;
            return ss.length;
        }
        function strstr(hay, needle) {
            const h = fromCStr(hay), n = fromCStr(needle);
            const idx = h.indexOf(n);
            if (idx === -1) return null;
            return __mkPtr(toCStrArr(h), idx);
        }
        let __strtokBuf = null, __strtokPos = 0;
        function strtok(s, delim) {
            const d = fromCStr(delim);
            if (s !== null) { __strtokBuf = s; __strtokPos = 0; }
            if (!__strtokBuf) return null;
            const arr = __strtokBuf.__ptr ? __strtokBuf.base : __strtokBuf;
            while (arr[__strtokPos] && d.indexOf(String.fromCharCode(arr[__strtokPos])) !== -1) __strtokPos++;
            if (!arr[__strtokPos]) return null;
            const start = __strtokPos;
            while (arr[__strtokPos] && d.indexOf(String.fromCharCode(arr[__strtokPos])) === -1) __strtokPos++;
            if (arr[__strtokPos]) { arr[__strtokPos] = 0; __strtokPos++; }
            return __mkPtr(arr, start);
        }
        function tolower(c) { return (c >= 65 && c <= 90) ? c + 32 : c; }
        function toupper(c) { return (c >= 97 && c <= 122) ? c - 32 : c; }
        function isalpha(c) { return ((c >= 65 && c <= 90) || (c >= 97 && c <= 122)) ? 1 : 0; }
        function isdigit(c) { return (c >= 48 && c <= 57) ? 1 : 0; }
        function isalnum(c) { return (isalpha(c) || isdigit(c)) ? 1 : 0; }
        function isspace(c) { return (c === 32 || c === 9 || c === 10 || c === 13) ? 1 : 0; }
        function atoi(s) { return parseInt(fromCStr(s), 10) || 0; }
        function atof(s) { return parseFloat(fromCStr(s)) || 0; }
        function malloc(bytes, templateFn) {
            const elemSz = templateFn ? 512 : 4;
            const cnt = Math.max(1, Math.ceil((bytes || elemSz) / elemSz));
            const arr = new Array(cnt);
            for (let i = 0; i < cnt; i++) arr[i] = templateFn ? templateFn() : 0;
            return __mkPtr(arr, 0);
        }
        function calloc(n, sz, templateFn) {
            const cnt = Math.max(1, n || 1);
            const arr = new Array(cnt);
            for (let i = 0; i < cnt; i++) arr[i] = templateFn ? templateFn() : 0;
            return __mkPtr(arr, 0);
        }
        function realloc(ptr, bytes, templateFn) {
            if (!ptr || !ptr.__ptr) return malloc(bytes, templateFn);
            const elemSz = templateFn ? 512 : 4;
            const cnt = Math.max(1, Math.ceil((bytes || elemSz) / elemSz));
            const old = ptr.base;
            const arr = new Array(cnt);
            for (let i = 0; i < cnt; i++) arr[i] = i < old.length ? old[i] : (templateFn ? templateFn() : 0);
            return __mkPtr(arr, 0);
        }
        function free() {}
        function qsort(basePtr, n, sz, cmpFn) {
            const arr = basePtr && basePtr.__ptr ? basePtr.base : basePtr;
            const sub = arr.slice(0, n);
            sub.sort(function(a, b) {
                return cmpFn(__mkPtr([a], 0), __mkPtr([b], 0));
            });
            for (let i = 0; i < n; i++) arr[i] = sub[i];
        }

        function __arr1d(n, init, elemSz) {
            const a = new Array(Math.max(1, n || 64)).fill(0);
            a.__elemSz = elemSz || (typeof init === "string" ? 1 : 4);
            if (Array.isArray(init)) for (let i = 0; i < init.length; i++) a[i] = init[i];
            else if (typeof init === "string") writeIntoArr(a, init);
            return a;
        }
        function __arr2d(r, c, initRows) {
            const a = new Array(Math.max(1, r || 20));
            for (let i = 0; i < a.length; i++) {
                a[i] = new Array(Math.max(1, c || 20)).fill(0);
                if (initRows && Array.isArray(initRows[i])) {
                    for (let j = 0; j < initRows[i].length; j++) a[i][j] = initRows[i][j];
                }
            }
            return a;
        }
        function __fReadToken(fp) {
            if (!fp || !fp.file) return null;
            const b = fp.file.bytes;
            while (fp.pos < b.length && (b[fp.pos] === 32 || b[fp.pos] === 10 || b[fp.pos] === 13 || b[fp.pos] === 9)) fp.pos++;
            if (fp.pos >= b.length) { fp.eof = true; return null; }
            let tok = "";
            while (fp.pos < b.length && b[fp.pos] !== 32 && b[fp.pos] !== 10 && b[fp.pos] !== 13 && b[fp.pos] !== 9) {
                tok += String.fromCharCode(b[fp.pos++]);
            }
            return tok;
        }
        function __fReadInt(fp) { const t = __fReadToken(fp); return t === null ? null : parseInt(t, 10); }
        function __fReadFloat(fp) { const t = __fReadToken(fp); return t === null ? null : parseFloat(t); }
        function __fReadStr(fp, dest) { const t = __fReadToken(fp); if (t === null) return 0; writeIntoArr(dest, t); return 1; }
        function __sReadInt(posObj, s) { const t = readTokenFromStr(s, posObj); return t === null ? null : parseInt(t, 10); }
        function __sReadFloat(posObj, s) { const t = readTokenFromStr(s, posObj); return t === null ? null : parseFloat(t); }
        function __sReadStr(posObj, s, dest) { const t = readTokenFromStr(s, posObj); if (t === null) return 0; writeIntoArr(dest, t); return 1; }

        function __transpileC(raw) {
            let s = raw;
            s = s.replace(/\/\*[\s\S]*?\*\//g, " ");
            s = s.replace(/\/\/[^\n]*/g, " ");
            const strLits = [];
            s = s.replace(/"(?:\\.|[^"\\])*"/g, function(m) {
                const id = "@@STR" + strLits.length + "@@";
                strLits.push(m);
                return id;
            });
            s = s.replace(/'(\\.|[^'\\])'/g, function(_, ch) {
                if (ch === "\\0") return "0";
                if (ch === "\\n") return "10";
                if (ch === "\\r") return "13";
                if (ch === "\\t") return "9";
                if (ch === "\\\\") return "92";
                if (ch === "\\'") return "39";
                return String(ch.charCodeAt(0));
            });
            s = s.replace(/^\s*#include[^\n]*$/gm, "");
            s = s.replace(/^\s*#define\s+([A-Za-z_]\w*)\s+([^\n]+)$/gm, "const $1 = $2;");
            s = s.replace(/\bSEEK_SET\b/g, "0").replace(/\bSEEK_CUR\b/g, "1").replace(/\bSEEK_END\b/g, "2")
                 .replace(/\bEOF\b/g, "-1").replace(/\bNULL\b/g, "null")
                 .replace(/\bEXIT_SUCCESS\b/g, "0").replace(/\bEXIT_FAILURE\b/g, "1")
                 .replace(/\bBUFSIZ\b/g, "512").replace(/\b_IOFBF\b/g, "0").replace(/\b_IOLBF\b/g, "1").replace(/\b_IONBF\b/g, "2");
            // Strip C numeric suffixes (e.g., 1.65f, 7.0f, 10UL, 0L)
            s = s.replace(/\b(\d+(?:\.\d+)?)[fFlLuU]+\b/g, "$1");
            // Rename C identifier 'in' (reserved JS keyword) safely outside member access
            s = s.replace(/(?<![.\w>])\bin\b(?!\s*:)/g, "__c_in");

            // Enum definitions (also track enum type names)
            const enumNames = [];
            s = s.replace(/\b(?:typedef\s+)?enum(?:\s+([A-Za-z_]\w*))?\s*\{([^}]*)\}\s*([A-Za-z_]\w*)?\s*;/g, function(_, tag, body, alias) {
                if (tag && enumNames.indexOf(tag) === -1) enumNames.push(tag);
                if (alias && enumNames.indexOf(alias) === -1) enumNames.push(alias);
                let nextVal = 0;
                const items = body.split(",").map(function(x) { return x.trim(); }).filter(Boolean);
                return items.map(function(it) {
                    const eq = it.split("=");
                    const name = eq[0].trim();
                    if (eq.length > 1) nextVal = parseInt(eq[1].trim(), 10) || 0;
                    const stmt = "const " + name + " = " + nextVal + ";";
                    nextVal++;
                    return stmt;
                }).join(" ");
            });

            function __splitTopArgs(str) {
                const out = [];
                let cur = "", dP = 0, dB = 0, dK = 0;
                for (let i = 0; i < str.length; i++) {
                    const ch = str[i];
                    if (ch === "(") dP++; else if (ch === ")") dP--;
                    else if (ch === "{") dB++; else if (ch === "}") dB--;
                    else if (ch === "[") dK++; else if (ch === "]") dK--;
                    if (ch === "," && dP === 0 && dB === 0 && dK === 0) { out.push(cur.trim()); cur = ""; }
                    else cur += ch;
                }
                if (cur.trim()) out.push(cur.trim());
                return out;
            }

            // Collect struct/union definitions (including nested anonymous structs/unions inside structs!)
            const structNames = [];
            const structFactories = [];
            let __anonIdx = 0;
            function parseStructBody(body) {
                const fields = [];
                const stmts = body.split(";").map(function(x) { return x.trim(); }).filter(Boolean);
                for (let i = 0; i < stmts.length; i++) {
                    let st = stmts[i].replace(/\s*:\s*\d+\s*$/, "").trim(); // strip bit-fields
                    const mArr = st.match(/([A-Za-z_]\w*)\s*\[([^\]]+)\]$/);
                    if (mArr) {
                        const isChar = /\bchar\b/.test(st);
                        fields.push({ name: mArr[1], arr: mArr[2], isChar: isChar, subType: null });
                    } else {
                        let subType = null;
                        for (let si = 0; si < structNames.length; si++) {
                            if (new RegExp("^\\s*(?:struct|union)?\\s*" + structNames[si] + "\\b").test(st) && st.indexOf("*") === -1) {
                                subType = structNames[si];
                                break;
                            }
                        }
                        const cleaned = st.replace(/^\s*(?:(?:const|unsigned|signed)\s+|(?:struct|union|enum)\s+\w+\s+|[A-Za-z_]\w*\s+(?=[A-Za-z_*]))+/, "");
                        const parts = cleaned.split(",");
                        for (let p = 0; p < parts.length; p++) {
                            const fn = parts[p].replace(/\*/g, "").trim();
                            if (/^[A-Za-z_]\w*$/.test(fn)) fields.push({ name: fn, arr: null, isChar: false, subType: subType });
                        }
                    }
                }
                return fields;
            }
            function registerStructDef(tag, body, alias) {
                const name = alias || tag;
                const fields = parseStructBody(body);
                if (alias && structNames.indexOf(alias) === -1) structNames.push(alias);
                if (tag && structNames.indexOf(tag) === -1) structNames.push(tag);
                const metaArr = "[" + fields.map(function(f) {
                    return "{ name: '" + f.name + "', arr: " + (f.arr ? "true" : "false") + ", isChar: " + (f.isChar ? "true" : "false") + ", subFn: " + (f.subType ? "__make_" + f.subType : "null") + " }";
                }).join(", ") + "]";
                const props = fields.map(function(f) {
                    if (f.arr) return f.name + ": __arr1d(" + f.arr + ", null, " + (f.isChar ? 1 : 4) + ")";
                    if (f.subType) return f.name + ": __make_" + f.subType + "()";
                    return f.name + ": 0";
                }).join(", ");
                structFactories.push("function __make_" + name + "(initVal) { const obj = { " + props + " }; return __applyStructInit(obj, " + metaArr + ", initVal); }");
                if (tag && alias && tag !== alias) {
                    structFactories.push("function __make_" + tag + "(initVal) { return __make_" + alias + "(initVal); }");
                }
            }
            // Extract ONLY inner anonymous struct/union blocks inside an outer struct/union (brace depth >= 1)
            for (let pass = 0; pass < 4; pass++) {
                const before = s;
                s = s.replace(/\b(struct|union)(?:\s+[A-Za-z_]\w*)?\s*\{([^{}]*)\}\s*([A-Za-z_]\w*)\s*;/g, function(full, kw, body, varName, offset, fullStr) {
                    const prefix = fullStr.slice(0, offset);
                    const depth = (prefix.match(/\{/g) || []).length - (prefix.match(/\}/g) || []).length;
                    if (depth < 1) return full;
                    const anonName = "__Anon" + (++__anonIdx);
                    registerStructDef(null, body, anonName);
                    return anonName + " " + varName + ";";
                });
                if (s === before) break;
            }
            s = s.replace(/\btypedef\s+(?:struct|union)(?:\s+([A-Za-z_]\w*))?\s*\{([^{}]*)\}\s*([A-Za-z_]\w*)\s*;/g, function(_, tag, body, alias) {
                registerStructDef(tag, body, alias);
                return "";
            });
            s = s.replace(/\b(?:struct|union)\s+([A-Za-z_]\w*)\s*\{([^{}]*)\}\s*;/g, function(_, tag, body) {
                registerStructDef(tag, body, null);
                return "";
            });

            // Convert C99 compound literals: (StructName){ ... } BEFORE cast removal!
            if (structNames.length > 0) {
                const clRe = new RegExp("\\(\\s*(?:struct\\s+)?(" + structNames.join("|") + ")\\s*\\)\\s*\\{([^{}]*)\\}", "g");
                s = s.replace(clRe, function(_, stType, inner) {
                    const fBody = inner.replace(/\.\s*([A-Za-z_]\w*)\s*=/g, "$1:");
                    if (fBody.indexOf(":") !== -1) return "__make_" + stType + "({" + fBody + "})";
                    return "__make_" + stType + "([" + fBody + "])";
                });
            }

            // Handle malloc/calloc/realloc with sizeof(StructName) before turning sizeof into bytes
            structNames.forEach(function(sn) {
                const szRe = new RegExp("\\bsizeof\\s*\\(\\s*(?:struct\\s+)?" + sn + "\\s*\\)");
                s = s.replace(/\b(malloc)\s*\(((?:[^()]|\([^()]*\))*)\)/g, function(all, fn, arg) {
                    return szRe.test(arg) ? (fn + "(" + arg + ", __make_" + sn + ")") : all;
                });
                s = s.replace(/\b(realloc)\s*\(((?:[^(),]|\([^()]*\))*),((?:[^()]|\([^()]*\))*)\)/g, function(all, fn, pArg, szArg) {
                    return szRe.test(szArg) ? (fn + "(" + pArg + ", " + szArg + ", __make_" + sn + ")") : all;
                });
                s = s.replace(/\b(calloc)\s*\(((?:[^(),]|\([^()]*\))*),((?:[^()]|\([^()]*\))*)\)/g, function(all, nArg, szArg) {
                    return szRe.test(szArg) ? ("calloc(" + nArg + ", " + szArg + ", __make_" + sn + ")") : all;
                });
            });

            // Handle sizeof(*ptr) / sizeof(Type) before removing casts, and convert remaining sizeof(expr) to __sizeof(expr)
            s = s.replace(/\bsizeof\s*\(\s*\*+[^()]+\)/g, "4");
            s = s.replace(/\bsizeof\s*\(\s*(?:(?:struct|union|enum)\s+)?([A-Za-z_]\w*)\s*(\*+)?\s*\)/g, function(_, t, ptr) {
                if (ptr) return "8";
                if (t === "char") return "1";
                if (t === "int" || t === "float") return "4";
                if (t === "double" || t === "long") return "8";
                if (structNames.indexOf(t) !== -1) return "512";
                if (enumNames.indexOf(t) !== -1) return "4";
                return "__sizeof(" + t + ")";
            });
            s = s.replace(/\bsizeof\s*\(([^()]+)\)/g, "__sizeof($1)");
            s = s.replace(/\bremove\s*\(/g, "removeFile(").replace(/\brename\s*\(/g, "renameFile(");

            // Replace known C casts safely without touching (op)(3, 4) or (turma + i), including (void *)&x
            const knownTypesList = ["void", "int", "float", "double", "char", "long", "short", "size_t", "ptrdiff_t", "bool", "_Bool", "FILE"].concat(structNames).concat(enumNames);
            const castRe = new RegExp("\\(\\s*(?:const\\s+|unsigned\\s+|signed\\s+|struct\\s+|union\\s+|enum\\s+)*(?:" + knownTypesList.join("|") + ")(?:\\s+(?:const|unsigned|signed))*(?:\\s*\\*+)?\\s*\\)\\s*(?=[A-Za-z_(0-9&*+\\-])", "g");
            s = s.replace(castRe, "");

            // Strict C type pattern (NEVER matches control keywords like 'else')
            const extraTypes = structNames.concat(enumNames);
            const extraAlt = extraTypes.length ? ("|" + extraTypes.join("|")) : "";
            const cBuiltinType = "(?:(?:const\\s+|unsigned\\s+|signed\\s+)*(?:void|int|float|double|char|long|short|size_t|ptrdiff_t|bool|_Bool|FILE|(?:struct|union|enum)\\s+[A-Za-z_]\\w*" + extraAlt + "))";
            s = s.replace(new RegExp("\\b" + cBuiltinType + "\\s*\\(\\s*\\*\\s*([A-Za-z_]\\w*)\\s*\\)\\s*\\([^)]*\\)\\s*=\\s*([^;]+);", "g"), "let $1 = $2;");

            // Prototypes (supports *cria, **alocar_matriz, and nested fn ptr/array params)
            s = s.replace(new RegExp("^\\s*" + cBuiltinType + "(?:\\s+|\\s*\\*+\\s*)([A-Za-z_]\\w*)\\s*\\((?:[^()]|\\([^()]*\\))*\\)\\s*;", "gm"), "");

            // Track pointer variables (including pointer params and locals!)
            const ptrVars = new Set();
            function addPtrVar(nm) { if (nm && /^[A-Za-z_]\w*$/.test(nm)) ptrVars.add(nm); }
            // Function definitions (supports *cria, **alocar_matriz, int (*m)[3], callbacks)
            s = s.replace(new RegExp("\\b" + cBuiltinType + "(?:\\s+|\\s*\\*+\\s*)([A-Za-z_]\\w*)\\s*\\(((?:[^()]|\\([^()]*\\))*)\\)\\s*\\{", "g"), function(_, fnName, params) {
                const pClean = params.trim() === "void" || params.trim() === "" ? "" :
                    params.split(",").map(function(p) {
                        const tp = p.trim();
                        const mFnPtr = tp.match(/\(\s*\*\s*([A-Za-z_]\w*)\s*\)/);
                        if (mFnPtr) return mFnPtr[1];
                        const m = tp.replace(/\[[^\]]*\]/g, "").trim().match(/([A-Za-z_]\w*)$/);
                        if (m && tp.indexOf("*") !== -1 && tp.indexOf("(*") === -1) addPtrVar(m[1]);
                        return m ? m[1] : "";
                    }).filter(Boolean).join(", ");
                return "function " + fnName + "(" + pClean + ") {";
            });

            // Track struct variable names (non-pointer struct values & arrays)
            const structVars = new Set();
            if (structNames.length > 0) {
                const svRe = new RegExp("\\b(?:struct\\s+|union\\s+)?(?:" + structNames.join("|") + ")\\s+([^;{}]+);", "g");
                let m;
                while ((m = svRe.exec(s)) !== null) {
                    __splitTopArgs(m[1]).forEach(function(item) {
                        const isPtr = /^\*/.test(item.trim());
                        const nm = item.replace(/^\*+\s*(?:const\s+)?/, "").split(/[=\[]/)[0].trim();
                        if (/^[A-Za-z_]\w*$/.test(nm)) {
                            if (isPtr) addPtrVar(nm);
                            else structVars.add(nm);
                        }
                    });
                }
            }

            // Track array variable names so &v[0] -> __mkPtr(v, 0) and arrays are never scalar-boxed
            const arrVars = new Set();
            {
                const arRe = new RegExp("\\b" + cBuiltinType + "\\s+([^;{}]+);", "g");
                let m;
                while ((m = arRe.exec(s)) !== null) {
                    __splitTopArgs(m[1]).forEach(function(item) {
                        const t = item.trim();
                        const mAr = t.match(/^([A-Za-z_]\w*)\s*\[/);
                        if (mAr && /^[A-Za-z_]\w*$/.test(mAr[1])) arrVars.add(mAr[1]);
                        else if (/^\*/.test(t)) {
                            const pn = t.replace(/^\*+\s*(?:const\s+)?/, "").split("=")[0].trim();
                            addPtrVar(pn);
                        }
                    });
                }
            }

            // Detect scalar/pointer variables whose &x is passed outside scanf/fscanf/sscanf/fwrite/fread (NOT && !)
            const addrVars = new Set();
            const safeCallMasks = s.replace(/\b(?:scanf|fscanf|fwrite|fread|sscanf)\s*\((?:[^()]|\([^()]*\))*\)/g, " ");
            const ampRe = /(?:^|[^&])&\s*([A-Za-z_]\w*)(?!\s*\[|\s*\.)/g;
            let ampM;
            while ((ampM = ampRe.exec(safeCallMasks)) !== null) {
                const vn = ampM[1];
                if (!structVars.has(vn) && !arrVars.has(vn)) addrVars.add(vn);
            }

            // for (Type *cur = ...; ...) and for (int i = ...; ...)
            if (structNames.length > 0) {
                s = s.replace(new RegExp("\\bfor\\s*\\(\\s*(?:struct\\s+)?(?:" + structNames.join("|") + ")\\s*\\*?\\s*", "g"), "for (let ");
            }
            s = s.replace(new RegExp("\\bfor\\s*\\(\\s*" + cBuiltinType + "\\s*\\*?\\s*", "g"), "for (let ");

            // 2D arrays with optional initializer ({{1,2},{3,4}} or {0})
            s = s.replace(new RegExp("\\b" + cBuiltinType + "\\s+([A-Za-z_]\\w*)\\s*\\[([^\\]]+)\\]\\s*\\[([^\\]]+)\\]\\s*=\\s*\\{((?:[^{}]|\\{[^{}]*\\})*)\\}\\s*;", "g"), function(_, name, r, c, initInner) {
                if (initInner.indexOf("{") !== -1) {
                    const jsRows = initInner.replace(/\{([^{}]*)\}/g, "[$1]");
                    return "let " + name + " = __arr2d(" + r + ", " + c + ", [" + jsRows + "]);";
                }
                return "let " + name + " = __arr2d(" + r + ", " + c + ");";
            });
            s = s.replace(new RegExp("\\b" + cBuiltinType + "\\s+([A-Za-z_]\\w*)\\s*\\[([^\\]]+)\\]\\s*\\[([^\\]]+)\\]\\s*;", "g"), "let $1 = __arr2d($2, $3);");

            // Struct variable declarations (including nested/positional/designated init & struct arrays)
            if (structNames.length > 0) {
                const stRegex = new RegExp("\\b(?:struct\\s+|union\\s+)?(" + structNames.join("|") + ")\\s+([^;]+);", "g");
                s = s.replace(stRegex, function(_, stType, declList) {
                    const parts = __splitTopArgs(declList);
                    return parts.map(function(p) {
                        const isPtrDecl = /^\s*\*/.test(p);
                        const cleanP = p.replace(/^\*+\s*(?:const\s+)?/, "").trim();
                        if (isPtrDecl) addPtrVar(cleanP.split("=")[0].trim());
                        const mArrInit = cleanP.match(/^([A-Za-z_]\w*)\s*\[([^\]]*)\]\s*=\s*\{([\s\S]*)\}$/);
                        if (mArrInit) {
                            const items = __splitTopArgs(mArrInit[3]).map(function(it) {
                                const inBody = it.trim().replace(/^\{|\}$/g, "").replace(/\.\s*([A-Za-z_]\w*)\s*=/g, "$1:");
                                if (inBody.indexOf(":") !== -1) return "__make_" + stType + "({" + inBody + "})";
                                return "__make_" + stType + "([" + inBody + "])";
                            });
                            return "let " + mArrInit[1] + " = [" + items.join(", ") + "];";
                        }
                        const mArr = cleanP.match(/^([A-Za-z_]\w*)\s*\[([^\]]+)\]$/);
                        if (mArr) return "let " + mArr[1] + " = Array.from({length:" + mArr[2] + "}, function(){ return __make_" + stType + "(); });";
                        const mInit = cleanP.match(/^([A-Za-z_]\w*)\s*=\s*\{([\s\S]*)\}$/);
                        if (mInit) {
                            const fieldsBody = mInit[2].replace(/\.\s*([A-Za-z_]\w*)\s*=/g, "$1:");
                            if (fieldsBody.indexOf(":") !== -1) {
                                return "let " + mInit[1] + " = __make_" + stType + "({" + fieldsBody + "});";
                            }
                            const posBody = fieldsBody.replace(/\{([^{}:]*)\}/g, "[$1]");
                            return "let " + mInit[1] + " = __make_" + stType + "([" + posBody + "]);";
                        }
                        if (cleanP.indexOf("=") !== -1) {
                            let rhs = cleanP.slice(cleanP.indexOf("=") + 1).trim();
                            const lhs = cleanP.slice(0, cleanP.indexOf("=")).trim();
                            if (isPtrDecl && rhs.indexOf("malloc(") !== -1 && rhs.indexOf("__make_") === -1) {
                                rhs = rhs.replace(/malloc\(([^)]+)\)/, "malloc(512, __make_" + stType + ")");
                            }
                            if (isPtrDecl && addrVars.has(lhs)) return "let __box_" + lhs + " = [" + rhs + "];";
                            return "let " + lhs + " = " + rhs + ";";
                        }
                        if (isPtrDecl && addrVars.has(cleanP)) return "let __box_" + cleanP + " = [null];";
                        return "let " + cleanP + " = " + (isPtrDecl ? "null" : ("__make_" + stType + "()")) + ";";
                    }).join(" ");
                });
            }

            // Standard scalar/1D/pointer declarations (now includes void * and enum types!)
            const scalarDeclAlt = enumNames.length ? ("|" + enumNames.join("|")) : "";
            s = s.replace(new RegExp("\\b(?:const\\s+)?(?:unsigned\\s+|signed\\s+)?(?:void|int|float|double|char|long|short|size_t|ptrdiff_t|bool|_Bool|FILE" + scalarDeclAlt + ")\\s+([^;]+);", "g"), function(_, declList) {
                const parts = __splitTopArgs(declList);
                return parts.map(function(p) {
                    const isPtrDecl = /^\s*\*+/.test(p);
                    const cp = p.replace(/^\*+\s*(?:const\s+)?/, "").trim();
                    let m = cp.match(/^([A-Za-z_]\w*)\s*\[([^\]]*)\]\s*=\s*\{([^}]*)\}$/);
                    if (m) return "let " + m[1] + " = __arr1d(" + (m[2] || "64") + ", [" + m[3] + "]);";
                    m = cp.match(/^([A-Za-z_]\w*)\s*\[([^\]]*)\]\s*=\s*(@@STR\d+@@)$/);
                    if (m) return "let " + m[1] + " = __arr1d(" + (m[2] || "64") + ", " + m[3] + ", 1);";
                    m = cp.match(/^([A-Za-z_]\w*)\s*\[([^\]]*)\]$/);
                    if (m) return "let " + m[1] + " = __arr1d(" + (m[2] || "64") + ");";
                    const eqIdx = cp.indexOf("=");
                    const vName = (eqIdx !== -1 ? cp.slice(0, eqIdx) : cp).trim();
                    let vInit = eqIdx !== -1 ? cp.slice(eqIdx + 1).trim() : (isPtrDecl ? "null" : "0");
                    if (isPtrDecl) {
                        addPtrVar(vName);
                        if (/^@@STR\d+@@$/.test(vInit)) vInit = "__mkPtr(toCStrArr(" + vInit + "), 0)";
                        else if (arrVars.has(vInit)) vInit = "__mkPtr(" + vInit + ", 0)";
                    }
                    if (addrVars.has(vName)) {
                        return "let __box_" + vName + " = [" + vInit + "];";
                    }
                    return "let " + vName + " = " + vInit + ";";
                }).join(" ");
            });

            // Simplify *(&x) and *&x before pointer/deref passes
            s = s.replace(/\*\s*\(\s*&\s*([A-Za-z_]\w*)\s*\)/g, "$1").replace(/\*&\s*([A-Za-z_]\w*)/g, "$1");
            // Convert &arr[idx] -> __mkPtr(arr, idx) (ignore && !)
            s = s.replace(/(^|[^&])&\s*([A-Za-z_]\w*)\s*\[([^\]]+)\]/g, "$1__mkPtr($2, $3)");

            // Struct & Pointer operators
            s = s.replace(/->/g, ".");
            s = s.replace(/\(\s*([A-Za-z_]\w*)\s*\+\s*([^()]+)\)\s*\./g, "__ptrAdd($1, $2).");

            // Double pointers & 2D array pointer notation: *(*(m + i) + j), **pp += expr, **pp = expr, (*pp)[i]
            s = s.replace(/\*\s*\(\s*\*\s*\(\s*([A-Za-z_]\w*)\s*\+\s*([^()]+)\)\s*\+\s*([^()]+)\)\s*=\s*([^;]+);/g, "$1[$2][$3] = $4;");
            s = s.replace(/\*\s*\(\s*\*\s*\(\s*([A-Za-z_]\w*)\s*\+\s*([^()]+)\)\s*\+\s*([^()]+)\)/g, "$1[$2][$3]");
            s = s.replace(/(^|[;\n{\s])\*\*([A-Za-z_]\w*)\s*([+\-*\/])=\s*([^;]+);/gm, "$1__derefSet(__derefGet($2), __derefGet(__derefGet($2)) $3 ($4));");
            s = s.replace(/(^|[;\n{\s])\*\*([A-Za-z_]\w*)\s*=\s*([^;]+);/gm, "$1__derefSet(__derefGet($2), $3);");
            s = s.replace(/\*\*([A-Za-z_]\w*)/g, "__derefGet(__derefGet($1))");
            s = s.replace(/\(\s*\*([A-Za-z_]\w*)\s*\)\s*\[([^\]]+)\]/g, "__derefGet($1)[$2]");

            // Rewrite *p++ (post-inc deref), (*p)++, *p += expr;, *p = expr;, and *(ptr + idx)
            s = s.replace(/\*([A-Za-z_]\w*)\+\+/g, "(function(){ const __v = __derefGet($1); $1 = __ptrStep($1, 1); return __v; })()");
            s = s.replace(/\(\s*\*([A-Za-z_]\w*)\s*\)\s*\+\+/g, "__derefSet($1, __derefGet($1) + 1)");
            s = s.replace(/\(\s*\*([A-Za-z_]\w*)\s*\)\s*--/g, "__derefSet($1, __derefGet($1) - 1)");
            s = s.replace(/\*\s*\(\s*([A-Za-z_]\w*)\s*\+\s*([^)]+)\)\s*=\s*([^;]+);/g, "__derefSet(__ptrAdd($1, $2), $3);");
            s = s.replace(/\*\s*\(\s*([A-Za-z_]\w*)\s*\+\s*([^)]+)\)/g, "__derefGet(__ptrAdd($1, $2))");
            s = s.replace(/\*\s*\(\s*([A-Za-z_]\w*)\s*\)/g, "__derefGet($1)");
            s = s.replace(/(^|[;\n{\s])\*([A-Za-z_]\w*)\s*([+\-*\/])=\s*([^;]+);/gm, "$1__derefSet($2, __derefGet($2) $3 ($4));");
            s = s.replace(/(^|[;\n{\s])\*([A-Za-z_]\w*)\s*=\s*([^;]+);/gm, "$1__derefSet($2, $3);");
            s = s.replace(/([=(,\[\s?:!<>+\-\/])\*([A-Za-z_]\w*)(?!\s*=[^=])/g, "$1__derefGet($2)");

            // Pointer arithmetic on known pointer variables AND array decay (p++, p--, p1 + k, s + 3, p2 - p1)
            const allPtrOrArr = Array.from(new Set([].concat(Array.from(ptrVars), Array.from(arrVars))));
            if (ptrVars.size > 0) {
                const pvPat = Array.from(ptrVars).join("|");
                s = s.replace(new RegExp("\\b(" + pvPat + ")\\s*\\+\\+", "g"), "($1 = __ptrStep($1, 1))");
                s = s.replace(new RegExp("\\b(" + pvPat + ")\\s*--", "g"), "($1 = __ptrStep($1, -1))");
                s = s.replace(new RegExp("\\b(" + pvPat + ")\\s*-\\s*(" + pvPat + ")\\b", "g"), "__ptrDiff($1, $2)");
            }
            if (allPtrOrArr.length > 0) {
                const apPat = allPtrOrArr.join("|");
                s = s.replace(new RegExp("\\b(" + apPat + ")\\s*\\+\\s*([A-Za-z_0-9]+(?:\\s*-\\s*[A-Za-z_0-9]+)?)(?!\\s*\\])", "g"), "__ptrAdd($1, $2)");
            }

            // Convert scanf(...), fscanf(...), sscanf(...) WHILE strings are STILL stashed as @@STRn@@!
            s = s.replace(/\bscanf\s*\(\s*(@@STR\d+@@)\s*,((?:[^()]|\([^()]*\))*)\)/g, function(_, fmtId, argsStr) {
                const fmt = strLits[Number(fmtId.replace(/@@STR|@@/g, ""))].slice(1, -1);
                const specs = fmt.match(/\s*%[a-zA-Z0-9]+/g) || [];
                const args = __splitTopArgs(argsStr);
                const stmts = [];
                for (let i = 0; i < specs.length && i < args.length; i++) {
                    const sp = specs[i];
                    const cleanVar = args[i].replace(/^&\s*/, "");
                    const ptrOff = cleanVar.match(/^([A-Za-z_]\w*)\s*\+\s*([A-Za-z_]\w*|\d+)$/);
                    const ptrAddCall = cleanVar.match(/^__ptrAdd\(([^)]+)\)$/);
                    const writeExpr = function(valExpr) {
                        if (ptrOff) return "__derefSet(__ptrAdd(" + ptrOff[1] + ", " + ptrOff[2] + "), " + valExpr + ");";
                        if (ptrAddCall && cleanVar.indexOf(".") === -1) return "__derefSet(" + cleanVar + ", " + valExpr + ");";
                        return cleanVar + " = " + valExpr + ";";
                    };
                    if (sp.indexOf("d") !== -1 || sp.indexOf("i") !== -1 || sp.indexOf("u") !== -1) stmts.push(writeExpr("__readInt()"));
                    else if (sp.indexOf("f") !== -1 || sp.indexOf("lf") !== -1) stmts.push(writeExpr("__readFloat()"));
                    else if (sp.indexOf("s") !== -1) stmts.push("__readStr(" + cleanVar + ");");
                    else if (sp.indexOf("c") !== -1) stmts.push(writeExpr("__readChar(" + (sp[0] === " " ? "true" : "false") + ")"));
                }
                return "(function(){ " + stmts.join(" ") + " return " + Math.min(specs.length, args.length) + "; })()";
            });

            s = s.replace(/\bfscanf\s*\(\s*([A-Za-z_]\w*)\s*,\s*(@@STR\d+@@)\s*,((?:[^()]|\([^()]*\))*)\)/g, function(_, fpVar, fmtId, argsStr) {
                const fmt = strLits[Number(fmtId.replace(/@@STR|@@/g, ""))].slice(1, -1);
                const specs = fmt.match(/\s*%[a-zA-Z0-9]+/g) || [];
                const args = __splitTopArgs(argsStr).map(function(a) { return a.replace(/^&\s*/, ""); });
                const reads = [];
                for (let i = 0; i < specs.length && i < args.length; i++) {
                    const sp = specs[i];
                    if (sp.indexOf("d") !== -1) reads.push("((__tv = __fReadInt(" + fpVar + ")) !== null ? (" + args[i] + " = __tv, 1) : 0)");
                    else if (sp.indexOf("f") !== -1) reads.push("((__tv = __fReadFloat(" + fpVar + ")) !== null ? (" + args[i] + " = __tv, 1) : 0)");
                    else reads.push("__fReadStr(" + fpVar + ", " + args[i] + ")");
                }
                return "(function(){ let __tv, __ok=0; " + reads.map(function(r) { return "__ok += " + r + ";"; }).join(" ") + " return __ok === " + specs.length + " ? " + specs.length + " : -1; })()";
            });

            s = s.replace(/\bsscanf\s*\(\s*([A-Za-z_]\w*(?:\([^)]*\))?)\s*,\s*(@@STR\d+@@)\s*,((?:[^()]|\([^()]*\))*)\)/g, function(_, srcVar, fmtId, argsStr) {
                const fmt = strLits[Number(fmtId.replace(/@@STR|@@/g, ""))].slice(1, -1);
                const specs = fmt.match(/\s*%[a-zA-Z0-9]+/g) || [];
                const args = __splitTopArgs(argsStr).map(function(a) { return a.replace(/^&\s*/, ""); });
                const reads = [];
                for (let i = 0; i < specs.length && i < args.length; i++) {
                    const sp = specs[i];
                    if (sp.indexOf("d") !== -1) reads.push("((__tv = __sReadInt(__sp, __ss)) !== null ? (" + args[i] + " = __tv, 1) : 0)");
                    else if (sp.indexOf("f") !== -1) reads.push("((__tv = __sReadFloat(__sp, __ss)) !== null ? (" + args[i] + " = __tv, 1) : 0)");
                    else reads.push("__sReadStr(__sp, __ss, " + args[i] + ")");
                }
                return "(function(){ const __ss = fromCStr(" + srcVar + "); const __sp = {pos:0}; let __tv, __ok=0; " + reads.map(function(r) { return "__ok += " + r + ";"; }).join(" ") + " return __ok; })()";
            });

            // Replace &var and scalar references ONLY inside function bodies that declared let __box_v
            if (addrVars.size > 0) {
                const fnBlocks = s.split(/(?=\bfunction\s+[A-Za-z_]\w*\s*\()/);
                s = fnBlocks.map(function(blk) {
                    const hd = blk.match(/^function\s+[A-Za-z_]\w*\s*\(([^)]*)\)/);
                    const paramsSet = new Set(hd && hd[1].trim() ? hd[1].split(",").map(function(p) { return p.trim(); }) : []);
                    let outBlk = blk;
                    addrVars.forEach(function(v) {
                        if (paramsSet.has(v)) return;
                        if (outBlk.indexOf("let __box_" + v + " ") === -1) return;
                        outBlk = outBlk.replace(new RegExp("\\b" + v + "\\b", "g"), function(match, offset, full) {
                            const prev10 = full.slice(Math.max(0, offset - 10), offset);
                            const prev2 = prev10.slice(-2);
                            if (prev2.endsWith(".")) return match;
                            if (/let\s+$/.test(prev10) || /__box_$/.test(prev10)) return match;
                            if (prev2.endsWith("&") && !prev2.endsWith("&&")) return "__mkPtr(__box_" + v + ", 0)";
                            return "__box_" + v + "[0]";
                        });
                        outBlk = outBlk.replace(new RegExp("&\\s*__mkPtr\\(__box_" + v + ", 0\\)", "g"), "__mkPtr(__box_" + v + ", 0)");
                    });
                    return outBlk;
                }).join("");
            }
            // Strip residual & before structs/fields/ptrs (ignore && !)
            s = s.replace(/(^|[^&])&\s*(__ptrAdd\([^)]+\)\.[A-Za-z_]\w*|[A-Za-z_]\w*(?:\[[^\]]+\])?(?:\.[A-Za-z_]\w*)*)/g, "$1$2");

            // Restore string literals AT THE VERY END so inner \n / variable names are never touched
            s = s.replace(/@@STR(\d+)@@/g, function(_, idx) { return strLits[Number(idx)]; });

            // Inject loop guard into EVERY while (...) { and for (...) { regardless of nested parens!
            (function injectGuards() {
                let out = "", i = 0;
                const guard = " if (++__steps > 100000) throw new Error('Tempo limite excedido (possível loop infinito).'); ";
                while (i < s.length) {
                    const m = (i === 0 || !/[A-Za-z0-9_]/.test(s[i - 1])) ? s.slice(i).match(/^(?:while|for)\s*\(/) : null;
                    if (m) {
                        let p = i + m[0].length - 1, d = 0, inStr = false, qCh = "";
                        while (p < s.length) {
                            const ch = s[p];
                            if (inStr) { if (ch === "\\") p++; else if (ch === qCh) inStr = false; }
                            else {
                                if (ch === '"' || ch === "'") { inStr = true; qCh = ch; }
                                else if (ch === "(") d++;
                                else if (ch === ")") { d--; if (d === 0) break; }
                            }
                            p++;
                        }
                        let after = p + 1;
                        while (after < s.length && /\s/.test(s[after])) after++;
                        if (s[after] === "{") {
                            out += s.slice(i, after + 1) + guard;
                            i = after + 1;
                            continue;
                        }
                    }
                    out += s[i++];
                }
                s = out;
            })();
            return structFactories.join("\n") + "\n" + s;
        }

        try {
            const jsCode = __transpileC(sourceCode);
            const runner = new Function(
                "stdin", "stdout", "stderr", "errno", "strerror", "setvbuf",
                "__readInt", "__readFloat", "__readChar", "__readStr",
                "fgets", "getchar", "putchar", "puts", "printf", "fprintf", "sprintf", "snprintf", "perror",
                "fopen", "fclose", "fflush", "feof", "ferror", "clearerr", "rewind", "ftell", "fseek",
                "removeFile", "renameFile", "tmpfile", "fputc", "fputs", "fgetc", "fwrite", "fread",
                "__fReadInt", "__fReadFloat", "__fReadStr", "__sReadInt", "__sReadFloat", "__sReadStr", "fromCStr", "toCStrArr",
                "strlen", "strcpy", "strncpy", "strcat", "strcmp", "strncmp", "strcspn", "strstr", "strtok",
                "tolower", "toupper", "isalpha", "isdigit", "isalnum", "isspace", "atoi", "atof",
                "malloc", "calloc", "realloc", "free", "qsort",
                "__arr1d", "__arr2d", "__mkPtr", "__derefGet", "__derefSet", "__ptrAdd", "__ptrDiff", "__ptrStep", "__sizeof", "__applyStructInit",
                "let __steps = 0;\n" + jsCode + "\nif (typeof main === 'function') { main.length >= 2 ? main(3, __mkPtr([toCStrArr('app'), toCStrArr('entrada.txt'), toCStrArr('saida.txt')], 0)) : main(); }"
            );
            runner(
                stdin, stdout, stderr, errno, strerror, setvbuf,
                __readInt, __readFloat, __readChar, __readStr,
                fgets, getchar, putchar, puts, printf, fprintf, sprintf, snprintf, perror,
                fopen, fclose, fflush, feof, ferror, clearerr, rewind, ftell, fseek,
                removeFile, renameFile, tmpfile, fputc, fputs, fgetc, fwrite, fread,
                __fReadInt, __fReadFloat, __fReadStr, __sReadInt, __sReadFloat, __sReadStr, fromCStr, toCStrArr,
                strlen, strcpy, strncpy, strcat, strcmp, strncmp, strcspn, strstr, strtok,
                tolower, toupper, isalpha, isdigit, isalnum, isspace, atoi, atof,
                malloc, calloc, realloc, free, qsort,
                __arr1d, __arr2d, __mkPtr, __derefGet, __derefSet, __ptrAdd, __ptrDiff, __ptrStep, __sizeof, __applyStructInit
            );
            const vfsSnapshot = {};
            const fnames = Object.keys(__vfs);
            for (let i = 0; i < fnames.length; i++) {
                const fn = fnames[i];
                const bytes = __vfs[fn].bytes;
                let preview = "";
                for (let b = 0; b < bytes.length && b < 400; b++) {
                    const c = bytes[b];
                    preview += (c >= 32 && c <= 126) || c === 10 || c >= 128 ? String.fromCharCode(c) : ".";
                }
                vfsSnapshot[fn] = { size: bytes.length, preview: preview };
            }
            return { ok: true, output: __stdoutBuf, files: vfsSnapshot };
        } catch (err) {
            return { ok: false, error: err && err.message ? err.message : String(err), output: __stdoutBuf, files: {} };
        }
    }

    function escapeHtml(str) {
        return String(str || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
    }

    function highlightC(code) {
        const tokens = [];
        function stash(cls, txt) {
            const id = "@@HL" + tokens.length + "@@";
            tokens.push('<span class="' + cls + '">' + txt + '</span>');
            return id;
        }
        let s = escapeHtml(code);
        s = s.replace(/\/\*[\s\S]*?\*\//g, function(m) { return stash("tok-cmt", m); });
        s = s.replace(/\/\/[^\n]*/g, function(m) { return stash("tok-cmt", m); });
        s = s.replace(/&quot;(?:\\.|[^&]|&(?!quot;))*?&quot;/g, function(m) { return stash("tok-str", m); });
        s = s.replace(/&#39;(?:\\.|[^&#]|&(?!#39;))*?&#39;/g, function(m) { return stash("tok-str", m); });
        s = s.replace(/^#\s*(?:include|define)[^\n]*/gm, function(m) { return stash("tok-pp", m); });
        s = s.replace(/\b(for|while|do|if|else|switch|case|default|break|continue|return|sizeof|typedef|struct|union|enum)\b/g, '<span class="tok-kw">$1</span>');
        s = s.replace(/\b(int|float|double|char|void|size_t|const|unsigned|long|FILE|NULL|EOF|SEEK_SET|SEEK_CUR|SEEK_END)\b/g, '<span class="tok-type">$1</span>');
        s = s.replace(/\b(\d+(?:\.\d+)?)\b/g, '<span class="tok-num">$1</span>');
        s = s.replace(/@@HL(\d+)@@/g, function(_, i) { return tokens[Number(i)]; });
        return s;
    }

    function showToast(msg) {
        const t = document.getElementById("toast");
        if (!t) return;
        t.textContent = msg;
        t.classList.add("show");
        clearTimeout(t._tid);
        t._tid = setTimeout(function() { t.classList.remove("show"); }, 2300);
    }

    function copyTextSafe(text) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(function() { showToast("Código copiado!"); }).catch(function() { fallbackCopy(text); });
        } else fallbackCopy(text);
    }
    function fallbackCopy(text) {
        const ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand("copy"); showToast("Código copiado!"); } catch (e) {}
        document.body.removeChild(ta);
    }

    /* ==================== STATE & STORAGE ==================== */
    let doneTopics = new Set();
    try {
        const r = localStorage.getItem(STORAGE_KEY);
        if (r) doneTopics = new Set(JSON.parse(r) || []);
        const ca = localStorage.getItem(CAT_ANS_KEY);
        if (ca) catAnswers = JSON.parse(ca) || {};
        const ce = localStorage.getItem(CE_ANS_KEY);
        if (ce) ceAnswers = JSON.parse(ce) || {};
        const fq = localStorage.getItem(FAV_Q_KEY);
        if (fq) favQuestions = new Set(JSON.parse(fq) || []);
    } catch (e) {}

    function saveDone() { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(doneTopics))); } catch (e) {} }
    function saveCatAnswers() { try { localStorage.setItem(CAT_ANS_KEY, JSON.stringify(catAnswers)); } catch (e) {} }
    function saveCeAnswers() { try { localStorage.setItem(CE_ANS_KEY, JSON.stringify(ceAnswers)); } catch (e) {} }
    function saveFavQuestions() { try { localStorage.setItem(FAV_Q_KEY, JSON.stringify(Array.from(favQuestions))); } catch (e) {} }

    let isDarkMode = false;
    function applyTheme(dark) {
        isDarkMode = Boolean(dark);
        document.body.classList.toggle("dark-mode", isDarkMode);
        const btn = document.getElementById("btn-theme-toggle");
        const icon = document.getElementById("theme-icon");
        const lbl = document.getElementById("theme-label");
        if (btn) btn.setAttribute("aria-pressed", String(isDarkMode));
        if (icon) icon.textContent = isDarkMode ? "☀️" : "🌙";
        if (lbl) lbl.textContent = isDarkMode ? "Claro" : "Escuro";
    }
    try { applyTheme(localStorage.getItem(THEME_KEY) === "dark"); } catch (e) {}

    let curFontSize = 15;
    function applyFontSize(sz) {
        curFontSize = Math.max(13, Math.min(19, sz));
        document.body.style.fontSize = curFontSize + "px";
        try { localStorage.setItem(FONT_KEY, String(curFontSize)); } catch (e) {}
    }
    try { const sf = parseInt(localStorage.getItem(FONT_KEY) || "15", 10); if (!isNaN(sf)) applyFontSize(sf); } catch (e) {}

    /* ==================== NAVIGATION ==================== */
    function scrollToCardSafe(targetId) {
        const el = document.getElementById(targetId);
        if (!el) return;
        setTimeout(function() { el.scrollIntoView({ behavior: "smooth", block: "start" }); }, 60);
    }

    function saveLastLocation(view, targetId, label) {
        try { localStorage.setItem(LAST_LOC_KEY, JSON.stringify({ view: view, targetId: targetId || "", label: label || "" })); } catch (e) {}
        renderHomeResume();
    }

    function switchView(viewName, scrollTargetId) {
        stopAllInlinePlay();
        const panels = document.querySelectorAll(".view-panel");
        for (let i = 0; i < panels.length; i++) panels[i].classList.remove("active");
        const target = document.getElementById("view-" + viewName);
        if (target) target.classList.add("active");

        const tabs = document.querySelectorAll(".nav-tab, .mbn-btn");
        for (let i = 0; i < tabs.length; i++) {
            tabs[i].classList.toggle("active", tabs[i].getAttribute("data-view") === viewName);
        }
        if (viewName === "pratica") renderPracticeHub();
        if (viewName === "ex-ponteiros") renderCategoryView("ponteiros");
        if (viewName === "ex-structs") renderCategoryView("structs");
        if (viewName === "ex-arquivos") renderCategoryView("arquivos");
        if (viewName === "simulados") renderSimulados();

        saveLastLocation(viewName, scrollTargetId || "", viewName.toUpperCase());
        if (scrollTargetId) scrollToCardSafe(scrollTargetId);
        else window.scrollTo({ top: 0, behavior: "smooth" });
    }

    /* ==================== CHEAT SHEET & HOME ==================== */
    function renderCheatSheet() {
        const tabsEl = document.getElementById("cs-tabs");
        const bodyEl = document.getElementById("cs-body");
        if (!tabsEl || !bodyEl || !DATA.cheatsheet) return;
        let tabsHtml = "";
        let activePanel = DATA.cheatsheet[0];
        for (let i = 0; i < DATA.cheatsheet.length; i++) {
            const p = DATA.cheatsheet[i];
            if (p.id === curCsTab) activePanel = p;
            tabsHtml += '<button type="button" class="pill-btn lab-pill ' + (p.id === curCsTab ? 'active' : '') + '" data-cs-tab="' + p.id + '">' + escapeHtml(p.tabLabel) + '</button>';
        }
        tabsEl.innerHTML = tabsHtml;
        if (!activePanel) return;
        let cards = '<h3 style="font-size:15.5px; margin-bottom:10px;">' + escapeHtml(activePanel.title) + '</h3><div class="cs-grid">';
        for (let c = 0; c < activePanel.cards.length; c++) {
            const card = activePanel.cards[c];
            const itemsHtml = Array.isArray(card.items) && card.items.length
                ? '<ul style="padding-left:18px; margin:6px 0;">' + card.items.map(function(it) { return '<li>' + escapeHtml(it) + '</li>'; }).join("") + '</ul>'
                : '';
            cards += '<div class="cs-mini-card">' +
                '<span class="mod-badge" style="margin-bottom:4px;">' + escapeHtml(card.badge) + '</span>' +
                '<h4>' + escapeHtml(card.title) + '</h4>' +
                (card.html ? '<div>' + card.html + '</div>' : '') +
                (card.summary ? '<p style="margin-bottom:4px;">' + escapeHtml(card.summary) + '</p>' : '') +
                itemsHtml +
                (card.code ? '<pre class="mono">' + highlightC(card.code) + '</pre>' : '') +
                (card.tip ? '<div style="margin-top:6px; font-size:12px; color:var(--lab); font-weight:600;">💡 ' + escapeHtml(card.tip) + '</div>' : '') +
            '</div>';
        }
        cards += '</div>';
        bodyEl.innerHTML = cards;
    }

    function renderHomeResume() {
        const host = document.getElementById("home-resume-host");
        if (!host) return;
        let loc = null;
        try { loc = JSON.parse(localStorage.getItem(LAST_LOC_KEY) || "null"); } catch (e) {}
        if (!loc || !loc.view || loc.view === "home") { host.innerHTML = ""; return; }
        host.innerHTML = '<div class="resume-banner">' +
            '<div><strong>Continuar de onde parou:</strong> Módulo <code>' + escapeHtml(loc.label || loc.view) + '</code></div>' +
            '<button type="button" class="btn btn-primary" data-resume-view="' + escapeHtml(loc.view) + '" data-resume-card="' + escapeHtml(loc.targetId || "") + '">Retomar Estudo →</button>' +
        '</div>';
    }

    /* ==================== MICRO-SANDBOXES v4.0 ==================== */
    function renderPtrSandbox() {
        const memEl = document.getElementById("ptr-sb-mem");
        const stEl = document.getElementById("ptr-sb-stats");
        if (!memEl || !stEl) return;
        const stepBytes = ptrSbType === "char" ? 1 : (ptrSbType === "double" ? 8 : 4);
        const baseAddr = 0x1000;
        let html = "";
        for (let i = 0; i < ptrSbVals.length; i++) {
            const addr = "0x" + (baseAddr + i * stepBytes).toString(16).toUpperCase();
            const isAct = (i === ptrSbIdx);
            const dispVal = ptrSbType === "char" ? "'" + String.fromCharCode(65 + i) + "'" : (ptrSbType === "double" ? ptrSbVals[i].toFixed(1) : String(ptrSbVals[i]));
            html += '<div style="text-align:center;">' +
                '<div class="ram-cell-live ' + (isAct ? 'active-cell' : '') + '">' +
                    '<div class="mem-idx mono">v[' + i + ']</div>' +
                    '<div class="mem-val mono">' + dispVal + '</div>' +
                    '<div class="mem-addr mono">' + addr + '</div>' +
                '</div>' +
                (isAct ? '<span class="ptr-badge mono">p (aponta)</span>' : '') +
            '</div>';
        }
        memEl.innerHTML = html;
        const curAddr = "0x" + (baseAddr + ptrSbIdx * stepBytes).toString(16).toUpperCase();
        const dispStarP = ptrSbType === "char"
            ? "'" + String.fromCharCode(65 + ptrSbIdx) + "' (ASCII " + (65 + ptrSbIdx) + ")"
            : (ptrSbType === "double" ? ptrSbVals[ptrSbIdx].toFixed(1) : String(ptrSbVals[ptrSbIdx]));
        stEl.innerHTML =
            '<div class="stat-mini"><span>sizeof(' + ptrSbType + ')</span><strong>' + stepBytes + ' bytes</strong></div>' +
            '<div class="stat-mini"><span>Endereço guardado em p</span><strong>' + curAddr + '</strong></div>' +
            '<div class="stat-mini"><span>Desreferenciação *p</span><strong>' + dispStarP + '</strong></div>' +
            '<div class="stat-mini"><span>Equivalência</span><strong>*(v + ' + ptrSbIdx + ') == v[' + ptrSbIdx + ']</strong></div>';
    }

    function renderStrcSandbox() {
        const memEl = document.getElementById("strc-sb-mem");
        const stEl = document.getElementById("strc-sb-stats");
        if (!memEl || !stEl) return;
        let slots = [];
        let total = 0, used = 0, note = "";
        if (strcSbMode === "unaligned") {
            slots = [
                { idx: "0x2000", val: "char a", tag: "1 B" },
                { idx: "0x2001..03", val: "PADDING", tag: "3 B desperdício", pad: true },
                { idx: "0x2004..07", val: "int b", tag: "4 B (alinhado em 4)" },
                { idx: "0x2008", val: "char c", tag: "1 B" },
                { idx: "0x2009..0B", val: "PADDING", tag: "3 B fim struct", pad: true }
            ];
            total = 12; used = 6;
            note = "Campos desalinhados inserem 6 bytes vazios de padding!";
        } else if (strcSbMode === "packed") {
            slots = [
                { idx: "0x2000..03", val: "int b", tag: "4 B" },
                { idx: "0x2004", val: "char a", tag: "1 B" },
                { idx: "0x2005", val: "char c", tag: "1 B" },
                { idx: "0x2006..07", val: "PADDING", tag: "2 B fim struct", pad: true }
            ];
            total = 8; used = 6;
            note = "Reordenar do maior para o menor tipo economizou 4 bytes (33%)!";
        } else {
            slots = [
                { idx: "0x2000", val: "a (byte 0) / int b", tag: "Mesmo endereço!", active: true },
                { idx: "0x2001..03", val: "bytes 1..3 de b", tag: "Sobreposição total" }
            ];
            total = 4; used = 4;
            note = "Em union, todos os membros começam em 0x2000; vale só o último escrito.";
        }
        memEl.innerHTML = slots.map(function(s) {
            return '<div class="ram-cell-live ' + (s.pad ? 'null-byte' : (s.active ? 'active-cell' : '')) + '" style="min-width:128px;">' +
                '<div class="mem-idx mono">' + s.idx + '</div>' +
                '<div class="mem-val mono" style="font-size:13px;">' + s.val + '</div>' +
                '<div class="mem-tag">' + s.tag + '</div>' +
            '</div>';
        }).join("");
        stEl.innerHTML =
            '<div class="stat-mini"><span>sizeof total</span><strong>' + total + ' bytes</strong></div>' +
            '<div class="stat-mini"><span>Dados úteis</span><strong>' + used + ' bytes</strong></div>' +
            '<div class="stat-mini"><span>Acesso p/ variável / ponteiro</span><strong>s.b == ptr-&gt;b</strong></div>' +
            '<div class="stat-mini"><span>Observação</span><strong>' + note + '</strong></div>';
    }

    function renderArqSandbox() {
        const memEl = document.getElementById("arq-sb-mem");
        const stEl = document.getElementById("arq-sb-stats");
        if (!memEl || !stEl) return;
        let html = "";
        for (let i = 0; i <= arqSbBytes.length; i++) {
            const isCur = (i === arqSbCursor);
            const ch = i < arqSbBytes.length ? arqSbBytes[i] : "EOF";
            html += '<div style="text-align:center;">' +
                '<div class="ram-cell-live ' + (isCur ? 'active-cell' : '') + (i === arqSbBytes.length ? ' null-byte' : '') + '" style="min-width:56px;">' +
                    '<div class="mem-idx mono">+' + i + '</div>' +
                    '<div class="mem-val mono">' + escapeHtml(ch) + '</div>' +
                '</div>' +
                (isCur ? '<span class="ptr-badge mono">cursor</span>' : '') +
            '</div>';
        }
        memEl.innerHTML = html;
        stEl.innerHTML =
            '<div class="stat-mini"><span>Modo fopen</span><strong>"' + arqSbMode + '" (' + (arqSbOpen ? "Aberto" : "Fechado") + ')</strong></div>' +
            '<div class="stat-mini"><span>ftell(fp)</span><strong>' + arqSbCursor + ' bytes</strong></div>' +
            '<div class="stat-mini"><span>feof(fp)</span><strong>' + (arqSbEof ? "1 (Verdadeiro)" : "0 (Falso)") + '</strong></div>' +
            '<div class="stat-mini"><span>Buffer em RAM</span><strong>' + (arqSbDirty ? "Pendente (fflush!)" : "Sincronizado no disco") + '</strong></div>';
    }

    /* ==================== INLINE TRACERS ==================== */
    function getInlineState(tid) {
        if (!inlineStates[tid]) inlineStates[tid] = { algoIdx: 0, stepIdx: 0, speedMs: 950, showFullTable: false };
        return inlineStates[tid];
    }
    function stopInlinePlay(tid) {
        if (inlineTimers[tid]) { clearInterval(inlineTimers[tid]); delete inlineTimers[tid]; }
    }
    function stopAllInlinePlay() {
        Object.keys(inlineTimers).forEach(function(k) { stopInlinePlay(k); });
    }
    function startInlinePlay(tid) {
        stopInlinePlay(tid);
        const topic = topicById[tid];
        if (!topic || !topic.tracers.length) return;
        const st = getInlineState(tid);
        const tr = topic.tracers[st.algoIdx];
        inlineTimers[tid] = setInterval(function() {
            if (st.stepIdx < tr.steps.length - 1) {
                st.stepIdx++;
                renderInlineTracer(tid);
            } else {
                stopInlinePlay(tid);
                renderInlineTracer(tid);
            }
        }, st.speedMs);
        renderInlineTracer(tid);
    }

    function renderInlineTracer(tid) {
        const host = document.getElementById("itr-" + tid);
        const topic = topicById[tid];
        if (!host || !topic || !topic.tracers || !topic.tracers.length) return;
        const st = getInlineState(tid);
        if (st.algoIdx >= topic.tracers.length) st.algoIdx = 0;
        const tr = topic.tracers[st.algoIdx];
        if (st.stepIdx >= tr.steps.length) st.stepIdx = tr.steps.length - 1;
        if (st.stepIdx < 0) st.stepIdx = 0;
        const step = tr.steps[st.stepIdx];
        const prevStep = st.stepIdx > 0 ? tr.steps[st.stepIdx - 1] : null;
        const stepPct = Math.round(((st.stepIdx + 1) / tr.steps.length) * 100);
        const isPlaying = Boolean(inlineTimers[tid]);

        let algoTabsHtml = "";
        if (topic.tracers.length > 1) {
            algoTabsHtml = '<div class="inline-tr-algo-pills">' + topic.tracers.map(function(sub, a) {
                return '<button type="button" class="pill-btn lab-pill ' + (a === st.algoIdx ? 'active' : '') + '" data-itr-id="' + tid + '" data-itr-algo="' + a + '">' + escapeHtml(sub.tabLabel || sub.title) + '</button>';
            }).join("") + '</div>';
        }

        const isOneBased = !tr.steps.some(function(x) { return x.line === 0; }) && tr.steps.some(function(x) { return x.line === tr.codeLines.length; });
        let codeHtml = "";
        for (let i = 0; i < tr.codeLines.length; i++) {
            const cmpIdx = isOneBased ? (i + 1) : i;
            const isAct = (step.line === cmpIdx);
            codeHtml += '<div class="code-line ' + (isAct ? 'active-line' : '') + '"><span class="line-no">' + (i + 1) + '</span><span>' + (isAct ? escapeHtml(tr.codeLines[i]) : highlightC(tr.codeLines[i])) + '</span></div>';
        }

        let dotsHtml = tr.steps.map(function(_, s) {
            return '<button type="button" class="step-dot ' + (s === st.stepIdx ? 'current' : '') + '" data-itr-id="' + tid + '" data-itr-step="' + s + '">' + (s + 1) + '</button>';
        }).join("");

        let memVisualHtml = "";
        if (tr.kind === "1d") {
            const baseAddr = tr.baseAddr || 0x1000;
            const byteStep = tr.byteStep || 4;
            const actList = step.active || [];
            memVisualHtml = '<div class="mem-strip">' + (step.cells || []).map(function(rawCell, c) {
                const isObj = rawCell && typeof rawCell === "object";
                const lbl = isObj ? (rawCell.label || (rawCell.idx !== undefined ? "[" + rawCell.idx + "]" : "[" + c + "]")) : ("[" + c + "]");
                const val = isObj ? (rawCell.val !== undefined ? String(rawCell.val) : "") : String(rawCell);
                const addr = (isObj && rawCell.addr) ? rawCell.addr : ("0x" + (baseAddr + c * byteStep).toString(16).toUpperCase());
                const isAct = (isObj ? Boolean(rawCell.active || rawCell.changed || rawCell.state === "active" || rawCell.state === "write" || rawCell.state === "dirty") : false) || actList.indexOf(c) !== -1;
                let ptrBadge = "";
                if (isObj && Array.isArray(rawCell.ptrs) && rawCell.ptrs.length) ptrBadge = rawCell.ptrs.join(", ");
                else if (isObj && rawCell.ptr) ptrBadge = String(rawCell.ptr);
                else if (step.ptrs) {
                    if (Array.isArray(step.ptrs)) {
                        const hit = step.ptrs.find(function(pr) { return String(pr[1]) === String(c); });
                        if (hit) ptrBadge = hit[0];
                    } else if (step.ptrs[String(c)]) {
                        ptrBadge = step.ptrs[String(c)];
                    }
                }
                return '<div style="text-align:center;"><div class="ram-cell-live ' + (isAct ? 'active-cell' : '') + '"><div class="mem-idx mono">' + escapeHtml(String(lbl)) + '</div><div class="mem-val mono">' + escapeHtml(val) + '</div><div class="mem-addr mono">' + escapeHtml(addr) + '</div></div>' + (ptrBadge ? '<span class="ptr-badge mono">' + escapeHtml(ptrBadge) + '</span>' : '') + '</div>';
            }).join("") + '</div>';
        } else {
            const cols = tr.cols || (step.grid && step.grid[0] ? step.grid[0].length : 1);
            const act2d = step.active2d || [];
            let gridHtml = '<div style="display:inline-grid; grid-template-columns:repeat(' + cols + ', minmax(68px, 110px)); gap:8px; max-width:100%;">';
            for (let r = 0; r < (step.grid || []).length; r++) {
                for (let c = 0; c < step.grid[r].length; c++) {
                    const gCell = step.grid[r][c];
                    const isObj = gCell && typeof gCell === "object";
                    const lbl = isObj ? (gCell.label || ("[" + r + "][" + c + "]")) : ("[" + r + "][" + c + "]");
                    const val = isObj ? (gCell.val !== undefined ? String(gCell.val) : "") : String(gCell);
                    const gAddr = isObj && gCell.addr ? ('<div class="mem-addr mono">' + escapeHtml(gCell.addr) + '</div>') : '';
                    const isAct = (isObj ? Boolean(gCell.active || gCell.changed || gCell.state === "active") : false) || act2d.some(function(p) { return p[0] === r && p[1] === c; });
                    gridHtml += '<div class="ram-cell-live ' + (isAct ? 'active-cell' : '') + '"><div class="mem-idx mono">' + escapeHtml(String(lbl)) + '</div><div class="mem-val mono">' + escapeHtml(val) + '</div>' + gAddr + '</div>';
                }
            }
            gridHtml += '</div>';
            memVisualHtml = gridHtml;
        }

        const stepVars = step.vars || {};
        const prevVars = prevStep && prevStep.vars ? prevStep.vars : null;
        const varsHtml = Object.keys(stepVars).map(function(key) {
            const changed = prevVars && prevVars[key] !== undefined && prevVars[key] !== stepVars[key];
            return '<div class="var-chip ' + (changed ? 'var-changed' : '') + '"><span>' + escapeHtml(key) + ':</span><strong>' + escapeHtml(String(stepVars[key])) + '</strong></div>';
        }).join("");

        const maxRowStep = st.showFullTable ? (tr.steps.length - 1) : st.stepIdx;
        const colKeys = [];
        for (let s = 0; s <= maxRowStep; s++) {
            Object.keys(tr.steps[s].vars || {}).forEach(function(k) { if (colKeys.indexOf(k) === -1) colKeys.push(k); });
        }
        let tableHtml = '<div class="trace-table-wrap"><table class="trace-table"><thead><tr><th>Passo</th><th>Linha</th>' +
            colKeys.map(function(k) { return '<th>' + escapeHtml(k) + '</th>'; }).join("") +
            '<th>Evento</th></tr></thead><tbody>';
        for (let s = 0; s <= maxRowStep; s++) {
            const rs = tr.steps[s];
            const rv = rs.vars || {};
            tableHtml += '<tr class="' + (s === st.stepIdx ? 'cur-row' : '') + '" data-itr-row-id="' + tid + '" data-itr-row-step="' + s + '"><td>' + (s + 1) + '</td><td>L' + (isOneBased ? rs.line : (rs.line + 1)) + '</td>' +
                colKeys.map(function(k) { return '<td>' + escapeHtml(rv[k] !== undefined ? String(rv[k]) : "—") + '</td>'; }).join("") +
                '<td>' + escapeHtml(rs.note) + '</td></tr>';
        }
        tableHtml += '</tbody></table></div>';

        host.innerHTML =
            '<div class="inline-tr-head">' +
                '<div><span class="mod-badge" style="background:var(--lab-bg); color:var(--lab);">' + escapeHtml(tr.badge) + '</span> <strong style="font-size:14.5px; margin-left:6px;">' + escapeHtml(tr.title) + '</strong></div>' +
                '<span class="mono" style="font-size:12px; font-weight:700; color:var(--lab);">Passo ' + (st.stepIdx + 1) + ' / ' + tr.steps.length + '</span>' +
            '</div>' +
            '<p style="font-size:12.8px; color:var(--text-muted); margin-bottom:8px;">' + escapeHtml(tr.desc) + '</p>' +
            algoTabsHtml +
            '<div class="itr-progress-track"><div class="itr-progress-fill" style="width:' + stepPct + '%;"></div></div>' +
            '<div class="itr-controls">' +
                '<button type="button" class="itr-btn" data-itr-id="' + tid + '" data-itr-act="reset">⏮ Início</button>' +
                '<button type="button" class="itr-btn" data-itr-id="' + tid + '" data-itr-act="prev">← Anterior</button>' +
                '<button type="button" class="itr-btn primary" data-itr-id="' + tid + '" data-itr-act="play">' + (isPlaying ? '⏸ Pausar' : '▶ Auto') + '</button>' +
                '<button type="button" class="itr-btn" data-itr-id="' + tid + '" data-itr-act="next">Próximo →</button>' +
                '<select class="itr-speed-sel" data-itr-speed="' + tid + '">' +
                    '<option value="1400" ' + (st.speedMs === 1400 ? 'selected' : '') + '>0.7x Lento</option>' +
                    '<option value="950" ' + (st.speedMs === 950 ? 'selected' : '') + '>1.0x Normal</option>' +
                    '<option value="500" ' + (st.speedMs === 500 ? 'selected' : '') + '>2.0x Rápido</option>' +
                '</select>' +
                '<button type="button" class="itr-btn" data-itr-id="' + tid + '" data-itr-act="table">' + (st.showFullTable ? 'Só até o passo' : 'Ver tabela inteira') + '</button>' +
            '</div>' +
            '<div class="step-dots">' + dotsHtml + '</div>' +
            '<div class="itr-split">' +
                '<div class="itr-code-box">' + codeHtml + '</div>' +
                '<div>' + memVisualHtml + '<div class="vars-row">' + varsHtml + '</div><div class="itr-note"><strong>Estado atual:</strong> ' + escapeHtml(step.note) + '</div></div>' +
            '</div>' +
            tableHtml;
    }

    function renderAllInlineTracers() {
        const all = [].concat(DATA.ponteiros, DATA.structs, DATA.arquivos);
        for (let i = 0; i < all.length; i++) renderInlineTracer(all[i].id);
    }

    /* ==================== MODULE RENDERER ==================== */
    function renderTocList(topics, tocContainerId, accentVar) {
        const tocEl = document.getElementById(tocContainerId);
        if (!tocEl) return;
        let doneCnt = 0;
        for (let i = 0; i < topics.length; i++) if (doneTopics.has(topics[i].id)) doneCnt++;
        const pct = topics.length > 0 ? Math.round((doneCnt / topics.length) * 100) : 0;
        const onlyPend = Boolean(tocOnlyPending[tocContainerId]);

        let html = '<div class="toc-prog-box">' +
            '<div style="display:flex; justify-content:space-between; font-size:11.5px; font-weight:700; margin-bottom:5px;"><span>Concluídos: ' + doneCnt + '/' + topics.length + '</span><span class="mono">' + pct + '%</span></div>' +
            '<div class="cat-progress-track" style="height:6px;"><div class="cat-progress-fill" style="width:' + pct + '%; background:' + accentVar + ';"></div></div>' +
            '<div class="toc-filter-row">' +
                '<button type="button" class="toc-flt-btn ' + (!onlyPend ? 'active' : '') + '" data-toc-filter="' + tocContainerId + '" data-toc-mode="all">Todos (' + topics.length + ')</button>' +
                '<button type="button" class="toc-flt-btn ' + (onlyPend ? 'active' : '') + '" data-toc-filter="' + tocContainerId + '" data-toc-mode="pend">Pendentes (' + (topics.length - doneCnt) + ')</button>' +
            '</div></div>';

        let shown = 0;
        for (let idx = 0; idx < topics.length; idx++) {
            const t = topics[idx];
            const isDone = doneTopics.has(t.id);
            if (onlyPend && isDone) continue;
            shown++;
            html += '<button type="button" class="toc-btn ' + (isDone ? 'done' : '') + (idx === 0 ? ' toc-active' : '') + '" id="toc-item-' + t.id + '" data-scroll-id="card-' + t.id + '">' +
                '<span class="toc-left"><span class="toc-num mono">' + escapeHtml(t.num) + '</span><span class="toc-title-txt">' + escapeHtml(t.title.split(":")[0]) + '</span></span>' +
                '<span class="toc-check">' + (isDone ? '✓' : '›') + '</span></button>';
        }
        if (!shown) html += '<div style="font-size:12px; color:var(--ok); text-align:center; padding:10px; font-weight:700;">🎉 Módulo 100% concluído!</div>';
        html += '<button type="button" class="toc-top-btn" data-scroll-top="1">↑ Topo</button>';
        tocEl.innerHTML = html;
    }

    function renderModule(topics, tocContainerId, contentContainerId, exViewName, accentVar) {
        const contentEl = document.getElementById(contentContainerId);
        renderTocList(topics, tocContainerId, accentVar);
        let cardsHtml = "";
        for (let idx = 0; idx < topics.length; idx++) {
            const t = topics[idx];
            topicById[t.id] = t;
            codeRegistry[t.id] = t.code;
            const isDone = doneTopics.has(t.id);
            let memHtml = "";
            if (t.memoryDiagram && t.memoryDiagram.cells) {
                memHtml = '<div class="mem-box"><div class="mem-caption">' + escapeHtml(t.memoryDiagram.caption) + '</div><div class="mem-strip">' +
                    t.memoryDiagram.cells.map(function(cell) {
                        const isNull = Boolean(cell.isNull) || (cell.val && cell.val.indexOf("\\0") !== -1);
                        return '<div class="mem-cell ' + (isNull ? 'null-byte' : '') + '"><div class="mem-idx mono">' + escapeHtml(cell.idx) + '</div><div class="mem-val mono">' + escapeHtml(cell.val) + '</div>' + (cell.tag ? '<div class="mem-tag">' + escapeHtml(cell.tag) + '</div>' : '') + '<div class="mem-addr mono">' + escapeHtml(cell.addr) + '</div></div>';
                    }).join("") + '</div></div>';
            }
            const prevT = idx > 0 ? topics[idx - 1] : null;
            const nextT = idx < topics.length - 1 ? topics[idx + 1] : null;
            const navFooter = '<div class="topic-nav-footer">' +
                (prevT ? '<button type="button" class="btn btn-outline" data-scroll-id="card-' + prevT.id + '">← ' + escapeHtml(prevT.num + ' ' + prevT.title.split(":")[0]) + '</button>' : '<span></span>') +
                (nextT ? '<button type="button" class="btn btn-outline" data-scroll-id="card-' + nextT.id + '">Próximo: ' + escapeHtml(nextT.num + ' ' + nextT.title.split(":")[0]) + ' →</button>' : '<button type="button" class="btn btn-primary" style="background:' + accentVar + ';" data-goto-view="' + exViewName + '">Praticar Exercícios deste Módulo →</button>') +
            '</div>';

            cardsHtml += '<article class="topic-card" id="card-' + t.id + '">' +
                '<div class="topic-top"><div><h3 style="font-size:18.5px; line-height:1.3;"><span class="topic-num">' + escapeHtml(t.num) + '</span>' + escapeHtml(t.title) + '</h3><span class="pdf-ref">📚 Referência: ' + escapeHtml(t.pdfRef) + '</span></div>' +
                '<button type="button" class="done-toggle ' + (isDone ? 'completed' : '') + '" data-toggle-done="' + t.id + '">' + (isDone ? '✓ Concluído' : 'Marcar como estudado') + '</button></div>' +
                '<div class="topic-summary">' + escapeHtml(t.summary) + '</div>' +
                '<div class="concept-body">' + t.conceptHtml + '</div>' +
                memHtml +
                '<div class="code-panel"><div class="code-header"><span class="code-title-wrap"><span class="mac-dots" aria-hidden="true"><i></i><i></i><i></i></span><span>exemplo_' + escapeHtml(t.id.replace("-", "_")) + '.c</span></span><span class="code-actions"><button type="button" class="run-pg-btn" data-open-pg="' + t.id + '" data-pg-title="' + escapeHtml(t.num) + '">⚡ Testar Código</button><button type="button" class="copy-btn" data-copy-id="' + t.id + '">Copiar</button></span></div><pre class="code-pre"><code>' + highlightC(t.code) + '</code></pre></div>' +
                '<div class="inline-tracer-host" id="itr-' + t.id + '"></div>' +
                '<div class="sub-heading">Lógica Detalhada Passo a Passo</div><ol class="logic-list">' + t.logicSteps.map(function(s) { return '<li>' + s + '</li>'; }).join("") + '</ol>' +
                '<div class="callout callout-danger"><strong>Atenção — Erro Comum:</strong> ' + t.pitfall + '</div>' +
                navFooter +
            '</article>';
        }
        contentEl.innerHTML = cardsHtml;
    }

    /* ==================== EXERCÍCIOS & CERTO/ERRADO ==================== */
    const CAT_META = {
        ponteiros: { key: "ponteiros", view: "ex-ponteiros", modLabel: "Ponteiros", title: "Exercícios de Ponteiros e Memória", badge: "30 A–E + 10 C/E + 2 Clássicos", colorVar: "var(--ptr)", cardCls: "cat-ptr", desc: "& e *, NULL, %p, aritmética de ponteiros, matrizes dinâmicas, malloc/calloc/realloc/free, callbacks qsort, void*, const e leaks.", chips: ["& e *", "malloc/free", "int **", "qsort / void *", "const & Leaks"] },
        structs: { key: "structs", view: "ex-structs", modLabel: "Structs", title: "Exercícios de Structs, Unions & Enums", badge: "30 A–E + 10 C/E + 2 Clássicos", colorVar: "var(--strc)", cardCls: "cat-strc", desc: "typedef, . vs ->, inicialização designada, fgets/buffer, ordenação de vetores de structs, aninhadas, union, enum, padding e listas.", chips: [". vs ->", "typedef", "union & enum", "Padding sizeof", "struct No *prox"] },
        arquivos: { key: "arquivos", view: "ex-arquivos", modLabel: "Arquivos", title: "Exercícios de Arquivos (FILE *)", badge: "30 A–E + 10 C/E + 2 Clássicos", colorVar: "var(--arq)", cardCls: "cat-arq", desc: "fopen r/w/a/+, fprintf/fscanf/fgets, bug while(!feof), fwrite/fread, fseek/ftell, errno/perror, fflush, argc/argv, CSV e CRUD.", chips: ["fopen modos", "while(!feof) bug", "fwrite/fread", "fseek & ftell", "CSV & CRUD"] }
    };

    function getCatStats(catKey) {
        const list = DATA.categoryExercises[catKey] || [];
        let answered = 0, correct = 0, favs = 0;
        for (let i = 0; i < list.length; i++) {
            const q = list[i], ans = catAnswers[q.id];
            if (ans !== undefined) { answered++; if (ans === q.correct) correct++; }
            if (favQuestions.has(q.id)) favs++;
        }
        return { total: list.length, answered: answered, correct: correct, favs: favs };
    }

    function levelBadgeClass(level) {
        const l = String(level || "").toLowerCase();
        if (l.indexOf("básic") !== -1 || l.indexOf("bas") !== -1) return "lvl-facil";
        if (l.indexOf("avan") !== -1) return "lvl-dificil";
        return "lvl-medio";
    }

    function renderCeCards(items) {
        if (!items || !items.length) return "";
        return '<div class="ce-grid">' + items.map(function(it, idx) {
            const chosen = ceAnswers[it.id];
            const hasAns = (chosen !== undefined);
            const isRight = hasAns && (chosen === it.answer);
            return '<div class="ce-card">' +
                '<div>' +
                    '<div style="display:flex; justify-content:space-between; align-items:center; gap:6px; margin-bottom:6px;">' +
                        '<span class="mod-badge">#' + (idx + 1) + ' • ' + escapeHtml(it.subtopic) + '</span>' +
                        (hasAns ? '<span class="lvl-badge ' + (isRight ? 'lvl-facil' : 'lvl-dificil') + '">' + (isRight ? '✓ Acertou' : '✗ Errou') + '</span>' : '') +
                    '</div>' +
                    '<p style="font-size:13.8px; font-weight:600; margin-bottom:8px;">' + escapeHtml(it.statement) + '</p>' +
                '</div>' +
                '<div>' +
                    '<div class="ce-actions">' +
                        '<button type="button" class="ce-btn ' + (chosen === true ? (it.answer ? 'ce-true-sel' : 'ce-false-sel') : '') + '" data-ce-id="' + it.id + '" data-ce-val="true" ' + (hasAns ? 'disabled' : '') + '>✓ Certo</button>' +
                        '<button type="button" class="ce-btn ' + (chosen === false ? (!it.answer ? 'ce-true-sel' : 'ce-false-sel') : '') + '" data-ce-id="' + it.id + '" data-ce-val="false" ' + (hasAns ? 'disabled' : '') + '>✗ Errado</button>' +
                    '</div>' +
                    (hasAns ? '<div class="callout ' + (isRight ? 'callout-ok' : 'callout-danger') + '" style="margin:8px 0 0; font-size:12.6px;"><strong>Gabarito: ' + (it.answer ? 'CERTO' : 'ERRADO') + '.</strong> ' + escapeHtml(it.keyPoint) + '<ul style="padding-left:18px; margin-top:4px;">' + it.steps.map(function(s) { return '<li>' + escapeHtml(s) + '</li>'; }).join("") + '</ul></div>' : '') +
                '</div>' +
            '</div>';
        }).join("") + '</div>';
    }

    function renderPracticeHub() {
        const root = document.getElementById("pratica-hub-root");
        if (!root) return;
        const s1 = getCatStats("ponteiros"), s2 = getCatStats("structs"), s3 = getCatStats("arquivos");
        const totQ = s1.total + s2.total + s3.total;
        const totAns = s1.answered + s2.answered + s3.answered;
        const totCor = s1.correct + s2.correct + s3.correct;
        const totPct = totQ > 0 ? Math.round((totCor / totQ) * 100) : 0;

        const cardsHtml = ["ponteiros", "structs", "arquivos"].map(function(k) {
            const m = CAT_META[k], st = getCatStats(k), pct = st.total ? Math.round((st.correct / st.total) * 100) : 0;
            return '<div class="cat-card ' + m.cardCls + '">' +
                '<div>' +
                    '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;"><span class="mod-badge" style="color:' + m.colorVar + ';">' + escapeHtml(m.badge) + '</span>' + (st.favs ? '<span class="mono" style="font-size:11.5px; color:#d97706;">★ ' + st.favs + '</span>' : '') + '</div>' +
                    '<h3 style="font-size:18px; margin-bottom:6px;">' + escapeHtml(m.title) + '</h3>' +
                    '<p style="font-size:13.5px; color:var(--text-muted); margin-bottom:10px;">' + escapeHtml(m.desc) + '</p>' +
                    '<div class="cat-topics-chips">' + m.chips.map(function(c) { return '<span class="cat-chip">' + escapeHtml(c) + '</span>'; }).join("") + '</div>' +
                '</div>' +
                '<div>' +
                    '<div style="display:flex; justify-content:space-between; font-size:12.5px; margin-bottom:5px;"><span><strong>' + st.correct + ' / ' + st.total + ' corretas</strong> (' + st.answered + ' resp.)</span><strong class="mono">' + pct + '%</strong></div>' +
                    '<div class="cat-progress-track"><div class="cat-progress-fill" style="width:' + pct + '%; background:' + m.colorVar + ';"></div></div>' +
                    '<button type="button" class="btn btn-primary" style="width:100%; margin-top:12px; background:' + m.colorVar + ';" data-goto-view="' + m.view + '">Abrir Aba de ' + escapeHtml(m.modLabel) + ' →</button>' +
                '</div>' +
            '</div>';
        }).join("");

        const ceList = (DATA.certoErrado || []).filter(function(c) { return ceFilterCat === "todas" || c.category === ceFilterCat; });
        root.innerHTML =
            '<div class="module-header-banner"><h2>Central Prática (90 Questões A–E + 30 Certo/Errado + 6 Problemas Clássicos)</h2><p>Escolha um módulo para abrir sua bateria exclusiva de 30 questões, ou treine afirmações rápidas de Certo ou Errado logo abaixo.</p></div>' +
            '<div class="ex-global-bar"><div><strong>Desempenho Geral A–E:</strong> ' + totCor + ' / ' + totQ + ' acertos (' + totPct + '%) • ' + totAns + ' respondidas</div><button type="button" class="btn btn-outline" id="btn-reset-all-cat-ex">Reiniciar Todas as Questões</button></div>' +
            '<div class="cat-hub-grid">' + cardsHtml + '</div>' +
            '<div class="module-header-banner" style="border-left-color:var(--lab);"><h3>Treino Rápido — 30 Afirmações Certo ou Errado</h3>' +
            '<div class="filter-pills" style="margin:8px 0 0;">' +
                '<button type="button" class="pill-btn lab-pill ' + (ceFilterCat === 'todas' ? 'active' : '') + '" data-ce-filter="todas">Todas (30)</button>' +
                '<button type="button" class="pill-btn lab-pill ' + (ceFilterCat === 'ponteiros' ? 'active' : '') + '" data-ce-filter="ponteiros">Ponteiros (10)</button>' +
                '<button type="button" class="pill-btn lab-pill ' + (ceFilterCat === 'structs' ? 'active' : '') + '" data-ce-filter="structs">Structs (10)</button>' +
                '<button type="button" class="pill-btn lab-pill ' + (ceFilterCat === 'arquivos' ? 'active' : '') + '" data-ce-filter="arquivos">Arquivos (10)</button>' +
            '</div></div>' +
            renderCeCards(ceList);
    }

    function renderCategoryView(catKey) {
        const meta = CAT_META[catKey];
        const root = document.getElementById("ex-cat-root-" + catKey);
        if (!meta || !root) return;
        const list = DATA.categoryExercises[catKey] || [];
        const st = getCatStats(catKey);
        const pct = st.total ? Math.round((st.correct / st.total) * 100) : 0;
        const activeFilter = catFilters[catKey] || "Todas";
        const qSearch = (catSearchTerms[catKey] || "").trim().toLowerCase();

        const filterDefs = [
            { id: "Todas", label: "Todas (" + list.length + ")" },
            { id: "Básico", label: "Básico" },
            { id: "Intermediário", label: "Intermediário" },
            { id: "Avançado", label: "Avançado" },
            { id: "Pendentes", label: "Pendentes" },
            { id: "Erradas", label: "Para Revisar" },
            { id: "Favoritas", label: "★ Favoritas (" + st.favs + ")" }
        ];
        const filterPills = filterDefs.map(function(fd) {
            return '<button type="button" class="pill-btn ' + (activeFilter === fd.id ? 'active' : '') + '" data-qcat-filter-cat="' + catKey + '" data-qcat-filter="' + fd.id + '">' + escapeHtml(fd.label) + '</button>';
        }).join("");

        let minimapHtml = '<div class="q-minimap-wrap"><div class="q-minimap-lbl"><span>Mapa Rápido (1..' + list.length + '):</span><span>✓ ' + st.correct + ' certas • ✗ ' + (st.answered - st.correct) + ' revisar</span></div><div class="q-minimap-grid">';
        for (let i = 0; i < list.length; i++) {
            const q = list[i], ans = catAnswers[q.id];
            let cls = "q-map-btn" + (ans !== undefined ? (ans === q.correct ? " map-ok" : " map-err") : "") + (favQuestions.has(q.id) ? " map-fav" : "");
            minimapHtml += '<button type="button" class="' + cls + '" data-map-cat="' + catKey + '" data-map-qid="qcard-' + q.id + '">' + (i + 1) + '</button>';
        }
        minimapHtml += '</div></div>';

        let qHtml = "";
        for (let i = 0; i < list.length; i++) {
            const q = list[i], chosen = catAnswers[q.id], hasAns = (chosen !== undefined), isFav = favQuestions.has(q.id);
            if (activeFilter === "Básico" && q.level !== "Básico") continue;
            if (activeFilter === "Intermediário" && q.level !== "Intermediário") continue;
            if (activeFilter === "Avançado" && q.level !== "Avançado") continue;
            if (activeFilter === "Pendentes" && hasAns) continue;
            if (activeFilter === "Erradas" && !(hasAns && chosen !== q.correct)) continue;
            if (activeFilter === "Favoritas" && !isFav) continue;
            if (qSearch && (q.title + " " + q.subtopic + " " + q.stem + " " + (q.code || "")).toLowerCase().indexOf(qSearch) === -1) continue;

            const codeId = "qstem-" + q.id, solId = "qsol-" + q.id;
            if (q.code && q.code.trim()) codeRegistry[codeId] = q.code;
            if (q.solutionCode && q.solutionCode.trim()) codeRegistry[solId] = q.solutionCode;
            const showGab = hasAns || openQGabaritos.has(q.id);

            const optsHtml = '<div class="ex-options-list">' + q.options.map(function(opt, o) {
                let cls = "quiz-opt";
                if (hasAns) { if (o === q.correct) cls += " correct"; else if (o === chosen) cls += " wrong"; }
                return '<button type="button" class="' + cls + '" data-cat-key="' + catKey + '" data-cat-qid="' + q.id + '" data-cat-opt="' + o + '" ' + (hasAns ? 'disabled' : '') + '><span class="opt-letter">' + String.fromCharCode(65 + o) + '</span><span>' + escapeHtml(opt) + '</span></button>';
            }).join("") + '</div>';

            let gabHtml = "";
            if (showGab) {
                gabHtml = '<div class="gabarito-box">' +
                    '<div class="callout callout-ok" style="margin-top:0;"><strong>Gabarito: Alternativa ' + String.fromCharCode(65 + q.correct) + '.</strong> ' + escapeHtml(q.gabaritoResumo) + '</div>' +
                    '<ol class="logic-list">' + q.steps.map(function(s) { return '<li>' + escapeHtml(s) + '</li>'; }).join("") + '</ol>' +
                    '<div style="font-size:12.8px; margin:8px 0;"><strong>Análise das 5 alternativas:</strong><ul style="padding-left:18px;">' + q.optionExplanations.map(function(e, oi) {
                        return '<li><strong>' + String.fromCharCode(65 + oi) + ')</strong> ' + escapeHtml(e) + '</li>';
                    }).join("") + '</ul></div>' +
                    '<div class="code-panel"><div class="code-header"><span>Solução Completa em C</span><span class="code-actions"><button type="button" class="run-pg-btn" data-open-pg="' + solId + '" data-pg-title="Solução #' + (i + 1) + '">⚡ Testar</button><button type="button" class="copy-btn" data-copy-id="' + solId + '">Copiar</button></span></div><pre class="code-pre"><code>' + highlightC(q.solutionCode) + '</code></pre></div>' +
                '</div>';
            }

            qHtml += '<article class="ex-card" id="qcard-' + q.id + '">' +
                '<div class="ex-card-head"><div><span class="mod-badge">Questão #' + (i + 1) + ' • ' + escapeHtml(q.subtopic) + '</span> <span class="lvl-badge ' + levelBadgeClass(q.level) + '">' + escapeHtml(q.level) + '</span></div>' +
                '<div style="display:flex; gap:6px;"><button type="button" class="fav-q-btn ' + (isFav ? 'is-fav' : '') + '" data-fav-cat="' + catKey + '" data-fav-qid="' + q.id + '">' + (isFav ? '★ Favorita' : '☆ Favoritar') + '</button>' +
                '<button type="button" class="btn btn-outline" style="padding:3px 10px; font-size:12px;" data-toggle-qgab="' + catKey + '" data-qgab-id="' + q.id + '">' + (showGab ? 'Ocultar Gabarito' : 'Ver Gabarito') + '</button></div></div>' +
                '<h3 style="font-size:16.5px; margin-bottom:6px;">' + escapeHtml(q.title) + '</h3>' +
                '<p style="font-size:13.8px; margin-bottom:8px;">' + escapeHtml(q.stem) + '</p>' +
                (q.code && q.code.trim() ? '<div class="code-panel" style="margin:8px 0;"><div class="code-header"><span>Código da Questão #' + (i + 1) + '</span><span class="code-actions"><button type="button" class="run-pg-btn" data-open-pg="' + codeId + '" data-pg-title="Q#' + (i + 1) + '">⚡ Testar</button><button type="button" class="copy-btn" data-copy-id="' + codeId + '">Copiar</button></span></div><pre class="code-pre"><code>' + highlightC(q.code) + '</code></pre></div>' : '') +
                optsHtml + gabHtml +
            '</article>';
        }

        const ceItems = (DATA.certoErrado || []).filter(function(x) { return x.category === catKey; });
        const clItems = (DATA.classical || []).filter(function(x) { return x.module === meta.modLabel; });
        const clHtml = clItems.map(function(cl) {
            codeRegistry[cl.id] = cl.code;
            return '<article class="topic-card"><div class="topic-top"><div><span class="mod-badge">' + escapeHtml(cl.source) + '</span><h3 style="margin-top:6px;">' + escapeHtml(cl.title) + '</h3></div></div>' +
                '<p style="margin-bottom:8px;"><strong>Problema:</strong> ' + escapeHtml(cl.problem) + '</p>' +
                '<div class="callout callout-info"><strong>Ideia Central:</strong> ' + escapeHtml(cl.idea) + '</div>' +
                '<div class="code-panel"><div class="code-header"><span>Código Comentado em C</span><span class="code-actions"><button type="button" class="run-pg-btn" data-open-pg="' + cl.id + '" data-pg-title="' + escapeHtml(cl.title) + '">⚡ Testar</button><button type="button" class="copy-btn" data-copy-id="' + cl.id + '">Copiar</button></span></div><pre class="code-pre"><code>' + highlightC(cl.code) + '</code></pre></div>' +
                '<div style="font-size:13px; color:var(--text-muted);"><strong>Rastreio:</strong> ' + escapeHtml(cl.trace) + '</div></article>';
        }).join("");

        root.innerHTML =
            '<div class="module-header-banner" style="border-left-color:' + meta.colorVar + ';"><h2>' + escapeHtml(meta.title) + '</h2><p>' + escapeHtml(meta.desc) + '</p></div>' +
            '<div class="cat-controls-box" style="flex-direction:column; align-items:stretch;">' +
                '<div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:10px;">' +
                    '<div class="filter-pills" style="margin:0;">' + filterPills + '</div>' +
                    '<div style="display:flex; gap:8px; flex-wrap:wrap;">' +
                        '<input type="search" class="cat-search-input" data-cat-search="' + catKey + '" value="' + escapeHtml(catSearchTerms[catKey] || "") + '" placeholder="Filtrar questões nesta categoria...">' +
                        '<span class="mono" style="font-size:12.5px; font-weight:700; align-self:center;">' + st.correct + '/' + st.total + ' (' + pct + '%)</span>' +
                        '<button type="button" class="btn btn-outline" data-reset-cat="' + catKey + '">Resetar</button>' +
                    '</div>' +
                '</div>' + minimapHtml +
            '</div>' +
            (qHtml || '<div class="callout">Nenhuma questão encontrada para este filtro.</div>') +
            '<div class="module-header-banner" style="border-left-color:var(--lab);"><h3>10 Afirmações Certo ou Errado — ' + escapeHtml(meta.modLabel) + '</h3></div>' +
            renderCeCards(ceItems) +
            '<div class="module-header-banner" style="border-left-color:' + meta.colorVar + ';"><h3>2 Problemas Clássicos Resolvidos — ' + escapeHtml(meta.modLabel) + '</h3></div>' +
            clHtml;
    }

    /* ==================== SIMULADOS ATP ==================== */
    let simState = { mode: "lobby", simIndex: 0, remainingSec: 7200, timerId: null, confirmFinish: false, mcqAns: {}, codeAns: {}, textAns: {}, bugAns: {}, sampleRunOut: {}, grading: null };
    function formatClock(sec) { const s = Math.max(0, sec); return String(Math.floor(s / 3600)).padStart(2, "0") + ":" + String(Math.floor((s % 3600) / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); }
    function stopSimTimer() { if (simState.timerId) { clearInterval(simState.timerId); simState.timerId = null; } }
    function normOut(str) { return String(str || "").trim().split(/\r?\n/).map(function(l) { return l.trim().replace(/\s+/g, " "); }).filter(Boolean).join("\n"); }
    function scoreKeywordText(ans, keywords, maxPts) {
        const clean = String(ans || "").toLowerCase().replace(/\s+/g, " ").trim();
        if (!clean || clean.length < 4) return 0;
        let hits = 0;
        for (let i = 0; i < (keywords || []).length; i++) if (clean.indexOf(keywords[i].toLowerCase()) !== -1) hits++;
        if (hits >= 2) return maxPts;
        if (hits === 1) return Number((maxPts * 0.6).toFixed(2));
        return clean.length >= 25 ? Number((maxPts * 0.35).toFixed(2)) : 0;
    }
    function runCodeTests(q, userCode) {
        let passedTests = 0; const testResults = [];
        for (let t = 0; t < q.tests.length; t++) {
            const tc = q.tests[t], res = runCProgram(userCode, tc.in), got = normOut(res.output), exp = normOut(tc.out), pass = res.ok && got === exp;
            if (pass) passedTests++;
            testResults.push({ pass: pass, input: tc.in, expected: exp, got: res.ok ? (got || "(vazio)") : ("ERRO: " + res.error) });
        }
        return { passedTests: passedTests, totalTests: q.tests.length, testResults: testResults };
    }
    function startSimulado(idx) {
        stopSimTimer();
        const sim = DATA.simulados[idx];
        simState = { mode: "running", simIndex: idx, remainingSec: sim.durationSec || 7200, timerId: null, confirmFinish: false, mcqAns: {}, codeAns: {}, textAns: {}, bugAns: {}, sampleRunOut: {}, grading: null };
        sim.questions.forEach(function(q) {
            if (q.type === "code" || q.type === "step_code") simState.codeAns[q.id] = q.starter || "";
            if (q.type === "bughunt") simState.bugAns[q.id] = [{ line: "", problem: "", fix: "" }, { line: "", problem: "", fix: "" }, { line: "", problem: "", fix: "" }, { line: "", problem: "", fix: "" }];
        });
        renderSimulados();
        simState.timerId = setInterval(function() {
            simState.remainingSec--;
            const el = document.getElementById("sim-timer-display");
            if (el) { el.textContent = formatClock(simState.remainingSec); el.classList.toggle("urgent", simState.remainingSec <= 600); }
            if (simState.remainingSec <= 0) finishSimulado(true);
        }, 1000);
    }
    function finishSimulado(autoByTimeout) {
        stopSimTimer();
        const sim = DATA.simulados[simState.simIndex];
        let mcqRight = 0, mcqTotal = 0, pracPts = 0, pracMax = 0, totalPts = 0, maxPts = 0;
        const perQ = {};
        sim.questions.forEach(function(q) {
            maxPts += q.points;
            if (q.type === "mcq") {
                mcqTotal++;
                const ok = simState.mcqAns[q.id] === q.correct;
                const earned = ok ? q.points : 0;
                if (ok) mcqRight++;
                totalPts += earned;
                perQ[q.id] = { earned: earned, ok: ok };
            } else if (q.type === "trace") {
                pracMax += q.points;
                const outOk = normOut(simState.textAns[q.id + "-a"] || "") === normOut(q.expectedOutput);
                const ptsA = outOk ? q.partAPoints : 0;
                const ptsB = scoreKeywordText(simState.textAns[q.id + "-b"] || "", q.partBKeywords, q.partBPoints);
                const earned = Number((ptsA + ptsB).toFixed(2));
                pracPts += earned; totalPts += earned;
                perQ[q.id] = { earned: earned, ptsA: ptsA, ptsB: ptsB, outOk: outOk };
            } else if (q.type === "bughunt") {
                pracMax += q.points;
                const rows = simState.bugAns[q.id] || [];
                const matched = new Set();
                const rowGrades = rows.map(function(r) {
                    const ln = parseInt(String(r.line || "").replace(/\D/g, ""), 10);
                    let hitIdx = -1;
                    for (let b = 0; b < q.bugs.length; b++) {
                        if (matched.has(b)) continue;
                        const bg = q.bugs[b];
                        if (ln === bg.line || (bg.altLines && bg.altLines.indexOf(ln) !== -1)) { hitIdx = b; break; }
                    }
                    if (hitIdx !== -1) { matched.add(hitIdx); return { ok: true, bug: q.bugs[hitIdx] }; }
                    return { ok: false, bug: null };
                });
                const earned = Number((matched.size * 0.25).toFixed(2));
                pracPts += earned; totalPts += earned;
                perQ[q.id] = { earned: earned, found: matched.size, rowGrades: rowGrades };
            } else if (q.type === "step_code") {
                pracMax += q.points;
                const ptsA = scoreKeywordText(simState.textAns[q.id + "-a"] || "", q.partAKeywords, q.partAPoints);
                const rt = runCodeTests(q, simState.codeAns[q.id] || "");
                const ptsB = Number((q.partBPoints * (rt.passedTests / rt.totalTests)).toFixed(2));
                const earned = Number((ptsA + ptsB).toFixed(2));
                pracPts += earned; totalPts += earned;
                perQ[q.id] = { earned: earned, ptsA: ptsA, ptsB: ptsB, passedTests: rt.passedTests, totalTests: rt.totalTests, testResults: rt.testResults };
            } else {
                pracMax += q.points;
                const rt = runCodeTests(q, simState.codeAns[q.id] || "");
                const earned = Number((q.points * (rt.passedTests / rt.totalTests)).toFixed(2));
                pracPts += earned; totalPts += earned;
                perQ[q.id] = { earned: earned, passedTests: rt.passedTests, totalTests: rt.totalTests, testResults: rt.testResults };
            }
        });
        simState.mode = "finished";
        simState.grading = { autoByTimeout: Boolean(autoByTimeout), spentSec: (sim.durationSec || 7200) - simState.remainingSec, mcqRight: mcqRight, mcqTotal: mcqTotal, pracPts: pracPts, pracMax: pracMax, totalPts: totalPts, maxPts: maxPts, perQ: perQ };
        renderSimulados();
        window.scrollTo({ top: 0, behavior: "smooth" });
    }
    function renderCodeKeybar(qId) {
        const keys = ["{ }", "[ ]", "->", "&", "*", ";", "\\0", "NULL", "sizeof()", "fopen"];
        return '<div class="c-keybar">' + keys.map(function(k) {
            return '<button type="button" class="c-key-btn" data-ins-target="' + qId + '" data-ins-val="' + escapeHtml(k) + '">' + escapeHtml(k) + '</button>';
        }).join("") + '</div>';
    }
    function renderSimulados() {
        const root = document.getElementById("sim-root");
        if (!root) return;
        if (simState.mode === "lobby") {
            root.innerHTML =
                '<div class="module-header-banner" style="border-left:5px solid #be123c;"><h2>Simulados Oficiais Padrão ATP (IFAM — TADS)</h2><p>3 provas cronometradas de 2 horas (14 questões, 10,0 pontos): Parte I (10 questões A–E • 5,0 pts) + Parte II (Rastreamento, Caça aos Erros, Análise &amp; Código C e Problema Completo • 5,0 pts).</p></div>' +
                '<div class="module-grid">' + DATA.simulados.map(function(sim, i) {
                    return '<div class="mod-card" style="border-top:4px solid #be123c;"><div><span class="mod-badge sim-kicker-badge">Padrão Prova ATP • 2h • 10,0 pts</span><h3>' + escapeHtml(sim.title) + '</h3><p>' + escapeHtml(sim.subtitle) + '</p></div><button type="button" class="btn btn-primary" style="background:#be123c;" data-start-sim="' + i + '">Iniciar Prova →</button></div>';
                }).join("") + '</div>';
            return;
        }
        const sim = DATA.simulados[simState.simIndex];
        const isFin = (simState.mode === "finished");
        let html = "";
        function renderPromptHtml(p) {
            const s = String(p || "");
            if (/<\/?(?:p|code|strong|em|ol|ul|li|br)\b/i.test(s)) return '<div class="sim-prompt-html" style="font-size:13.8px; margin-bottom:8px;">' + s + '</div>';
            return '<p style="font-size:13.8px; margin-bottom:8px;">' + escapeHtml(s) + '</p>';
        }
        if (!isFin) {
            html += '<div class="sim-header-bar"><div><div style="font-size:11px; font-weight:800; color:#be123c;">AVALIAÇÃO EM ANDAMENTO</div><div style="font-weight:800;">' + escapeHtml(sim.title) + '</div></div>' +
                '<div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;"><div id="sim-timer-display" class="sim-timer">' + formatClock(simState.remainingSec) + '</div><button type="button" class="btn btn-outline" id="btn-sim-back-lobby">← Lobby</button><button type="button" class="btn btn-primary" style="background:#be123c;" id="btn-sim-ask-finish">Entregar e Corrigir</button></div>' +
                '<div class="sim-nav-strip">' + sim.questions.map(function(sq, qi) { return '<button type="button" class="sim-q-pill" data-scroll-id="simq-' + sq.id + '">Q' + (qi + 1) + '</button>'; }).join("") + '</div>' +
                (simState.confirmFinish ? '<div class="sim-confirm-box"><span><strong>Confirmar entrega?</strong></span><div style="display:flex; gap:8px;"><button type="button" class="btn btn-outline" id="btn-sim-cancel-finish">Continuar</button><button type="button" class="btn btn-primary" style="background:#be123c;" id="btn-sim-confirm-finish">Corrigir Agora</button></div></div>' : '') +
            '</div>';
        } else {
            const g = simState.grading;
            html += '<div class="module-header-banner" style="border-left:5px solid var(--ok);"><div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:10px;"><div><h2>Resultado: ' + g.totalPts.toFixed(2).replace(".", ",") + ' / 10,0 pontos</h2><p>Parte I: ' + g.mcqRight + '/' + g.mcqTotal + ' acertos • Parte II: ' + g.pracPts.toFixed(2).replace(".", ",") + '/' + g.pracMax.toFixed(1).replace(".", ",") + ' pts • Tempo: ' + formatClock(g.spentSec) + '</p></div><div style="display:flex; gap:8px;"><button type="button" class="btn btn-outline" id="btn-sim-back-lobby">← Lobby</button><button type="button" class="btn btn-primary" style="background:#be123c;" data-start-sim="' + simState.simIndex + '">Refazer</button></div></div></div>';
        }

        sim.questions.forEach(function(q) {
            const gr = isFin ? simState.grading.perQ[q.id] : null;
            if (q.type === "mcq") {
                const chosen = simState.mcqAns[q.id];
                html += '<div class="sim-q-card" id="simq-' + q.id + '"><h3 style="font-size:16px; margin-bottom:6px;">' + escapeHtml(q.title) + ' <span class="mod-badge">' + q.points.toFixed(1) + ' pt</span></h3>' + renderPromptHtml(q.prompt) +
                    (q.code ? '<div class="code-panel"><pre class="code-pre"><code>' + highlightC(q.code) + '</code></pre></div>' : '') +
                    '<div class="ex-options-list">' + q.options.map(function(opt, o) {
                        let cls = "quiz-opt";
                        if (isFin) { if (o === q.correct) cls += " correct"; else if (o === chosen) cls += " wrong"; }
                        else if (chosen === o) cls += " selected";
                        return '<button type="button" class="' + cls + '" data-sim-mcq="' + q.id + '" data-sim-opt="' + o + '" ' + (isFin ? 'disabled' : '') + '><span class="opt-letter">' + String.fromCharCode(65 + o) + '</span><span>' + escapeHtml(opt) + '</span></button>';
                    }).join("") + '</div>' +
                    (isFin ? '<div class="callout callout-info" style="margin-top:10px;"><strong>Gabarito ' + String.fromCharCode(65 + q.correct) + ':</strong> ' + escapeHtml(q.explanations[q.correct]) + '</div>' : '') +
                '</div>';
            } else if (q.type === "trace") {
                html += '<div class="sim-q-card" id="simq-' + q.id + '"><h3 style="font-size:16px; margin-bottom:6px;">' + escapeHtml(q.title) + ' (' + q.points.toFixed(1) + ' pt)</h3>' + renderPromptHtml(q.prompt) +
                    '<div class="code-panel"><pre class="code-pre"><code>' + highlightC(q.code) + '</code></pre></div>' +
                    '<div class="sim-sub-label">' + escapeHtml(q.partAPrompt) + '</div><textarea class="sim-text-area mono" data-sim-text="' + q.id + '-a" ' + (isFin ? 'readonly' : '') + '>' + escapeHtml(simState.textAns[q.id + "-a"] || "") + '</textarea>' +
                    '<div class="sim-sub-label">' + escapeHtml(q.partBPrompt) + '</div><textarea class="sim-text-area" data-sim-text="' + q.id + '-b" ' + (isFin ? 'readonly' : '') + '>' + escapeHtml(simState.textAns[q.id + "-b"] || "") + '</textarea>' +
                    (isFin && gr ? '<div class="callout callout-info" style="margin-top:10px;"><strong>Correção: ' + gr.earned.toFixed(2) + ' pt</strong><br>Saída esperada: <code>' + escapeHtml(q.expectedOutput) + '</code><br>Modelo Item B: ' + escapeHtml(q.partBModel) + '</div>' : '') +
                '</div>';
            } else if (q.type === "bughunt") {
                const rows = simState.bugAns[q.id] || [];
                const numCode = q.numberedCode.map(function(l, idx) { return String(idx + 1).padStart(2, " ") + " | " + l; }).join("\n");
                html += '<div class="sim-q-card" id="simq-' + q.id + '"><h3 style="font-size:16px; margin-bottom:6px;">' + escapeHtml(q.title) + ' (' + q.points.toFixed(1) + ' pt)</h3>' + renderPromptHtml(q.prompt) +
                    '<div class="code-panel"><pre class="code-pre"><code>' + escapeHtml(numCode) + '</code></pre></div>' +
                    [0, 1, 2, 3].map(function(r) {
                        const rv = rows[r] || { line: "", problem: "", fix: "" };
                        return '<div class="bug-row"><input class="bug-inp mono" placeholder="Linha" data-bug-q="' + q.id + '" data-bug-row="' + r + '" data-bug-fld="line" value="' + escapeHtml(rv.line) + '" ' + (isFin ? 'readonly' : '') + '><input class="bug-inp" placeholder="Problema encontrado" data-bug-q="' + q.id + '" data-bug-row="' + r + '" data-bug-fld="problem" value="' + escapeHtml(rv.problem) + '" ' + (isFin ? 'readonly' : '') + '><input class="bug-inp mono" placeholder="Correção" data-bug-q="' + q.id + '" data-bug-row="' + r + '" data-bug-fld="fix" value="' + escapeHtml(rv.fix) + '" ' + (isFin ? 'readonly' : '') + '></div>';
                    }).join("") +
                    (isFin && gr ? '<div class="callout callout-info" style="margin-top:10px;"><strong>Encontrados: ' + gr.found + '/4 (' + gr.earned.toFixed(2) + ' pt)</strong><ul style="padding-left:18px; margin-top:4px;">' + q.bugs.map(function(b) { return '<li><strong>Linha ' + b.line + ':</strong> ' + escapeHtml(b.problem) + ' → <code>' + escapeHtml(b.fix) + '</code></li>'; }).join("") + '</ul></div>' : '') +
                '</div>';
            } else {
                codeRegistry["model-" + q.id] = q.modelCode;
                const valCode = simState.codeAns[q.id] !== undefined ? simState.codeAns[q.id] : q.starter;
                const sampleOut = simState.sampleRunOut[q.id];
                const isStep = (q.type === "step_code");
                html += '<div class="sim-q-card" id="simq-' + q.id + '"><h3 style="font-size:16px; margin-bottom:6px;">' + escapeHtml(q.title) + ' (' + q.points.toFixed(1) + ' pt)</h3>' + renderPromptHtml(q.prompt) +
                    (isStep ? '<div class="sim-sub-label">' + escapeHtml(q.partAPrompt) + '</div><textarea class="sim-text-area" data-sim-text="' + q.id + '-a" ' + (isFin ? 'readonly' : '') + '>' + escapeHtml(simState.textAns[q.id + "-a"] || "") + '</textarea><div class="sim-sub-label">' + escapeHtml(q.partBPrompt) + '</div>' : '') +
                    '<div class="sim-io-box">' + escapeHtml(q.ioExample) + '</div>' +
                    (!isFin ? renderCodeKeybar(q.id) : '') +
                    '<textarea class="sim-code-area" id="code-area-' + q.id + '" data-sim-code="' + q.id + '" ' + (isFin ? 'readonly' : '') + '>' + escapeHtml(valCode) + '</textarea>' +
                    (!isFin ? '<div style="margin-top:8px;"><button type="button" class="btn btn-outline" data-test-sample="' + q.id + '">▶ Testar Código</button></div>' + (sampleOut ? '<div class="sim-io-box" style="margin-top:8px;">' + escapeHtml(sampleOut.text) + '</div>' : '') : '') +
                    (isFin && gr ? '<div style="margin-top:10px;"><strong>Correção: ' + gr.earned.toFixed(2) + ' / ' + q.points.toFixed(1) + ' pt (' + gr.passedTests + '/' + gr.totalTests + ' casos)</strong>' + gr.testResults.map(function(tr, ti) {
                        return '<div class="sim-test-row ' + (tr.pass ? 'pass' : 'fail') + '">Caso ' + (ti + 1) + ': ' + (tr.pass ? '✓ APROVADO' : '✗ DIVERGENTE') + ' | Esperado: ' + escapeHtml(tr.expected) + ' | Obtido: ' + escapeHtml(tr.got) + '</div>';
                    }).join("") + '<div class="callout callout-info">' + escapeHtml(q.solutionNote) + '</div><div class="code-panel"><div class="code-header"><span>Código Modelo</span><button type="button" class="copy-btn" data-copy-id="model-' + q.id + '">Copiar</button></div><pre class="code-pre"><code>' + highlightC(q.modelCode) + '</code></pre></div></div>' : '') +
                '</div>';
            }
        });
        root.innerHTML = html;
    }

    /* ==================== PROGRESS & SEARCH ==================== */
    function countDone(list) { let c = 0; for (let i = 0; i < list.length; i++) if (doneTopics.has(list[i].id)) c++; return c; }
    function updateProgressUI() {
        const dPtr = countDone(DATA.ponteiros), tPtr = DATA.ponteiros.length;
        const dStrc = countDone(DATA.structs), tStrc = DATA.structs.length;
        const dArq = countDone(DATA.arquivos), tArq = DATA.arquivos.length;
        const total = tPtr + tStrc + tArq, done = dPtr + dStrc + dArq;
        const pct = total ? Math.round((done / total) * 100) : 0;

        document.getElementById("progress-text").textContent = done + " / " + total + " estudados";
        document.getElementById("progress-fill").style.width = pct + "%";
        document.getElementById("tab-cnt-ptr").textContent = dPtr + "/" + tPtr;
        document.getElementById("tab-cnt-strc").textContent = dStrc + "/" + tStrc;
        document.getElementById("tab-cnt-arq").textContent = dArq + "/" + tArq;
        document.getElementById("kpi-topics-val").textContent = done + " / " + total;
        document.getElementById("kpi-topics-sub").textContent = pct + "% da teoria concluída";

        [["ptr", dPtr, tPtr], ["strc", dStrc, tStrc], ["arq", dArq, tArq]].forEach(function(item) {
            const p = item[2] ? Math.round((item[1] / item[2]) * 100) : 0;
            const tx = document.getElementById("home-prog-txt-" + item[0]);
            const pc = document.getElementById("home-prog-pct-" + item[0]);
            const br = document.getElementById("home-prog-bar-" + item[0]);
            if (tx) tx.textContent = item[1] + " / " + item[2] + " estudados";
            if (pc) pc.textContent = p + "%";
            if (br) br.style.width = p + "%";
        });

        const s1 = getCatStats("ponteiros"), s2 = getCatStats("structs"), s3 = getCatStats("arquivos");
        const qTot = s1.total + s2.total + s3.total, qAns = s1.answered + s2.answered + s3.answered, qCor = s1.correct + s2.correct + s3.correct;
        document.getElementById("tab-cnt-prat").textContent = qAns + "/" + qTot;
        document.getElementById("kpi-quest-val").textContent = qAns + " / " + qTot;
        document.getElementById("kpi-acc-val").textContent = qAns > 0 ? Math.round((qCor / qAns) * 100) + "%" : "—";
        document.getElementById("kpi-acc-sub").textContent = qAns > 0 ? (qCor + " acertos de " + qAns) : "Responda questões para medir";
    }

    function handleSearch(query) {
        const drop = document.getElementById("search-results");
        if (!drop) return;
        const q = String(query || "").trim().toLowerCase();
        if (q.length < 2) { drop.classList.remove("open"); drop.innerHTML = ""; return; }
        const hits = [];
        [["ponteiros", DATA.ponteiros, "Ponteiros"], ["structs", DATA.structs, "Structs"], ["arquivos", DATA.arquivos, "Arquivos"]].forEach(function(grp) {
            grp[1].forEach(function(t) {
                if ((t.title + " " + t.summary + " " + t.num).toLowerCase().indexOf(q) !== -1) {
                    hits.push({ view: grp[0], id: "card-" + t.id, title: t.num + " — " + t.title, meta: "Teoria • " + grp[2] });
                }
            });
        });
        ["ponteiros", "structs", "arquivos"].forEach(function(cat) {
            (DATA.categoryExercises[cat] || []).forEach(function(ex, idx) {
                if ((ex.title + " " + ex.subtopic + " " + ex.stem).toLowerCase().indexOf(q) !== -1) {
                    hits.push({ view: "ex-" + cat, id: "qcard-" + ex.id, title: "Q#" + (idx + 1) + ": " + ex.title, meta: "Exercício • " + cat });
                }
            });
        });
        drop.innerHTML = hits.length ? hits.slice(0, 14).map(function(h) {
            return '<button type="button" class="search-item" data-search-view="' + h.view + '" data-search-card="' + h.id + '"><span class="search-item-title">' + escapeHtml(h.title) + '</span><span class="search-item-meta">' + escapeHtml(h.meta) + '</span></button>';
        }).join("") : '<div style="padding:10px; font-size:13px; color:var(--text-soft);">Nenhum resultado para "' + escapeHtml(query) + '".</div>';
        drop.classList.add("open");
    }

    /* ==================== PLAYGROUND C MODAL ==================== */
    const PG_TEMPLATES = {
        ptr: '#include <stdio.h>\n#include <stdlib.h>\n\nvoid troca(int *a, int *b) {\n    int tmp = *a;\n    *a = *b;\n    *b = tmp;\n}\n\nint main(void) {\n    int x = 10, y = 25;\n    troca(&x, &y);\n    printf("x=%d y=%d\\n", x, y);\n    int *v = (int *)malloc(3 * sizeof(int));\n    v[0] = 5; *(v + 1) = 15; v[2] = 25;\n    printf("Soma heap = %d\\n", v[0] + v[1] + v[2]);\n    free(v);\n    return 0;\n}',
        strc: '#include <stdio.h>\n#include <string.h>\n\ntypedef struct {\n    int id;\n    char nome[40];\n    float nota;\n} Aluno;\n\nvoid bonus(Aluno *p, float extra) {\n    p->nota += extra;\n}\n\nint main(void) {\n    Aluno a = {.id = 1, .nome = "Ana", .nota = 8.0};\n    bonus(&a, 1.5);\n    printf("%d - %s: %.1f\\n", a.id, a.nome, a.nota);\n    return 0;\n}',
        arq: '#include <stdio.h>\n\nint main(void) {\n    FILE *fp = fopen("notas.txt", "w");\n    if (fp == NULL) return 1;\n    fprintf(fp, "Ana 9.5\\nBruno 8.0\\n");\n    fclose(fp);\n\n    fp = fopen("notas.txt", "r");\n    char nome[40];\n    float n;\n    while (fscanf(fp, "%s %f", nome, &n) == 2) {\n        printf("Lido: %s -> %.1f\\n", nome, n);\n    }\n    fclose(fp);\n    return 0;\n}',
        clean: '#include <stdio.h>\n\nint main(void) {\n    printf("Ola, Ponteiros, Structs e Arquivos!\\n");\n    return 0;\n}'
    };

    function preparePlaygroundCode(raw) {
        const s = String(raw || "").trim();
        if (!s) return PG_TEMPLATES.ptr;
        if (/\bmain\s*\(/.test(s)) return s;
        return '#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint main(void) {\n    ' +
            s.split('\n').join('\n    ') + '\n    return 0;\n}';
    }

    function openPlayground(code, titleHint) {
        const modal = document.getElementById("c-playground-modal");
        document.getElementById("code-area-pg").value = preparePlaygroundCode(code);
        document.getElementById("pg-modal-title").textContent = titleHint ? ("⚡ Playground C — " + titleHint) : "⚡ Playground & Testador de Código C";
        document.getElementById("pg-stdout").textContent = 'Clique em "▶ Executar Código C".';
        document.getElementById("pg-stdout").classList.remove("err");
        document.getElementById("pg-vfs-wrap").style.display = "none";
        modal.classList.add("open");
    }
    function closePlayground() { document.getElementById("c-playground-modal").classList.remove("open"); }
    function executePlayground() {
        const res = runCProgram(document.getElementById("code-area-pg").value, document.getElementById("pg-stdin").value);
        const outEl = document.getElementById("pg-stdout");
        const metaEl = document.getElementById("pg-exec-meta");
        const vfsWrap = document.getElementById("pg-vfs-wrap");
        const vfsOut = document.getElementById("pg-vfs-out");
        if (res.ok) {
            outEl.classList.remove("err");
            outEl.textContent = res.output || "(Executado com sucesso; saída vazia)";
            metaEl.textContent = "✓ OK";
        } else {
            outEl.classList.add("err");
            outEl.textContent = (res.output ? res.output + "\n" : "") + "Erro: " + res.error;
            metaEl.textContent = "✗ Erro";
        }
        const fnames = Object.keys(res.files || {});
        if (fnames.length > 0) {
            vfsWrap.style.display = "block";
            vfsOut.textContent = fnames.map(function(fn) {
                return "[" + fn + "] (" + res.files[fn].size + " bytes)\n" + res.files[fn].preview;
            }).join("\n---\n");
        } else {
            vfsWrap.style.display = "none";
        }
    }

    /* ==================== INITIAL RENDER & EVENTS ==================== */
    renderModule(DATA.ponteiros, "toc-ponteiros", "content-ponteiros", "ex-ponteiros", "var(--ptr)");
    renderModule(DATA.structs, "toc-structs", "content-structs", "ex-structs", "var(--strc)");
    renderModule(DATA.arquivos, "toc-arquivos", "content-arquivos", "ex-arquivos", "var(--arq)");
    renderAllInlineTracers();
    renderCheatSheet();
    renderHomeResume();
    renderPtrSandbox();
    renderStrcSandbox();
    renderArqSandbox();
    updateProgressUI();

    window.__runCProgramTest = runCProgram;
    window.__selfTestAll = function() {
        const fails = [];
        let total = 0, passed = 0;
        const dummyIn = "3\n1 Ana 8.5\n2 Bruno 7.0\n3 Carla 9.0\n10 20 30\n";
        function chk(lbl, code, stdinOverride) {
            total++;
            const r = runCProgram(code, stdinOverride !== undefined ? stdinOverride : dummyIn);
            if (r.ok) passed++;
            else fails.push(lbl + " -> " + r.error);
        }
        Object.keys(PG_TEMPLATES).forEach(function(k) { chk("PG:" + k, PG_TEMPLATES[k]); });
        [].concat(DATA.ponteiros, DATA.structs, DATA.arquivos).forEach(function(t) { chk("topic:" + t.id, t.code); });
        ["ponteiros", "structs", "arquivos"].forEach(function(cat) {
            (DATA.categoryExercises[cat] || []).forEach(function(q) { chk("mcq_sol:" + q.id, q.solutionCode); });
        });
        (DATA.classical || []).forEach(function(cl) { chk("classical:" + cl.id, cl.code); });
        let simPassed = 0, simTotal = 0;
        (DATA.simulados || []).forEach(function(sim) {
            sim.questions.forEach(function(q) {
                if (q.modelCode && q.tests) {
                    q.tests.forEach(function(tc, ti) {
                        simTotal++; total++;
                        const r = runCProgram(q.modelCode, tc.in);
                        if (r.ok && normOut(r.output) === normOut(tc.out)) { passed++; simPassed++; }
                        else fails.push("sim:" + q.id + "#" + (ti + 1) + " -> " + (r.error || ("got=" + normOut(r.output))));
                    });
                }
            });
        });
        return { total: total, passed: passed, simPassed: simPassed, simTotal: simTotal, fails: fails };
    };
    if (window.location.search.indexOf("selftest=1") !== -1) {
        const res = window.__selfTestAll();
        const box = document.createElement("div");
        box.id = "selftest-report";
        box.style.cssText = "background:#0f172a;color:#e2e8f0;padding:12px 16px;font-family:monospace;font-size:12px;border-bottom:2px solid #22c55e;white-space:pre-wrap;";
        box.textContent = "SELFTEST: " + res.passed + "/" + res.total + " PASS | SIMULADOS: " + res.simPassed + "/" + res.simTotal + (res.fails.length ? ("\nFAILS:\n" + res.fails.join("\n")) : "\nALL 0 ERRORS!");
        document.body.insertBefore(box, document.body.firstChild);
    }

    document.addEventListener("click", function(e) {
        if (e.target && e.target.id === "c-playground-modal") { closePlayground(); return; }
        const rowTarget = e.target.closest("tr[data-itr-row-id]");
        if (rowTarget) {
            const tid = rowTarget.getAttribute("data-itr-row-id");
            stopInlinePlay(tid);
            getInlineState(tid).stepIdx = parseInt(rowTarget.getAttribute("data-itr-row-step"), 10);
            renderInlineTracer(tid);
            return;
        }
        if (!e.target.closest(".search-wrap")) {
            const sr = document.getElementById("search-results");
            if (sr) sr.classList.remove("open");
        }
        const btn = e.target.closest("button");
        if (!btn) return;

        if (btn.id === "btn-pomodoro") { togglePomodoro(); return; }
        if (btn.id === "btn-open-playground" || btn.id === "btn-hero-playground") { openPlayground(PG_TEMPLATES.ptr, "Laboratório"); return; }
        if (btn.id === "btn-pg-close") { closePlayground(); return; }
        if (btn.id === "btn-pg-run") { executePlayground(); return; }
        if (btn.id === "btn-pg-copy") { copyTextSafe(document.getElementById("code-area-pg").value); return; }
        if (btn.id === "btn-theme-toggle") { applyTheme(!isDarkMode); try { localStorage.setItem(THEME_KEY, isDarkMode ? "dark" : "light"); } catch (err) {} return; }
        if (btn.id === "btn-font-dec") { applyFontSize(curFontSize - 1); return; }
        if (btn.id === "btn-font-inc") { applyFontSize(curFontSize + 1); return; }
        if (btn.id === "btn-search-toggle") { document.getElementById("search-wrap").classList.toggle("mobile-open"); return; }
        if (btn.id === "btn-fab-top") { window.scrollTo({ top: 0, behavior: "smooth" }); return; }

        if (btn.hasAttribute("data-view") || btn.hasAttribute("data-goto-view")) {
            switchView(btn.getAttribute("data-view") || btn.getAttribute("data-goto-view"));
            return;
        }
        if (btn.hasAttribute("data-resume-view")) {
            switchView(btn.getAttribute("data-resume-view"), btn.getAttribute("data-resume-card") || undefined);
            return;
        }
        if (btn.hasAttribute("data-search-view")) {
            document.getElementById("search-results").classList.remove("open");
            switchView(btn.getAttribute("data-search-view"), btn.getAttribute("data-search-card"));
            return;
        }
        if (btn.hasAttribute("data-open-pg")) {
            openPlayground(codeRegistry[btn.getAttribute("data-open-pg")] || "", btn.getAttribute("data-pg-title") || "");
            return;
        }
        if (btn.hasAttribute("data-copy-id")) {
            copyTextSafe(codeRegistry[btn.getAttribute("data-copy-id")] || "");
            return;
        }
        if (btn.hasAttribute("data-cs-tab")) { curCsTab = btn.getAttribute("data-cs-tab"); renderCheatSheet(); return; }
        if (btn.hasAttribute("data-toggle-toc")) {
            const side = document.getElementById(btn.getAttribute("data-toggle-toc"));
            if (side) side.classList.toggle("toc-open");
            return;
        }
        if (btn.hasAttribute("data-toc-filter")) {
            const cid = btn.getAttribute("data-toc-filter");
            tocOnlyPending[cid] = (btn.getAttribute("data-toc-mode") === "pend");
            if (cid === "toc-ponteiros") renderTocList(DATA.ponteiros, "toc-ponteiros", "var(--ptr)");
            if (cid === "toc-structs") renderTocList(DATA.structs, "toc-structs", "var(--strc)");
            if (cid === "toc-arquivos") renderTocList(DATA.arquivos, "toc-arquivos", "var(--arq)");
            return;
        }
        if (btn.hasAttribute("data-scroll-id")) { scrollToCardSafe(btn.getAttribute("data-scroll-id")); return; }
        if (btn.hasAttribute("data-scroll-top")) { window.scrollTo({ top: 0, behavior: "smooth" }); return; }
        if (btn.hasAttribute("data-toggle-done")) {
            const id = btn.getAttribute("data-toggle-done");
            if (doneTopics.has(id)) { doneTopics.delete(id); btn.classList.remove("completed"); btn.textContent = "Marcar como estudado"; }
            else { doneTopics.add(id); btn.classList.add("completed"); btn.textContent = "✓ Concluído"; showToast("Tópico marcado como estudado!"); }
            saveDone();
            renderTocList(DATA.ponteiros, "toc-ponteiros", "var(--ptr)");
            renderTocList(DATA.structs, "toc-structs", "var(--strc)");
            renderTocList(DATA.arquivos, "toc-arquivos", "var(--arq)");
            updateProgressUI();
            return;
        }
        // Micro-sandbox clicks
        if (btn.hasAttribute("data-ptr-type")) {
            ptrSbType = btn.getAttribute("data-ptr-type");
            document.querySelectorAll("[data-ptr-type]").forEach(function(b) { b.classList.toggle("active", b === btn); });
            renderPtrSandbox(); return;
        }
        if (btn.hasAttribute("data-ptr-act")) {
            const act = btn.getAttribute("data-ptr-act");
            if (act === "prev" && ptrSbIdx > 0) ptrSbIdx--;
            else if (act === "next" && ptrSbIdx < ptrSbVals.length - 1) ptrSbIdx++;
            else if (act === "incval") ptrSbVals[ptrSbIdx] += 10;
            else if (act === "reset") { ptrSbIdx = 0; ptrSbVals = [10, 20, 30, 40, 50]; }
            renderPtrSandbox(); return;
        }
        if (btn.hasAttribute("data-strc-mode")) {
            strcSbMode = btn.getAttribute("data-strc-mode");
            document.querySelectorAll("[data-strc-mode]").forEach(function(b) { b.classList.toggle("active", b === btn); });
            renderStrcSandbox(); return;
        }
        if (btn.hasAttribute("data-arq-mode")) {
            arqSbMode = btn.getAttribute("data-arq-mode");
            arqSbOpen = true; arqSbEof = false;
            if (arqSbMode === "w") { arqSbBytes = []; arqSbCursor = 0; arqSbDirty = true; }
            else if (arqSbMode === "a") { arqSbBytes = ["A", "T", "P", "-", "C", "\\n"]; arqSbCursor = arqSbBytes.length; arqSbDirty = false; }
            else { arqSbBytes = ["A", "T", "P", "-", "C", "\\n"]; arqSbCursor = 0; arqSbDirty = false; }
            document.querySelectorAll("[data-arq-mode]").forEach(function(b) { b.classList.toggle("active", b === btn); });
            renderArqSandbox(); return;
        }
        if (btn.hasAttribute("data-arq-act")) {
            const act = btn.getAttribute("data-arq-act");
            if (act === "read1") {
                if (arqSbCursor < arqSbBytes.length) { arqSbCursor++; arqSbEof = false; }
                else arqSbEof = true;
            } else if (act === "writeX") {
                if (arqSbMode === "r") showToast('Modo "r" é somente leitura!');
                else { arqSbBytes[arqSbMode === "a" ? arqSbBytes.length : arqSbCursor++] = "X"; if (arqSbMode === "a") arqSbCursor = arqSbBytes.length; arqSbDirty = true; }
            } else if (act === "rewind") { arqSbCursor = 0; arqSbEof = false; }
            else if (act === "end") { arqSbCursor = arqSbBytes.length; arqSbEof = false; }
            else if (act === "flush") { arqSbDirty = false; showToast("Buffer descarregado no disco!"); }
            renderArqSandbox(); return;
        }
        // Inline tracers
        if (btn.hasAttribute("data-itr-id")) {
            const tid = btn.getAttribute("data-itr-id"), st = getInlineState(tid), tr = topicById[tid].tracers[st.algoIdx];
            if (btn.hasAttribute("data-itr-algo")) { stopInlinePlay(tid); st.algoIdx = parseInt(btn.getAttribute("data-itr-algo"), 10); st.stepIdx = 0; }
            else if (btn.hasAttribute("data-itr-step")) { stopInlinePlay(tid); st.stepIdx = parseInt(btn.getAttribute("data-itr-step"), 10); }
            else {
                const act = btn.getAttribute("data-itr-act");
                if (act === "reset") { stopInlinePlay(tid); st.stepIdx = 0; }
                else if (act === "prev") { stopInlinePlay(tid); if (st.stepIdx > 0) st.stepIdx--; }
                else if (act === "next") { stopInlinePlay(tid); if (st.stepIdx < tr.steps.length - 1) st.stepIdx++; }
                else if (act === "table") st.showFullTable = !st.showFullTable;
                else if (act === "play") { if (inlineTimers[tid]) stopInlinePlay(tid); else startInlinePlay(tid); return; }
            }
            renderInlineTracer(tid); return;
        }
        // Quiz & Certo/Errado & Simulados
        if (btn.hasAttribute("data-cat-qid")) {
            const cat = btn.getAttribute("data-cat-key"), qid = btn.getAttribute("data-cat-qid"), opt = parseInt(btn.getAttribute("data-cat-opt"), 10);
            catAnswers[qid] = opt; saveCatAnswers(); renderCategoryView(cat); updateProgressUI(); return;
        }
        if (btn.hasAttribute("data-toggle-qgab")) {
            const cat = btn.getAttribute("data-toggle-qgab"), qid = btn.getAttribute("data-qgab-id");
            if (openQGabaritos.has(qid)) openQGabaritos.delete(qid); else openQGabaritos.add(qid);
            renderCategoryView(cat); return;
        }
        if (btn.hasAttribute("data-qcat-filter")) {
            catFilters[btn.getAttribute("data-qcat-filter-cat")] = btn.getAttribute("data-qcat-filter");
            renderCategoryView(btn.getAttribute("data-qcat-filter-cat")); return;
        }
        if (btn.hasAttribute("data-map-qid")) {
            const ck = btn.getAttribute("data-map-cat"), qid = btn.getAttribute("data-map-qid");
            if (catFilters[ck] !== "Todas" || catSearchTerms[ck]) { catFilters[ck] = "Todas"; catSearchTerms[ck] = ""; renderCategoryView(ck); }
            scrollToCardSafe(qid); return;
        }
        if (btn.hasAttribute("data-fav-qid")) {
            const ck = btn.getAttribute("data-fav-cat"), qid = btn.getAttribute("data-fav-qid");
            if (favQuestions.has(qid)) favQuestions.delete(qid); else favQuestions.add(qid);
            saveFavQuestions(); renderCategoryView(ck); return;
        }
        if (btn.hasAttribute("data-reset-cat")) {
            const ck = btn.getAttribute("data-reset-cat");
            (DATA.categoryExercises[ck] || []).forEach(function(q) { delete catAnswers[q.id]; openQGabaritos.delete(q.id); });
            saveCatAnswers(); renderCategoryView(ck); updateProgressUI(); return;
        }
        if (btn.id === "btn-reset-all-cat-ex") {
            catAnswers = {}; ceAnswers = {}; openQGabaritos.clear();
            saveCatAnswers(); saveCeAnswers(); renderPracticeHub(); updateProgressUI(); return;
        }
        if (btn.hasAttribute("data-ce-filter")) { ceFilterCat = btn.getAttribute("data-ce-filter"); renderPracticeHub(); return; }
        if (btn.hasAttribute("data-ce-id")) {
            const id = btn.getAttribute("data-ce-id"), val = btn.getAttribute("data-ce-val") === "true";
            ceAnswers[id] = val; saveCeAnswers();
            if (document.getElementById("view-pratica").classList.contains("active")) renderPracticeHub();
            ["ponteiros", "structs", "arquivos"].forEach(function(ck) {
                if (document.getElementById("view-ex-" + ck).classList.contains("active")) renderCategoryView(ck);
            });
            return;
        }
        if (btn.hasAttribute("data-start-sim")) { startSimulado(parseInt(btn.getAttribute("data-start-sim"), 10)); return; }
        if (btn.id === "btn-sim-ask-finish") { simState.confirmFinish = true; renderSimulados(); return; }
        if (btn.id === "btn-sim-cancel-finish") { simState.confirmFinish = false; renderSimulados(); return; }
        if (btn.id === "btn-sim-confirm-finish") { finishSimulado(false); return; }
        if (btn.id === "btn-sim-back-lobby") { stopSimTimer(); simState.mode = "lobby"; renderSimulados(); return; }
        if (btn.hasAttribute("data-sim-mcq")) {
            if (simState.mode === "running") { simState.mcqAns[btn.getAttribute("data-sim-mcq")] = parseInt(btn.getAttribute("data-sim-opt"), 10); renderSimulados(); }
            return;
        }
        if (btn.hasAttribute("data-test-sample")) {
            const qid = btn.getAttribute("data-test-sample"), q = DATA.simulados[simState.simIndex].questions.find(function(x) { return x.id === qid; });
            if (q && q.tests.length) {
                const res = runCProgram(simState.codeAns[qid] || "", q.tests[0].in);
                simState.sampleRunOut[qid] = { ok: res.ok && normOut(res.output) === normOut(q.tests[0].out), text: res.ok ? ("Entrada: " + q.tests[0].in + "\nSua saída: " + (res.output || "(vazio)") + "\nEsperado: " + q.tests[0].out) : ("Erro: " + res.error) };
                renderSimulados();
            }
            return;
        }
        if (btn.hasAttribute("data-ins-target")) {
            const ta = document.getElementById("code-area-" + btn.getAttribute("data-ins-target"));
            const v = btn.getAttribute("data-ins-val");
            if (ta && !ta.readOnly) {
                const st = ta.selectionStart || 0, en = ta.selectionEnd || 0;
                ta.value = ta.value.slice(0, st) + v + ta.value.slice(en);
                if (btn.getAttribute("data-ins-target") !== "pg") simState.codeAns[btn.getAttribute("data-ins-target")] = ta.value;
                ta.focus();
            }
        }
    });

    document.getElementById("btn-pomodoro").addEventListener("dblclick", resetPomodoro);

    document.addEventListener("change", function(e) {
        if (e.target && e.target.hasAttribute("data-itr-speed")) {
            const tid = e.target.getAttribute("data-itr-speed");
            getInlineState(tid).speedMs = parseInt(e.target.value, 10) || 950;
            if (inlineTimers[tid]) startInlinePlay(tid);
        }
        if (e.target && e.target.id === "pg-template-sel" && PG_TEMPLATES[e.target.value]) {
            document.getElementById("code-area-pg").value = PG_TEMPLATES[e.target.value];
            executePlayground();
        }
    });

    document.addEventListener("input", function(e) {
        const el = e.target;
        if (!el) return;
        if (el.id === "global-search") handleSearch(el.value);
        if (el.hasAttribute("data-cat-search")) {
            const ck = el.getAttribute("data-cat-search");
            catSearchTerms[ck] = el.value;
            renderCategoryView(ck);
        }
        if (el.hasAttribute("data-sim-code")) simState.codeAns[el.getAttribute("data-sim-code")] = el.value;
        if (el.hasAttribute("data-sim-text")) simState.textAns[el.getAttribute("data-sim-text")] = el.value;
        if (el.hasAttribute("data-bug-q")) {
            const qid = el.getAttribute("data-bug-q"), r = parseInt(el.getAttribute("data-bug-row"), 10), f = el.getAttribute("data-bug-fld");
            if (simState.bugAns[qid] && simState.bugAns[qid][r]) simState.bugAns[qid][r][f] = el.value;
        }
    });

    document.addEventListener("keydown", function(e) {
        if ((e.key === "/" || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") {
            e.preventDefault();
            document.getElementById("global-search").focus();
        } else if (e.key === "Escape") {
            closePlayground();
            document.getElementById("search-results").classList.remove("open");
        } else if ((e.ctrlKey || e.metaKey) && e.key === "Enter" && document.getElementById("c-playground-modal").classList.contains("open")) {
            e.preventDefault();
            executePlayground();
        }
    });

    window.addEventListener("scroll", function() {
        const doc = document.documentElement;
        const maxScroll = Math.max(1, doc.scrollHeight - window.innerHeight);
        document.getElementById("scroll-progress-line").style.width = Math.min(100, Math.round((window.scrollY / maxScroll) * 100)) + "%";
        document.getElementById("btn-fab-top").classList.toggle("visible", window.scrollY > 360);
    }, { passive: true });
})();
</script>
</body>
</html>
"""
