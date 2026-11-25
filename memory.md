# Memória Curta do Time ADS

- **Perfil:** Estudante de Análise e Desenvolvimento de Sistemas (ADS), foco atual em ATP (linguagem C).
- **Estilo de texto:** Direto ao ponto, zero enrolação, blocos escaneáveis, analogias curtas e código comentado.
- **Formato padrão v4.0 (Guia Mestre):** Módulos temáticos com roteiro lateral sticky + filtro de pendentes, rastreio passo a passo na RAM embutido em cada código, Micro-Sandboxes ao vivo, Central Prática (30 MCQs A–E por módulo com minimapa 1..30 e favoritos + 10 Certo/Errado + 2 clássicos resolvidos), Simulados ATP cronometrados de 2h (14 questões) e Playground C com structs/ponteiros/`FILE *` virtual, compatível com GitHub Pages e iframe 700px do Google Sites.
- **Padrão UI v4.0:** Design System com barra de progresso de leitura, Modo Escuro completo, controle `A−`/`A+`, Timer Pomodoro (`🍅 25:00`), busca global (`/` ou `Ctrl+K`), Cheat Sheet de 4 abas, animações com suporte a `prefers-reduced-motion` e persistência via `localStorage`.
- **Critério mínimo de aprovação:** Nota >= 85 no Verificador, zero erros de console, 100% dos subtópicos solicitados com rastreios e testes funcionais nos Simulados ATP (`18/18` nos casos C de prova).
- **Métrica semanal de sucesso:** Taxa de Aprovação de Primeira (% de pacotes aprovados na Rodada 1).
- **Lições aprendidas (top 5):**
  1. Em C, nunca serializar `struct` contendo ponteiro interno (`char *`) com `fwrite` direto — usar arrays fixos ou serialização campo a campo.
  2. Sempre validar retorno `NULL` de `fopen` e usar `"rb"`/`"wb"` para arquivos binários no Windows (e `fseek`/`fflush` ao alternar leitura/escrita em `r+`).
  3. Testar a interface em largura estreita (`~700px` Google Sites) garantindo `min-width: 0` em filhos de CSS Grid para zerar overflow horizontal.
  4. Cuidar de concordância singular/plural e oferecer botão `← Lobby` mesmo durante simulado em andamento.
  5. Ao transpilar C para JS em Playground/Simulados, dividir declarações de struct respeitando profundidade de parênteses (`__splitTopArgs`), suportar `malloc(n * sizeof(Struct))` com fábrica de objeto e aplicar boxing `&var` por escopo de função.
