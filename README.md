# ADS Study Team — Fábrica Multiagente de Materiais Interativos

Time real de 5 agentes de IA construído com **Google Antigravity Skills** e **Google ADK 2.15.0** (`gemini-4-neon`) em arquitetura de **grafo com execução paralela (fan-out + join), loop de qualidade (máx. 2 rodadas), aprovação humana (HITL) e revisão semanal**.

## O que este projeto resolve
Transforma qualquer assunto de aula de **Análise e Desenvolvimento de Sistemas (ADS)** em um pacote interativo de estudo direto ao ponto — sem enrolação — pronto para **GitHub Pages** e **Google Sites**:
- **Visualização e Simulação v4.0 (Guia Mestre em C):**
  - **53 Tópicos completos** (18 Ponteiros + 18 Structs + 17 Arquivos) com diagramas de memória, rastreio passo a passo embutido e 3 Micro-Sandboxes interativos (Stack/Heap, Padding/Union, Modos `fopen`/`fseek`).
  - **120+ Itens Práticos:** 90 questões A–E (30 por categoria com minimapa `1..30` e favoritos `★`), 30 afirmações Certo/Errado, 6 problemas clássicos resolvidos e **3 Simulados ATP cronometrados (2h, 14 questões)** com corretor automático C.
  - **Playground C Estendido:** executa `struct`, `.` / `->`, `&` / `*`, `malloc`/`calloc`/`realloc`/`free` e sistema de arquivos virtual (`FILE *` com `fopen`, `fprintf`, `fscanf`, `fwrite`, `fread`, `fseek`, `ftell`).
  - **UX de Estudo:** Modo Escuro, `A−`/`A+`, busca global (`/` ou `Ctrl+K`), Cheat Sheet pré-prova em 4 abas e Timer Pomodoro (`🍅 25:00`).

---

## Instalação em 3 passos

1. **Clone o repositório e crie o ambiente virtual:**
   ```powershell
   git clone https://github.com/MarcoPop32/ADS-Study-Team.git
   cd ADS-Study-Team
   python -m venv .venv
   ```

2. **Instale as dependências no `.venv`:**
   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. **Configure sua chave da API Gemini no ambiente (nunca no código):**
   ```powershell
   $env:GEMINI_API_KEY = "SUA_CHAVE_AQUI"
   ```
   *(Opcional no Antigravity: abra esta pasta como workspace para executar diretamente pelas 5 Skills em `.agents/skills/`.)*

---

## Como rodar (comando único)

- **Validar o grafo ADK 2.x:**
  ```powershell
  .\.venv\Scripts\python.exe run_team.py --validate-graph
  ```
- **Gerar um novo material pela API Gemini (`gemini-4-neon`):**
  ```powershell
  .\.venv\Scripts\python.exe run_team.py --topic "Alocação Dinâmica (malloc/free) em C"
  ```
- **Gerar/Recompilar o Guia Mestre v4.0:**
  ```powershell
  .\.venv\Scripts\python.exe builder\build_master_site.py
  ```
- **Validar o pacote v4:**
  ```powershell
  .\.venv\Scripts\python.exe builder\build_master_site.py
  ```

---

## Publicação no GitHub Pages e Google Sites

1. **GitHub Pages:** no repositório do GitHub, vá em **Settings → Pages → Build and deployment**, escolha **Deploy from a branch**, selecione `main` e a pasta `/docs`.
2. **Google Sites (2 opções):**
   - **Por URL (recomendado):** *Inserir → Incorporar → Por URL* e cole a URL publicada do seu GitHub Pages.
   - **Por código HTML único:** *Inserir → Incorporar → Incorporar código* e cole o conteúdo de `docs/embed-google-sites.html`.

---

## Arquitetura do Time (5 Agentes)

| Agente | Papel |
| :--- | :--- |
| **Lead** | Lê `memory.md`, fecha o briefing, coordena o grafo, registra `logs/runs.jsonl` e conduz a revisão semanal. |
| **Pesquisador** | Consulta fontes técnicas reais e gera `dossie.md` enxuto (mín. 3 referências). |
| **Conteudista** *(Paralelo A)* | Gera `content.json` aderente ao `schema.json` (resumo, Certo/Errado passo a passo e Simulado). |
| **Construtor** *(Paralelo B)* | Gera interface responsiva (`index.html`, `styles.css`, `app.js`) compatível com GitHub Pages e iframe do Google Sites. |
| **Verificador** | Audita precisão, schema e UI (nota 0–100; aprova ≥ 85 ou devolve ao agente responsável em até 2 rodadas). |

## Estrutura do Projeto
- `.agents/skills/` — As 5 Skills do time no Google Antigravity
- `src/ads_team/` — Grafo ADK 2.15.0 (`workflow.py`), prompts (`prompts.py`) e validadores (`tools.py`)
- `builder/` — Módulos geradores da v4.0 (`spec.py`, `mod_*.py`, `ex_*.py`, `simulados_atp.py`, `ui_template.py`, `build_master_site.py`)
- `docs/` — Pacote web publicado (`v4`: Guia Mestre — 53 tópicos de Ponteiros, Structs e Arquivos em C)
- `outputs/` — Histórico evolutivo auditado (`v1` → `v2` → `v3` → `v4-guia-mestre-ponteiros-structs-arquivos`)
- `logs/runs.jsonl` — Métricas das execuções para o loop semanal
- `memory.md` & `schema.json` — Memória curta do time e contrato de dados
