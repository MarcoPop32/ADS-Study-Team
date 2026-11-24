# Briefing — Material de Estudo ADS (v2)

- **Disciplina:** ATP (Algoritmo e Técnicas de Programação)
- **Tema:** Ponteiros, Struct e Arquivo em Linguagem C
- **Público:** Estudante de ADS buscando revisão prática direta ao ponto para atividades e prova.
- **Memória aplicada (`memory.md`):** Blocos curtos e escaneáveis, analogias objetivas, código C comentado, compatível com GitHub Pages e iframe do Google Sites (~700px).
- **Subtópicos obrigatórios:**
  1. Ponteiros: endereço (`&`), desreferência (`*`), ponteiro `NULL` e passagem por referência em funções.
  2. Structs: definição com `typedef struct`, acesso com `.` vs ponteiro para struct com `->`.
  3. Arquivos (`FILE *`): `fopen`, `fclose`, modos texto (`"r"`, `"w"`, `"a"`) vs binário (`"rb"`, `"wb"`), `fprintf`/`fscanf`, `fread`/`fwrite`, checagem de `NULL` e `feof`/`ferror`.
  4. Integração dos 3: gravar e ler `struct` em arquivo usando ponteiros (e por que nunca usar `fwrite` direto em `struct` que guarda ponteiro interno como `char *`).
- **Entregáveis esperados:** `dossie.md` (<= 1 página, 3+ fontes reais), `content.json` (min. 6 Certo/Errado passo a passo + min. 5 Simulado), UI web responsiva.
