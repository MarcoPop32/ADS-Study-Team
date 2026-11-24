(function () {
  "use strict";

  const STORAGE_KEY = "ads_study_v2_progress";
  const THEME_KEY = "ads_study_theme";

  const MEMORY_STEPS = [
    {
      code: "int x = 10;",
      explain: "Passo 1: A variável inteira x nasce no endereço 0x7ff0 com valor 10.",
      boxes: [
        { addr: "0x7ff0", name: "int x", val: "10", changed: true, ptr: false }
      ]
    },
    {
      code: "int *p = &x;",
      explain: "Passo 2: O ponteiro p (em 0x7ff4) guarda o endereço &x (0x7ff0).",
      boxes: [
        { addr: "0x7ff0", name: "int x", val: "10", changed: false, ptr: false },
        { addr: "0x7ff4", name: "int *p", val: "0x7ff0 -> x", changed: true, ptr: true }
      ]
    },
    {
      code: "*p = 20;",
      explain: "Passo 3: *p segue 0x7ff0 e altera o valor original de x para 20.",
      boxes: [
        { addr: "0x7ff0", name: "int x", val: "20", changed: true, ptr: false },
        { addr: "0x7ff4", name: "int *p", val: "0x7ff0 -> x", changed: false, ptr: true }
      ]
    },
    {
      code: "Aluno a = {101, 7.5}; Aluno *pa = &a;",
      explain: "Passo 4: A struct a ocupa 0x7ff8 e o ponteiro pa guarda 0x7ff8.",
      boxes: [
        { addr: "0x7ff8", name: "Aluno a", val: "{id: 101, nota: 7.5}", changed: true, ptr: false },
        { addr: "0x7ffc", name: "Aluno *pa", val: "0x7ff8 -> a", changed: true, ptr: true }
      ]
    },
    {
      code: "pa->nota = 8.5;",
      explain: "Passo 5: O operador seta (->) acessa (*pa).nota e atualiza a.nota para 8.5.",
      boxes: [
        { addr: "0x7ff8", name: "Aluno a", val: "{id: 101, nota: 8.5}", changed: true, ptr: false },
        { addr: "0x7ffc", name: "Aluno *pa", val: "0x7ff8 -> a", changed: false, ptr: true }
      ]
    }
  ];

  let studyData = null;
  let memIndex = 0;
  let ceAnswers = {};
  let simAnswers = {};
  let simFinished = false;
  let filterWrongOnly = false;
  let retrySubsetIds = null;
  let pendingHighlight = new Set();
  let timerSeconds = 0;
  let timerId = null;

  function plural(n, singular, pluralWord) {
    return n + " " + (n === 1 ? singular : pluralWord);
  }

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    return node;
  }

  function saveState() {
    try {
      localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ ceAnswers, simAnswers, simFinished })
      );
    } catch (_) {}
  }

  function loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      const parsed = JSON.parse(raw);
      ceAnswers = parsed.ceAnswers || {};
      simAnswers = parsed.simAnswers || {};
      simFinished = Boolean(parsed.simFinished);
    } catch (_) {}
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    const btn = document.getElementById("btn-theme");
    btn.textContent = theme === "dark" ? "Modo Claro" : "Modo Escuro";
  }

  function setupToolbar() {
    const savedTheme = localStorage.getItem(THEME_KEY) || "light";
    applyTheme(savedTheme);

    document.getElementById("btn-theme").addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
      const next = current === "dark" ? "light" : "dark";
      localStorage.setItem(THEME_KEY, next);
      applyTheme(next);
    });

    document.getElementById("btn-print").addEventListener("click", () => {
      window.print();
    });

    document.getElementById("btn-clear-progress").addEventListener("click", () => {
      ceAnswers = {};
      simAnswers = {};
      simFinished = false;
      filterWrongOnly = false;
      retrySubsetIds = null;
      pendingHighlight.clear();
      try {
        localStorage.removeItem(STORAGE_KEY);
      } catch (_) {}
      document.getElementById("sim-resultado").hidden = true;
      document.getElementById("sim-warning").hidden = true;
      renderCertoErrado(studyData);
      renderSimulado(studyData);
      syncSimButtons();
    });
  }

  function renderMemorySimulator() {
    const step = MEMORY_STEPS[memIndex];
    document.getElementById("mem-step-badge").textContent =
      "Passo " + (memIndex + 1) + " / " + MEMORY_STEPS.length;
    document.getElementById("mem-code-line").textContent = step.code;
    document.getElementById("mem-explain").textContent = step.explain;

    const grid = document.getElementById("mem-boxes");
    grid.innerHTML = "";
    step.boxes.forEach((b) => {
      const box = el(
        "div",
        "mem-box" + (b.changed ? " changed" : "") + (b.ptr ? " pointer-active" : "")
      );
      box.appendChild(el("div", "mem-addr", "End: " + b.addr));
      box.appendChild(el("div", "mem-name", b.name));
      box.appendChild(el("div", "mem-val", "Valor: " + b.val));
      grid.appendChild(box);
    });

    document.getElementById("mem-prev").disabled = memIndex === 0;
    document.getElementById("mem-next").disabled = memIndex === MEMORY_STEPS.length - 1;
  }

  function setupMemorySimulator() {
    document.getElementById("mem-prev").addEventListener("click", () => {
      if (memIndex > 0) {
        memIndex -= 1;
        renderMemorySimulator();
      }
    });
    document.getElementById("mem-next").addEventListener("click", () => {
      if (memIndex < MEMORY_STEPS.length - 1) {
        memIndex += 1;
        renderMemorySimulator();
      }
    });
    document.getElementById("mem-reset").addEventListener("click", () => {
      memIndex = 0;
      renderMemorySimulator();
    });
    renderMemorySimulator();
  }

  async function loadData() {
    if (window.__STUDY_DATA__) return window.__STUDY_DATA__;
    const resp = await fetch("./content.json");
    if (!resp.ok) throw new Error("Nao foi possivel carregar content.json");
    return resp.json();
  }

  function setupTabs() {
    const buttons = document.querySelectorAll(".tab-btn");
    const panels = document.querySelectorAll(".tab-panel");
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const target = btn.getAttribute("data-tab");
        buttons.forEach((b) => {
          const active = b === btn;
          b.classList.toggle("active", active);
          b.setAttribute("aria-selected", active ? "true" : "false");
        });
        panels.forEach((p) => p.classList.toggle("active", p.id === "tab-" + target));
      });
    });
  }

  function createCodeBlock(codeText) {
    const wrap = el("div", "code-wrap");
    const btn = el("button", "copy-btn no-print", "Copiar código");
    btn.type = "button";
    btn.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(codeText);
        btn.textContent = "Copiado!";
        setTimeout(() => {
          btn.textContent = "Copiar código";
        }, 1500);
      } catch (_) {
        btn.textContent = "Selecione e copie";
      }
    });
    const pre = el("pre");
    pre.appendChild(el("code", null, codeText));
    wrap.appendChild(btn);
    wrap.appendChild(pre);
    return wrap;
  }

  function renderHeader(data) {
    document.title = data.meta.titulo + " | Guia ADS";
    document.getElementById("meta-disciplina").textContent = data.meta.disciplina;
    document.getElementById("meta-versao").textContent = data.meta.versao;
    document.getElementById("meta-titulo").textContent = data.meta.titulo;
    document.getElementById("meta-resumo").textContent = data.meta.resumo_curto;
    document.getElementById("meta-tempo").textContent =
      "Leitura estimada: " + data.meta.tempo_leitura_min + " min";
    document.getElementById("meta-contagem").textContent =
      data.secoes_estudo.length +
      " blocos • " +
      data.certo_errado.length +
      " Certo/Errado • " +
      data.simulado.length +
      " questões no Simulado";
  }

  function renderResumo(data) {
    const root = document.getElementById("resumo-cards");
    root.innerHTML = "";

    data.secoes_estudo.forEach((sec) => {
      const card = el("article", "card");
      card.appendChild(el("h3", null, sec.titulo));
      card.appendChild(el("p", null, sec.explicacao_curta));

      const analogia = el("div", "callout callout-analogia");
      analogia.appendChild(el("strong", null, "Analogia rápida: "));
      analogia.appendChild(document.createTextNode(sec.analogia));
      card.appendChild(analogia);

      card.appendChild(createCodeBlock(sec.codigo_c));
      card.appendChild(el("p", null, sec.explicacao_codigo));

      const trap = el("div", "callout callout-armadilha");
      trap.appendChild(el("strong", null, "Armadilha comum: "));
      trap.appendChild(document.createTextNode(sec.armadilha_comum));
      card.appendChild(trap);

      root.appendChild(card);
    });
  }

  function updateCeScore() {
    const total = studyData.certo_errado.length;
    const answered = Object.keys(ceAnswers).length;
    const hits = studyData.certo_errado.filter((q) => ceAnswers[q.id] === q.gabarito).length;
    document.getElementById("ce-placar").textContent =
      answered + " / " + total + " " + (answered === 1 ? "respondida" : "respondidas") +
      " (" + plural(hits, "acerto", "acertos") + ")";
  }

  function renderCertoErrado(data) {
    const root = document.getElementById("ce-lista");
    root.innerHTML = "";

    data.certo_errado.forEach((q, idx) => {
      const card = el("article", "card");
      card.appendChild(el("h3", null, "Questão " + (idx + 1)));
      card.appendChild(el("p", null, q.enunciado));

      const actions = el("div", "ce-actions");
      const btnCerto = el("button", "btn-choice", "Certo");
      btnCerto.type = "button";
      const btnErrado = el("button", "btn-choice", "Errado");
      btnErrado.type = "button";
      const feedback = el("div", "feedback-box");
      feedback.hidden = true;

      function showChoice(choice) {
        const ok = choice === q.gabarito;
        btnCerto.className = "btn-choice" + (choice === true ? (ok ? " selected-ok" : " selected-err") : "");
        btnErrado.className = "btn-choice" + (choice === false ? (ok ? " selected-ok" : " selected-err") : "");

        feedback.className = "feedback-box " + (ok ? "ok" : "err");
        feedback.innerHTML = "";
        feedback.appendChild(
          el(
            "strong",
            null,
            (ok ? "Você acertou! " : "Resposta incorreta. ") +
              "Gabarito: " +
              (q.gabarito ? "CERTO" : "ERRADO")
          )
        );
        const ol = el("ol");
        q.explicacao_passos.forEach((s) => ol.appendChild(el("li", null, s)));
        feedback.appendChild(ol);

        const pk = el("p");
        pk.appendChild(el("strong", null, "Ponto-chave: "));
        pk.appendChild(document.createTextNode(q.ponto_chave));
        feedback.appendChild(pk);
        feedback.hidden = false;
      }

      if (typeof ceAnswers[q.id] === "boolean") {
        showChoice(ceAnswers[q.id]);
      }

      function onSelect(choice) {
        ceAnswers[q.id] = choice;
        saveState();
        showChoice(choice);
        updateCeScore();
      }

      btnCerto.addEventListener("click", () => onSelect(true));
      btnErrado.addEventListener("click", () => onSelect(false));

      actions.appendChild(btnCerto);
      actions.appendChild(btnErrado);
      card.appendChild(actions);
      card.appendChild(feedback);
      root.appendChild(card);
    });

    updateCeScore();
  }

  function activeQuestions() {
    if (!retrySubsetIds) return studyData.simulado;
    return studyData.simulado.filter((q) => retrySubsetIds.has(q.id));
  }

  function updateSimProgress() {
    const list = activeQuestions();
    const total = list.length;
    const marked = list.filter((q) => simAnswers[q.id] !== undefined).length;
    document.getElementById("sim-progresso").textContent =
      marked + " / " + total + " " + (marked === 1 ? "marcada" : "marcadas");
    const pct = total ? Math.round((marked / total) * 100) : 0;
    document.getElementById("sim-progress-fill").style.width = pct + "%";
  }

  function renderSimulado(data) {
    const root = document.getElementById("sim-lista");
    root.innerHTML = "";
    const list = activeQuestions();

    list.forEach((q, idx) => {
      const ok = simAnswers[q.id] === q.correta;
      if (simFinished && filterWrongOnly && ok) return;

      const card = el("article", "card" + (pendingHighlight.has(q.id) ? " sim-pending-card" : ""));
      card.appendChild(el("h3", null, "Questão " + (idx + 1)));
      card.appendChild(el("p", null, q.enunciado));

      if (q.codigo_opcional && q.codigo_opcional.trim()) {
        card.appendChild(createCodeBlock(q.codigo_opcional));
      }

      const optsWrap = el("div", "sim-options");
      q.alternativas.forEach((alt, optIdx) => {
        const label = el("label", "opt-label");
        const radio = document.createElement("input");
        radio.type = "radio";
        radio.name = "sim-" + q.id;
        radio.value = String(optIdx);
        radio.checked = simAnswers[q.id] === optIdx;
        radio.disabled = simFinished;
        radio.addEventListener("change", () => {
          simAnswers[q.id] = optIdx;
          pendingHighlight.delete(q.id);
          card.classList.remove("sim-pending-card");
          saveState();
          updateSimProgress();
        });
        label.appendChild(radio);
        label.appendChild(el("span", null, String.fromCharCode(65 + optIdx) + ") " + alt));

        if (simFinished) {
          if (optIdx === q.correta) label.classList.add("opt-correct");
          else if (simAnswers[q.id] === optIdx) label.classList.add("opt-wrong");
        }
        optsWrap.appendChild(label);
      });
      card.appendChild(optsWrap);

      if (simFinished) {
        const fb = el("div", "feedback-box " + (ok ? "ok" : "err"));
        fb.appendChild(
          el(
            "strong",
            null,
            (ok ? "Acertou! " : "Errou. ") +
              "Alternativa correta: " +
              String.fromCharCode(65 + q.correta)
          )
        );
        fb.appendChild(el("p", null, q.explicacao_correta));
        const why = el("p");
        why.appendChild(el("strong", null, "Por que as outras falham: "));
        why.appendChild(document.createTextNode(q.por_que_outras_falham));
        fb.appendChild(why);
        card.appendChild(fb);
      }

      root.appendChild(card);
    });

    updateSimProgress();
  }

  function formatTimer(sec) {
    const m = String(Math.floor(sec / 60)).padStart(2, "0");
    const s = String(sec % 60).padStart(2, "0");
    return m + ":" + s;
  }

  function setupTimer() {
    const display = document.getElementById("sim-timer");
    const btnToggle = document.getElementById("btn-timer-toggle");
    const btnReset = document.getElementById("btn-timer-reset");

    btnToggle.addEventListener("click", () => {
      if (timerId) {
        clearInterval(timerId);
        timerId = null;
        btnToggle.textContent = "Retomar Timer";
      } else {
        timerId = setInterval(() => {
          timerSeconds += 1;
          display.textContent = formatTimer(timerSeconds);
        }, 1000);
        btnToggle.textContent = "Pausar Timer";
      }
    });

    btnReset.addEventListener("click", () => {
      clearInterval(timerId);
      timerId = null;
      timerSeconds = 0;
      display.textContent = "00:00";
      btnToggle.textContent = "Iniciar Timer";
    });
  }

  function syncSimButtons() {
    const btnFinish = document.getElementById("btn-finalizar-simulado");
    const btnForce = document.getElementById("btn-force-finalizar");
    const btnFilter = document.getElementById("btn-filter-wrong");
    const btnRetryWrong = document.getElementById("btn-retry-wrong");
    const btnReset = document.getElementById("btn-refazer-simulado");
    const banner = document.getElementById("sim-resultado");

    btnFinish.hidden = simFinished;
    btnForce.hidden = true;
    btnFilter.hidden = !simFinished;
    btnReset.hidden = !simFinished;

    if (simFinished) {
      const list = activeQuestions();
      const total = list.length;
      const hits = list.filter((q) => simAnswers[q.id] === q.correta).length;
      const wrongCount = total - hits;
      const pct = total ? Math.round((hits / total) * 100) : 0;
      banner.textContent =
        "Placar Final: " + plural(hits, "acerto", "acertos") +
        " de " + total + " (" + pct + "%) • Tempo: " + formatTimer(timerSeconds);
      banner.hidden = false;
      btnRetryWrong.hidden = wrongCount === 0;
      btnFilter.textContent = filterWrongOnly ? "Ver todas as questões" : "Ver apenas as que errei";
    } else {
      banner.hidden = true;
      btnRetryWrong.hidden = true;
    }
  }

  function finishSimulado() {
    simFinished = true;
    pendingHighlight.clear();
    document.getElementById("sim-warning").hidden = true;
    if (timerId) {
      clearInterval(timerId);
      timerId = null;
      document.getElementById("btn-timer-toggle").textContent = "Iniciar Timer";
    }
    saveState();
    syncSimButtons();
    renderSimulado(studyData);
  }

  function setupSimButtons() {
    const btnFinish = document.getElementById("btn-finalizar-simulado");
    const btnForce = document.getElementById("btn-force-finalizar");
    const btnFilter = document.getElementById("btn-filter-wrong");
    const btnRetryWrong = document.getElementById("btn-retry-wrong");
    const btnReset = document.getElementById("btn-refazer-simulado");
    const warning = document.getElementById("sim-warning");

    btnFinish.addEventListener("click", () => {
      const list = activeQuestions();
      const missingNums = [];
      pendingHighlight.clear();
      list.forEach((q, idx) => {
        if (simAnswers[q.id] === undefined) {
          missingNums.push(idx + 1);
          pendingHighlight.add(q.id);
        }
      });

      if (missingNums.length > 0) {
        warning.textContent =
          "Faltam responder: Questão " +
          missingNums.join(", ") +
          ". Responda ou clique em 'Finalizar mesmo assim'.";
        warning.hidden = false;
        btnForce.hidden = false;
        renderSimulado(studyData);
        return;
      }
      finishSimulado();
    });

    btnForce.addEventListener("click", finishSimulado);

    btnFilter.addEventListener("click", () => {
      filterWrongOnly = !filterWrongOnly;
      syncSimButtons();
      renderSimulado(studyData);
    });

    btnRetryWrong.addEventListener("click", () => {
      const wrongIds = activeQuestions()
        .filter((q) => simAnswers[q.id] !== q.correta)
        .map((q) => q.id);
      if (wrongIds.length === 0) return;
      retrySubsetIds = new Set(wrongIds);
      wrongIds.forEach((id) => delete simAnswers[id]);
      simFinished = false;
      filterWrongOnly = false;
      saveState();
      syncSimButtons();
      renderSimulado(studyData);
    });

    btnReset.addEventListener("click", () => {
      simFinished = false;
      filterWrongOnly = false;
      retrySubsetIds = null;
      pendingHighlight.clear();
      Object.keys(simAnswers).forEach((k) => delete simAnswers[k]);
      warning.hidden = true;
      saveState();
      syncSimButtons();
      renderSimulado(studyData);
    });
  }

  function renderReferences(data) {
    const ul = document.getElementById("lista-referencias");
    ul.innerHTML = "";
    data.referencias.forEach((ref) => {
      const li = el("li");
      const a = document.createElement("a");
      a.href = ref.url;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.textContent = ref.titulo;
      li.appendChild(a);
      li.appendChild(document.createTextNode(" (" + ref.tipo + ")"));
      ul.appendChild(li);
    });
  }

  async function init() {
    try {
      loadState();
      setupToolbar();
      setupTabs();
      setupMemorySimulator();
      setupTimer();
      setupSimButtons();
      studyData = await loadData();
      renderHeader(studyData);
      renderResumo(studyData);
      renderCertoErrado(studyData);
      renderSimulado(studyData);
      syncSimButtons();
      renderReferences(studyData);
    } catch (err) {
      document.getElementById("meta-titulo").textContent = "Erro ao carregar material";
      document.getElementById("meta-resumo").textContent = String(err);
    }
  }

  document.addEventListener("DOMContentLoaded", init);
})();
