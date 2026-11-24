# Dossiê Técnico — Ponteiros, Struct e Arquivo em C (ATP)

## 1. Conceitos Centrais (Direto ao Ponto)
- **Ponteiros:** guardam um endereço de memória (`&var` obtém o endereço; `*ptr` acessa/altera o valor no endereço). Sempre inicializar ponteiros não atribuídos com `NULL` e validar antes de desreferenciar. Passar ponteiro para função permite alterar o dado original sem copiar grandes blocos.
- **Struct (`typedef struct`):** agrupa variáveis heterogêneas em um registro. Com variável direta usa-se ponto (`aluno.nota`); com **ponteiro para struct** usa-se seta (`p->nota`, equivalente a `(*p).nota`).
- **Arquivos (`FILE *`):** `FILE` é uma estrutura opaca de `<stdio.h>` que controla o fluxo (*stream*). Você sempre manipula via ponteiro `FILE *`.
  - `fopen(nome, modo)`: abre o arquivo (`"r"`, `"w"`, `"a"`, `"rb"`, `"wb"`, `"r+"`, `"w+"`, `"a+"`). No Windows, o modificador `"b"` evita conversão automática de `\n` para `\r\n` e tratamento especial de `\x1A`. Retorna `NULL` se falhar.
  - `fclose(fp)`: descarrega o buffer e libera o recurso.
  - Texto (`fprintf`, `fscanf`, `fgets`) vs Binário (`fread`, `fwrite`, que retornam a quantidade de itens lidos/escritos).

## 2. Exemplo Integrado Válido (Struct + Ponteiro + Arquivo Binário)
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int matricula;
    char nome[40]; // Array fixo: seguro para gravar em bloco
    float media;
} Aluno;

void atualizarMedia(Aluno *a, float novaMedia) {
    if (a != NULL) {
        a->media = novaMedia; // Acesso via ponteiro com '->'
    }
}

int main(void) {
    Aluno a1 = {101, "Ana Silva", 7.5f};
    atualizarMedia(&a1, 8.5f);

    FILE *fp = fopen("alunos.bin", "wb");
    if (fp == NULL) {
        perror("Erro ao abrir arquivo");
        return EXIT_FAILURE;
    }
    if (fwrite(&a1, sizeof(Aluno), 1, fp) != 1) {
        fprintf(stderr, "Falha na gravacao.\n");
    }
    fclose(fp);

    Aluno lido;
    fp = fopen("alunos.bin", "rb");
    if (fp != NULL && fread(&lido, sizeof(Aluno), 1, fp) == 1) {
        printf("%d - %s: %.1f\n", lido.matricula, lido.nome, lido.media);
    }
    if (fp != NULL) fclose(fp);
    return 0;
}
```

## 3. Armadilhas Clássicas de ATP
1. **Esquecer `if (fp == NULL)` após `fopen`:** tentar ler/gravar em ponteiro nulo gera falha de segmentação (*Segmentation Fault*).
2. **Gravar `struct` com ponteiro interno (`char *nome`) via `fwrite`:** grava apenas o endereço de memória temporário, não a string. Na leitura seguinte o endereço será inválido (*dangling pointer*). Além disso, Beej's Guide alerta que `fwrite` direto de `struct` não é portável entre compiladores/arquiteturas por causa de *padding* e *endianness* (para portabilidade real, serialize campo a campo).
3. **Confundir `.` com `->` ou esquecer `"b"` no Windows:** usar `p.campo` quando `p` é ponteiro causa erro de compilação; abrir binário sem `"b"` no Windows corrompe bytes `0x0A`/`0x1A`.

## 4. Fontes Verificadas
1. **Beej's Guide to C Programming — File I/O (Cap. 9):** https://beej.us/guide/bgc/html/split/file-inputoutput.html
2. **Beej's Guide to C Programming — Structs (Cap. 8):** https://beej.us/guide/bgc/html/split/structs.html
3. **cppreference — `fopen, fopen_s` (`<stdio.h>`):** https://en.cppreference.com/c/io/fopen
4. **cppreference — `fread` (`<stdio.h>`):** https://en.cppreference.com/w/c/io/fread
5. **cppreference — `fwrite` (`<stdio.h>`):** https://en.cppreference.com/w/c/io/fwrite
