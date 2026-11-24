# Dossiê Técnico — Ponteiros, Struct e Arquivo em C (ATP - v3)

## 1. Conceitos Centrais (Direto ao Ponto)
- **Ponteiros:** guardam endereço de memória (`&var` obtém endereço; `*ptr` acessa/altera o valor). Sempre inicializar ponteiros sem destino com `NULL` e validar antes de desreferenciar.
- **Struct (`typedef struct`):** agrupa campos heterogêneos. Instância direta usa ponto (`a.nota`); ponteiro para struct usa seta (`pa->nota`, equivalente a `(*pa).nota`). Passar `struct` grande por valor copia todos os bytes na pilha e não altera o original; passar por ponteiro (`Aluno *pa`) altera o original e evita cópia.
- **Arquivos (`FILE *`):** manipulados por ponteiro `FILE *` via `fopen(caminho, modo)` e fechados com `fclose(fp)`.
  - Modos texto (`"r"`, `"w"`, `"a"`, `"r+"`, `"w+"`, `"a+"`) vs binário (`"rb"`, `"wb"`, `"ab"`, `"r+b"`, `"w+b"`). No Windows, `"b"` evita tradução `\n` ↔ `\r\n` e `\x1A`.
  - **Regra crítica de atualização (`'+'`, ex.: `"r+"`):** segundo o cppreference, após escrever e antes de ler é obrigatório chamar `fflush`, `fseek`, `fsetpos` ou `rewind`; após ler e antes de escrever é obrigatório chamar `fseek`, `fsetpos` ou `rewind` (salvo EOF).
  - `fread`/`fwrite` retornam o **número de itens** processados, nunca bytes. `fgetc` retorna `int` para distinguir `EOF`. `fgets` protege contra *buffer overflow*.

## 2. Armadilhas Clássicas de ATP
1. Esquecer `if (fp == NULL)` após `fopen`.
2. Gravar `struct` com `char *nome` via `fwrite` (grava o endereço em vez da string) ou confiar em `fwrite` de `struct` como formato portável entre arquiteturas (*padding*/*endianness*).
3. Alternar escrita e leitura em modo `"r+"` sem `fseek`/`fflush`/`rewind`.

## 3. Fontes Verificadas
1. **Beej's Guide to C Programming — File I/O (Cap. 9):** https://beej.us/guide/bgc/html/split/file-inputoutput.html
2. **Beej's Guide to C Programming — Structs (Cap. 8):** https://beej.us/guide/bgc/html/split/structs.html
3. **cppreference — `fopen, fopen_s` (`<stdio.h>`):** https://en.cppreference.com/c/io/fopen
4. **cppreference — `fread` (`<stdio.h>`):** https://en.cppreference.com/w/c/io/fread
5. **cppreference — `fwrite` (`<stdio.h>`):** https://en.cppreference.com/w/c/io/fwrite
