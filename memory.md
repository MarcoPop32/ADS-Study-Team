# Memória Curta do Time ADS

- **Perfil:** Estudante de Análise e Desenvolvimento de Sistemas (ADS), foco atual em ATP (linguagem C).
- **Estilo de texto:** Direto ao ponto, zero enrolação, blocos escaneáveis, analogias curtas e código comentado.
- **Formato padrão:** 3 abas (`Resumo Direto`, `Certo ou Errado`, `Simulado`), compatível com GitHub Pages e iframe do Google Sites.
- **Padrão UI v2+:** Simulador visual de memória/ponteiros, botão Copiar código, Modo Escuro, Imprimir/PDF, Timer de prova, filtro de erros, persistência em `localStorage` e busca rápida + cola `fopen`.
- **Critério mínimo de aprovação:** Nota >= 85 no Verificador, zero erros de console, gabarito 100% alinhado ao dossiê e links reais.
- **Métrica semanal de sucesso:** Taxa de Aprovação de Primeira (% de pacotes aprovados na Rodada 1).
- **Lições aprendidas (top 4):**
  1. Em C, nunca serializar `struct` contendo ponteiro interno (`char *`) com `fwrite` direto — usar arrays fixos ou serialização campo a campo.
  2. Sempre validar retorno `NULL` de `fopen` e usar `"rb"`/`"wb"` para arquivos binários no Windows (e `fseek`/`fflush` ao alternar leitura/escrita em `r+`).
  3. Testar a interface também em largura estreita (~700px) para evitar corte horizontal no embed do Google Sites.
  4. Cuidar de concordância singular/plural (`1 acerto` vs `2 acertos`) e avisar antes de finalizar simulado incompleto.
