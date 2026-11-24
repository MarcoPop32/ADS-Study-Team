(function () {
  "use strict";

  let studyData = null;
  const ceAnswers = {};
  const simAnswers = {};
  let simFinished = false;

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    return node;
  }

  async function loadData() {
    if (window.__STUDY_DATA__) {
      return window.__STUDY_DATA__;
    }
    const resp = await fetch("./content.json");
    if (!resp.ok) {
      throw new Error("Nao foi possivel carregar content.json");
    }
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
        panels.forEach((p) => {
          p.classList.toggle("active", p.id === "tab-" + target);
        });
      });
    });
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
    const root = document.getElementById("tab-resumo");
    root.innerHTML = "";
    const stack = el("div", "stack");

    data.secoes_estudo.forEach((sec) => {
      const card = el("article", "card");
      card.appendChild(el("h3", null, sec.titulo));
      card.appendChild(el("p", null, sec.explicacao_curta));

      const analogia = el("div", "callout callout-analogia");
      const strongA = el("strong", null, "Analogia rápida: ");
      analogia.appendChild(strongA);
      analogia.appendChild(document.createTextNode(sec.analogia));
      card.appendChild(analogia);

      const pre = el("pre");
      const code = el("code", null, sec.codigo_c);
      pre.appendChild(code);
      card.appendChild(pre);

      card.appendChild(el("p", null, sec.explicacao_codigo));

      const trap = el("div", "callout callout-armadilha");
      const strongT = el("strong", null, "Armadilha comum: ");
      trap.appendChild(strongT);
      trap.appendChild(document.createTextNode(sec.armadilha_comum));
      card.appendChild(trap);

      stack.appendChild(card);
    });

    root.appendChild(stack);
  }

  function updateCeScore() {
    const total = studyData.certo_errado.length;
    const answered = Object.keys(ceAnswers).length;
    const hits = studyData.certo_errado.filter(
      (q) => ceAnswers[q.id] === q.gabarito
    ).length;
    document.getElementById("ce-placar").textContent =
      answered + " / " + total + " respondidas (" + hits + " acertos)";
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

      function handleChoice(choice) {
        ceAnswers[q.id] = choice;
        const ok = choice === q.gabarito;
        btnCerto.className = "btn-choice" + (choice === true ? (ok ? " selected-ok" : " selected-err") : "");
        btnErrado.className = "btn-choice" + (choice === false ? (ok ? " selected-ok" : " selected-err") : "");

        feedback.className = "feedback-box " + (ok ? "ok" : "err");
        feedback.innerHTML = "";
        const statusText = ok
          ? "Você acertou! Gabarito: " + (q.gabarito ? "CERTO" : "ERRADO")
          : "Resposta incorreta. Gabarito: " + (q.gabarito ? "CERTO" : "ERRADO");
        feedback.appendChild(el("strong", null, statusText));

        const ol = el("ol");
        q.explicacao_passos.forEach((step) => {
          ol.appendChild(el("li", null, step));
        });
        feedback.appendChild(ol);

        const pk = el("p");
        pk.appendChild(el("strong", null, "Ponto-chave: "));
        pk.appendChild(document.createTextNode(q.ponto_chave));
        feedback.appendChild(pk);

        feedback.hidden = false;
        updateCeScore();
      }

      btnCerto.addEventListener("click", () => handleChoice(true));
      btnErrado.addEventListener("click", () => handleChoice(false));

      actions.appendChild(btnCerto);
      actions.appendChild(btnErrado);
      card.appendChild(actions);
      card.appendChild(feedback);
      root.appendChild(card);
    });

    updateCeScore();
  }

  function updateSimProgress() {
    const total = studyData.simulado.length;
    const marked = Object.keys(simAnswers).length;
    document.getElementById("sim-progresso").textContent =
      marked + " / " + total + " marcadas";
  }

  function renderSimulado(data) {
    const root = document.getElementById("sim-lista");
    root.innerHTML = "";

    data.simulado.forEach((q, idx) => {
      const card = el("article", "card");
      card.setAttribute("data-qid", q.id);
      card.appendChild(el("h3", null, "Questão " + (idx + 1)));
      card.appendChild(el("p", null, q.enunciado));

      if (q.codigo_opcional && q.codigo_opcional.trim()) {
        const pre = el("pre");
        pre.appendChild(el("code", null, q.codigo_opcional));
        card.appendChild(pre);
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
          updateSimProgress();
        });

        label.appendChild(radio);
        label.appendChild(el("span", null, String.fromCharCode(65 + optIdx) + ") " + alt));

        if (simFinished) {
          if (optIdx === q.correta) {
            label.classList.add("opt-correct");
          } else if (simAnswers[q.id] === optIdx) {
            label.classList.add("opt-wrong");
          }
        }
        optsWrap.appendChild(label);
      });
      card.appendChild(optsWrap);

      if (simFinished) {
        const ok = simAnswers[q.id] === q.correta;
        const fb = el("div", "feedback-box " + (ok ? "ok" : "err"));
        fb.appendChild(
          el(
            "strong",
            null,
            ok
              ? "Acertou! Alternativa correta: " + String.fromCharCode(65 + q.correta)
              : "Errou. Alternativa correta: " + String.fromCharCode(65 + q.correta)
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

  function setupSimButtons() {
    const btnFinish = document.getElementById("btn-finalizar-simulado");
    const btnReset = document.getElementById("btn-refazer-simulado");
    const banner = document.getElementById("sim-resultado");

    btnFinish.addEventListener("click", () => {
      simFinished = true;
      const total = studyData.simulado.length;
      const hits = studyData.simulado.filter(
        (q) => simAnswers[q.id] === q.correta
      ).length;
      const pct = Math.round((hits / total) * 100);

      banner.textContent =
        "Placar Final: " + hits + " de " + total + " acertos (" + pct + "%)";
      banner.hidden = false;
      btnFinish.hidden = true;
      btnReset.hidden = false;
      renderSimulado(studyData);
    });

    btnReset.addEventListener("click", () => {
      simFinished = false;
      Object.keys(simAnswers).forEach((k) => delete simAnswers[k]);
      banner.hidden = true;
      btnFinish.hidden = false;
      btnReset.hidden = true;
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
      setupTabs();
      setupSimButtons();
      studyData = await loadData();
      renderHeader(studyData);
      renderResumo(studyData);
      renderCertoErrado(studyData);
      renderSimulado(studyData);
      renderReferences(studyData);
    } catch (err) {
      document.getElementById("meta-titulo").textContent = "Erro ao carregar material";
      document.getElementById("meta-resumo").textContent = String(err);
    }
  }

  document.addEventListener("DOMContentLoaded", init);
})();
