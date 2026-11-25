"""Banco de Exercícios — Módulo 3: Arquivos em C (30 MCQs, 10 C/E, 2 Clássicos)."""
from __future__ import annotations

MCQ_ARQUIVOS = [
    {
        "id": "q-arq-1",
        "category": "arquivos",
        "subtopic": "3.1 Conceito",
        "level": "Básico",
        "title": "Persistência e Diferença entre Arquivo Texto e Binário",
        "stem": (
            "Sobre a representação do inteiro `int x = 1000000;` (em sistema de 32 bits) gravado em um arquivo texto "
            "via `fprintf(ft, \"%d\", x)` em comparação com um arquivo binário via `fwrite(&x, sizeof(int), 1, fb)`, "
            "assinale a alternativa correta:"
        ),
        "options": [
            "Ambos os arquivos passam a ocupar exatamente 4 bytes em disco.",
            "O arquivo texto grava 7 bytes ('1' e seis '0's em ASCII), enquanto o binário grava 4 bytes fixos.",
            "O arquivo binário grava 7 bytes, enquanto o arquivo texto grava 4 bytes.",
            "O arquivo texto não permite armazenar números inteiros negativos.",
            "O arquivo binário só funciona em sistemas Linux, pois Windows não suporta bytes crus."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `fprintf` converte o número para dígitos ASCII (7 caracteres = 7 bytes), não 4 bytes.",
            "Correta: `1000000` tem 7 dígitos ASCII (7 bytes em texto), mas um `int` de 32 bits ocupa sempre 4 bytes em binário.",
            "Incorreta: a relação é exatamente oposta.",
            "Incorreta: `fprintf` grava '-' seguido dos dígitos normalmente.",
            "Incorreta: ambos os sistemas suportam arquivos binários (no Windows usa-se o sufixo `'b'` em `fopen`)."
        ],
        "gabaritoResumo": "Texto converte números para caracteres ASCII (1 byte por dígito); binário copia sizeof(int) = 4 bytes.",
        "steps": [
            "Conte os caracteres da representação decimal de 1000000: '1' + seis '0's = 7 bytes em ASCII.",
            "Verifique o tamanho de `int` em 32 bits: `sizeof(int) == 4` bytes fixos em `fwrite`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    int x = 1000000;\n"
            "    FILE *ft = fopen(\"t.txt\", \"w\");\n"
            "    FILE *fb = fopen(\"b.bin\", \"wb\");\n"
            "    if (ft && fb) {\n"
            "        fprintf(ft, \"%d\", x);           // 7 bytes\n"
            "        fwrite(&x, sizeof(int), 1, fb);  // 4 bytes\n"
            "    }\n"
            "    if (ft) fclose(ft);\n"
            "    if (fb) fclose(fb);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-2",
        "category": "arquivos",
        "subtopic": "3.2 Ponteiro FILE *",
        "level": "Básico",
        "title": "Papel do Tipo FILE * em <stdio.h>",
        "stem": "Na linguagem C, ao declarar `FILE *fp;` com `<stdio.h>`, o que `fp` efetivamente armazena após um `fopen` bem-sucedido?",
        "options": [
            "Uma cópia completa de todos os bytes do arquivo carregada na stack.",
            "O nome literal do arquivo como uma string C.",
            "O endereço de uma estrutura de controle de fluxo (descritor, buffer, posição e flags) gerenciada pela libc.",
            "Apenas o número da porta de entrada/saída do controlador de disco.",
            "Um ponteiro para a primeira função do arquivo executável."
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: `fopen` não carrega o arquivo inteiro para a stack; a leitura é feita sob demanda via buffer.",
            "Incorreta: o nome do arquivo é apenas passado como `const char *` para `fopen`.",
            "Correta: `FILE` é uma `struct` opaca em `<stdio.h>` contendo descritor, ponteiros de buffer, offset atual e flags.",
            "Incorreta: arquivos são abstraídos pelo SO e pela libc, sem acesso direto a portas de hardware.",
            "Incorreta: `FILE *` é ponteiro para dados de stream, não ponteiro para função."
        ],
        "gabaritoResumo": "FILE * aponta para a estrutura de controle de stream mantida por <stdio.h>.",
        "steps": [
            "Identifique que `FILE` é definido via `typedef struct` em `<stdio.h>`.",
            "Lembre que `fopen` retorna o endereço (`FILE *`) dessa estrutura para as demais funções de E/S."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"arq.txt\", \"w\");\n"
            "    if (fp != NULL) {\n"
            "        fputs(\"ok\", fp);\n"
            "        fclose(fp);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-3",
        "category": "arquivos",
        "subtopic": "3.3 Abertura e fechamento",
        "level": "Básico",
        "title": "Tratamento Correto de Falha em fopen",
        "stem": "Qual trecho demonstra o tratamento seguro e sem comportamento indefinido ao tentar abrir `cfg.txt` apenas para leitura?",
        "options": [
            "FILE *fp = fopen(\"cfg.txt\", \"r\"); fclose(fp);",
            "FILE *fp = fopen(\"cfg.txt\", \"r\"); if (!fp) { fclose(fp); return 1; }",
            "FILE *fp = fopen(\"cfg.txt\", \"r\"); if (fp == NULL) { perror(\"cfg.txt\"); return 1; }",
            "FILE fp = fopen(\"cfg.txt\", \"r\"); if (fp == 0) return 1;",
            "FILE *fp; fopen(\"cfg.txt\", \"r\"); if (fp == NULL) return 1;"
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: se `fopen` retornar `NULL`, chamar `fclose(NULL)` gera comportamento indefinido (crash).",
            "Incorreta: chama `fclose(fp)` justamente dentro do `if (!fp)`, quando `fp` é `NULL`!",
            "Correta: testa `fp == NULL` antes de usar `fp`, relata o erro e retorna sem chamar `fclose(NULL)`.",
            "Incorreta: `fopen` retorna `FILE *`, não `FILE` por valor.",
            "Incorreta: o retorno de `fopen` foi descartado e `fp` continua não inicializado."
        ],
        "gabaritoResumo": "Verifique if (fp == NULL) antes de usar fp e nunca passe NULL para fclose().",
        "steps": [
            "Descarte opções que chamam `fclose(fp)` quando `fp` é `NULL` ou ignoram o retorno de `fopen`.",
            "Confirme o tipo `FILE *fp` e a guarda `if (fp == NULL)` com saída antecipada."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"cfg.txt\", \"r\");\n"
            "    if (fp == NULL) {\n"
            "        perror(\"cfg.txt\");\n"
            "        return 1;\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-4",
        "category": "arquivos",
        "subtopic": "3.4 Modos de abertura",
        "level": "Básico",
        "title": "Comportamento Destrutivo do Modo \"w\"",
        "stem": (
            "Um arquivo `clientes.txt` já existe no disco e possui 500 bytes de dados. Um programa executa "
            "`FILE *fp = fopen(\"clientes.txt\", \"w\");` e imediatamente chama `fclose(fp);`. O que acontece com o arquivo?"
        ),
        "options": [
            "Mantém os 500 bytes intactos, pois nada foi escrito com fprintf.",
            "Retorna NULL porque o arquivo já existe.",
            "Os 500 bytes são preservados e o cursor fica no final do arquivo.",
            "O arquivo é truncado para 0 bytes (seu conteúdo anterior é apagado).",
            "O arquivo é renomeado para clientes.txt.bak automaticamente."
        ],
        "correct": 3,
        "optionExplanations": [
            "Incorreta: o truncamento ocorre no próprio `fopen(..., \"w\")`, antes de qualquer escrita.",
            "Incorreta: o modo `\"w\"` sobrescreve arquivos existentes em vez de falhar.",
            "Incorreta: esse é o comportamento do modo `\"a\"` (append), não do `\"w\"`.",
            "Correta: abrir com `\"w\"` (ou `\"wb\"`/`\"w+\"`) zera imediatamente o arquivo existente.",
            "Incorreta: a biblioteca padrão C não cria backups automáticos."
        ],
        "gabaritoResumo": "O modo \"w\" trunca o arquivo existente para 0 bytes no momento da abertura.",
        "steps": [
            "Identifique que o modo `\"w\"` significa escrita destrutiva (cria se ausente, zera se existente).",
            "Conclua que mesmo fechando sem escrever, os 500 bytes anteriores foram perdidos."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    // Para preservar conteúdo e escrever ao final, use \"a\" (ou \"r+\" para atualizar):\n"
            "    FILE *fp = fopen(\"clientes.txt\", \"a\");\n"
            "    if (fp != NULL) fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-5",
        "category": "arquivos",
        "subtopic": "3.4 Modos de abertura",
        "level": "Intermediário",
        "title": "Escolha de Modo para Atualização Binária In-Loco",
        "stem": (
            "Você precisa abrir um arquivo binário `estoque.dat` que já existe, ler registros de produtos, alterar o preço "
            "de um deles com `fseek` e `fwrite`, sem apagar os demais registros. Qual modo de `fopen` deve ser usado?"
        ),
        "options": [
            "\"wb\"",
            "\"ab\"",
            "\"w+b\"",
            "\"r+b\"",
            "\"rb\""
        ],
        "correct": 3,
        "optionExplanations": [
            "Incorreta: `\"wb\"` apaga o arquivo existente e não permite leitura.",
            "Incorreta: `\"ab\"` não permite leitura e força toda escrita para o fim do arquivo, ignorando `fseek`.",
            "Incorreta: `\"w+b\"` permite leitura e escrita, mas apaga todo o conteúdo anterior na abertura!",
            "Correta: `\"r+b\"` abre binário existente para leitura e escrita sem truncar, permitindo atualizar posições específicas.",
            "Incorreta: `\"rb\"` é somente leitura."
        ],
        "gabaritoResumo": "Use \"r+b\" para ler e sobrescrever trechos de um arquivo binário existente sem zerá-lo.",
        "steps": [
            "Exclua modos com `'w'` porque truncam o arquivo existente.",
            "Exclua `\"ab\"` porque escritas em append sempre vão ao EOF; resta `\"r+b\"`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"estoque.dat\", \"r+b\");\n"
            "    if (!fp) return 1;\n"
            "    // fread + fseek + fwrite...\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-6",
        "category": "arquivos",
        "subtopic": "3.4 Modos de abertura",
        "level": "Intermediário",
        "title": "Restrição de Escrita no Modo \"a+\"",
        "stem": (
            "Um arquivo `log.txt` contém `\"ABC\"`. Ele é aberto com `\"a+\"`, executa-se `rewind(fp);` seguido de "
            "`fputc('X', fp);` e depois `fclose(fp);`. Qual será o conteúdo final de `log.txt`?"
        ),
        "options": [
            "\"XBC\"",
            "\"XABC\"",
            "\"ABCX\"",
            "\"X\"",
            "O programa falha com erro porque \"a+\" não permite rewind."
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: sobrescrever na posição 0 ocorreria em `\"r+\"`, não em `\"a+\"`.",
            "Incorreta: arquivos não inserem bytes no meio deslocando o restante automaticamente.",
            "Correta: no modo `\"a+\"`, `fseek`/`rewind` só afetam a leitura; toda operação de escrita é forçada ao fim do arquivo.",
            "Incorreta: `\"a+\"` não trunca o arquivo.",
            "Incorreta: `rewind` é válido em `\"a+\"` para reposicionar o cursor de leitura."
        ],
        "gabaritoResumo": "Em \"a\" e \"a+\", toda escrita vai obrigatoriamente para o fim do arquivo, mesmo após rewind/fseek.",
        "steps": [
            "Observe que `\"a+\"` é modo append + leitura.",
            "Pelo padrão C, toda escrita em stream aberto com `'a'` move o cursor de escrita para o EOF antes de gravar `'X'`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"log.txt\", \"a+\");\n"
            "    if (!fp) return 1;\n"
            "    rewind(fp);      // Afeta leitura\n"
            "    fputc('X', fp);  // Escreve sempre no fim: \"ABCX\"\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-7",
        "category": "arquivos",
        "subtopic": "3.5 Escrita em texto",
        "level": "Básico",
        "title": "Diferença entre puts e fputs quanto ao \\n",
        "stem": "Ao executar `fputs(\"ADS\", fp); fputs(\"2026\", fp);` em um arquivo de texto vazio, o que é gravado exatamente?",
        "options": [
            "\"ADS\\n2026\\n\"",
            "\"ADS\\02026\\0\"",
            "\"ADS2026\"",
            "\"ADS 2026\"",
            "\"ADS\\n2026\""
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: `puts` adiciona `'\\n'` automático em `stdout`, mas `fputs` não adiciona.",
            "Incorreta: `fputs` para no `'\\0'` e não grava o byte nulo no arquivo.",
            "Correta: `fputs` grava apenas os caracteres antes do `'\\0'` sem inserir espaço nem quebra de linha.",
            "Incorreta: nenhum espaço é adicionado automaticamente.",
            "Incorreta: não há `'\\n'` na primeira string."
        ],
        "gabaritoResumo": "fputs grava os caracteres da string sem incluir '\\0' e sem acrescentar '\\n' automático.",
        "steps": [
            "A primeira chamada grava `'A'`, `'D'`, `'S'`.",
            "A segunda chamada grava `'2'`, `'0'`, `'2'`, `'6'` logo em seguida: `\"ADS2026\"`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"s.txt\", \"w\");\n"
            "    if (fp) {\n"
            "        fputs(\"ADS\\n\", fp);\n"
            "        fputs(\"2026\\n\", fp);\n"
            "        fclose(fp);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-8",
        "category": "arquivos",
        "subtopic": "3.6 Leitura em texto",
        "level": "Intermediário",
        "title": "Tipo de Retorno de fgetc e Bug com char",
        "stem": "Qual o motivo técnico pelo qual o retorno de `fgetc(fp)` deve ser armazenado em `int`, e não em `char`?",
        "options": [
            "Porque fgetc lê 4 bytes de cada vez do arquivo.",
            "Porque char não suporta letras minúsculas em C.",
            "Para distinguir todos os 256 valores de byte possíveis (0..255) do valor sentinela negativo EOF (-1).",
            "Porque fgetc retorna o tamanho total do arquivo antes do caractere.",
            "Para que o compilador ative o modo binário automaticamente."
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: `fgetc` lê exatamente 1 byte por chamada.",
            "Incorreta: `char` armazena normalmente caracteres ASCII.",
            "Correta: se `char` for `unsigned`, nunca iguala `EOF` (-1); se for `signed`, o byte `0xFF` (-1) é confundido com `EOF`.",
            "Incorreta: `fgetc` retorna apenas o byte lido ou `EOF`.",
            "Incorreta: o modo depende de `fopen`, não do tipo da variável."
        ],
        "gabaritoResumo": "fgetc retorna int para comportar os 256 bytes (0..255 como unsigned char) mais EOF (-1).",
        "steps": [
            "Um `char` tem apenas 256 estados possíveis; não há espaço para 256 bytes + 1 marcador `EOF`.",
            "Armazenar em `int` garante que `0xFF` seja `255` e somente fim/erro seja `EOF` (`-1`)."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"in.bin\", \"rb\");\n"
            "    if (!fp) return 1;\n"
            "    int ch;\n"
            "    while ((ch = fgetc(fp)) != EOF) {\n"
            "        putchar(ch);\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-9",
        "category": "arquivos",
        "subtopic": "3.6 Leitura em texto",
        "level": "Intermediário",
        "title": "Comportamento de fgets com Buffer e Quebra de Linha",
        "stem": (
            "Considere `char s[6];` e um arquivo cuja primeira linha é `\"Casa\\n\"`. Após `fgets(s, sizeof(s), fp);`, "
            "quais caracteres compõem `s`?"
        ),
        "options": [
            "\"Casa\\0\"",
            "\"Casa\\n\\0\"",
            "\"Casa\\n\" sem terminador '\\0'",
            "\"Cas\\n\\0\"",
            "Estouro de buffer, pois \"Casa\\n\" tem 5 caracteres."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `fgets` mantém o `'\\n'` no buffer se houver espaço antes do limite `n - 1`.",
            "Correta: `sizeof(s)` é 6, logo `fgets` lê até 5 caracteres (`'C','a','s','a','\\n'`) e grava `'\\0'` no índice 5.",
            "Incorreta: `fgets` sempre garante terminação nula `'\\0'`.",
            "Incorreta: cabem os 5 caracteres inteiros mais o `'\\0'` em `s[6]`.",
            "Incorreta: 5 caracteres + `'\\0'` = 6 bytes, exatamente o tamanho de `s`."
        ],
        "gabaritoResumo": "fgets(s, 6, fp) lê até 5 caracteres incluindo '\\n' e acrescenta '\\0' ao final.",
        "steps": [
            "Calcule o máximo de caracteres lidos: `n - 1 = 6 - 1 = 5`.",
            "`\"Casa\\n\"` possui 5 caracteres, cabendo integralmente em `s[0..4]`, com `'\\0'` em `s[5]`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "int main(void) {\n"
            "    char s[6];\n"
            "    FILE *fp = fopen(\"casa.txt\", \"r\");\n"
            "    if (fp && fgets(s, sizeof(s), fp) != NULL) {\n"
            "        s[strcspn(s, \"\\r\\n\")] = '\\0';\n"
            "        puts(s);\n"
            "    }\n"
            "    if (fp) fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-10",
        "category": "arquivos",
        "subtopic": "3.7 Fim de arquivo",
        "level": "Intermediário",
        "title": "O Erro Clássico de while(!feof(fp))",
        "stem": (
            "Um arquivo `num.txt` contém apenas `\"10 20\"`. O código abaixo é executado:\n"
            "```c\nint x, s = 0;\nwhile (!feof(fp)) {\n    fscanf(fp, \"%d\", &x);\n    s += x;\n}\n```\n"
            "Qual será o valor final de `s` e por quê?"
        ),
        "code": "int x, s = 0;\nwhile (!feof(fp)) {\n    fscanf(fp, \"%d\", &x);\n    s += x;\n}",
        "options": [
            "30, pois o loop para exatamente após ler o 20.",
            "50, pois feof(fp) só ativa após fscanf falhar na tentativa seguinte, somando x (20) duas vezes.",
            "0, pois feof(fp) começa verdadeiro no início do arquivo.",
            "20, pois fscanf sobrescreve s na segunda iteração.",
            "Loop infinito, pois fscanf nunca atualiza a flag feof."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `feof(fp)` ainda vale 0 imediatamente após ler `20` se o cursor não tentou passar do fim.",
            "Correta: na 3ª volta `!feof(fp)` ainda é verdadeiro, `fscanf` falha sem alterar `x` (`20`), e `s += x` soma `20` de novo (`10+20+20=50`).",
            "Incorreta: `feof(fp)` inicia sempre em 0.",
            "Incorreta: `s` não é passado para `fscanf`.",
            "Incorreta: quando `fscanf` tenta ler após o fim, ele liga a flag EOF e o loop encerra na 4ª verificação."
        ],
        "gabaritoResumo": "feof() só retorna != 0 depois que uma leitura falha por EOF; testar !feof no while duplica o último valor.",
        "steps": [
            "Volta 1: lê `x=10`, `s=10`, `feof=0`.",
            "Volta 2: lê `x=20`, `s=30`, `feof=0` (ainda não houve tentativa frustrada!).",
            "Volta 3: entra no while, `fscanf` retorna `EOF`, `feof=1`, `x` continua `20` e `s` vira `50`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"num.txt\", \"r\");\n"
            "    if (!fp) return 1;\n"
            "    int x, s = 0;\n"
            "    while (fscanf(fp, \"%d\", &x) == 1) {\n"
            "        s += x;\n"
            "    }\n"
            "    printf(\"%d\\n\", s);\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-11",
        "category": "arquivos",
        "subtopic": "3.7 Fim de arquivo",
        "level": "Básico",
        "title": "Condição Correta de Laço para Leitura de Registros",
        "stem": "Qual estrutura de repetição lê corretamente todos os registros de `Pessoa` de um arquivo binário `fp` sem processar lixo no final?",
        "options": [
            "while (!feof(fp)) { fread(&p, sizeof(Pessoa), 1, fp); processa(p); }",
            "while (fread(&p, sizeof(Pessoa), 1, fp) == sizeof(Pessoa)) { processa(p); }",
            "while (fread(&p, sizeof(Pessoa), 1, fp) == 1) { processa(p); }",
            "while (ferror(fp) == 0) { fread(&p, sizeof(Pessoa), 1, fp); processa(p); }",
            "do { fread(&p, sizeof(Pessoa), 1, fp); processa(p); } while (!feof(fp));"
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: `while (!feof(fp))` processa o último registro duas vezes (ou lixo se o arquivo estiver vazio).",
            "Incorreta: `fread` retorna quantidade de itens (`1`), não `sizeof(Pessoa)` bytes!",
            "Correta: `fread(..., 1, fp)` retorna `1` somente quando conseguiu ler um registro completo.",
            "Incorreta: `ferror` permanece `0` quando atinge `EOF` normal, causando loop infinito.",
            "Incorreta: `do..while` executa `processa(p)` mesmo se o arquivo tiver 0 bytes."
        ],
        "gabaritoResumo": "Controle o laço testando diretamente se fread(..., 1, fp) == 1.",
        "steps": [
            "Lembre que `fread` recebe `qtd = 1` e retorna quantos blocos foram lidos.",
            "Quando retorna `0`, o laço termina antes de `processa(p)` ser chamado."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { int id; } Pessoa;\n"
            "void processa(Pessoa p) { printf(\"%d\\n\", p.id); }\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"p.dat\", \"rb\");\n"
            "    if (!fp) return 1;\n"
            "    Pessoa p;\n"
            "    while (fread(&p, sizeof(Pessoa), 1, fp) == 1) {\n"
            "        processa(p);\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-12",
        "category": "arquivos",
        "subtopic": "3.8 Arquivos binários",
        "level": "Básico",
        "title": "Retorno de fwrite e Ordem dos Argumentos",
        "stem": (
            "Considere `double v[10];` e a chamada `size_t n = fwrite(v, sizeof(double), 10, fp);`. "
            "Supondo que não houve erro de gravação e `sizeof(double) == 8`, qual valor `n` recebe?"
        ),
        "options": [
            "80",
            "8",
            "10",
            "1",
            "0"
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: 80 é o total de bytes gravados, mas `fwrite` retorna a contagem de itens (`qtd`), não de bytes.",
            "Incorreta: 8 é o tamanho de um único `double`.",
            "Correta: o 3º argumento especifica 10 elementos de tamanho 8 bytes; em sucesso, `fwrite` retorna 10.",
            "Incorreta: retornaria 1 apenas se `qtd` fosse 1 (ou se gravasse parcialmente 1 elemento).",
            "Incorreta: 0 indica falha na gravação de qualquer item."
        ],
        "gabaritoResumo": "fwrite e fread retornam o número de elementos (qtd) transferidos, não o total de bytes.",
        "steps": [
            "Identifique os argumentos: ponteiro `v`, tamanho unitário `8`, quantidade `10`.",
            "Em sucesso integral, o retorno é igual ao argumento quantidade (`10`)."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    double v[10] = {0};\n"
            "    FILE *fp = fopen(\"v.bin\", \"wb\");\n"
            "    if (!fp) return 1;\n"
            "    size_t n = fwrite(v, sizeof(double), 10, fp);\n"
            "    if (n != 10) fprintf(stderr, \"Erro de escrita\\n\");\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-13",
        "category": "arquivos",
        "subtopic": "3.8 Arquivos binários",
        "level": "Intermediário",
        "title": "Eficiência de Leitura/Escrita em Bloco vs Caractere a Caractere",
        "stem": "Por que copiar um arquivo grande (ex.: 50 MB) usando `fread`/`fwrite` com buffer de 4 KB é muito mais eficiente que `fgetc`/`fputc`?",
        "options": [
            "Porque fgetc e fputc não usam cache de disco no sistema operacional.",
            "Porque reduz drasticamente o número de chamadas de função e cópias byte a byte no laço, transferindo lotes inteiros de RAM.",
            "Porque fwrite compacta automaticamente os bytes em formato ZIP.",
            "Porque fread ignora verificações de fim de arquivo.",
            "Porque fputc só funciona em modo texto."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: streams padrão usam buffer da libc, mas ainda há 50 milhões de chamadas de função e verificações de lock/estado.",
            "Correta: `fread`/`fwrite` com buffer de 4 KB reduz o laço de 50 milhões de iterações para cerca de 12.800 chamadas usando cópia em bloco (`memcpy`).",
            "Incorreta: `fwrite` não realiza compressão.",
            "Incorreta: `fread` detecta EOF normalmente retornando menor que `qtd`.",
            "Incorreta: `fputc` também funciona em modo binário."
        ],
        "gabaritoResumo": "Transferir blocos via fread/fwrite reduz milhões de chamadas por byte para poucas transferências em lote.",
        "steps": [
            "Compare 50.000.000 de chamadas a `fgetc` + `fputc` com ~12.800 chamadas com buffer de 4096 bytes.",
            "Conclua que a redução de overhead de chamadas e cópia contígua torna o bloco muito mais rápido."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int copiar_bloco(FILE *in, FILE *out) {\n"
            "    unsigned char buf[4096];\n"
            "    size_t n;\n"
            "    while ((n = fread(buf, 1, sizeof(buf), in)) > 0) {\n"
            "        if (fwrite(buf, 1, n, out) != n) return 0;\n"
            "    }\n"
            "    return !ferror(in);\n"
            "}"
        )
    },
    {
        "id": "q-arq-14",
        "category": "arquivos",
        "subtopic": "3.9 Structs em arquivos",
        "level": "Avançado",
        "title": "Perigo de Ponteiros Dentro de Struct Gravada com fwrite",
        "stem": (
            "Considere `typedef struct { int id; char *nome; } Usuario;`. Um programa aloca `u.nome = malloc(30); strcpy(u.nome, \"Ana\");` "
            "e executa `fwrite(&u, sizeof(Usuario), 1, fp);`. Ao encerrar o programa e ler `u` em uma nova execução com `fread`, o que ocorre ao imprimir `u.nome`?"
        ),
        "code": "typedef struct { int id; char *nome; } Usuario;",
        "options": [
            "Imprime \"Ana\" normalmente, pois fwrite segue ponteiros automaticamente.",
            "Imprime \"Ana\" apenas se o arquivo foi aberto em modo \"wb+\".",
            "Comportamento indefinido / Segmentation Fault, pois foi gravado o endereço de memória antigo e não os caracteres de \"Ana\".",
            "O compilador recusa compilar fwrite quando há ponteiros na struct.",
            "O arquivo armazena a string logo após a struct automaticamente."
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: C não faz serialização profunda automática; `fwrite` copia apenas os `sizeof(Usuario)` bytes da struct.",
            "Incorreta: o modo não altera o que `fwrite` copia.",
            "Correta: o campo `char *nome` guarda apenas um endereço virtual da execução anterior, inválido na nova execução.",
            "Incorreta: `fwrite` recebe `const void *`, portanto compila sem erro.",
            "Incorreta: para gravar strings dinâmicas em binário, é preciso gravar explicitamente o tamanho e os caracteres (ou usar `char nome[30]`)."
        ],
        "gabaritoResumo": "Nunca grave structs com ponteiros via fwrite direto: apenas o endereço é gravado, não os dados apontados.",
        "steps": [
            "Verifique o layout de `Usuario`: 1 inteiro + 1 ponteiro (`sizeof(char *)`).",
            "`fwrite(&u, sizeof(Usuario), 1, fp)` grava o endereço do heap, que deixa de ser válido ao encerrar o processo."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct {\n"
            "    int id;\n"
            "    char nome[30]; // Vetor fixo embutido: seguro para fwrite/fread\n"
            "} Usuario;\n"
            "int main(void) {\n"
            "    Usuario u = {1, \"Ana\"};\n"
            "    FILE *fp = fopen(\"u.dat\", \"wb\");\n"
            "    if (fp) { fwrite(&u, sizeof(Usuario), 1, fp); fclose(fp); }\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-15",
        "category": "arquivos",
        "subtopic": "3.10 Posicionamento e fseek/ftell",
        "level": "Básico",
        "title": "Calculando o Tamanho de um Arquivo Binário",
        "stem": "Qual sequência padrão em C calcula o tamanho em bytes de um arquivo binário aberto em `fp` e depois retorna o cursor ao início?",
        "options": [
            "fseek(fp, 0L, SEEK_SET); long tam = ftell(fp); rewind(fp);",
            "fseek(fp, 0L, SEEK_END); long tam = ftell(fp); rewind(fp);",
            "rewind(fp); long tam = fseek(fp, 0L, SEEK_END);",
            "long tam = ftell(fp); fseek(fp, 0L, SEEK_CUR);",
            "fseek(fp, -1L, SEEK_SET); long tam = ftell(fp);"
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `SEEK_SET` com offset `0` coloca o cursor no início, então `ftell` retorna `0`.",
            "Correta: `fseek(fp, 0L, SEEK_END)` vai ao último byte; `ftell(fp)` lê o deslocamento total; `rewind(fp)` volta ao byte `0`.",
            "Incorreta: `fseek` retorna `0` (sucesso) ou não-zero (erro), não o tamanho do arquivo!",
            "Incorreta: `ftell` no início vale `0`, e `SEEK_CUR` com `0` não move o cursor.",
            "Incorreta: deslocamento `-1` antes do início (`SEEK_SET`) é inválido."
        ],
        "gabaritoResumo": "fseek(fp, 0L, SEEK_END) + ftell(fp) obtém o total de bytes; rewind(fp) volta ao início.",
        "steps": [
            "Posicione o cursor no final com `SEEK_END` e offset `0L`.",
            "Consulte o offset com `ftell(fp)` e restaure o início com `rewind(fp)`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "long tamanho_arquivo(FILE *fp) {\n"
            "    fseek(fp, 0L, SEEK_END);\n"
            "    long tam = ftell(fp);\n"
            "    rewind(fp);\n"
            "    return tam;\n"
            "}"
        )
    },
    {
        "id": "q-arq-16",
        "category": "arquivos",
        "subtopic": "3.10 Posicionamento e fseek/ftell",
        "level": "Intermediário",
        "title": "Acesso Direto ao k-ésimo Registro em Binário",
        "stem": (
            "Em um arquivo binário `alunos.dat` contendo registros `Aluno` (indexados a partir de 0), "
            "como posicionar diretamente no 5º registro (índice 4) a partir do início do arquivo?"
        ),
        "options": [
            "fseek(fp, 5L * sizeof(Aluno), SEEK_SET);",
            "fseek(fp, 4L * sizeof(Aluno), SEEK_SET);",
            "fseek(fp, 4L, SEEK_SET);",
            "fseek(fp, 4L * sizeof(Aluno), SEEK_END);",
            "ftell(fp, 4L * sizeof(Aluno));"
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `5 * sizeof(Aluno)` aponta para o 6º registro (índice 5).",
            "Correta: como o índice 0 está no offset 0, o 5º registro (índice 4) inicia exatamente em `4L * sizeof(Aluno)` a partir de `SEEK_SET`.",
            "Incorreta: pular apenas 4 bytes ignora o tamanho da struct `Aluno`.",
            "Incorreta: deslocamento positivo após `SEEK_END` aponta além do fim do arquivo.",
            "Incorreta: `ftell` recebe apenas `FILE *` e não move o cursor."
        ],
        "gabaritoResumo": "Para acessar o registro 0-based de índice idx: fseek(fp, (long)idx * sizeof(Tipo), SEEK_SET).",
        "steps": [
            "Converta a posição ordinal '5º registro' para índice 0-based: `idx = 4`.",
            "Multiplique pelo tamanho do registro `sizeof(Aluno)` usando origem `SEEK_SET`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { int id; double nota; } Aluno;\n"
            "int ler_indice(FILE *fp, long idx, Aluno *out) {\n"
            "    if (fseek(fp, idx * (long)sizeof(Aluno), SEEK_SET) != 0) return 0;\n"
            "    return fread(out, sizeof(Aluno), 1, fp) == 1;\n"
            "}"
        )
    },
    {
        "id": "q-arq-17",
        "category": "arquivos",
        "subtopic": "3.11 Operações sobre arquivos",
        "level": "Básico",
        "title": "Uso de remove, rename e tmpfile",
        "stem": "Qual afirmação está correta sobre as funções `remove`, `rename` e `tmpfile` de `<stdio.h>`?",
        "options": [
            "remove(\"a.txt\") apaga apenas a última linha do arquivo.",
            "rename retorna 1 quando tem sucesso e 0 quando falha.",
            "tmpfile() abre um arquivo binário temporário (\"wb+\") que é apagado automaticamente ao ser fechado ou ao fim do programa.",
            "remove e rename exigem que o arquivo esteja aberto via fopen no momento da chamada.",
            "tmpfile() retorna o nome do arquivo como uma string char *."
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: `remove` exclui o arquivo inteiro do sistema de arquivos.",
            "Incorreta: tanto `remove` quanto `rename` retornam `0` em caso de sucesso e valor diferente de zero em erro.",
            "Correta: `tmpfile()` cria um stream temporário em `" + "\"wb+\"" + "` com remoção automática garantida pela biblioteca padrão.",
            "Incorreta: deve-se fechar o stream com `fclose` antes de remover ou renomear o arquivo.",
            "Incorreta: `tmpfile()` retorna `FILE *` (ponteiro de stream), não `char *`."
        ],
        "gabaritoResumo": "remove e rename retornam 0 no sucesso (com arquivos fechados); tmpfile() retorna FILE * em wb+ auto-removível.",
        "steps": [
            "Confirme que `remove` e `rename` seguem a convenção `0 == sucesso`.",
            "Lembre que `tmpfile()` retorna `FILE *` aberto em `" + "\"wb+\"" + "` e removido automaticamente ao fechar."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *tmp = tmpfile();\n"
            "    if (!tmp) return 1;\n"
            "    fputs(\"dados temporarios\", tmp);\n"
            "    rewind(tmp);\n"
            "    fclose(tmp); // Arquivo é removido automaticamente\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-18",
        "category": "arquivos",
        "subtopic": "3.12 Tratamento de erros",
        "level": "Intermediário",
        "title": "Diferenciando Fim de Arquivo de Erro Real com ferror e perror",
        "stem": (
            "Após o término de um laço `while ((c = fgetc(fp)) != EOF)`, qual combinação permite saber se a parada foi "
            "causada por falha física de leitura e imprimir o motivo do sistema?"
        ),
        "options": [
            "if (feof(fp)) perror(\"Erro\");",
            "if (ferror(fp)) perror(\"Erro de leitura\");",
            "if (clearerr(fp)) perror(\"Erro\");",
            "if (errno == 0) perror(\"Erro\");",
            "if (fclose(fp) == 0) perror(\"Erro\");"
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `feof(fp)` indica fim normal dos dados, não erro.",
            "Correta: `fgetc` retorna `EOF` tanto no fim normal quanto em erro; `ferror(fp)` confirma se houve erro real e `perror` exibe o diagnóstico.",
            "Incorreta: `clearerr` retorna `void` e apenas limpa as flags.",
            "Incorreta: `errno == 0` indica ausência de erro.",
            "Incorreta: `fclose(fp) == 0` indica fechamento bem-sucedido."
        ],
        "gabaritoResumo": "Quando fgetc/fread para prematuramente, ferror(fp) verifica erro de E/S e perror() imprime errno.",
        "steps": [
            "Lembre que `EOF` pode sinalizar fim do arquivo ou falha de leitura.",
            "Use `ferror(fp)` para detectar falha de I/O e `perror` para exibir a mensagem do `errno`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"dados.txt\", \"r\");\n"
            "    if (!fp) { perror(\"fopen\"); return 1; }\n"
            "    int c;\n"
            "    while ((c = fgetc(fp)) != EOF) { }\n"
            "    if (ferror(fp)) {\n"
            "        perror(\"Erro de leitura\");\n"
            "        clearerr(fp);\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-19",
        "category": "arquivos",
        "subtopic": "3.12 Tratamento de erros",
        "level": "Avançado",
        "title": "Preservação de errno e Função de clearerr",
        "stem": (
            "Sobre `errno` (`<errno.h>`) e `clearerr(FILE *fp)`, assinale a alternativa verdadeira:"
        ),
        "options": [
            "clearerr(fp) também zera a variável global errno.",
            "clearerr(fp) apaga os últimos bytes gravados no arquivo.",
            "clearerr(fp) limpa as flags de EOF e de erro internas do stream fp, sem apagar o conteúdo do arquivo.",
            "errno deve ser lida somente depois de chamar printf(\"Falha\\n\"), para dar tempo de atualizar.",
            "perror(\"msg\") escreve a mensagem no fluxo stdout."
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: `clearerr` atua nas flags do objeto `FILE`, não em `errno`.",
            "Incorreta: `clearerr` não altera o conteúdo do arquivo em disco.",
            "Correta: `clearerr(fp)` reinicia apenas os indicadores de fim de arquivo (`feof`) e erro (`ferror`) daquele stream.",
            "Incorreta: `printf` pode alterar `errno`! Deve-se inspecionar `errno` ou chamar `perror` imediatamente após a falha.",
            "Incorreta: `perror` escreve sempre em `stderr`."
        ],
        "gabaritoResumo": "clearerr(fp) reseta as flags feof e ferror do stream; errno deve ser lido antes de qualquer outra chamada.",
        "steps": [
            "Separe o escopo de `errno` (código global da libc) das flags do `FILE *` (`feof`/`ferror`).",
            "Confirme que `clearerr(fp)` limpa exatamente as flags do stream."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "#include <errno.h>\n"
            "#include <string.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"nao_existe.txt\", \"r\");\n"
            "    if (!fp) {\n"
            "        int err = errno; // Captura imediata antes de outras chamadas\n"
            "        fprintf(stderr, \"Erro %d: %s\\n\", err, strerror(err));\n"
            "        return 1;\n"
            "    }\n"
            "    clearerr(fp);\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-20",
        "category": "arquivos",
        "subtopic": "3.13 Buffer de E/S",
        "level": "Intermediário",
        "title": "Efeito do Buffer, fflush e Esquecimento de fclose",
        "stem": (
            "Um programa abre `saida.txt` com `\"w\"`, executa `fprintf(fp, \"Linha 1\\n\");` e encerra abruptamente com "
            "`_Exit(1)` (ou queda de energia) antes de chamar `fclose(fp)` ou `fflush(fp)`. O que tende a ocorrer?"
        ),
        "options": [
            "O arquivo garante 100% da gravação porque fprintf grava direto nos setores do disco.",
            "O arquivo pode ficar vazio (0 bytes) ou incompleto porque os dados ainda estavam retidos no buffer em RAM.",
            "O compilador insere fclose automático antes de _Exit(1).",
            "A próxima execução do sistema recupera o buffer da stack automaticamente.",
            "O arquivo é deletado automaticamente pelo sistema operacional."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: arquivos em disco usam buffer completo (`_IOFBF`) por padrão; `fprintf` escreve no buffer em RAM.",
            "Correta: sem `fflush(fp)` ou `fclose(fp)`, o buffer em espaço de usuário nunca é enviado ao sistema operacional em `_Exit`/`abort`.",
            "Incorreta: `_Exit` e `abort` encerram o processo sem descarregar buffers de `stdio`.",
            "Incorreta: a RAM do processo é destruída ao término.",
            "Incorreta: o arquivo permanece criado (frequentemente com 0 bytes)."
        ],
        "gabaritoResumo": "Sem fclose ou fflush, dados no buffer em RAM podem não ser persistidos em caso de término anormal.",
        "steps": [
            "Lembre que streams de arquivo usam buffer completo (`_IOFBF`) em RAM.",
            "Conclua que `fflush(fp)` força a descarga imediata e `fclose(fp)` realiza o flush final."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"saida.txt\", \"w\");\n"
            "    if (!fp) return 1;\n"
            "    setvbuf(fp, NULL, _IOLBF, 0);\n"
            "    fprintf(fp, \"Linha 1\\n\");\n"
            "    fflush(fp);\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-21",
        "category": "arquivos",
        "subtopic": "3.13 Buffer de E/S",
        "level": "Avançado",
        "title": "Uso Correto de setvbuf e Portabilidade de fflush",
        "stem": "Qual afirmação descreve corretamente `setvbuf` e `fflush` segundo o padrão ISO C?",
        "options": [
            "fflush(stdin) é o método padrão garantido pelo ISO C para descartar o '\\n' do teclado.",
            "setvbuf deve ser chamada depois de pelo menos um fread ou fprintf no stream.",
            "setvbuf permite escolher _IOFBF, _IOLBF ou _IONBF e deve ser chamada logo após fopen, antes de qualquer I/O.",
            "fflush(fp) fecha o arquivo após limpar o buffer.",
            "stderr é sempre totalmente bufferizado (_IOFBF) por padrão."
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: `fflush(stdin)` tem comportamento indefinido no padrão ISO C (funciona apenas como extensão em alguns compiladores).",
            "Incorreta: `setvbuf` deve ser chamada antes de qualquer outra operação de leitura ou escrita no stream.",
            "Correta: `setvbuf(fp, buf, modo, tam)` configura `_IOFBF`, `_IOLBF` ou `_IONBF` imediatamente após `fopen`.",
            "Incorreta: `fflush` apenas descarrega o buffer mantendo o arquivo aberto.",
            "Incorreta: `stderr` nunca é totalmente bufferizado por padrão (geralmente `_IONBF`), para que erros apareçam de imediato."
        ],
        "gabaritoResumo": "setvbuf configura _IOFBF/_IOLBF/_IONBF antes do primeiro I/O; fflush(stdin) é indefinido pelo padrão C.",
        "steps": [
            "Descarte `fflush(stdin)` (indefinido) e `setvbuf` tardio (inválido).",
            "Confirme a regra de chamar `setvbuf` logo após `fopen`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"trace.log\", \"w\");\n"
            "    if (!fp) return 1;\n"
            "    setvbuf(fp, NULL, _IONBF, 0); // Sem buffer para log crítico\n"
            "    fprintf(fp, \"Evento critico\\n\");\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-22",
        "category": "arquivos",
        "subtopic": "3.14 Fluxos padrão",
        "level": "Básico",
        "title": "Separação entre stdout e stderr no Redirecionamento",
        "stem": (
            "Um programa imprime resultados com `printf(\"OK;10\\n\");` e erros com `fprintf(stderr, \"ERRO\\n\");`. "
            "Ao executá-lo no terminal com `./app > dados.csv`, o que acontece?"
        ),
        "options": [
            "Tanto \"OK;10\" quanto \"ERRO\" são gravados dentro de dados.csv.",
            "\"OK;10\" vai para dados.csv e \"ERRO\" continua aparecendo no terminal (pois stderr não foi redirecionado).",
            "\"ERRO\" vai para dados.csv e \"OK;10\" aparece no terminal.",
            "O programa precisa chamar fopen(\"stdout\", \"w\") antes.",
            "Redirecionar stdout com '>' fecha automaticamente stderr."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `>` redireciona apenas o descritor 1 (`stdout`), mantendo o descritor 2 (`stderr`) no terminal.",
            "Correta: `stdout` vai para `dados.csv`, enquanto `stderr` permanece visível na tela (ou pode ser redirecionado separadamente com `2>`).",
            "Incorreta: o direcionamento é o oposto.",
            "Incorreta: `stdin`, `stdout` e `stderr` já vêm abertos automaticamente.",
            "Incorreta: `stderr` permanece aberto e independente."
        ],
        "gabaritoResumo": "'>' redireciona apenas stdout (fd 1); mensagens em stderr (fd 2) continuam no terminal ou usam '2>'.",
        "steps": [
            "Associe `printf` a `stdout` (fd 1) e `fprintf(stderr, ...)` a `stderr` (fd 2).",
            "Observe que `>` atua apenas em fd 1, preservando o arquivo CSV livre de mensagens de erro."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    fprintf(stdout, \"OK;10\\n\");\n"
            "    fprintf(stderr, \"ERRO: aviso de diagnostico\\n\");\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-23",
        "category": "arquivos",
        "subtopic": "3.15 Argumentos de linha de comando",
        "level": "Básico",
        "title": "Índices de argv[] e Verificação de argc",
        "stem": (
            "Ao executar no terminal o comando `./analisar notas.csv relatorio.txt`, quais são os valores de `argc`, "
            "`argv[0]` e `argv[2]` dentro de `int main(int argc, char *argv[])`?"
        ),
        "options": [
            "argc = 2, argv[0] = \"notas.csv\", argv[2] = NULL",
            "argc = 3, argv[0] = \"./analisar\", argv[2] = \"relatorio.txt\"",
            "argc = 3, argv[0] = \"notas.csv\", argv[2] = \"relatorio.txt\"",
            "argc = 2, argv[0] = \"./analisar\", argv[2] = \"relatorio.txt\"",
            "argc = 4, argv[0] = \"./analisar\", argv[2] = \"notas.csv\""
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `argv[0]` sempre guarda o nome/invocação do executável, portanto `argc` inclui o próprio programa.",
            "Correta: há 3 tokens na linha de comando (`./analisar`, `notas.csv`, `relatorio.txt`), logo `argc == 3`, `argv[0]` é `\"./analisar\"` e `argv[2]` é `\"relatorio.txt\"`.",
            "Incorreta: `argv[0]` não é o primeiro parâmetro de arquivo.",
            "Incorreta: se `argc` fosse 2, `argv[2]` seria `NULL`.",
            "Incorreta: `argc` conta 3 strings, não 4 (`argv[3]` é `NULL`)."
        ],
        "gabaritoResumo": "argv[0] é o programa e argv[1..argc-1] são os parâmetros; para 2 arquivos, argc == 3.",
        "steps": [
            "Conte todos os tokens separados por espaço incluindo o comando `./analisar`: total 3.",
            "Mapeie `argv[0] = \"./analisar\"`, `argv[1] = \"notas.csv\"`, `argv[2] = \"relatorio.txt\"`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(int argc, char *argv[]) {\n"
            "    if (argc != 3) {\n"
            "        fprintf(stderr, \"Uso: %s <csv> <relatorio>\\n\", argv[0]);\n"
            "        return 1;\n"
            "    }\n"
            "    FILE *in = fopen(argv[1], \"r\");\n"
            "    FILE *out = fopen(argv[2], \"w\");\n"
            "    if (in) fclose(in);\n"
            "    if (out) fclose(out);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-24",
        "category": "arquivos",
        "subtopic": "3.16 Algoritmos clássicos e CSV",
        "level": "Intermediário",
        "title": "Contagem de Palavras em Arquivo Texto com Máquina de Estados",
        "stem": (
            "Para contar corretamente o número de palavras em um arquivo texto que pode conter múltiplos espaços seguidos, "
            "tabulações e linhas em branco usando `fgetc`, qual lógica é correta?"
        ),
        "options": [
            "Contar apenas quantas vezes aparece o caractere ' ' e somar 1.",
            "Contar quantas vezes aparece '\\n' no arquivo.",
            "Manter uma flag em_palavra: ao ler caractere que não é espaço (!isspace) estando fora de palavra, incrementa palavras e marca em_palavra = 1.",
            "Usar strlen em cada fgetc.",
            "Dividir o tamanho retornado por ftell por 5."
        ],
        "correct": 2,
        "optionExplanations": [
            "Incorreta: dois espaços seguidos, `\\t` ou `\\n` quebrariam a contagem por espaço simples.",
            "Incorreta: conta linhas, não palavras.",
            "Correta: uma palavra começa exatamente na transição de separador (`isspace((unsigned char)c)`) para caractere não-separador.",
            "Incorreta: `fgetc` retorna `int`, não string.",
            "Incorreta: palavras não têm tamanho fixo de 5 bytes."
        ],
        "gabaritoResumo": "A contagem estilo wc detecta a transição de fora para dentro de palavra usando isspace((unsigned char)c).",
        "steps": [
            "Considere que espaços, `'\\t'` e `'\\n'` são detectados por `isspace((unsigned char)c)`.",
            "Incremente o contador somente quando `em_palavra == 0` e surge um caractere que não é espaço."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "#include <ctype.h>\n"
            "int contar_palavras(FILE *fp) {\n"
            "    int c, em_palavra = 0, palavras = 0;\n"
            "    while ((c = fgetc(fp)) != EOF) {\n"
            "        if (isspace((unsigned char)c)) {\n"
            "            em_palavra = 0;\n"
            "        } else if (!em_palavra) {\n"
            "            em_palavra = 1;\n"
            "            palavras++;\n"
            "        }\n"
            "    }\n"
            "    return palavras;\n"
            "}"
        )
    },
    {
        "id": "q-arq-25",
        "category": "arquivos",
        "subtopic": "3.16 Algoritmos clássicos e CSV",
        "level": "Intermediário",
        "title": "Particularidades de strtok no Parsing de CSV",
        "stem": "Ao fazer parsing da linha CSV `\"10;;Teclado\\n\"` com `strtok(linha, \";\")`, o que ocorre na segunda chamada `strtok(NULL, \";\")`?",
        "options": [
            "Retorna uma string vazia \"\" representando o segundo campo.",
            "Pula os dois ';' consecutivos e retorna diretamente \"Teclado\\n\", desalinhando as colunas.",
            "Retorna NULL imediatamente no primeiro ';'.",
            "Converte \"10\" automaticamente para inteiro.",
            "Aloca uma nova string no heap para cada campo."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `strtok` trata sequências de delimitadores como um único separador, não retornando tokens vazios.",
            "Correta: `strtok` ignora delimitadores repetidos (`\";;\"`), deslocando a 3ª coluna (`Teclado`) para a 2ª posição.",
            "Incorreta: retorna `\"10\"` na 1ª chamada e só retorna `NULL` quando não há mais tokens.",
            "Incorreta: `strtok` apenas retorna `char *`.",
            "Incorreta: `strtok` modifica a string original substituindo delimitadores por `'\\0'`."
        ],
        "gabaritoResumo": "strtok modifica a string original e ignora delimitadores consecutivos; para campos vazios use sscanf/varredura manual.",
        "steps": [
            "Identifique que `strtok` consome múltiplos delimitadores adjacentes de uma só vez.",
            "Conclua que `\";;\"` faz o campo vazio sumir e desalinhar as colunas seguintes."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "int main(void) {\n"
            "    char linha[] = \"10;Maria;9.5\";\n"
            "    int id = 0; char nome[32] = \"\"; double nota = 0.0;\n"
            "    if (sscanf(linha, \"%d;%31[^;];%lf\", &id, nome, &nota) == 3) {\n"
            "        printf(\"%d %s %.1f\\n\", id, nome, nota);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-26",
        "category": "arquivos",
        "subtopic": "3.16 Algoritmos clássicos e CSV",
        "level": "Básico",
        "title": "Conversão para Maiúsculas e Concatenação de Arquivos",
        "stem": (
            "Um algoritmo deve ler todo o texto de `origem.txt`, converter as letras minúsculas para maiúsculas e "
            "acrescentar o resultado ao final de `destino.txt` sem apagar o que `destino.txt` já contém. Quais modos de abertura "
            "e função de conversão devem ser usados?"
        ),
        "options": [
            "origem em \"r\", destino em \"w\", conversão com toupper((unsigned char)c).",
            "origem em \"r\", destino em \"a\", conversão com toupper((unsigned char)c).",
            "origem em \"w\", destino em \"a\", conversão com tolower(c).",
            "origem em \"rb\", destino em \"r+\", conversão com atoi(c).",
            "origem em \"a\", destino em \"r\", conversão com toupper((unsigned char)c)."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: abrir `destino.txt` em `\"w\"` apagaria o conteúdo prévio de destino.",
            "Correta: `\"r\"` lê origem, `\"a\"` preserva destino acrescentando ao fim, e `toupper((unsigned char)c)` evita comportamento indefinido para bytes acentuados.",
            "Incorreta: `\"w\"` apaga `origem.txt` e `tolower` converte para minúsculas.",
            "Incorreta: `\"r+\"` sobrescreve do início em vez de concatenar ao final, e `atoi` espera string.",
            "Incorreta: os modos estão invertidos entre origem e destino."
        ],
        "gabaritoResumo": "Leia origem com \"r\", acrescente em destino com \"a\" e converta com toupper((unsigned char)c).",
        "steps": [
            "Escolha `\"r\"` para leitura da origem e `\"a\"` para concatenar ao final do destino.",
            "Passe `(unsigned char)c` para `toupper` de `<ctype.h>` para segurança com acentos."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "#include <ctype.h>\n"
            "int main(void) {\n"
            "    FILE *in = fopen(\"origem.txt\", \"r\");\n"
            "    FILE *out = fopen(\"destino.txt\", \"a\");\n"
            "    if (!in || !out) { if (in) fclose(in); if (out) fclose(out); return 1; }\n"
            "    int c;\n"
            "    while ((c = fgetc(in)) != EOF) {\n"
            "        fputc(toupper((unsigned char)c), out);\n"
            "    }\n"
            "    fclose(in); fclose(out);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-27",
        "category": "arquivos",
        "subtopic": "3.17 CRUD e erros comuns",
        "level": "Intermediário",
        "title": "Exclusão Lógica vs. Exclusão Física em Arquivos",
        "stem": "Qual é a principal diferença operacional entre exclusão lógica e exclusão física em um CRUD baseado em arquivos binários?",
        "options": [
            "A exclusão lógica apaga o arquivo inteiro com remove(), enquanto a física altera apenas uma flag.",
            "A exclusão lógica marca o registro como inativo (ex.: ativo = 0) in-loco em O(1), enquanto a física copia apenas registros ativos para um arquivo temporário e substitui o original.",
            "A exclusão física não requer fechar o arquivo antes de renomear.",
            "A exclusão lógica reduz imediatamente o tamanho em bytes do arquivo no disco.",
            "A exclusão física só é possível em arquivos de texto."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: as definições estão invertidas e `remove()` apaga o arquivo todo.",
            "Correta: exclusão lógica é rápida (altera um campo e sobrescreve o registro), deixando espaço morto; exclusão física reconstrói o arquivo sem os removidos usando temporário + `remove` + `rename`.",
            "Incorreta: é obrigatório chamar `fclose` antes de `remove`/`rename`.",
            "Incorreta: o arquivo mantém o mesmo tamanho na exclusão lógica.",
            "Incorreta: exclusão física funciona perfeitamente em arquivos binários e texto."
        ],
        "gabaritoResumo": "Lógica marca campo ativo=0 in-loco; física filtra para temporário, fecha ambos, e faz remove + rename.",
        "steps": [
            "Associe lógica à marcação de flag (`ativo = 0`) sem diminuir o tamanho do arquivo.",
            "Associe física à cópia seletiva para arquivo temporário com substituição via `remove`/`rename`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { int id; int ativo; } Reg;\n"
            "int compactar_fisico(const char *arq) {\n"
            "    FILE *in = fopen(arq, \"rb\");\n"
            "    FILE *tmp = fopen(\"tmp.dat\", \"wb\");\n"
            "    if (!in || !tmp) { if (in) fclose(in); if (tmp) fclose(tmp); return 0; }\n"
            "    Reg r;\n"
            "    while (fread(&r, sizeof(Reg), 1, in) == 1) {\n"
            "        if (r.ativo) fwrite(&r, sizeof(Reg), 1, tmp);\n"
            "    }\n"
            "    fclose(in); fclose(tmp);\n"
            "    return remove(arq) == 0 && rename(\"tmp.dat\", arq) == 0;\n"
            "}"
        )
    },
    {
        "id": "q-arq-28",
        "category": "arquivos",
        "subtopic": "3.17 CRUD e erros comuns",
        "level": "Avançado",
        "title": "Alternância entre Leitura e Escrita em Modo '+'",
        "stem": (
            "Um estudante abriu um arquivo em `\"r+b\"`, leu um registro com `fread(&r, sizeof(r), 1, fp)`, alterou `r.qtd` "
            "e chamou `fwrite(&r, sizeof(r), 1, fp)` diretamente sem chamar `fseek` nem `fflush`. Quais dois problemas ocorrem?"
        ),
        "options": [
            "Nenhum problema: fwrite sobrescreve o mesmo registro automaticamente.",
            "1) Grava por cima do PRÓXIMO registro (cursor já avançou); 2) Viola a regra do padrão C que exige fseek/rewind entre leitura e escrita em modo '+'.",
            "fwrite retorna EOF porque \"r+b\" é somente leitura.",
            "O arquivo é truncado para zero bytes.",
            "O compilador converte o stream para modo texto."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: `fread` avança o cursor para o registro seguinte!",
            "Correta: sem `fseek(fp, -(long)sizeof(r), SEEK_CUR)` (ou `SEEK_SET` no índice), grava-se no registro errado e ocorre comportamento indefinido de buffer no modo `+`.",
            "Incorreta: `\"r+b\"` permite leitura e escrita.",
            "Incorreta: `\"r+b\"` não trunca.",
            "Incorreta: o modo binário permanece."
        ],
        "gabaritoResumo": "Em modos '+', toda transição leitura<->escrita exige fseek/rewind (ou fflush após escrita) e reposicionamento.",
        "steps": [
            "Observe que `fread` deslocou o ponteiro do arquivo em `+sizeof(r)` bytes.",
            "Lembre a regra ISO C: leitura seguida de escrita em stream de atualização exige chamada de posicionamento (`fseek`/`rewind`)."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { int id; int qtd; } Prod;\n"
            "void alterar(FILE *fp, Prod p) {\n"
            "    fseek(fp, -(long)sizeof(Prod), SEEK_CUR);\n"
            "    fwrite(&p, sizeof(Prod), 1, fp);\n"
            "    fflush(fp);\n"
            "}"
        )
    },
    {
        "id": "q-arq-29",
        "category": "arquivos",
        "subtopic": "3.17 CRUD e erros comuns",
        "level": "Avançado",
        "title": "Portabilidade Binária: Padding e Endianness",
        "stem": (
            "Um arquivo binário gravado com `fwrite(&reg, sizeof(Registro), 1, fp)` em um PC x86-64 (little-endian) "
            "pode falhar ao ser lido diretamente com `fread` em outro computador ou compilador devido a:"
        ),
        "options": [
            "Apenas diferenças de acentuação UTF-8.",
            "Padding (alinhamento de bytes na struct), tamanho distinto de tipos (ex.: long) e endianness (ordem dos bytes).",
            "Limitação de fwrite a no máximo 100 registros.",
            "Conversão automática de int para string pelo fread.",
            "Diferença no caractere delimitador ';' do arquivo binário."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: arquivos binários brutos não dependem de UTF-8.",
            "Correta: compiladores inserem bytes de padding conforme a ABI, `long` varia entre 4 e 8 bytes, e arquiteturas big-endian invertem a ordem dos bytes.",
            "Incorreta: `fwrite` não tem limite de 100 registros.",
            "Incorreta: `fread` não converte tipos.",
            "Incorreta: arquivos binários de struct não usam delimitadores `';'`."
        ],
        "gabaritoResumo": "fwrite(&struct) não é portável entre arquiteturas/compiladores por causa de padding, sizeof e endianness.",
        "steps": [
            "Identifique os fatores físicos da representação em RAM: alinhamento (padding), largura de palavra e endianness.",
            "Para troca entre máquinas heterogêneas, usa-se formato texto (CSV/JSON) ou serialização binária canônica campo a campo."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "#include <stdint.h>\n"
            "// Para portabilidade binária, serialize campo a campo com tipos de largura fixa (uint32_t)\n"
            "void gravar_u32_le(FILE *fp, uint32_t v) {\n"
            "    unsigned char b[4] = {\n"
            "        (unsigned char)(v & 0xFF), (unsigned char)((v >> 8) & 0xFF),\n"
            "        (unsigned char)((v >> 16) & 0xFF), (unsigned char)((v >> 24) & 0xFF)\n"
            "    };\n"
            "    fwrite(b, 1, 4, fp);\n"
            "}"
        )
    },
    {
        "id": "q-arq-30",
        "category": "arquivos",
        "subtopic": "3.17 CRUD e erros comuns",
        "level": "Intermediário",
        "title": "Busca Binária Direta em Arquivo Ordenado",
        "stem": (
            "Um arquivo binário `indices.dat` possui 1.000.000 de registros `Item` ordenados crescentemente pelo campo `id`. "
            "Qual técnica permite localizar um `id` sem carregar o arquivo inteiro na RAM e em no máximo ~20 leituras?"
        ),
        "options": [
            "Busca sequencial com fgets e strtok.",
            "Busca binária em disco calculando o total de registros (fseek+ftell) e saltando para o meio com fseek(fp, mid * sizeof(Item), SEEK_SET).",
            "Reabrir o arquivo em modo \"w+\" a cada tentativa.",
            "Usar fgetc contando quantas vírgulas existem até o id.",
            "Chamar tmpfile() para duplicar o arquivo antes de cada busca."
        ],
        "correct": 1,
        "optionExplanations": [
            "Incorreta: leitura sequencial é O(n) (até 1 milhão de registros) e `fgets`/`strtok` é para texto.",
            "Correta: como todos os registros têm tamanho fixo `sizeof(Item)` e estão ordenados, podemos calcular `mid = (ini + fim) / 2` e ler apenas `~log2(10^6) ≈ 20` registros com `fseek` + `fread`.",
            "Incorreta: `\"w+\"` apagaria o arquivo todo.",
            "Incorreta: arquivos binários de tamanho fixo não usam vírgulas.",
            "Incorreta: duplicar o arquivo seria O(n) e desnecessário."
        ],
        "gabaritoResumo": "Arquivos binários de tamanho fixo ordenados suportam busca binária direta no disco via fseek + fread em O(log n).",
        "steps": [
            "Determine o número de registros: `n = tamanho_bytes / sizeof(Item)`.",
            "Aplique busca binária com `ini = 0`, `fim = n - 1`, lendo o elemento `mid` via `fseek(fp, mid * sizeof(Item), SEEK_SET)`."
        ],
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { int id; double val; } Item;\n"
            "int busca_bin_disco(FILE *fp, int alvo, Item *out) {\n"
            "    fseek(fp, 0L, SEEK_END);\n"
            "    long ini = 0, fim = (ftell(fp) / (long)sizeof(Item)) - 1;\n"
            "    while (ini <= fim) {\n"
            "        long mid = ini + (fim - ini) / 2;\n"
            "        fseek(fp, mid * (long)sizeof(Item), SEEK_SET);\n"
            "        if (fread(out, sizeof(Item), 1, fp) != 1) return 0;\n"
            "        if (out->id == alvo) return 1;\n"
            "        if (out->id < alvo) ini = mid + 1;\n"
            "        else fim = mid - 1;\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
    }
]

CE_ARQUIVOS = [
    {
        "id": "ce-arq-1",
        "category": "arquivos",
        "subtopic": "3.3 Abertura e fechamento",
        "statement": (
            "Se fopen(\"dados.txt\", \"r\") falhar e retornar NULL, chamar fclose(fp) dentro do bloco de tratamento de erro "
            "é uma boa prática para garantir que nenhum recurso fique aberto."
        ),
        "answer": False,
        "steps": [
            "Quando fopen retorna NULL, nenhum arquivo ou stream foi aberto.",
            "Passar NULL para fclose() causa comportamento indefinido (tipicamente Segmentation Fault)."
        ],
        "keyPoint": "Só chame fclose(fp) quando fp != NULL."
    },
    {
        "id": "ce-arq-2",
        "category": "arquivos",
        "subtopic": "3.4 Modos de abertura",
        "statement": (
            "Abrir um arquivo existente com o modo \"w+\" permite ler e escrever preservando o conteúdo prévio do arquivo."
        ),
        "answer": False,
        "steps": [
            "Embora \"w+\" habilite leitura e escrita, o prefixo 'w' sempre trunca o arquivo existente para 0 bytes na abertura.",
            "Para ler e escrever preservando o conteúdo existente, deve-se usar \"r+\" (ou \"r+b\" em binário)."
        ],
        "keyPoint": "Qualquer modo iniciado com 'w' (\"w\", \"wb\", \"w+\", \"w+b\") zera o arquivo existente."
    },
    {
        "id": "ce-arq-3",
        "category": "arquivos",
        "subtopic": "3.7 Fim de arquivo",
        "statement": (
            "Em C, a função feof(fp) só retorna valor diferente de zero depois que uma operação de leitura anterior "
            "tentou ler além do final do arquivo e falhou."
        ),
        "answer": True,
        "steps": [
            "feof(fp) apenas lê a flag interna de EOF da estrutura FILE, sem espiar o próximo byte do disco.",
            "Por isso while (!feof(fp)) entra em uma iteração extra após o último registro válido; deve-se testar o retorno de fscanf/fgets/fread/fgetc."
        ],
        "keyPoint": "feof(fp) é reativa (pós-falha de leitura), nunca preditiva."
    },
    {
        "id": "ce-arq-4",
        "category": "arquivos",
        "subtopic": "3.6 Leitura em texto",
        "statement": (
            "Armazenar o retorno de fgetc(fp) em uma variável do tipo char é totalmente seguro em qualquer arquivo, "
            "inclusive arquivos binários."
        ),
        "answer": False,
        "steps": [
            "fgetc retorna int para representar todos os 256 valores possíveis de byte (0..255) além de EOF (-1).",
            "Em char com sinal, o byte 0xFF vira -1 (falso EOF); em char sem sinal, EOF (-1) vira 255 (loop infinito)."
        ],
        "keyPoint": "Use sempre int c; ao ler com fgetc(fp)."
    },
    {
        "id": "ce-arq-5",
        "category": "arquivos",
        "subtopic": "3.8 Arquivos binários",
        "statement": (
            "Na chamada fread(vetor, sizeof(int), 5, fp), o valor retornado em caso de leitura completa de todos os dados é 5, "
            "e não 20."
        ),
        "answer": True,
        "steps": [
            "fread e fwrite retornam a quantidade de elementos/blocos efetivamente transferidos (terceiro argumento).",
            "Como foram solicitados 5 elementos de tamanho sizeof(int), o retorno em sucesso é 5."
        ],
        "keyPoint": "fread/fwrite retornam quantidade de itens, não bytes."
    },
    {
        "id": "ce-arq-6",
        "category": "arquivos",
        "subtopic": "3.9 Structs em arquivos",
        "statement": (
            "É seguro usar fwrite(&reg, sizeof(reg), 1, fp) para persistir uma struct que contém um campo char *descricao "
            "alocado com malloc, pois fwrite copia automaticamente a string apontada para o arquivo."
        ),
        "answer": False,
        "steps": [
            "fwrite faz cópia rasa dos bytes contidos dentro da struct, gravando apenas o endereço numérico de memoria do ponteiro.",
            "Ao encerrar o processo e reler em outra execução, esse endereço será inválido (dangling pointer)."
        ],
        "keyPoint": "Para fwrite direto, use arrays fixos na struct (char descricao[N]) ou serialize a string separadamente."
    },
    {
        "id": "ce-arq-7",
        "category": "arquivos",
        "subtopic": "3.10 Posicionamento e fseek/ftell",
        "statement": (
            "Em um arquivo binário de tamanho fixo por registro, fseek(fp, 0L, SEEK_END) seguido de ftell(fp) retorna "
            "o tamanho total do arquivo em bytes."
        ),
        "answer": True,
        "steps": [
            "SEEK_END com offset 0 posiciona o cursor no final exato do stream binário.",
            "ftell(fp) devolve a distância em bytes desde o início até a posição atual."
        ],
        "keyPoint": "Total de registros = ftell(fp) / sizeof(Registro) após fseek(fp, 0L, SEEK_END)."
    },
    {
        "id": "ce-arq-8",
        "category": "arquivos",
        "subtopic": "3.13 Buffer de E/S",
        "statement": (
            "A função fflush(stdin) é garantida pelo padrão ISO C como a forma portável oficial de limpar caracteres pendentes "
            "do buffer de entrada do teclado."
        ),
        "answer": False,
        "steps": [
            "O padrão ISO C define fflush() apenas para streams de saída ou streams de atualização cuja última operação foi de escrita.",
            "Em streams de entrada como stdin, fflush tem comportamento indefinido."
        ],
        "keyPoint": "fflush é para buffers de saída; para limpar entrada use um laço com fgetc/getchar até '\\n'."
    },
    {
        "id": "ce-arq-9",
        "category": "arquivos",
        "subtopic": "3.14 Fluxos padrão",
        "statement": (
            "Escrever mensagens de erro em stderr (via fprintf(stderr, ...) ou perror) evita que diagnósticos contaminem "
            "a saída de dados quando o usuário redireciona stdout no terminal com '>'."
        ),
        "answer": True,
        "steps": [
            "O operador '>' redireciona apenas stdout (descritor 1), mantendo stderr (descritor 2) separado.",
            "Além disso, stderr não é totalmente bufferizado, exibindo falhas imediatamente."
        ],
        "keyPoint": "Separe saída de programa (stdout) de mensagens de erro (stderr)."
    },
    {
        "id": "ce-arq-10",
        "category": "arquivos",
        "subtopic": "3.17 CRUD e erros comuns",
        "statement": (
            "Em um arquivo aberto em modo de atualização \"r+b\", após ler um registro com fread e encontrar o ID desejado, "
            "é obrigatório reposicionar o cursor com fseek (ou rewind) antes de chamar fwrite para sobrescrevê-lo."
        ),
        "answer": True,
        "steps": [
            "fread avança o cursor para o próximo registro, então escrever sem recuar corromperia o registro seguinte.",
            "Além disso, o padrão C proíbe alternar leitura para escrita em modos '+' sem uma chamada intermediária de fseek/rewind."
        ],
        "keyPoint": "Em modos '+', nunca troque diretamente de leitura para escrita sem fseek/rewind."
    }
]

CLASSICAL_ARQUIVOS = [
    {
        "id": "class-arq-1",
        "module": "Arquivos",
        "source": "Clássico ADS · Deitel Cap. 11 & Strings (3.16)",
        "title": "Analisador de CSV e Gerador de Relatório",
        "problem": (
            "Dado um arquivo texto `vendas.csv` com cabeçalho na primeira linha e registros no formato "
            "`produto;categoria;quantidade;preco_unitario` (um por linha), leia todos os registros com segurança, "
            "calcule o faturamento por item e o total geral, e gere um arquivo `relatorio.txt` formatado contendo cada "
            "item, o subtotal, o produto de maior faturamento e o resumo consolidado."
        ),
        "idea": (
            "Leia linha a linha com `fgets` para evitar estouro de buffer e pule o cabeçalho inicial. Remova `'\\r'` e `'\\n'` "
            "com `strcspn`. Quebre os campos com `strtok` (ou `sscanf` com scanset `%[^;]`), converta valores numéricos, "
            "acumule estatísticas em uma única passada O(n) e grave a tabela alinhada em `relatorio.txt` via `fprintf`."
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n\n"
            "int gerar_relatorio_csv(const char *csv_path, const char *rel_path) {\n"
            "    FILE *in = fopen(csv_path, \"r\");\n"
            "    if (!in) {\n"
            "        perror(csv_path);\n"
            "        return 0;\n"
            "    }\n"
            "    FILE *out = fopen(rel_path, \"w\");\n"
            "    if (!out) {\n"
            "        perror(rel_path);\n"
            "        fclose(in);\n"
            "        return 0;\n"
            "    }\n\n"
            "    char linha[256];\n"
            "    if (fgets(linha, sizeof(linha), in) == NULL) {\n"
            "        fprintf(out, \"Arquivo CSV vazio.\\n\");\n"
            "        fclose(in);\n"
            "        fclose(out);\n"
            "        return 1;\n"
            "    }\n\n"
            "    fprintf(out, \"%-20s | %-12s | %5s | %9s | %10s\\n\",\n"
            "            \"Produto\", \"Categoria\", \"Qtd\", \"Unit(R$)\", \"Subtot(R$)\");\n"
            "    fprintf(out, \"---------------------------------------------------------------------\\n\");\n\n"
            "    double total_geral = 0.0, maior_sub = -1.0;\n"
            "    char campeao[64] = \"N/A\";\n"
            "    int itens_validos = 0;\n\n"
            "    while (fgets(linha, sizeof(linha), in) != NULL) {\n"
            "        linha[strcspn(linha, \"\\r\\n\")] = '\\0';\n"
            "        if (linha[0] == '\\0') continue;\n\n"
            "        char *prod = strtok(linha, \";\");\n"
            "        char *cat  = strtok(NULL, \";\");\n"
            "        char *qtds = strtok(NULL, \";\");\n"
            "        char *prus = strtok(NULL, \";\");\n\n"
            "        int qtd = 0;\n"
            "        double unit = 0.0;\n"
            "        if (!prod || !cat || !qtds || !prus) continue;\n"
            "        if (sscanf(qtds, \"%d\", &qtd) != 1 || sscanf(prus, \"%lf\", &unit) != 1) continue;\n\n"
            "        double sub = qtd * unit;\n"
            "        total_geral += sub;\n"
            "        itens_validos++;\n"
            "        if (sub > maior_sub) {\n"
            "            maior_sub = sub;\n"
            "            snprintf(campeao, sizeof(campeao), \"%s\", prod);\n"
            "        }\n"
            "        fprintf(out, \"%-20.20s | %-12.12s | %5d | %9.2f | %10.2f\\n\",\n"
            "                prod, cat, qtd, unit, sub);\n"
            "    }\n\n"
            "    fprintf(out, \"---------------------------------------------------------------------\\n\");\n"
            "    fprintf(out, \"Registros validos : %d\\n\", itens_validos);\n"
            "    fprintf(out, \"Maior faturamento : %s (R$ %.2f)\\n\", campeao, maior_sub > 0 ? maior_sub : 0.0);\n"
            "    fprintf(out, \"TOTAL GERAL       : R$ %.2f\\n\", total_geral);\n\n"
            "    fclose(in);\n"
            "    fclose(out);\n"
            "    return 1;\n"
            "}\n"
        ),
        "trace": (
            "Entrada vendas.csv:\n"
            "  produto;categoria;quantidade;preco_unitario\n"
            "  Teclado;Perifericos;4;120.00\n"
            "  Mouse;Perifericos;10;55.50\n\n"
            "Passo 1: fgets consome cabeçalho.\n"
            "Passo 2: linha 1 -> prod=\"Teclado\", cat=\"Perifericos\", qtd=4, unit=120.00 -> sub=480.00, total=480.00, campeao=\"Teclado\".\n"
            "Passo 3: linha 2 -> prod=\"Mouse\", cat=\"Perifericos\", qtd=10, unit=55.50 -> sub=555.00, total=1035.00, campeao=\"Mouse\".\n"
            "Passo 4: fgets retorna NULL (EOF) -> escreve rodapé com 2 registros, Mouse (R$ 555.00) e TOTAL R$ 1035.00; fecha in e out."
        )
    },
    {
        "id": "class-arq-2",
        "module": "Arquivos",
        "source": "Clássico ADS · Deitel Cap. 11.8–11.10 (3.17)",
        "title": "CRUD Binário de Produtos com Exclusão Física",
        "problem": (
            "Implemente as operações essenciais de um CRUD em arquivo binário `produtos.dat` para `Produto { int id; char nome[40]; "
            "int estoque; double preco; }`: cadastrar novo produto (append `\"ab\"`), buscar e alterar preço in-loco por ID "
            "(`\"r+b\"` com `fseek` + `fwrite`), e excluir fisicamente um produto pelo ID sem deixar registros vazios no arquivo."
        ),
        "idea": (
            "1) Cadastro usa `\"ab\"` para anexar ao fim sem perder os anteriores. 2) Alteração usa `\"r+b\"`: lê com `fread` "
            "até achar o ID, recua exatamente `sizeof(Produto)` bytes com `fseek(fp, -(long)sizeof(Produto), SEEK_CUR)` e "
            "sobrescreve com `fwrite` + `fflush`. 3) Exclusão física lê todos os registros de `produtos.dat` e grava apenas "
            "os que têm `id != id_alvo` em `produtos.tmp`, fecha ambos e executa `remove` + `rename`."
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n\n"
            "typedef struct {\n"
            "    int id;\n"
            "    char nome[40];\n"
            "    int estoque;\n"
            "    double preco;\n"
            "} Produto;\n\n"
            "int cadastrar_produto(const char *arq, Produto p) {\n"
            "    FILE *fp = fopen(arq, \"ab\");\n"
            "    if (!fp) return 0;\n"
            "    int ok = (fwrite(&p, sizeof(Produto), 1, fp) == 1);\n"
            "    fclose(fp);\n"
            "    return ok;\n"
            "}\n\n"
            "int alterar_preco(const char *arq, int id_alvo, double novo_preco) {\n"
            "    FILE *fp = fopen(arq, \"r+b\");\n"
            "    if (!fp) return 0;\n"
            "    Produto p;\n"
            "    while (fread(&p, sizeof(Produto), 1, fp) == 1) {\n"
            "        if (p.id == id_alvo) {\n"
            "            p.preco = novo_preco;\n"
            "            if (fseek(fp, -(long)sizeof(Produto), SEEK_CUR) != 0) {\n"
            "                fclose(fp);\n"
            "                return 0;\n"
            "            }\n"
            "            int ok = (fwrite(&p, sizeof(Produto), 1, fp) == 1);\n"
            "            fflush(fp);\n"
            "            fclose(fp);\n"
            "            return ok;\n"
            "        }\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}\n\n"
            "int excluir_fisico(const char *arq, int id_alvo) {\n"
            "    FILE *in = fopen(arq, \"rb\");\n"
            "    if (!in) return 0;\n"
            "    FILE *tmp = fopen(\"produtos.tmp\", \"wb\");\n"
            "    if (!tmp) {\n"
            "        fclose(in);\n"
            "        return 0;\n"
            "    }\n"
            "    Produto p;\n"
            "    int achou = 0;\n"
            "    while (fread(&p, sizeof(Produto), 1, in) == 1) {\n"
            "        if (p.id == id_alvo) {\n"
            "            achou = 1;\n"
            "            continue; // Omite o registro removido\n"
            "        }\n"
            "        if (fwrite(&p, sizeof(Produto), 1, tmp) != 1) {\n"
            "            fclose(in);\n"
            "            fclose(tmp);\n"
            "            remove(\"produtos.tmp\");\n"
            "            return 0;\n"
            "        }\n"
            "    }\n"
            "    fclose(in);\n"
            "    fclose(tmp);\n"
            "    if (!achou) {\n"
            "        remove(\"produtos.tmp\");\n"
            "        return 0;\n"
            "    }\n"
            "    if (remove(arq) != 0) return 0;\n"
            "    return rename(\"produtos.tmp\", arq) == 0;\n"
            "}\n"
        ),
        "trace": (
            "Suponha produtos.dat com [{id:1, preco:10.0}, {id:2, preco:25.0}, {id:3, preco:40.0}] (sizeof=56B):\n"
            "1) alterar_preco(..., 2, 29.9): 1º fread lê id=1 (cursor=56); 2º fread lê id=2 (cursor=112).\n"
            "   fseek(fp, -56, SEEK_CUR) volta cursor para 56; fwrite grava {id:2, preco:29.9} exatamente nos bytes 56..111.\n"
            "2) excluir_fisico(..., 2): lê id=1 -> copia para produtos.tmp; lê id=2 -> achou=1, pula; lê id=3 -> copia.\n"
            "   Fecha in e tmp -> remove(\"produtos.dat\") -> rename(\"produtos.tmp\", \"produtos.dat\").\n"
            "   Arquivo final tem exatamente 2 registros (112 bytes), sem buracos."
        )
    }
]
