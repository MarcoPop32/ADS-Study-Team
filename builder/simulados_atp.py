"""Dados do Cheat Sheet e dos 3 Simulados estilo ATP (ADS Study Team v4.0)."""
from __future__ import annotations

CHEATSHEET_DATA = [
    {
        "id": "cs-ptr",
        "tabLabel": "Ponteiros & Memória",
        "title": "Referência Rápida: Ponteiros e Alocação Dinâmica",
        "cards": [
            {
                "title": "Operadores &, * e Ponteiro NULL",
                "badge": "Fundamentos",
                "summary": "Um ponteiro armazena o endereço de memória de outra variável. Use & para obter o endereço e * para ler ou gravar no endereço apontado.",
                "items": [
                    "int x = 10; int *p = &x; -> p guarda o endereço de x.",
                    "*p = 25; -> altera o conteúdo de x para 25 (desreferência).",
                    "Sempre inicialize ponteiros sem alvo com NULL e teste if (p != NULL) antes de usar *p.",
                    "Ponteiros não inicializados (selvagens) apontam para lixo e causam comportamento indefinido.",
                ],
                "code": (
                    "int x = 10;\n"
                    "int *p = &x;\n"
                    "if (p != NULL) {\n"
                    "    *p = 42; // x passa a valer 42\n"
                    "}"
                ),
                "tip": "Em declarações, * indica que a variável é ponteiro; em expressões, * acessa o valor apontado.",
            },
            {
                "title": "Aritmética de Ponteiros e Vetores",
                "badge": "Endereços",
                "summary": "Somar ou subtrair inteiros de um ponteiro desloca em múltiplos de sizeof(*p), nunca em bytes avulsos.",
                "items": [
                    "p + k avança k * sizeof(*p) bytes na memória.",
                    "*(v + i) é estritamente equivalente a v[i].",
                    "q - p (ambos no mesmo vetor) retorna a distância em quantidade de elementos.",
                    "Cuidado: *p++ avança o ponteiro após ler *p; (*p)++ incrementa o valor apontado.",
                ],
                "code": (
                    "int v[3] = {10, 20, 30};\n"
                    "int *p = v;        // aponta para v[0]\n"
                    "int a = *(p + 2);  // 30\n"
                    "(*p)++;            // v[0] vira 11"
                ),
                "tip": "O nome de um vetor decai para ponteiro do primeiro elemento (&v[0]) na maioria das expressões.",
            },
            {
                "title": "Alocação Dinâmica: malloc, calloc, realloc e free",
                "badge": "Heap",
                "summary": "Variáveis na Heap sobrevivem ao fim da função e têm tamanho definido em tempo de execução, exigindo liberação manual.",
                "items": [
                    "malloc(n * sizeof(T)): aloca bytes com conteúdo não inicializado (lixo).",
                    "calloc(n, sizeof(T)): aloca n elementos de tamanho sizeof(T) e zera todos os bits.",
                    "realloc(p, novo_tam): redimensiona bloco; use ponteiro temporário tmp para não perder p se retornar NULL.",
                    "free(p); p = NULL;: libera a memória e evita uso posterior (dangling pointer).",
                ],
                "code": (
                    "int *v = (int *) malloc(5 * sizeof(int));\n"
                    "if (v == NULL) return 1;\n"
                    "int *tmp = (int *) realloc(v, 10 * sizeof(int));\n"
                    "if (tmp != NULL) v = tmp;\n"
                    "free(v);\n"
                    "v = NULL;"
                ),
                "tip": "Nunca atribua o retorno de realloc diretamente no ponteiro original antes de checar != NULL.",
            },
            {
                "title": "Ponteiro Genérico (void *) e Qualificador const",
                "badge": "Qualificadores",
                "summary": "void * aceita qualquer endereço sem tipo fixo, enquanto const protege ou o dado apontado ou o próprio ponteiro.",
                "items": [
                    "void *p: não permite desreferência (*p) nem aritmética direta sem cast prévio para tipo concreto.",
                    "const int *p: o valor *p é somente leitura, mas p pode mudar de endereço.",
                    "int * const p: o ponteiro p é fixo (não muda de endereço), mas *p pode ser alterado.",
                    "const int * const p: nem o ponteiro nem o conteúdo podem ser alterados.",
                ],
                "code": (
                    "int a = 5, b = 8;\n"
                    "const int *p1 = &a; // *p1 = 9 erro; p1 = &b ok\n"
                    "int * const p2 = &a; // *p2 = 9 ok; p2 = &b erro\n"
                    "void *gen = &a;\n"
                    "int val = *(int *)gen;"
                ),
                "tip": "Leia declarações com ponteiros e const da direita para a esquerda para não confundir em prova.",
            },
            {
                "title": "Passagem por Referência e Ponteiro para Ponteiro (**)",
                "badge": "Funções",
                "summary": "C passa argumentos por valor. Para alterar uma variável ou um ponteiro do chamador, passe seu endereço.",
                "items": [
                    "Para alterar int x dentro de uma função, passe &x para parâmetro int *p.",
                    "Para alocar e alterar um ponteiro int *p dentro de uma função, passe &p para int **pp.",
                    "Matrizes dinâmicas 2D usam T **m com alocação das linhas e de cada coluna, e free na ordem inversa.",
                ],
                "code": (
                    "void alocar(int **pp, int n) {\n"
                    "    *pp = (int *) malloc(n * sizeof(int));\n"
                    "}\n"
                    "void trocar(int *a, int *b) {\n"
                    "    int t = *a; *a = *b; *b = t;\n"
                    "}"
                ),
                "tip": "Passar T * altera o valor de T; passar T ** altera para onde o ponteiro T * aponta.",
            },
        ],
    },
    {
        "id": "cs-strc",
        "tabLabel": "Structs, Unions & Enums",
        "title": "Referência Rápida: Registros Compostos",
        "cards": [
            {
                "title": "Declaração de struct e typedef",
                "badge": "Sintaxe",
                "summary": "struct agrupa campos de tipos diferentes em um registro contínuo. typedef cria um apelido limpo para o tipo.",
                "items": [
                    "Sempre termine a definição da struct com ponto e vírgula (;).",
                    "Sem typedef, cada variável exige a palavra-chave struct: struct Aluno a;.",
                    "Com typedef struct { ... } Aluno;, declara-se diretamente Aluno a;.",
                    "Structs autorreferenciadas (listas/árvores) devem usar ponteiro (struct No *prox;), nunca valor direto.",
                ],
                "code": (
                    "typedef struct No {\n"
                    "    int valor;\n"
                    "    struct No *prox;\n"
                    "} No;"
                ),
                "tip": "Esquecer o ; após a chave de fechamento da struct gera erros em cascata na linha seguinte.",
            },
            {
                "title": "Acesso com Ponto (.) vs Seta (->)",
                "badge": "Acesso",
                "summary": "Use ponto (.) em variáveis/elementos de struct e seta (->) em ponteiros para struct.",
                "items": [
                    "a.nota: acesso direto quando a é do tipo Aluno.",
                    "p->nota: atalho idiomático equivalente a (*p).nota quando p é Aluno *.",
                    "ARMADILHA: *p.nota falha porque o ponto (.) tem precedência maior que *.",
                    "Passar struct por valor copia todos os bytes; passar ponteiro (Aluno *) evita cópia e permite edição.",
                ],
                "code": (
                    "void darBonus(Aluno *p, double b) {\n"
                    "    if (p != NULL) {\n"
                    "        p->nota += b; // igual a (*p).nota += b\n"
                    "    }\n"
                    "}"
                ),
                "tip": "Se à esquerda há um ponteiro para struct, use ->; se há uma instância direta (ou v[i]), use .",
            },
            {
                "title": "Inicialização Designada, Cópia e Strings em Struct",
                "badge": "Uso Prático",
                "summary": "Structs aceitam atribuição direta (=) e inicializadores designados (C99+), mas campos char[] exigem strcpy.",
                "items": [
                    "Aluno a = {.id = 10, .nota = 8.5}; inicializa campos pelo nome e zera os omitidos.",
                    "b = a; copia todos os campos de a para b (cuidado: se houver char *, copia só o endereço!).",
                    "Em arrays char nome[40], atribuição posterior exige strcpy(a.nome, \"Ana\"), nunca a.nome = \"Ana\".",
                ],
                "code": (
                    "typedef struct { int id; char nome[30]; } Pessoa;\n"
                    "Pessoa p1 = {.id = 1, .nome = \"Ana\"};\n"
                    "Pessoa p2 = p1; // copia id e os 30 bytes de nome\n"
                    "strcpy(p2.nome, \"Bia\");"
                ),
                "tip": "Prefira char nome[TAM] fixo dentro de structs quando for copiar ou gravar em arquivo binário.",
            },
            {
                "title": "union vs struct e enum",
                "badge": "Memória",
                "summary": "Na struct cada campo tem espaço próprio; na union todos os campos compartilham a mesma região de memória.",
                "items": [
                    "sizeof(union) é pelo menos o tamanho do maior membro (com alinhamento), não a soma.",
                    "Escrever em um campo da union sobrescreve os demais; apenas o último gravado é válido.",
                    "enum define constantes inteiras nomeadas: começa em 0 e incrementa de 1 em 1 salvo valor explícito.",
                    "Combinação clássica (Tagged Union): struct contendo um enum tipo e uma union dado.",
                ],
                "code": (
                    "enum Status { PENDENTE = 1, PAGO = 5, CANCELADO }; // 1, 5, 6\n"
                    "union Valor {\n"
                    "    int inteiro;\n"
                    "    double real;\n"
                    "};"
                ),
                "tip": "Questões de union quase sempre perguntam sizeof(union) ou o efeito de sobrescrever um membro pelo outro.",
            },
            {
                "title": "Alinhamento, Padding e sizeof(Struct)",
                "badge": "Arquitetura",
                "summary": "O compilador insere bytes de preenchimento (padding) para alinhar cada campo ao seu múltiplo natural de endereço.",
                "items": [
                    "char (1B) + int (4B) + char (1B) costuma ocupar 12 bytes (3 de padding após o 1º char e 3 ao final).",
                    "Reordenar campos do maior para o menor (int, char, char) reduz para 8 bytes.",
                    "Sempre passe sizeof(TipoStruct) em malloc, fwrite e fread — nunca some os tamanhos na mão.",
                ],
                "code": (
                    "struct Desalinhada { char a; int b; char c; }; // tipicamente 12 B\n"
                    "struct Otimizada   { int b; char a; char c; }; // tipicamente 8 B"
                ),
                "tip": "Em provas, sizeof(struct) >= soma dos campos por causa do padding.",
            },
        ],
    },
    {
        "id": "cs-arq",
        "tabLabel": "Arquivos (FILE *)",
        "title": "Referência Rápida: Persistência e <stdio.h>",
        "cards": [
            {
                "title": "Modos de Abertura (r, w, a, + e b) e Validação",
                "badge": "Abertura",
                "summary": "fopen retorna FILE * ou NULL em erro. O modo controla existência prévia, truncamento e permissão de leitura/escrita.",
                "items": [
                    "\"r\": lê arquivo existente (NULL se não existir). \"w\": cria ou ZERA arquivo existente.",
                    "\"a\": cria ou acrescenta sempre no final. \"r+\": lê e escreve sem zerar (exige existir).",
                    "\"w+\": lê e escreve zerando antes. \"a+\": lê de qualquer ponto e escreve sempre no fim.",
                    "Sufixo \"b\" (\"rb\", \"wb\", \"rb+\"): modo binário; indispensável no Windows para evitar tradução de \\n.",
                ],
                "code": (
                    "FILE *fp = fopen(\"dados.bin\", \"rb\");\n"
                    "if (fp == NULL) {\n"
                    "    perror(\"Erro ao abrir\");\n"
                    "    return 1;\n"
                    "}\n"
                    "fclose(fp);"
                ),
                "tip": "Sempre cheque if (fp == NULL) logo após fopen e garanta fclose(fp) ao terminar.",
            },
            {
                "title": "Arquivos Texto: fprintf, fscanf, fgets e fputs",
                "badge": "Texto",
                "summary": "Funções orientadas a texto formatado ou linhas. Valide sempre o retorno da função de leitura.",
                "items": [
                    "fprintf(fp, fmt, ...): grava texto formatado como printf.",
                    "fscanf(fp, fmt, ...): retorna a quantidade de itens convertidos com sucesso (ou EOF).",
                    "fgets(buf, tam, fp): lê até tam-1 chars ou '\\n' (preserva '\\n' no buffer); retorna NULL no fim.",
                    "fputs(str, fp) grava string sem acrescentar '\\n' automático (diferente de puts).",
                ],
                "code": (
                    "char linha[100];\n"
                    "while (fgets(linha, sizeof(linha), fp) != NULL) {\n"
                    "    printf(\"%s\", linha);\n"
                    "}"
                ),
                "tip": "fscanf(\"%s\") para no primeiro espaço; use fgets quando a linha puder conter espaços.",
            },
            {
                "title": "Arquivos Binários: fwrite e fread",
                "badge": "Binário",
                "summary": "Copiam blocos brutos de bytes da RAM para o arquivo e vice-versa, ideais para arrays e structs sem ponteiros.",
                "items": [
                    "Assinatura: size_t fwrite(const void *ptr, size_t tam, size_t qtd, FILE *fp).",
                    "Retorno: número de ELEMENTOS (qtd) efetivamente lidos/escritos, NUNCA bytes.",
                    "NUNCA grave struct com campo char * ou ponteiros internos via fwrite (grava só o endereço!).",
                    "Teste if (fread(&reg, sizeof(Reg), 1, fp) == 1) para confirmar leitura íntegra.",
                ],
                "code": (
                    "Produto p;\n"
                    "while (fread(&p, sizeof(Produto), 1, fp) == 1) {\n"
                    "    printf(\"%d %s\\n\", p.codigo, p.nome);\n"
                    "}"
                ),
                "tip": "Em provas: se fread(&x, sizeof(int), 5, fp) lê tudo, retorna 5 (e não 20).",
            },
            {
                "title": "Posicionamento: fseek, ftell, rewind e fflush",
                "badge": "Acesso Aleatório",
                "summary": "Permitem pular diretamente para qualquer byte/registro do arquivo e sincronizar buffers.",
                "items": [
                    "fseek(fp, offset, origem): SEEK_SET (início), SEEK_CUR (posição atual), SEEK_END (fim).",
                    "ftell(fp): retorna a posição atual em bytes desde o início (long). Com SEEK_END, dá o tamanho.",
                    "rewind(fp): volta ao byte 0 e limpa indicadores de erro/EOF (equivale a fseek(fp,0,SEEK_SET) + clearerr).",
                    "Em modos \"+\" (r+, w+), é obrigatório chamar fseek, fsetpos, rewind ou fflush ao alternar leitura e escrita.",
                ],
                "code": (
                    "fseek(fp, 0, SEEK_END);\n"
                    "long totalBytes = ftell(fp);\n"
                    "long qtdReg = totalBytes / (long)sizeof(Produto);\n"
                    "fseek(fp, 2 * (long)sizeof(Produto), SEEK_SET); // 3º registro"
                ),
                "tip": "Índice 0-based: o k-ésimo registro (0, 1, 2...) fica em offset k * sizeof(Struct) com SEEK_SET.",
            },
            {
                "title": "Indicadores de Fim e Erro: feof, ferror e perror",
                "badge": "Diagnóstico",
                "summary": "feof(fp) só se torna verdadeiro DEPOIS que uma leitura falha ao tentar passar do fim do arquivo.",
                "items": [
                    "feof(fp) != 0 indica que a operação anterior tentou ler além do EOF.",
                    "ferror(fp) != 0 indica erro de hardware/permissão no stream (diferente de fim normal).",
                    "clearerr(fp) zera as flags de EOF e erro do stream.",
                    "perror(\"msg\") imprime \"msg: <descrição do errno>\" em stderr.",
                ],
                "code": (
                    "if (ferror(fp)) {\n"
                    "    perror(\"Falha de leitura\");\n"
                    "}"
                ),
                "tip": "Use feof(fp) apenas após um loop terminar para distinguir fim normal de erro de leitura.",
            },
        ],
    },
    {
        "id": "cs-debug",
        "tabLabel": "Armadilhas & Debug",
        "title": "Checklist de Ouro para Provas e Depuração",
        "cards": [
            {
                "title": "Armadilha #1: while (!feof(fp))",
                "badge": "Armadilha #1",
                "summary": "feof(fp) só liga APÓS uma leitura falhar no EOF. Testá-lo antes de ler faz a última iteração rodar duas vezes.",
                "items": [
                    "ERRADO: while (!feof(fp)) { fscanf(fp, \"%d\", &x); soma += x; } -> soma o último número 2x!",
                    "CORRETO: testar diretamente o retorno da função de leitura.",
                    "Texto formatado: while (fscanf(fp, \"%d %s\", &id, nome) == 2)",
                    "Linhas/Binário: while (fgets(buf, sizeof(buf), fp) != NULL) / while (fread(&r, sizeof(r), 1, fp) == 1)",
                ],
                "code": (
                    "// ERRADO: processa último item repetido ou lixo\n"
                    "// while (!feof(fp)) { fread(&p, sizeof(p), 1, fp); ... }\n\n"
                    "// CORRETO:\n"
                    "while (fread(&p, sizeof(Produto), 1, fp) == 1) { /* ... */ }"
                ),
                "tip": "Regra absoluta de prova: nunca use while (!feof(fp)) como condição de laço.",
            },
            {
                "title": "Armadilha #2: Modo \"w\" Apaga Dados & Alternância em \"+\"",
                "badge": "Armadilha #2",
                "summary": "Abrir um arquivo existente com \"w\" ou \"wb\" destrói todo o conteúdo imediatamente ao chamar fopen.",
                "items": [
                    "Para preservar dados e adicionar no final, use \"a\" ou \"ab\".",
                    "Para ler e alterar registros existentes no meio do arquivo, use \"r+\" ou \"rb+\".",
                    "Em \"r+\"/\"rb+\", nunca faça fread seguido de fwrite (ou vice-versa) sem fseek/fflush/rewind entre eles.",
                    "Esquecer fclose(fp) pode deixar dados presos no buffer sem gravar no disco.",
                ],
                "code": (
                    "FILE *fp = fopen(\"contas.bin\", \"rb+\");\n"
                    "fread(&c, sizeof(Conta), 1, fp);\n"
                    "c.saldo += 100.0;\n"
                    "fseek(fp, -(long)sizeof(Conta), SEEK_CUR); // volta + sincroniza\n"
                    "fwrite(&c, sizeof(Conta), 1, fp);"
                ),
                "tip": "Para atualizar o registro recém-lido em rb+, volte -(long)sizeof(Registro) com SEEK_CUR.",
            },
            {
                "title": "Armadilha #3: Memory Leak, Dangling Pointer e Double Free",
                "badge": "Armadilha #3",
                "summary": "Os três erros clássicos de gerenciamento manual da Heap em C.",
                "items": [
                    "Memory Leak: alocar com malloc e perder o ponteiro (ex.: sair da função sem free ou sobrescrever p = malloc(...)).",
                    "Dangling Pointer: usar p após free(p) ou retornar o endereço (&local) de uma variável local da pilha.",
                    "Double Free: chamar free(p) duas vezes no mesmo endereço sem ter reatribuído NULL (free(NULL) é seguro e não faz nada).",
                    "Antídoto: para cada malloc/calloc, trace exatamente onde ocorre o único free e faça p = NULL;.",
                ],
                "code": (
                    "int *criarErrado(void) {\n"
                    "    int x = 10;\n"
                    "    return &x; // BUG: x morre ao fim da função!\n"
                    "}"
                ),
                "tip": "Retornar ponteiro de uma função só é seguro se apontar para Heap (malloc), static ou buffer passado pelo chamador.",
            },
            {
                "title": "Armadilha #4: Sintaxe, Strings (=) e Precedência (*p.x)",
                "badge": "Armadilha #4",
                "summary": "Pequenos deslizes que derrubam a compilação ou corrompem a memória silenciosamente.",
                "items": [
                    "Falta de ponto e vírgula após struct { ... };",
                    "Usar = para copiar strings (aluno.nome = \"Ana\") em vez de strcpy(aluno.nome, \"Ana\").",
                    "Escrever *p.campo em vez de (*p).campo ou p->campo.",
                    "Passar p (ou *p) para scanf quando p já é ponteiro: se p é int *, use scanf(\"%d\", p), não &p.",
                ],
                "code": (
                    "Aluno *p = (Aluno *) malloc(sizeof(Aluno));\n"
                    "p->id = 1;\n"
                    "strcpy(p->nome, \"Carlos\");\n"
                    "scanf(\"%lf\", &p->nota); // & pega endereço do campo double"
                ),
                "tip": "&p->nota significa &(p->nota) porque -> tem precedência maior que &.",
            },
            {
                "title": "Flags de Compilação, AddressSanitizer e Valgrind",
                "badge": "Depuração",
                "summary": "Ferramentas padrão para detectar vazamentos, acessos fora do vetor e ponteiros inválidos automaticamente.",
                "items": [
                    "Compile sempre com avisos ligados: gcc -Wall -Wextra -Werror -g prog.c -o prog.",
                    "AddressSanitizer (ASan): gcc -g -fsanitize=address,undefined prog.c -o prog (detecta overflow, use-after-free e leak).",
                    "Valgrind (Linux): valgrind --leak-check=full --show-leak-kinds=all ./prog.",
                    "Na saída do Valgrind, busque: 'All heap blocks were freed -- no leaks are possible' e '0 errors'.",
                ],
                "code": (
                    "gcc -Wall -Wextra -g -fsanitize=address main.c -o main\n"
                    "./main\n"
                    "valgrind --leak-check=full ./main"
                ),
                "tip": "Em provas teóricas sobre debug, Valgrind e ASan identificam memory leaks, invalid read/write e double free em tempo de execução.",
            },
        ],
    },
]


SIMULADOS = [
    # =========================================================================
    # SIMULADO 1: Ponteiros + Alocação Dinâmica (Peso ATP)
    # =========================================================================
    {
        "id": "sim-1",
        "title": "Simulado 1: Ponteiros e Alocação Dinâmica",
        "subtitle": "Peso ATP: operadores & e *, aritmética de ponteiros, passagem por referência, malloc/calloc/realloc/free, void*, const e matrizes dinâmicas.",
        "durationSec": 7200,
        "questions": [
            {
                "id": "s1-q1",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Aliases com dois ponteiros",
                "prompt": "<p>Analise o trecho de código em C abaixo e assinale o valor impresso na tela:</p>",
                "code": (
                    "#include <stdio.h>\n"
                    "int main(void) {\n"
                    "    int a = 4, b = 10;\n"
                    "    int *p = &a;\n"
                    "    int *q = p;\n"
                    "    *q = *p + b;\n"
                    "    p = &b;\n"
                    "    *p = a - 2;\n"
                    "    printf(\"%d %d\\n\", a, b);\n"
                    "    return 0;\n"
                    "}"
                ),
                "options": [
                    "4 10",
                    "14 12",
                    "14 8",
                    "10 12",
                    "Erro de compilação ao atribuir q = p",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: *q altera a para 14 e *p posteriormente altera b para 12.",
                    "Correta! Inicialmente p e q apontam para a. *q = *p + b faz a = 4 + 10 = 14. Depois p passa a apontar para b, e *p = a - 2 faz b = 14 - 2 = 12.",
                    "Incorreta: quando *p = a - 2 executa, a já vale 14 (e não 10).",
                    "Incorreta: a recebeu 4 + 10 = 14 via *q.",
                    "Incorreta: atribuir um int * a outro int * (q = p) é totalmente válido.",
                ],
            },
            {
                "id": "s1-q2",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Precedência entre * e ++",
                "prompt": "<p>Considere o código a seguir e indique a saída exata produzida pelo <code>printf</code>:</p>",
                "code": (
                    "#include <stdio.h>\n"
                    "int main(void) {\n"
                    "    int v[4] = {10, 20, 30, 40};\n"
                    "    int *p = v;\n"
                    "    int x = *p++;\n"
                    "    int y = (*p)++;\n"
                    "    printf(\"%d %d %d\\n\", x, y, *p);\n"
                    "    return 0;\n"
                    "}"
                ),
                "options": [
                    "10 20 21",
                    "11 20 21",
                    "10 21 21",
                    "11 21 30",
                    "10 20 30",
                ],
                "correct": 0,
                "explanations": [
                    "Correta! *p++ lê o valor atual (10 -> x) e depois avança p para v[1]. Em seguida (*p)++ lê o valor de v[1] (20 -> y) e incrementa v[1] para 21 sem mover p, logo *p é 21.",
                    "Incorreta: o pós-incremento em *p++ aplica-se ao ponteiro p, não ao valor 10.",
                    "Incorreta: em y = (*p)++, o pós-incremento retorna o valor antigo (20) para y antes de somar 1 em v[1].",
                    "Incorreta: (*p)++ incrementa o conteúdo de v[1], não move p para v[2].",
                    "Incorreta: p não avançou para v[2] na segunda expressão.",
                ],
            },
            {
                "id": "s1-q3",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Aritmética e subtração de ponteiros",
                "prompt": "<p>Assumindo <code>sizeof(int) == 4</code>, qual é a saída do programa abaixo?</p>",
                "code": (
                    "#include <stdio.h>\n"
                    "int main(void) {\n"
                    "    int vet[6] = {2, 4, 6, 8, 10, 12};\n"
                    "    int *p = &vet[1];\n"
                    "    int *q = vet + 5;\n"
                    "    printf(\"%ld %d\\n\", (long)(q - p), *(q - 2));\n"
                    "    return 0;\n"
                    "}"
                ),
                "options": [
                    "16 8",
                    "4 8",
                    "4 6",
                    "16 6",
                    "5 10",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: a subtração q - p resulta no número de elementos (4), e não na diferença em bytes (16).",
                    "Correta! p aponta para vet[1] e q para vet[5]. A diferença q - p é 5 - 1 = 4 elementos. Já *(q - 2) acessa vet[5 - 2] = vet[3] = 8.",
                    "Incorreta: vet[3] vale 8, enquanto vet[2] vale 6.",
                    "Incorreta: nem a diferença é em bytes (16), nem vet[3] vale 6.",
                    "Incorreta: p aponta para o índice 1, não para o índice 0.",
                ],
            },
            {
                "id": "s1-q4",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Passagem por valor vs referência",
                "prompt": "<p>Observe a função <code>alterar</code> abaixo. Qual será a saída impressa no <code>main</code>?</p>",
                "code": (
                    "#include <stdio.h>\n"
                    "void alterar(int a, int *b) {\n"
                    "    a = a + 10;\n"
                    "    *b = *b + a;\n"
                    "}\n"
                    "int main(void) {\n"
                    "    int x = 5, y = 3;\n"
                    "    alterar(x, &y);\n"
                    "    printf(\"%d %d\\n\", x, y);\n"
                    "    return 0;\n"
                    "}"
                ),
                "options": [
                    "15 18",
                    "5 8",
                    "5 18",
                    "15 8",
                    "5 3",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: x foi passado por valor, portanto x continua valendo 5 no main.",
                    "Incorreta: dentro da função, o parâmetro local a passou para 15, e esse valor 15 foi somado a *b.",
                    "Correta! a é cópia de x (vira 15 localmente sem mudar x). *b aponta para y (3) e recebe 3 + 15 = 18. Logo, x = 5 e y = 18.",
                    "Incorreta: x não é alterado fora da função e *b recebeu a soma com 15.",
                    "Incorreta: y foi passado por referência (&y) e modificado via *b.",
                ],
            },
            {
                "id": "s1-q5",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Comparação entre malloc e calloc",
                "prompt": "<p>Sobre as funções de alocação dinâmica de <code>&lt;stdlib.h&gt;</code>, assinale a alternativa <strong>CORRETA</strong>:</p>",
                "code": "",
                "options": [
                    "malloc(n * sizeof(int)) sempre inicializa todos os elementos alocados com zero.",
                    "calloc(n, sizeof(int)) aloca memória na Stack e dispensa o uso de free().",
                    "calloc(n, sizeof(int)) recebe número de elementos e tamanho de cada um, inicializando todos os bytes com zero.",
                    "malloc(10) garante espaço suficiente para armazenar 10 variáveis do tipo double em qualquer sistema.",
                    "Se malloc falhar por falta de memória, ele encerra o programa automaticamente com abort().",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: malloc não zera a memória; os bytes contêm lixo de memória.",
                    "Incorreta: calloc aloca na Heap e exige free() exatamente como malloc.",
                    "Correta! calloc recebe (qtd, tamanho_unitario), aloca na Heap e zera todos os bits do bloco retornado.",
                    "Incorreta: malloc(10) aloca apenas 10 bytes, e 10 doubles precisam de 10 * sizeof(double) (tipicamente 80 bytes).",
                    "Incorreta: quando falha, malloc retorna NULL para que o programador trate o erro.",
                ],
            },
            {
                "id": "s1-q6",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Uso seguro de realloc",
                "prompt": "<p>Por que é considerada boa prática atribuir o retorno de <code>realloc(ptr, novo_tam)</code> a um ponteiro auxiliar <code>tmp</code> antes de atualizar <code>ptr</code>?</p>",
                "code": (
                    "int *tmp = (int *) realloc(ptr, novo_tam);\n"
                    "if (tmp != NULL) {\n"
                    "    ptr = tmp;\n"
                    "}"
                ),
                "options": [
                    "Porque realloc retorna o tamanho em bytes caso a alocação seja bem-sucedida.",
                    "Porque se realloc falhar, ele retorna NULL mantendo o bloco antigo alocado; atribuir direto a ptr causaria memory leak ao perder o endereço original.",
                    "Porque realloc sempre libera o ponteiro original mesmo quando retorna NULL.",
                    "Porque sem tmp o compilador C proíbe passar ptr como primeiro argumento.",
                    "Porque tmp converte automaticamente o bloco da Heap para a Stack.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: realloc retorna um ponteiro void * para o bloco (ou NULL em falha), nunca um inteiro de tamanho.",
                    "Correta! Se realloc falhar, ele devolve NULL sem liberar o bloco antigo. Sobrescrever ptr = realloc(ptr, ...) faria perder o único ponteiro para o bloco original (memory leak).",
                    "Incorreta: em caso de falha, o bloco original permanece intacto na Heap.",
                    "Incorreta: não há proibição sintática; o problema é perda de referência (memory leak).",
                    "Incorreta: realloc opera exclusivamente na Heap.",
                ],
            },
            {
                "id": "s1-q7",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Dangling pointer e tempo de vida",
                "prompt": "<p>Qual trecho abaixo produz um <strong>ponteiro pendente (dangling pointer)</strong>?</p>",
                "code": "",
                "options": [
                    "int *p = (int *) malloc(sizeof(int)); *p = 10; free(p); p = NULL;",
                    "int *p = (int *) calloc(4, sizeof(int)); p[0] = 5; free(p); p = NULL;",
                    "int *f(void) { int x = 7; return &x; }",
                    "void f(int *p) { if (p != NULL) *p = 20; }",
                    "int v[3] = {1, 2, 3}; int *p = v;",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: após free(p), atribuir p = NULL neutraliza o dangling pointer.",
                    "Incorreta: o bloco foi liberado e o ponteiro zerado com NULL com segurança.",
                    "Correta! x é variável automática local na Stack; ao encerrar f(), o frame de pilha é destruído e o endereço retornado aponta para memória inválida.",
                    "Incorreta: o ponteiro é validado contra NULL e pertence ao escopo do chamador.",
                    "Incorreta: enquanto v estiver no escopo atual, p aponta para memória válida.",
                ],
            },
            {
                "id": "s1-q8",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Ponteiro genérico void *",
                "prompt": "<p>Sobre o ponteiro genérico <code>void *ptr</code> em C padrão (ISO C), é <strong>CORRETO</strong> afirmar que:</p>",
                "code": "",
                "options": [
                    "Pode ser desreferenciado diretamente com *ptr, assumindo tipo int por padrão.",
                    "Não permite desreferência direta (*ptr) nem aritmética padrão (ptr + 1) sem antes realizar um cast para um tipo com tamanho conhecido.",
                    "Ocupa 0 bytes na memória, pois não possui tipo associado.",
                    "Aceita apenas endereços de variáveis alocadas com malloc(), nunca de variáveis locais.",
                    "É idêntico a NULL em qualquer expressão lógica.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: o compilador não sabe quantos bytes ler em *ptr sem um cast.",
                    "Correta! void * guarda apenas um endereço sem informação de tamanho do tipo apontado, exigindo cast como *(int *)ptr antes de desreferenciar.",
                    "Incorreta: void * é um ponteiro como qualquer outro e ocupa o tamanho de um endereço da arquitetura (ex.: 4 ou 8 bytes).",
                    "Incorreta: void * pode receber o endereço de qualquer variável ou objeto (ex.: void *p = &x;).",
                    "Incorreta: void * é um tipo de ponteiro; NULL é um valor de ponteiro nulo.",
                ],
            },
            {
                "id": "s1-q9",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Ponteiros com qualificador const",
                "prompt": "<p>Considere as declarações <code>int a = 1, b = 2;</code> e <code>const int *p = &amp;a;</code> e <code>int * const q = &amp;a;</code>. Quais instruções são válidas?</p>",
                "code": "",
                "options": [
                    "*p = 5; é válida e q = &b; é válida.",
                    "p = &b; é válida e *q = 5; é válida.",
                    "*p = 5; é válida e *q = 5; é inválida.",
                    "p = &b; é inválida e q = &b; é válida.",
                    "Todas as quatro atribuições geram erro de compilação.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: *p é const (não pode ser modificado) e q é ponteiro constante (não pode apontar para outro endereço).",
                    "Correta! Em const int *p, o dado apontado é constante, mas p pode mudar para &b. Em int * const q, o ponteiro q é constante, mas o valor *q pode ser alterado para 5.",
                    "Incorreta: inverte exatamente o papel do const antes e depois do *.",
                    "Incorreta: p pode ser reatribuído (p = &b), enquanto q não pode.",
                    "Incorreta: duas das quatro instruções são perfeitamente válidas.",
                ],
            },
            {
                "id": "s1-q10",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Liberação de matriz dinâmica (int **)",
                "prompt": "<p>Uma matriz dinâmica de <code>L</code> linhas por <code>C</code> colunas foi alocada como um vetor de <code>L</code> ponteiros (<code>int **m</code>), onde cada <code>m[i]</code> recebeu <code>malloc(C * sizeof(int))</code>. Qual é a forma <strong>CORRETA</strong> de liberá-la sem vazamentos nem acesso inválido?</p>",
                "code": "",
                "options": [
                    "Chamar apenas free(m); já libera todas as L linhas automaticamente.",
                    "Primeiro free(m); e depois um laço for (i = 0; i < L; i++) free(m[i]);.",
                    "Primeiro um laço for (i = 0; i < L; i++) free(m[i]); e por último free(m);.",
                    "Liberar apenas m[0] com free(m[0]); e depois free(m);.",
                    "Chamar free(&m); uma única vez.",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: free(m) libera somente o vetor de ponteiros das linhas, vazando todos os blocos m[i].",
                    "Incorreta: após free(m), acessar m[i] no laço é uso após liberação (use-after-free).",
                    "Correta! A liberação deve ocorrer na ordem inversa da alocação: primeiro libera cada linha m[i] e por último o vetor de ponteiros m.",
                    "Incorreta: as linhas m[1]..m[L-1] ficariam vazando na memória.",
                    "Incorreta: &m é o endereço da variável local m na Stack, nunca um ponteiro retornado por malloc.",
                ],
            },
            {
                "id": "s1-q11",
                "part": 2,
                "type": "trace",
                "points": 1.0,
                "title": "Teste de mesa: Ponteiros em vetor e função",
                "prompt": "<p>Faça o teste de mesa do programa em C abaixo e informe a saída exata e o motivo conceitual do resultado.</p>",
                "code": (
                    "#include <stdio.h>\n"
                    "\n"
                    "void ajustar(int *p, int k) {\n"
                    "    *p = *p + k;\n"
                    "    *(p + 1) = *(p + 1) * 2;\n"
                    "}\n"
                    "\n"
                    "int main(void) {\n"
                    "    int v[4] = {3, 5, 7, 9};\n"
                    "    int *ptr = v;\n"
                    "    ajustar(ptr, 4);\n"
                    "    ptr += 2;\n"
                    "    printf(\"%d %d %d\\n\", v[0], v[1], *ptr);\n"
                    "    return 0;\n"
                    "}"
                ),
                "partAPrompt": "Parte A (0,6 pt): Qual é a saída exata impressa no console (stdout)?",
                "partAPoints": 0.6,
                "expectedOutput": "7 10 7\n",
                "partBPrompt": "Parte B (0,4 pt): Explique por que ajustar() altera v[0] e v[1] no main e para qual posição ptr aponta após ptr += 2.",
                "partBPoints": 0.4,
                "partBKeywords": ["referencia", "ponteiro", "endereco", "v[0]", "v[1]", "v[2]", "aritmetica"],
                "partBModel": "Ao passar ptr (que guarda o endereço de v[0]), ajustar() opera diretamente sobre a memória do vetor no main: *p altera v[0] para 7 e *(p + 1) acessa o próximo int (v[1]), dobrando-o para 10. Depois, a aritmética ptr += 2 desloca ptr dois inteiros adiante, passando a apontar para v[2] (valor 7).",
                "traceSteps": [
                    {"line": 9, "vars": {"v": "[3, 5, 7, 9]"}, "note": "Inicializa o vetor v com 4 inteiros na Stack."},
                    {"line": 10, "vars": {"v": "[3, 5, 7, 9]", "ptr": "&v[0]"}, "note": "ptr recebe o endereço do primeiro elemento v[0]."},
                    {"line": 4, "vars": {"p": "&v[0]", "k": "4", "v[0]": "7"}, "note": "Dentro de ajustar, *p = *p + 4 altera v[0] de 3 para 7."},
                    {"line": 5, "vars": {"p": "&v[0]", "v[1]": "10"}, "note": "*(p + 1) acessa v[1] e dobra seu valor de 5 para 10."},
                    {"line": 12, "vars": {"ptr": "&v[2]", "*ptr": "7"}, "note": "ptr += 2 avança 2 elementos, apontando para v[2] (valor 7)."},
                    {"line": 13, "vars": {"v[0]": "7", "v[1]": "10", "*ptr": "7"}, "note": "printf imprime '7 10 7'."},
                ],
            },
            {
                "id": "s1-q12",
                "part": 2,
                "type": "bughunt",
                "points": 1.0,
                "title": "Caça aos Bugs: Alocação Dinâmica e Ponteiros",
                "prompt": "<p>O programa abaixo deveria ler <code>n</code> inteiros em um vetor alocado dinamicamente, dobrar os valores e liberar a memória. Encontre os <strong>4 bugs</strong> indicando a linha e a correção.</p>",
                "numberedCode": [
                    "#include <stdio.h>",
                    "#include <stdlib.h>",
                    "",
                    "void dobrar(int *p, int n) {",
                    "    for (int i = 0; i <= n; i++) {",
                    "        *(p + i) = *(p + i) * 2;",
                    "    }",
                    "}",
                    "",
                    "int main(void) {",
                    "    int n;",
                    "    scanf(\"%d\", n);",
                    "    int *v = (int *) malloc(n);",
                    "    for (int i = 0; i < n; i++) {",
                    "        scanf(\"%d\", &v[i]);",
                    "    }",
                    "    dobrar(v, n);",
                    "    free(v);",
                    "    printf(\"Primeiro: %d\\n\", v[0]);",
                    "    return 0;",
                    "}",
                ],
                "bugs": [
                    {
                        "line": 5,
                        "altLines": [],
                        "problem": "Condição i <= n acessa v[n], ultrapassando os limites do vetor alocado (buffer overflow).",
                        "fix": "for (int i = 0; i < n; i++) {",
                        "keywords": ["i < n", "limite", "overflow", "fora"],
                    },
                    {
                        "line": 12,
                        "altLines": [],
                        "problem": "scanf recebeu n por valor em vez do endereço &n, causando comportamento indefinido.",
                        "fix": "scanf(\"%d\", &n);",
                        "keywords": ["&n", "endereco", "scanf"],
                    },
                    {
                        "line": 13,
                        "altLines": [],
                        "problem": "malloc(n) aloca apenas n bytes em vez de n * sizeof(int) bytes (e falta validar NULL).",
                        "fix": "int *v = (int *) malloc(n * sizeof(int)); if (v == NULL) return 1;",
                        "keywords": ["sizeof", "bytes", "malloc", "null"],
                    },
                    {
                        "line": 19,
                        "altLines": [],
                        "problem": "Use-after-free (dangling pointer): acessa v[0] depois de já ter chamado free(v) na linha anterior.",
                        "fix": "Mover printf(\"Primeiro: %d\\n\", v[0]); para antes de free(v); (e atribuir v = NULL; após free).",
                        "keywords": ["free", "dangling", "antes", "use-after-free", "v[0]"],
                    },
                ],
            },
            {
                "id": "s1-q13",
                "part": 2,
                "type": "step_code",
                "points": 1.0,
                "title": "Implementação Guiada: Estatísticas com Ponteiros e Heap",
                "prompt": "<p>Responda à pergunta teórica da Parte A e implemente o programa completo em C na Parte B.</p>",
                "partAPrompt": "Parte A (0,4 pt): Por que a função stats(int *v, int n, int *min, int *max) precisa receber os ponteiros *min e *max, e por que é obrigatório chamar free(v) ao final do main?",
                "partAPoints": 0.4,
                "partAKeywords": ["referencia", "retornar", "dois", "free", "leak", "vazamento", "heap"],
                "partAModel": "Em C uma função retorna apenas um valor; recebendo int *min e int *max (passagem por referência), stats altera duas variáveis no main simultaneamente. Já free(v) libera o bloco alocado na Heap com malloc, evitando memory leak.",
                "partBPrompt": "Parte B (0,6 pt): Leia um inteiro n, aloque dinamicamente um vetor de n inteiros com malloc, leia os n valores, chame stats(v, n, &menor, &maior) usando ponteiros e imprima exatamente 'Min: <menor> | Max: <maior>' seguido de quebra de linha, liberando a memória ao final.",
                "partBPoints": 0.6,
                "ioExample": "Entrada:\n4\n12 5 19 8\n\nSaída:\nMin: 5 | Max: 19",
                "starter": (
                    "#include <stdio.h>\n"
                    "#include <stdlib.h>\n\n"
                    "void stats(int *v, int n, int *min, int *max) {\n"
                    "    // Calcule menor e maior via ponteiros\n"
                    "}\n\n"
                    "int main(void) {\n"
                    "    int n, i, menor, maior;\n"
                    "    if (scanf(\"%d\", &n) != 1 || n <= 0) return 0;\n"
                    "    // Aloque com malloc, leia os n inteiros, chame stats, imprima e libere\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "tests": [
                    {"in": "4\n12 5 19 8\n", "out": "Min: 5 | Max: 19\n"},
                    {"in": "5\n-3 0 -10 7 2\n", "out": "Min: -10 | Max: 7\n"},
                    {"in": "1\n42\n", "out": "Min: 42 | Max: 42\n"},
                ],
                "modelCode": (
                    "#include <stdio.h>\n"
                    "#include <stdlib.h>\n\n"
                    "void stats(int *v, int n, int *min, int *max) {\n"
                    "    int i;\n"
                    "    *min = *v;\n"
                    "    *max = *v;\n"
                    "    for (i = 1; i < n; i++) {\n"
                    "        if (*(v + i) < *min) *min = *(v + i);\n"
                    "        if (*(v + i) > *max) *max = *(v + i);\n"
                    "    }\n"
                    "}\n\n"
                    "int main(void) {\n"
                    "    int n, i, menor, maior;\n"
                    "    if (scanf(\"%d\", &n) != 1 || n <= 0) return 0;\n"
                    "    int *v = (int *) malloc(n * sizeof(int));\n"
                    "    if (v == NULL) return 1;\n"
                    "    for (i = 0; i < n; i++) {\n"
                    "        scanf(\"%d\", v + i);\n"
                    "    }\n"
                    "    stats(v, n, &menor, &maior);\n"
                    "    printf(\"Min: %d | Max: %d\\n\", menor, maior);\n"
                    "    free(v);\n"
                    "    v = NULL;\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "solutionNote": "stats() inicializa *min e *max com *v (v[0]) e percorre via aritmética *(v + i). No main, verifica-se v == NULL antes de ler e libera-se com free(v).",
            },
            {
                "id": "s1-q14",
                "part": 2,
                "type": "code",
                "points": 2.0,
                "title": "Problema Completo: Expansão Dinâmica com realloc e Filtro",
                "prompt": (
                    "<p>Escreva um programa em C que:</p>"
                    "<ol>"
                    "<li>Leia um inteiro <code>n</code> (&gt;= 1) e aloque dinamicamente um vetor de <code>n</code> inteiros com <code>malloc</code>, lendo os <code>n</code> valores.</li>"
                    "<li>Leia um inteiro <code>k</code> (&gt;= 0). Se <code>k &gt; 0</code>, expanda o vetor para <code>n + k</code> elementos usando <code>realloc</code> (com ponteiro temporário <code>tmp</code>) e leia os <code>k</code> novos inteiros.</li>"
                    "<li>Implemente uma função <code>int contarParesESomar(int *v, int total, int *soma)</code> que percorre os <code>total</code> elementos via ponteiro, armazena em <code>*soma</code> a soma de todos os elementos e retorna a quantidade de números pares.</li>"
                    "<li>Imprima exatamente <code>Total: &lt;n+k&gt; | Pares: &lt;pares&gt; | Soma: &lt;soma&gt;</code> e libere toda a memória alocada.</li>"
                    "</ol>"
                ),
                "ioExample": "Entrada:\n3\n2 5 8\n2\n4 7\n\nSaída:\nTotal: 5 | Pares: 3 | Soma: 26",
                "starter": (
                    "#include <stdio.h>\n"
                    "#include <stdlib.h>\n\n"
                    "int contarParesESomar(int *v, int total, int *soma) {\n"
                    "    // Retorne qtd de pares e grave a soma total em *soma\n"
                    "    return 0;\n"
                    "}\n\n"
                    "int main(void) {\n"
                    "    // Leia n, aloque, leia k, expanda com realloc, processe, imprima e dê free\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "tests": [
                    {"in": "3\n2 5 8\n2\n4 7\n", "out": "Total: 5 | Pares: 3 | Soma: 26\n"},
                    {"in": "4\n1 3 5 7\n0\n", "out": "Total: 4 | Pares: 0 | Soma: 16\n"},
                    {"in": "2\n-4 6\n3\n0 9 -2\n", "out": "Total: 5 | Pares: 4 | Soma: 9\n"},
                ],
                "modelCode": (
                    "#include <stdio.h>\n"
                    "#include <stdlib.h>\n\n"
                    "int contarParesESomar(int *v, int total, int *soma) {\n"
                    "    int i, pares = 0;\n"
                    "    *soma = 0;\n"
                    "    for (i = 0; i < total; i++) {\n"
                    "        int val = *(v + i);\n"
                    "        *soma += val;\n"
                    "        if (val % 2 == 0) {\n"
                    "            pares++;\n"
                    "        }\n"
                    "    }\n"
                    "    return pares;\n"
                    "}\n\n"
                    "int main(void) {\n"
                    "    int n, k, i, total, pares, soma;\n"
                    "    if (scanf(\"%d\", &n) != 1 || n <= 0) return 0;\n"
                    "    int *v = (int *) malloc(n * sizeof(int));\n"
                    "    if (v == NULL) return 1;\n"
                    "    for (i = 0; i < n; i++) {\n"
                    "        scanf(\"%d\", v + i);\n"
                    "    }\n"
                    "    if (scanf(\"%d\", &k) != 1 || k < 0) k = 0;\n"
                    "    total = n + k;\n"
                    "    if (k > 0) {\n"
                    "        int *tmp = (int *) realloc(v, total * sizeof(int));\n"
                    "        if (tmp == NULL) {\n"
                    "            free(v);\n"
                    "            return 1;\n"
                    "        }\n"
                    "        v = tmp;\n"
                    "        for (i = n; i < total; i++) {\n"
                    "            scanf(\"%d\", v + i);\n"
                    "        }\n"
                    "    }\n"
                    "    pares = contarParesESomar(v, total, &soma);\n"
                    "    printf(\"Total: %d | Pares: %d | Soma: %d\\n\", total, pares, soma);\n"
                    "    free(v);\n"
                    "    v = NULL;\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "solutionNote": "Usa malloc inicial, realloc seguro via tmp (liberando v caso tmp seja NULL), aritmética *(v + i) em contarParesESomar e passagem por referência em &soma.",
            },
        ],
    },

    # =========================================================================
    # SIMULADO 2: Structs + Unions + Enums + Ponteiros para Structs
    # =========================================================================
    {
        "id": "sim-2",
        "title": "Simulado 2: Structs, Unions, Enums e Ponteiros",
        "subtitle": "Avaliação estilo ATP: typedef struct, operadores . vs ->, passagem por valor vs referência, arrays dinâmicos de structs, unions, enums e padding.",
        "durationSec": 7200,
        "questions": [
            {
                "id": "s2-q1",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Declaração correta com typedef struct",
                "prompt": "<p>Qual das opções declara um tipo <code>Livro</code> usando <code>typedef struct</code> e acessa corretamente o campo <code>paginas</code> por meio de um ponteiro <code>ptr</code>?</p>",
                "code": "",
                "options": [
                    "typedef struct { int paginas; } Livro -> ptr.paginas",
                    "typedef struct { int paginas; } Livro; -> *ptr.paginas",
                    "typedef struct { int paginas; } Livro; -> ptr->paginas",
                    "struct typedef { int paginas; } Livro; -> ptr->paginas",
                    "typedef struct { int paginas; } Livro -> (*ptr)->paginas",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: falta ponto e vírgula ao final da definição da struct e usa ponto (.) em ponteiro.",
                    "Incorreta: *ptr.paginas falha pela precedência maior do ponto (.) sobre o operador *.",
                    "Correta! typedef struct { ... } Livro; finaliza com ; e ptr->paginas equivale a (*ptr).paginas.",
                    "Incorreta: a sintaxe em C exige typedef antes de struct, não struct typedef.",
                    "Incorreta: falta ; na definição e (*ptr) já é a struct (exigiria ponto, não ->).",
                ],
            },
            {
                "id": "s2-q2",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Precedência entre * e . em ponteiros para struct",
                "prompt": "<p>Dado <code>Aluno *p = &amp;a;</code>, por que a expressão <code>*p.nota = 9.0;</code> gera erro de compilação?</p>",
                "code": "",
                "options": [
                    "Porque campos float/double de uma struct não podem ser alterados por ponteiro.",
                    "Porque o operador ponto (.) tem precedência maior que (*), fazendo o compilador tentar avaliar *(p.nota).",
                    "Porque o operador (*) só funciona com tipos primitivos, nunca com structs.",
                    "Porque falta usar & antes de nota.",
                    "Porque em C é proibido usar ponto quando existe o operador ->.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: qualquer campo não-const pode ser alterado via ponteiro.",
                    "Correta! Como . precede *, o compilador interpreta *p.nota como *(p.nota), mas p é ponteiro e não tem operador . direto. O correto é (*p).nota ou p->nota.",
                    "Incorreta: * funciona perfeitamente em ponteiros para struct: (*p).nota é válido.",
                    "Incorreta: & obteria um endereço, o que não resolve a precedência.",
                    "Incorreta: (*p).nota usa ponto perfeitamente e é sinônimo de p->nota.",
                ],
            },
            {
                "id": "s2-q3",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Cópia por valor vs passagem por ponteiro",
                "prompt": "<p>Analise o comportamento da struct <code>Ponto</code> no código abaixo e assinale a saída correta:</p>",
                "code": (
                    "#include <stdio.h>\n"
                    "typedef struct { int x, y; } Ponto;\n"
                    "void moverValor(Ponto p) { p.x += 10; }\n"
                    "void moverRef(Ponto *p) { p->y += 10; }\n"
                    "int main(void) {\n"
                    "    Ponto pt = {2, 3};\n"
                    "    moverValor(pt);\n"
                    "    moverRef(&pt);\n"
                    "    printf(\"%d %d\\n\", pt.x, pt.y);\n"
                    "    return 0;\n"
                    "}"
                ),
                "options": [
                    "12 13",
                    "2 3",
                    "2 13",
                    "12 3",
                    "Erro: struct não pode ser passada por valor em C",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: moverValor recebe uma cópia local de pt, logo pt.x não muda no main.",
                    "Incorreta: moverRef recebe &pt e modifica pt.y diretamente.",
                    "Correta! moverValor altera apenas sua cópia local (pt.x segue 2), enquanto moverRef usa o endereço &pt para alterar pt.y de 3 para 13.",
                    "Incorreta: ocorreu exatamente o oposto entre x e y.",
                    "Incorreta: structs podem ser passadas por valor em C (embora por ponteiro seja mais eficiente e permita alteração).",
                ],
            },
            {
                "id": "s2-q4",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Inicialização designada e campos omitidos",
                "prompt": "<p>Considere a declaração <code>typedef struct { int id; double saldo; char ativo; } Conta;</code> e a linha <code>Conta c = {.saldo = 50.0};</code> (padrão C99+). Quais serão os valores de <code>c.id</code> e <code>c.ativo</code>?</p>",
                "code": "",
                "options": [
                    "Lixo de memória indeterminado em ambos.",
                    "c.id será 0 e c.ativo será 0 ('\\0').",
                    "Erro de compilação por omitir o primeiro campo.",
                    "c.id será 1 e c.ativo será 'S'.",
                    "Apenas c.id é zerado; c.ativo fica com lixo.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: só fica com lixo se não houver lista de inicialização (Conta c;).",
                    "Correta! Quando uma struct usa inicialização parcial ou designada ({.saldo = 50.0}), todos os campos omitidos são automaticamente inicializados com zero.",
                    "Incorreta: a inicialização designada em C99+ permite listar campos em qualquer ordem e omitir os demais.",
                    "Incorreta: o valor padrão de campos omitidos em inicialização parcial é sempre 0.",
                    "Incorreta: todos os campos não listados são zerados.",
                ],
            },
            {
                "id": "s2-q5",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Atribuição entre structs com ponteiro interno",
                "prompt": "<p>Suponha que <code>struct Pessoa</code> possua um campo <code>char *nome</code> apontando para um buffer alocado com <code>malloc</code>. Ao executar <code>Pessoa p2 = p1;</code> e depois <code>strcpy(p2.nome, \"Lucas\");</code>, o que acontece com <code>p1.nome</code>?</p>",
                "code": "",
                "options": [
                    "p1.nome permanece inalterado, pois a atribuição = em structs faz cópia profunda.",
                    "p1.nome também passa a exibir \"Lucas\", pois = copiou apenas o endereço do ponteiro (cópia rasa).",
                    "O compilador impede atribuir uma struct a outra usando =.",
                    "Ocorre double free imediato na linha de atribuição.",
                    "p2.nome passa a apontar para NULL automaticamente.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: o operador = em C realiza cópia byte a byte rasa (shallow copy), não seguindo ponteiros.",
                    "Correta! p2.nome recebe o mesmo endereço de memória que p1.nome. Alterar o conteúdo via p2.nome altera a mesma string vista por p1.nome.",
                    "Incorreta: atribuir structs do mesmo tipo com = é perfeitamente válido em C.",
                    "Incorreta: a atribuição não chama free; o risco de double free surge depois se o programa der free(p1.nome) e free(p2.nome).",
                    "Incorreta: p2.nome recebe o mesmo endereço de p1.nome.",
                ],
            },
            {
                "id": "s2-q6",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Comportamento e tamanho de union",
                "prompt": "<p>Observe a <code>union Dado</code> abaixo (considere <code>int</code> = 4 bytes, <code>double</code> = 8 bytes, <code>char</code> = 1 byte). O que é correto afirmar?</p>",
                "code": (
                    "union Dado {\n"
                    "    int i;\n"
                    "    double d;\n"
                    "    char c;\n"
                    "};"
                ),
                "options": [
                    "sizeof(union Dado) é 13 bytes (4 + 8 + 1).",
                    "Cada membro ocupa um endereço diferente dentro da union.",
                    "Todos os membros iniciam no mesmo endereço, sizeof(union Dado) é pelo menos 8 bytes, e gravar em d invalida o valor anterior de i.",
                    "É possível armazenar simultaneamente um int e um double válidos na mesma instância da union.",
                    "union não aceita ponteiros para seus membros com &.",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: a soma dos membros vale para struct, nunca para union.",
                    "Incorreta: na union todos os campos sobrepõem a mesma região de memória.",
                    "Correta! A union compartilha a mesma memória entre todos os campos, tendo tamanho suficiente para o maior deles (double = 8 bytes); escrever em um membro sobrescreve os outros.",
                    "Incorreta: apenas o último campo escrito contém um valor válido.",
                    "Incorreta: é totalmente válido obter &u.i ou usar u_ptr->d.",
                ],
            },
            {
                "id": "s2-q7",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Valores de enumeração (enum)",
                "prompt": "<p>Dado <code>enum Nivel { BAIXO, MEDIO = 5, ALTO, CRITICO };</code>, qual valor inteiro é impresso por <code>printf(\"%d %d\\n\", BAIXO, CRITICO);</code>?</p>",
                "code": "",
                "options": [
                    "1 7",
                    "0 7",
                    "0 6",
                    "1 6",
                    "5 7",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: o primeiro enumerador sem valor explícito começa em 0, não em 1.",
                    "Correta! BAIXO = 0 (padrão inicial), MEDIO = 5 (explícito), ALTO = 6 e CRITICO = 7 (incremento de 1 em 1).",
                    "Incorreta: 6 é o valor de ALTO, não de CRITICO.",
                    "Incorreta: BAIXO é 0 e CRITICO é 7.",
                    "Incorreta: 5 é o valor de MEDIO.",
                ],
            },
            {
                "id": "s2-q8",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Alinhamento e Padding de Struct",
                "prompt": "<p>Em uma arquitetura de 64 bits comum (<code>char</code> = 1B, <code>int</code> = 4B com alinhamento de 4B), por que <code>sizeof(struct A)</code> costuma ser 12 bytes e <code>sizeof(struct B)</code> costuma ser 8 bytes?</p>",
                "code": (
                    "struct A { char x; int y; char z; };\n"
                    "struct B { int y; char x; char z; };"
                ),
                "options": [
                    "Porque struct B comprime o int de 4 bytes para 2 bytes.",
                    "Por causa do padding de alinhamento: em A há 3 bytes de preenchimento após x e 3 ao final; em B, x e z ficam juntos antes de apenas 2 bytes finais de padding.",
                    "Porque a ordem dos campos nunca altera o tamanho da struct, apenas o compilador escolheu 12.",
                    "Porque char ocupa 4 bytes quando é o primeiro campo da struct.",
                    "Porque struct A aloca um ponteiro oculto de 4 bytes.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: o tamanho de int não muda conforme a ordem dos campos.",
                    "Correta! O campo int exige endereço múltiplo de 4. Em A: 1(x) + 3(pad) + 4(y) + 1(z) + 3(pad) = 12. Em B: 4(y) + 1(x) + 1(z) + 2(pad) = 8.",
                    "Incorreta: agrupar campos maiores antes dos menores frequentemente reduz o padding total.",
                    "Incorreta: sizeof(char) é sempre 1 byte.",
                    "Incorreta: structs em C não possuem ponteiros ocultos nem vtable.",
                ],
            },
            {
                "id": "s2-q9",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Vetor dinâmico de structs",
                "prompt": "<p>Considere <code>Item *lista = (Item *) malloc(n * sizeof(Item));</code>. Qual expressão acessa corretamente o campo <code>preco</code> do terceiro elemento (índice 2)?</p>",
                "code": "",
                "options": [
                    "lista->preco[2]",
                    "(lista + 2).preco",
                    "(lista + 2)->preco",
                    "*(lista + 2)->preco",
                    "&lista[2]->preco",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: lista->preco acessa o campo do índice 0 e tenta indexar um float/double.",
                    "Incorreta: (lista + 2) é do tipo Item * (ponteiro), exigindo -> em vez de ponto (.).",
                    "Correta! lista + 2 aponta para o 3º Item, então (lista + 2)->preco (equivalente a lista[2].preco) acessa seu campo preco.",
                    "Incorreta: o * extra tentaria desreferenciar o valor numérico preco.",
                    "Incorreta: lista[2] já é uma struct (não ponteiro), logo -> está errado aqui.",
                ],
            },
            {
                "id": "s2-q10",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Structs autorreferenciadas",
                "prompt": "<p>Na definição de um nó de lista encadeada, por que <code>struct No</code> pode conter <code>struct No *prox;</code>, mas NÃO pode conter <code>struct No prox;</code>?</p>",
                "code": "",
                "options": [
                    "Porque C não permite duas structs com o mesmo nome de campo.",
                    "Porque conter a própria struct por valor exigiria tamanho infinito (recursivo), enquanto um ponteiro tem tamanho fixo conhecido pelo compilador.",
                    "Porque o operador -> só funciona se o campo se chamar prox.",
                    "Porque variáveis struct não podem ficar dentro de outra struct.",
                    "Porque ponteiros para struct não ocupam espaço na memória.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: o problema não é o nome do campo.",
                    "Correta! Se struct No contivesse um struct No inteiro dentro de si, sizeof(struct No) seria infinito. Um ponteiro struct No * tem tamanho fixo (4 ou 8 bytes).",
                    "Incorreta: o nome do campo pode ser qualquer identificador válido.",
                    "Incorreta: composição com structs diferentes (ex.: Data dentro de Aluno) é perfeitamente válida.",
                    "Incorreta: ponteiros ocupam normalmente 4 ou 8 bytes.",
                ],
            },
            {
                "id": "s2-q11",
                "part": 2,
                "type": "trace",
                "points": 1.0,
                "title": "Teste de mesa: Structs por valor vs ponteiro e Enum",
                "prompt": "<p>Execute o rastreio do programa abaixo envolvendo <code>typedef struct</code>, passagem por valor e passagem por ponteiro.</p>",
                "code": (
                    "#include <stdio.h>\n"
                    "\n"
                    "typedef struct {\n"
                    "    int id;\n"
                    "    double nota;\n"
                    "} Aluno;\n"
                    "\n"
                    "void atualizar(Aluno a, Aluno *b) {\n"
                    "    a.nota = 10.0;\n"
                    "    b->nota += 1.5;\n"
                    "}\n"
                    "\n"
                    "int main(void) {\n"
                    "    Aluno x = {1, 6.0};\n"
                    "    Aluno y = {2, 7.0};\n"
                    "    atualizar(x, &y);\n"
                    "    printf(\"%.1f %.1f\\n\", x.nota, y.nota);\n"
                    "    return 0;\n"
                    "}"
                ),
                "partAPrompt": "Parte A (0,6 pt): Qual é a saída exata impressa no console (stdout)?",
                "partAPoints": 0.6,
                "expectedOutput": "6.0 8.5\n",
                "partBPrompt": "Parte B (0,4 pt): Explique por que x.nota permanece 6.0 enquanto y.nota muda para 8.5.",
                "partBPoints": 0.4,
                "partBKeywords": ["valor", "copia", "ponteiro", "referencia", "->", "endereco"],
                "partBModel": "x é passado por valor para o parâmetro a, criando uma cópia local independente; alterar a.nota não afeta x.nota. Já y tem seu endereço (&y) passado para o ponteiro b, e b->nota += 1.5 modifica diretamente o campo nota de y no main.",
                "traceSteps": [
                    {"line": 14, "vars": {"x.id": "1", "x.nota": "6.0"}, "note": "Inicializa struct x com nota 6.0."},
                    {"line": 15, "vars": {"y.id": "2", "y.nota": "7.0"}, "note": "Inicializa struct y com nota 7.0."},
                    {"line": 9, "vars": {"a.nota": "10.0", "x.nota": "6.0"}, "note": "atualizar() altera apenas a cópia local a; x.nota segue 6.0."},
                    {"line": 10, "vars": {"b": "&y", "y.nota": "8.5"}, "note": "b->nota += 1.5 soma 1.5 diretamente em y.nota (7.0 -> 8.5)."},
                    {"line": 17, "vars": {"x.nota": "6.0", "y.nota": "8.5"}, "note": "printf imprime '6.0 8.5'."},
                ],
            },
            {
                "id": "s2-q12",
                "part": 2,
                "type": "bughunt",
                "points": 1.0,
                "title": "Caça aos Bugs: Structs, Strings e Ponteiro ->",
                "prompt": "<p>O código abaixo deveria alocar uma struct <code>Produto</code> dinamicamente, preencher seus campos e imprimir o resultado. Localize os <strong>4 bugs</strong>.</p>",
                "numberedCode": [
                    "#include <stdio.h>",
                    "#include <stdlib.h>",
                    "#include <string.h>",
                    "",
                    "typedef struct {",
                    "    int cod;",
                    "    char nome[30];",
                    "    double preco;",
                    "} Produto",
                    "",
                    "int main(void) {",
                    "    Produto *p = (Produto *) malloc(sizeof(Produto));",
                    "    if (p == NULL) return 1;",
                    "    *p.cod = 101;",
                    "    p->nome = \"Teclado\";",
                    "    scanf(\"%lf\", p->preco);",
                    "    printf(\"%d %s %.2f\\n\", p->cod, p->nome, p->preco);",
                    "    free(p);",
                    "    return 0;",
                    "}",
                ],
                "bugs": [
                    {
                        "line": 9,
                        "altLines": [],
                        "problem": "Falta ponto e vírgula (;) ao final da definição de typedef struct.",
                        "fix": "} Produto;",
                        "keywords": [";", "ponto e virgula", "typedef", "struct"],
                    },
                    {
                        "line": 14,
                        "altLines": [],
                        "problem": "Precedência incorreta em *p.cod (o ponto . precede *); erro de compilação.",
                        "fix": "p->cod = 101;",
                        "keywords": ["p->cod", "(*p).cod", "seta", "precedencia"],
                    },
                    {
                        "line": 15,
                        "altLines": [],
                        "problem": "Em C não se copia string para array char[] usando operador =.",
                        "fix": "strcpy(p->nome, \"Teclado\");",
                        "keywords": ["strcpy", "string", "=", "nome"],
                    },
                    {
                        "line": 16,
                        "altLines": [],
                        "problem": "scanf(\"%lf\", p->preco) passa o valor double em vez do endereço do campo (&p->preco).",
                        "fix": "scanf(\"%lf\", &p->preco);",
                        "keywords": ["&p->preco", "endereco", "scanf", "&"],
                    },
                ],
            },
            {
                "id": "s2-q13",
                "part": 2,
                "type": "step_code",
                "points": 1.0,
                "title": "Implementação Guiada: Reajuste Salarial com Ponteiro para Struct",
                "prompt": "<p>Responda à Parte A conceitual e implemente o programa na Parte B.</p>",
                "partAPrompt": "Parte A (0,4 pt): Qual é a dupla vantagem de declarar void aplicarReajuste(Funcionario *f, double perc) em vez de receber Funcionario f por valor?",
                "partAPoints": 0.4,
                "partAKeywords": ["copia", "memoria", "original", "alterar", "referencia", "ponteiro", "->"],
                "partAModel": "Passar Funcionario *f evita copiar todos os bytes da struct na pilha e permite que a função altere diretamente o campo salario da variável original no main por meio do operador seta (->).",
                "partBPrompt": "Parte B (0,6 pt): Defina typedef struct { int id; char nome[40]; double salario; } Funcionario; e implemente aplicarReajuste(Funcionario *f, double perc) que soma perc% ao salario usando ->. Leia id, nome (palavra única), salario e perc; aplique o reajuste e imprima 'ID: <id> | Nome: <nome> | Salario: <salario:.2f>'.",
                "partBPoints": 0.6,
                "ioExample": "Entrada:\n10 Ana 2000.00 10.0\n\nSaída:\nID: 10 | Nome: Ana | Salario: 2200.00",
                "starter": (
                    "#include <stdio.h>\n\n"
                    "typedef struct {\n"
                    "    int id;\n"
                    "    char nome[40];\n"
                    "    double salario;\n"
                    "} Funcionario;\n\n"
                    "void aplicarReajuste(Funcionario *f, double perc) {\n"
                    "    // Aumente f->salario em perc%\n"
                    "}\n\n"
                    "int main(void) {\n"
                    "    Funcionario func;\n"
                    "    double perc;\n"
                    "    // Leia os dados, chame aplicarReajuste(&func, perc) e imprima\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "tests": [
                    {"in": "10 Ana 2000.00 10.0\n", "out": "ID: 10 | Nome: Ana | Salario: 2200.00\n"},
                    {"in": "25 Bruno 1500.00 20.0\n", "out": "ID: 25 | Nome: Bruno | Salario: 1800.00\n"},
                    {"in": "3 Carla 4000.00 5.5\n", "out": "ID: 3 | Nome: Carla | Salario: 4220.00\n"},
                ],
                "modelCode": (
                    "#include <stdio.h>\n\n"
                    "typedef struct {\n"
                    "    int id;\n"
                    "    char nome[40];\n"
                    "    double salario;\n"
                    "} Funcionario;\n\n"
                    "void aplicarReajuste(Funcionario *f, double perc) {\n"
                    "    if (f != NULL) {\n"
                    "        f->salario = f->salario * (1.0 + perc / 100.0);\n"
                    "    }\n"
                    "}\n\n"
                    "int main(void) {\n"
                    "    Funcionario func;\n"
                    "    double perc;\n"
                    "    if (scanf(\"%d %s %lf %lf\", &func.id, func.nome, &func.salario, &perc) != 4) {\n"
                    "        return 0;\n"
                    "    }\n"
                    "    aplicarReajuste(&func, perc);\n"
                    "    printf(\"ID: %d | Nome: %s | Salario: %.2f\\n\", func.id, func.nome, func.salario);\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "solutionNote": "Na entrada usa-se &func.id, func.nome (array já decai para char *) e &func.salario. Em aplicarReajuste, f->salario atualiza a struct original.",
            },
            {
                "id": "s2-q14",
                "part": 2,
                "type": "code",
                "points": 2.0,
                "title": "Problema Completo: Vetor Dinâmico de Structs e Melhor Aluno",
                "prompt": (
                    "<p>Escreva um programa em C para gerenciar notas de uma turma:</p>"
                    "<ol>"
                    "<li>Defina <code>typedef struct { int ra; char nome[40]; double n1; double n2; } Aluno;</code>.</li>"
                    "<li>Leia <code>n</code> (&gt;= 1) e aloque dinamicamente um vetor de <code>n</code> alunos com <code>malloc(n * sizeof(Aluno))</code>.</li>"
                    "<li>Para cada aluno, leia <code>ra nome n1 n2</code> (<code>nome</code> sem espaços).</li>"
                    "<li>Implemente <code>int indiceMelhor(Aluno *turma, int n)</code> que retorna o índice do aluno com maior média <code>(n1 + n2) / 2.0</code> (em caso de empate, mantenha o primeiro).</li>"
                    "<li>Para cada aluno, imprima <code>&lt;ra&gt; &lt;nome&gt; &lt;media:.2f&gt; &lt;APROVADO|REPROVADO&gt;</code> (aprovado se média &gt;= 6.0) e ao final imprima <code>Melhor: &lt;nome&gt; (&lt;media:.2f&gt;)</code>. Libere a memória alocada.</li>"
                    "</ol>"
                ),
                "ioExample": "Entrada:\n2\n101 Ana 7.0 8.0\n102 Joao 5.0 6.0\n\nSaída:\n101 Ana 7.50 APROVADO\n102 Joao 5.50 REPROVADO\nMelhor: Ana (7.50)",
                "starter": (
                    "#include <stdio.h>\n"
                    "#include <stdlib.h>\n\n"
                    "typedef struct {\n"
                    "    int ra;\n"
                    "    char nome[40];\n"
                    "    double n1;\n"
                    "    double n2;\n"
                    "} Aluno;\n\n"
                    "int indiceMelhor(Aluno *turma, int n) {\n"
                    "    return 0;\n"
                    "}\n\n"
                    "int main(void) {\n"
                    "    // Aloque turma com malloc, leia n alunos, imprima status e melhor aluno, libere com free\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "tests": [
                    {
                        "in": "2\n101 Ana 7.0 8.0\n102 Joao 5.0 6.0\n",
                        "out": "101 Ana 7.50 APROVADO\n102 Joao 5.50 REPROVADO\nMelhor: Ana (7.50)\n",
                    },
                    {
                        "in": "3\n1 Bia 4.0 5.0\n2 Lucas 6.0 6.0\n3 Mara 9.0 8.5\n",
                        "out": "1 Bia 4.50 REPROVADO\n2 Lucas 6.00 APROVADO\n3 Mara 8.75 APROVADO\nMelhor: Mara (8.75)\n",
                    },
                    {
                        "in": "1\n55 Rui 6.5 5.5\n",
                        "out": "55 Rui 6.00 APROVADO\nMelhor: Rui (6.00)\n",
                    },
                ],
                "modelCode": (
                    "#include <stdio.h>\n"
                    "#include <stdlib.h>\n\n"
                    "typedef struct {\n"
                    "    int ra;\n"
                    "    char nome[40];\n"
                    "    double n1;\n"
                    "    double n2;\n"
                    "} Aluno;\n\n"
                    "int indiceMelhor(Aluno *turma, int n) {\n"
                    "    int i, best = 0;\n"
                    "    double bestMed = (turma[0].n1 + turma[0].n2) / 2.0;\n"
                    "    for (i = 1; i < n; i++) {\n"
                    "        double m = ((turma + i)->n1 + (turma + i)->n2) / 2.0;\n"
                    "        if (m > bestMed) {\n"
                    "            bestMed = m;\n"
                    "            best = i;\n"
                    "        }\n"
                    "    }\n"
                    "    return best;\n"
                    "}\n\n"
                    "int main(void) {\n"
                    "    int n, i, best;\n"
                    "    if (scanf(\"%d\", &n) != 1 || n <= 0) return 0;\n"
                    "    Aluno *turma = (Aluno *) malloc(n * sizeof(Aluno));\n"
                    "    if (turma == NULL) return 1;\n"
                    "    for (i = 0; i < n; i++) {\n"
                    "        scanf(\"%d %s %lf %lf\", &turma[i].ra, turma[i].nome, &turma[i].n1, &turma[i].n2);\n"
                    "    }\n"
                    "    for (i = 0; i < n; i++) {\n"
                    "        double m = (turma[i].n1 + turma[i].n2) / 2.0;\n"
                    "        if (m >= 6.0) {\n"
                    "            printf(\"%d %s %.2f APROVADO\\n\", turma[i].ra, turma[i].nome, m);\n"
                    "        } else {\n"
                    "            printf(\"%d %s %.2f REPROVADO\\n\", turma[i].ra, turma[i].nome, m);\n"
                    "        }\n"
                    "    }\n"
                    "    best = indiceMelhor(turma, n);\n"
                    "    double bestMed = (turma[best].n1 + turma[best].n2) / 2.0;\n"
                    "    printf(\"Melhor: %s (%.2f)\\n\", turma[best].nome, bestMed);\n"
                    "    free(turma);\n"
                    "    turma = NULL;\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "solutionNote": "Aloca Aluno *turma dinamicamente, usa (turma + i)->campo e turma[i].campo de forma equivalente, encontra o melhor índice e libera a memória no fim.",
            },
        ],
    },

    # =========================================================================
    # SIMULADO 3: Integração Completa (Arquivos + Structs + Ponteiros)
    # =========================================================================
    {
        "id": "sim-3",
        "title": "Simulado 3: Integração Completa (Arquivos + Structs + Ponteiros)",
        "subtitle": "Avaliação integradora estilo ATP: persistência texto e binária (FILE *), modos r/w/a/+/b, fread/fwrite, fseek/ftell/rewind e manipulação dinâmica de structs.",
        "durationSec": 7200,
        "questions": [
            {
                "id": "s3-q1",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Retorno de fopen e tratamento de falha",
                "prompt": "<p>Ao tentar abrir um arquivo inexistente com <code>FILE *fp = fopen(\"relatorio.txt\", \"r\");</code>, o que ocorre?</p>",
                "code": "",
                "options": [
                    "fopen cria um arquivo vazio automaticamente e retorna um ponteiro válido.",
                    "fopen retorna NULL, e o programa deve testar if (fp == NULL) antes de qualquer leitura ou fclose(fp).",
                    "fopen retorna EOF (-1).",
                    "O programa aborta automaticamente antes da linha seguinte.",
                    "fopen abre o arquivo em modo escrita como alternativa.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: apenas modos de criação (\"w\", \"a\", \"w+\", \"a+\") criam o arquivo se não existir.",
                    "Correta! O modo \"r\" exige existência prévia; em falha, retorna NULL e usar fread/fscanf/fclose sobre NULL causa falha grave.",
                    "Incorreta: EOF é retornado por funções como fgetc/fscanf, não por fopen (que retorna FILE *).",
                    "Incorreta: cabe ao programador checar fp == NULL.",
                    "Incorreta: fopen nunca troca o modo solicitado silenciosamente.",
                ],
            },
            {
                "id": "s3-q2",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Modos w, a, r+ e sincronização",
                "prompt": "<p>Assinale a afirmação <strong>CORRETA</strong> sobre modos de abertura de arquivos em C:</p>",
                "code": "",
                "options": [
                    "O modo \"w\" preserva o conteúdo antigo e escreve ao final do arquivo.",
                    "O modo \"a\" apaga o arquivo existente antes de escrever.",
                    "Em modo \"r+\", o arquivo precisa existir, permite leitura e escrita sem truncar, e exige fseek/fflush/rewind ao alternar entre ler e escrever.",
                    "Em modo \"a+\", fseek(fp, 0, SEEK_SET) permite sobrescrever o primeiro byte do arquivo.",
                    "O modo \"w+\" só permite escrita após fechar e reabrir em \"r\".",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: \"w\" trunca (zera) o arquivo existente.",
                    "Incorreta: \"a\" (append) preserva o conteúdo e adiciona no final.",
                    "Correta! \"r+\" abre para atualização sem apagar; pelo padrão C, alternar entrada e saída no mesmo stream exige reposicionamento ou descarga (fseek/fflush/rewind).",
                    "Incorreta: em modo append (\"a\" / \"a+\"), toda operação de escrita é forçada para o final do arquivo.",
                    "Incorreta: \"w+\" já permite leitura e escrita no mesmo stream (zerando na abertura).",
                ],
            },
            {
                "id": "s3-q3",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "A armadilha de while (!feof(fp))",
                "prompt": "<p>Por que o padrão <code>while (!feof(fp)) { fscanf(fp, \"%d\", &amp;x); printf(\"%d \", x); }</code> costuma imprimir o último número duas vezes?</p>",
                "code": "",
                "options": [
                    "Porque fscanf lê os números de trás para frente no último bloco.",
                    "Porque feof(fp) só retorna verdadeiro DEPOIS que uma tentativa de leitura ultrapassa o fim do arquivo; assim, após ler o último número válido, !feof(fp) ainda é verdadeiro para mais uma iteração.",
                    "Porque feof(fp) apaga o buffer do printf.",
                    "Porque o modo \"r\" duplica automaticamente a última linha no disco.",
                    "Porque &x não pode ser usado dentro de laço while.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: fscanf lê sequencialmente do início ao fim.",
                    "Correta! Após ler o último inteiro, o indicador EOF ainda não foi ligado. O laço entra mais uma vez, fscanf falha deixando x com o valor anterior, e printf o imprime repetido.",
                    "Incorreta: feof apenas consulta uma flag do stream.",
                    "Incorreta: não há duplicação no disco.",
                    "Incorreta: usar &x em fscanf dentro de while é padrão.",
                ],
            },
            {
                "id": "s3-q4",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "fgets vs fscanf em arquivos texto",
                "prompt": "<p>Comparando <code>fgets(linha, sizeof(linha), fp)</code> e <code>fscanf(fp, \"%s\", palavra)</code>, qual afirmação está <strong>CORRETA</strong>?</p>",
                "code": "",
                "options": [
                    "fscanf(\"%s\") lê espaços em branco até o fim da linha.",
                    "fgets() descarta o caractere '\\n' automaticamente antes de gravá-lo no buffer.",
                    "fgets() limita a leitura a sizeof(linha) - 1 caracteres, lê espaços e preserva o '\\n' caso caiba no buffer.",
                    "fgets() retorna 1 quando lê uma linha e 0 quando falha.",
                    "fscanf(\"%s\") protege contra buffer overflow sem especificar largura máxima.",
                ],
                "correct": 2,
                "explanations": [
                    "Incorreta: %s para no primeiro caractere de espaço em branco (' ', '\\t', '\\n').",
                    "Incorreta: diferente do antigo gets, fgets mantém o '\\n' lido na string.",
                    "Correta! fgets é seguro contra estouro de buffer, aceita espaços e inclui o '\\n' antes do '\\0' (retornando NULL no EOF/erro).",
                    "Incorreta: fgets retorna o próprio ponteiro linha em sucesso, ou NULL em EOF/erro.",
                    "Incorreta: sem largura máxima (ex.: %39s), %s pode estourar o vetor.",
                ],
            },
            {
                "id": "s3-q5",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Arquivos binários no Windows (\"rb\" / \"wb\")",
                "prompt": "<p>Ao gravar structs com <code>fwrite</code> no Windows usando modo <code>\"w\"</code> (sem o <code>\"b\"</code>), qual problema pode ocorrer?</p>",
                "code": "",
                "options": [
                    "O compilador recusa passar um ponteiro FILE * para fwrite.",
                    "Bytes iguais a 0x0A ('\\n') dentro da struct são traduzidos para 0x0D 0x0A ('\\r\\n') e 0x1A pode ser tratado como EOF na leitura em modo texto, corrompendo os registros.",
                    "A struct é gravada em JSON automaticamente.",
                    "Os ponteiros internos são convertidos para texto legível.",
                    "Não há nenhuma diferença entre \"w\" e \"wb\" no Windows.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: não há erro de compilação ao passar FILE * aberto com \"w\".",
                    "Correta! Em modo texto no Windows ocorre tradução de quebra de linha e interpretação de Ctrl+Z (0x1A), corrompendo dados binários arbitrários.",
                    "Incorreta: fwrite sempre escreve bytes brutos.",
                    "Incorreta: fwrite nunca serializa ponteiros para texto.",
                    "Incorreta: a diferença existe exatamente no Windows por conta de CR/LF e 0x1A.",
                ],
            },
            {
                "id": "s3-q6",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Valor de retorno de fread",
                "prompt": "<p>Um arquivo binário contém exatamente 5 structs <code>Produto</code> (cada uma com 48 bytes). Ao executar <code>size_t r = fread(vet, sizeof(Produto), 10, fp);</code> no início do arquivo, quanto vale <code>r</code>?</p>",
                "code": "",
                "options": [
                    "240",
                    "480",
                    "10",
                    "5",
                    "1",
                ],
                "correct": 3,
                "explanations": [
                    "Incorreta: 240 é o total de bytes lidos (5 * 48), mas fread retorna quantidade de itens.",
                    "Incorreta: 480 seria 10 * 48 bytes.",
                    "Incorreta: 10 era o máximo pedido, mas só existiam 5 registros no arquivo.",
                    "Correta! fread retorna a quantidade de elementos completos (do tamanho sizeof(Produto)) lidos com sucesso: 5.",
                    "Incorreta: só retornaria 1 se apenas 1 registro existisse ou fosse solicitado.",
                ],
            },
            {
                "id": "s3-q7",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Struct com char * em fwrite",
                "prompt": "<p>Por que é um erro grave usar <code>fwrite(&amp;cli, sizeof(Cliente), 1, fp)</code> quando <code>Cliente</code> tem um campo <code>char *nome;</code> alocado com <code>malloc</code>?</p>",
                "code": "",
                "options": [
                    "Porque sizeof(Cliente) sempre retorna zero se houver ponteiro.",
                    "Porque fwrite grava apenas os bytes do endereço guardado em nome (ponteiro), não os caracteres da string; em outra execução esse endereço será inválido.",
                    "Porque fwrite ignora campos do tipo char * e pula para o próximo campo.",
                    "Porque ponteiros não podem existir dentro de structs em C.",
                    "Porque fread converte char * para int automaticamente.",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: sizeof inclui o tamanho do ponteiro (4 ou 8 bytes).",
                    "Correta! fwrite copia apenas os bytes da struct contígua. Um char * contém um endereço de RAM, não o texto; ao recarregar depois, o ponteiro aponta para lixo (dangling pointer).",
                    "Incorreta: ela copia os bytes do ponteiro normalmente, o que gera o problema lógico.",
                    "Incorreta: ponteiros em struct são comuns, mas exigem serialização campo a campo ao gravar em arquivo.",
                    "Incorreta: fread apenas restaura os bytes crus do endereço antigo.",
                ],
            },
            {
                "id": "s3-q8",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Descobrindo total de registros com fseek e ftell",
                "prompt": "<p>Para descobrir quantos registros <code>Aluno</code> existem em um arquivo binário aberto em <code>\"rb\"</code> e retornar ao início para lê-los, qual sequência está <strong>CORRETA</strong>?</p>",
                "code": "",
                "options": [
                    "fseek(fp, 0, SEEK_END); long qtd = ftell(fp) / sizeof(Aluno); rewind(fp);",
                    "rewind(fp); long qtd = ftell(fp) * sizeof(Aluno);",
                    "fseek(fp, 0, SEEK_SET); long qtd = ftell(fp) / sizeof(Aluno);",
                    "fseek(fp, sizeof(Aluno), SEEK_CUR); long qtd = feof(fp);",
                    "long qtd = sizeof(fp) / sizeof(Aluno);",
                ],
                "correct": 0,
                "explanations": [
                    "Correta! SEEK_END leva ao fim, ftell(fp) fornece o tamanho total em bytes, dividindo por sizeof(Aluno) obtém-se a quantidade de registros, e rewind(fp) volta ao byte 0.",
                    "Incorreta: após rewind, ftell retorna 0.",
                    "Incorreta: SEEK_SET posiciona no início (0 bytes).",
                    "Incorreta: feof retorna apenas indicador booleano de fim de arquivo, não quantidade.",
                    "Incorreta: sizeof(fp) é apenas o tamanho de um ponteiro FILE * (4 ou 8 bytes).",
                ],
            },
            {
                "id": "s3-q9",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Acesso direto com fseek e SEEK_SET",
                "prompt": "<p>Deseja-se ler diretamente o <strong>4º registro</strong> (índice 3, base 0) de um arquivo binário de structs <code>Conta</code> aberto em <code>\"rb\"</code>. Qual chamada posiciona o cursor corretamente?</p>",
                "code": "",
                "options": [
                    "fseek(fp, 4 * (long)sizeof(Conta), SEEK_SET);",
                    "fseek(fp, 3 * (long)sizeof(Conta), SEEK_SET);",
                    "fseek(fp, 3, SEEK_SET);",
                    "fseek(fp, 3 * (long)sizeof(Conta), SEEK_END);",
                    "rewind(fp + 3);",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: 4 * sizeof(Conta) pula os 4 primeiros (índices 0, 1, 2, 3), apontando para o 5º registro.",
                    "Correta! Os registros ficam nos offsets 0, 1*tam, 2*tam, 3*tam a partir de SEEK_SET; logo o 4º registro (índice 3) começa em 3 * sizeof(Conta).",
                    "Incorreta: desloca apenas 3 bytes, não 3 registros.",
                    "Incorreta: offset positivo a partir de SEEK_END vai além do fim do arquivo.",
                    "Incorreta: aritmética em ponteiro FILE * é totalmente inválida.",
                ],
            },
            {
                "id": "s3-q10",
                "part": 1,
                "type": "mcq",
                "points": 0.5,
                "title": "Importância de fclose e fflush",
                "prompt": "<p>O que pode ocorrer se um programa gravar dados com <code>fprintf</code> ou <code>fwrite</code> e encerrar abruptamente ou abrir o mesmo arquivo novamente sem chamar <code>fclose(fp)</code>?</p>",
                "code": "",
                "options": [
                    "Nada ocorre, pois C não utiliza buffer em operações de arquivo.",
                    "Os dados ainda retidos no buffer em RAM podem não ser descarregados para o disco (perda de dados) e o descritor de arquivo permanece vazando.",
                    "O arquivo é criptografado automaticamente pelo sistema operacional.",
                    "O conteúdo do arquivo é dobrado na memória.",
                    "fclose só é necessário em arquivos abertos com \"r\".",
                ],
                "correct": 1,
                "explanations": [
                    "Incorreta: streams FILE * de <stdio.h> são bufferizados por padrão para desempenho.",
                    "Correta! fclose(fp) descarrega (flush) o buffer pendente para o disco e libera o descritor do sistema.",
                    "Incorreta: não há criptografia envolvida.",
                    "Incorreta: não há duplicação.",
                    "Incorreta: fechar arquivos é ainda mais crítico após escrita devido ao buffer.",
                ],
            },
            {
                "id": "s3-q11",
                "part": 2,
                "type": "trace",
                "points": 1.0,
                "title": "Teste de mesa: Gravação e releitura em arquivo texto",
                "prompt": "<p>Rastreie o programa abaixo que cria o arquivo <code>log.txt</code>, fecha, reabre para leitura e totaliza os registros.</p>",
                "code": (
                    "#include <stdio.h>\n"
                    "\n"
                    "int main(void) {\n"
                    "    FILE *fp = fopen(\"log.txt\", \"w\");\n"
                    "    fprintf(fp, \"%d %.1f\\n\", 1, 8.0);\n"
                    "    fprintf(fp, \"%d %.1f\\n\", 2, 6.5);\n"
                    "    fclose(fp);\n"
                    "\n"
                    "    fp = fopen(\"log.txt\", \"r\");\n"
                    "    int id, cont = 0;\n"
                    "    double nota, soma = 0.0;\n"
                    "    while (fscanf(fp, \"%d %lf\", &id, &nota) == 2) {\n"
                    "        soma += nota;\n"
                    "        cont++;\n"
                    "    }\n"
                    "    fclose(fp);\n"
                    "    printf(\"Qtd=%d Soma=%.1f\\n\", cont, soma);\n"
                    "    return 0;\n"
                    "}"
                ),
                "partAPrompt": "Parte A (0,6 pt): Qual é a saída exata impressa no console (stdout)?",
                "partAPoints": 0.6,
                "expectedOutput": "Qtd=2 Soma=14.5\n",
                "partBPrompt": "Parte B (0,4 pt): Explique por que o programa fecha o arquivo antes de reabrir em \"r\" e por que testa fscanf(...) == 2 em vez de !feof(fp).",
                "partBPoints": 0.4,
                "partBKeywords": ["buffer", "fclose", "feof", "duplicar", "retorno", "leitura"],
                "partBModel": "fclose(fp) descarrega o buffer de escrita no disco e encerra o modo \"w\" antes de reabrir em \"r\" no início do arquivo. Já testar fscanf(...) == 2 garante que ambos os campos foram lidos com sucesso, evitando a leitura duplicada no fim do arquivo causada por while (!feof(fp)).",
                "traceSteps": [
                    {"line": 4, "vars": {"fp": "aberto (w)"}, "note": "Abre log.txt em modo escrita (cria ou zera)."},
                    {"line": 5, "vars": {"arquivo": "\"1 8.0\\n\""}, "note": "Grava primeiro registro no stream."},
                    {"line": 6, "vars": {"arquivo": "\"1 8.0\\n2 6.5\\n\""}, "note": "Grava segundo registro no stream."},
                    {"line": 7, "vars": {"fp": "fechado"}, "note": "fclose descarrega o buffer e fecha log.txt."},
                    {"line": 9, "vars": {"fp": "aberto (r)"}, "note": "Reabre log.txt no início em modo leitura."},
                    {"line": 12, "vars": {"id": "1", "nota": "8.0", "soma": "8.0", "cont": "1"}, "note": "1ª iteração: fscanf retorna 2, soma = 8.0, cont = 1."},
                    {"line": 13, "vars": {"id": "2", "nota": "6.5", "soma": "14.5", "cont": "2"}, "note": "2ª iteração: fscanf retorna 2, soma = 14.5, cont = 2; na 3ª tentativa retorna EOF e encerra."},
                    {"line": 17, "vars": {"cont": "2", "soma": "14.5"}, "note": "printf imprime 'Qtd=2 Soma=14.5'."},
                ],
            },
            {
                "id": "s3-q12",
                "part": 2,
                "type": "bughunt",
                "points": 1.0,
                "title": "Caça aos Bugs: Struct + Arquivo Binário",
                "prompt": "<p>O programa abaixo deveria ler registros <code>Item</code> do arquivo binário <code>itens.bin</code> e imprimi-los. Identifique os <strong>4 bugs</strong>.</p>",
                "numberedCode": [
                    "#include <stdio.h>",
                    "#include <stdlib.h>",
                    "",
                    "typedef struct {",
                    "    int id;",
                    "    char *nome;",
                    "    double preco;",
                    "} Item;",
                    "",
                    "int main(void) {",
                    "    FILE *fp = fopen(\"itens.bin\", \"r\");",
                    "    Item it;",
                    "    while (!feof(fp)) {",
                    "        if (fread(&it, sizeof(Item), 1, fp) == sizeof(Item)) {",
                    "            printf(\"%d %s %.2f\\n\", it.id, it.nome, it.preco);",
                    "        }",
                    "    }",
                    "    return 0;",
                    "}",
                ],
                "bugs": [
                    {
                        "line": 6,
                        "altLines": [],
                        "problem": "Campo char *nome é um ponteiro: fread/fwrite binário lê/grava apenas um endereço inválido em vez do texto.",
                        "fix": "char nome[40];",
                        "keywords": ["char *", "ponteiro", "array", "nome", "fixo"],
                    },
                    {
                        "line": 11,
                        "altLines": [],
                        "problem": "Abriu arquivo binário em modo texto \"r\" em vez de \"rb\" e não verificou se fp == NULL.",
                        "fix": "FILE *fp = fopen(\"itens.bin\", \"rb\"); if (fp == NULL) return 1;",
                        "keywords": ["rb", "binario", "null", "fopen"],
                    },
                    {
                        "line": 13,
                        "altLines": [],
                        "problem": "Uso da armadilha while (!feof(fp)) antes da leitura.",
                        "fix": "while (fread(&it, sizeof(Item), 1, fp) == 1) {",
                        "keywords": ["feof", "while", "fread"],
                    },
                    {
                        "line": 14,
                        "altLines": [],
                        "problem": "Comparou retorno de fread com sizeof(Item); fread retorna número de itens (1), não bytes (além de faltar fclose(fp) antes do return).",
                        "fix": "Comparar fread(...) == 1 diretamente no while e chamar fclose(fp); antes de return 0;",
                        "keywords": ["sizeof", "== 1", "itens", "bytes", "fclose"],
                    },
                ],
            },
            {
                "id": "s3-q13",
                "part": 2,
                "type": "step_code",
                "points": 1.0,
                "title": "Implementação Guiada: Persistência em Arquivo Texto",
                "prompt": "<p>Responda à Parte A conceitual e implemente o programa completo na Parte B.</p>",
                "partAPrompt": "Parte A (0,4 pt): Por que é indispensável fechar o arquivo com fclose(fp) após gravar em \"w\" antes de reabri-lo em \"r\", e qual condição correta deve controlar o while com fscanf?",
                "partAPoints": 0.4,
                "partAKeywords": ["fclose", "buffer", "flush", "fscanf", "retorno", "feof"],
                "partAModel": "fclose(fp) descarrega o buffer de escrita no disco e libera o stream para que a abertura seguinte em \"r\" leia todos os dados desde o início. No laço de leitura, deve-se testar while (fscanf(...) == 3) em vez de while (!feof(fp)).",
                "partBPrompt": "Parte B (0,6 pt): Leia n, depois n registros (int id; char nome[40]; double nota;). Grave-os no arquivo 'notas.txt' com fopen(\"notas.txt\", \"w\") e fprintf, feche com fclose, reabra com \"r\", leia todos com while (fscanf(fp, \"%d %s %lf\", &id, nome, &nota) == 3), conte aprovados (nota >= 6.0) e calcule a média geral, imprimindo 'Aprovados: <qtd> | Media: <media:.2f>'.",
                "partBPoints": 0.6,
                "ioExample": "Entrada:\n3\n1 Ana 8.0\n2 Bruno 5.0\n3 Carla 8.0\n\nSaída:\nAprovados: 2 | Media: 7.00",
                "starter": (
                    "#include <stdio.h>\n\n"
                    "int main(void) {\n"
                    "    int n, i, id, aprovados = 0, total = 0;\n"
                    "    char nome[40];\n"
                    "    double nota, soma = 0.0;\n"
                    "    // 1. Leia n e grave os n registros em notas.txt (\"w\")\n"
                    "    // 2. Feche e reabra notas.txt (\"r\")\n"
                    "    // 3. Leia com fscanf == 3, calcule aprovados e media, feche e imprima\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "tests": [
                    {
                        "in": "3\n1 Ana 8.0\n2 Bruno 5.0\n3 Carla 8.0\n",
                        "out": "Aprovados: 2 | Media: 7.00\n",
                    },
                    {
                        "in": "2\n10 Joao 4.5\n20 Maria 5.5\n",
                        "out": "Aprovados: 0 | Media: 5.00\n",
                    },
                    {
                        "in": "4\n1 A 6.0\n2 B 7.0\n3 C 8.0\n4 D 9.0\n",
                        "out": "Aprovados: 4 | Media: 7.50\n",
                    },
                ],
                "modelCode": (
                    "#include <stdio.h>\n\n"
                    "int main(void) {\n"
                    "    int n, i, id, aprovados = 0, total = 0;\n"
                    "    char nome[40];\n"
                    "    double nota, soma = 0.0;\n"
                    "    if (scanf(\"%d\", &n) != 1 || n <= 0) return 0;\n\n"
                    "    FILE *fp = fopen(\"notas.txt\", \"w\");\n"
                    "    if (fp == NULL) return 1;\n"
                    "    for (i = 0; i < n; i++) {\n"
                    "        scanf(\"%d %s %lf\", &id, nome, &nota);\n"
                    "        fprintf(fp, \"%d %s %.2f\\n\", id, nome, nota);\n"
                    "    }\n"
                    "    fclose(fp);\n\n"
                    "    fp = fopen(\"notas.txt\", \"r\");\n"
                    "    if (fp == NULL) return 1;\n"
                    "    while (fscanf(fp, \"%d %s %lf\", &id, nome, &nota) == 3) {\n"
                    "        soma += nota;\n"
                    "        total++;\n"
                    "        if (nota >= 6.0) {\n"
                    "            aprovados++;\n"
                    "        }\n"
                    "    }\n"
                    "    fclose(fp);\n\n"
                    "    printf(\"Aprovados: %d | Media: %.2f\\n\", aprovados, soma / total);\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "solutionNote": "O programa gera notas.txt a partir da entrada padrão, fecha o stream, reabre em \"r\" e usa o retorno == 3 de fscanf para evitar leitura duplicada.",
            },
            {
                "id": "s3-q14",
                "part": 2,
                "type": "code",
                "points": 2.0,
                "title": "Integração Completa: Estoque Dinâmico em Arquivo Binário",
                "prompt": (
                    "<p>Escreva um programa integrador em C unindo <strong>structs, alocação dinâmica, ponteiros e arquivo binário</strong>:</p>"
                    "<ol>"
                    "<li>Defina <code>typedef struct { int codigo; char nome[40]; double preco; int qtd; } Produto;</code> (sem ponteiros internos).</li>"
                    "<li>Leia <code>n</code> (&gt;= 1), aloque dinamicamente <code>Produto *vet = malloc(n * sizeof(Produto))</code> e leia <code>codigo nome preco qtd</code> para cada item.</li>"
                    "<li>Grave todos os registros em <code>\"estoque.bin\"</code> usando <code>fopen(\"estoque.bin\", \"wb\")</code> e <code>fwrite</code>, feche o arquivo e libere <code>vet</code>.</li>"
                    "<li>Reabra <code>\"estoque.bin\"</code> em modo <code>\"rb\"</code>, leia registro por registro com <code>while (fread(&amp;p, sizeof(Produto), 1, fp) == 1)</code>, calcule o valor total do estoque (<code>soma(preco * qtd)</code>) e descubra o produto de maior valor em estoque (<code>preco * qtd</code>).</li>"
                    "<li>Feche o arquivo e imprima exatamente em duas linhas:<br>"
                    "<code>Total: R$ &lt;total:.2f&gt;</code><br>"
                    "<code>Mais valioso: &lt;nome&gt; (R$ &lt;valor:.2f&gt;)</code></li>"
                    "</ol>"
                ),
                "ioExample": "Entrada:\n2\n10 Mouse 50.00 4\n20 Monitor 500.00 2\n\nSaída:\nTotal: R$ 1200.00\nMais valioso: Monitor (R$ 1000.00)",
                "starter": (
                    "#include <stdio.h>\n"
                    "#include <stdlib.h>\n"
                    "#include <string.h>\n\n"
                    "typedef struct {\n"
                    "    int codigo;\n"
                    "    char nome[40];\n"
                    "    double preco;\n"
                    "    int qtd;\n"
                    "} Produto;\n\n"
                    "int main(void) {\n"
                    "    // 1. Leia n, aloque vet, leia produtos\n"
                    "    // 2. Grave em estoque.bin (\"wb\"), feche e libere vet\n"
                    "    // 3. Reabra em \"rb\", leia com fread == 1, calcule total e mais valioso, feche e imprima\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "tests": [
                    {
                        "in": "2\n10 Mouse 50.00 4\n20 Monitor 500.00 2\n",
                        "out": "Total: R$ 1200.00\nMais valioso: Monitor (R$ 1000.00)\n",
                    },
                    {
                        "in": "3\n1 Cabo 15.00 10\n2 Teclado 120.00 3\n3 SSD 250.00 1\n",
                        "out": "Total: R$ 760.00\nMais valioso: Teclado (R$ 360.00)\n",
                    },
                    {
                        "in": "1\n99 Notebook 3500.50 2\n",
                        "out": "Total: R$ 7001.00\nMais valioso: Notebook (R$ 7001.00)\n",
                    },
                ],
                "modelCode": (
                    "#include <stdio.h>\n"
                    "#include <stdlib.h>\n"
                    "#include <string.h>\n\n"
                    "typedef struct {\n"
                    "    int codigo;\n"
                    "    char nome[40];\n"
                    "    double preco;\n"
                    "    int qtd;\n"
                    "} Produto;\n\n"
                    "int main(void) {\n"
                    "    int n, i;\n"
                    "    if (scanf(\"%d\", &n) != 1 || n <= 0) return 0;\n\n"
                    "    Produto *vet = (Produto *) malloc(n * sizeof(Produto));\n"
                    "    if (vet == NULL) return 1;\n\n"
                    "    for (i = 0; i < n; i++) {\n"
                    "        scanf(\"%d %s %lf %d\", &(vet + i)->codigo, (vet + i)->nome, &(vet + i)->preco, &(vet + i)->qtd);\n"
                    "    }\n\n"
                    "    FILE *fp = fopen(\"estoque.bin\", \"wb\");\n"
                    "    if (fp == NULL) {\n"
                    "        free(vet);\n"
                    "        return 1;\n"
                    "    }\n"
                    "    fwrite(vet, sizeof(Produto), n, fp);\n"
                    "    fclose(fp);\n"
                    "    free(vet);\n"
                    "    vet = NULL;\n\n"
                    "    fp = fopen(\"estoque.bin\", \"rb\");\n"
                    "    if (fp == NULL) return 1;\n\n"
                    "    Produto p;\n"
                    "    double total = 0.0, maxVal = -1.0;\n"
                    "    char melhorNome[40] = \"\";\n\n"
                    "    while (fread(&p, sizeof(Produto), 1, fp) == 1) {\n"
                    "        double sub = p.preco * p.qtd;\n"
                    "        total += sub;\n"
                    "        if (sub > maxVal) {\n"
                    "            maxVal = sub;\n"
                    "            strcpy(melhorNome, p.nome);\n"
                    "        }\n"
                    "    }\n"
                    "    fclose(fp);\n\n"
                    "    printf(\"Total: R$ %.2f\\n\", total);\n"
                    "    printf(\"Mais valioso: %s (R$ %.2f)\\n\", melhorNome, maxVal);\n"
                    "    return 0;\n"
                    "}\n"
                ),
                "solutionNote": "Integra array fixo char nome[40] na struct para serialização binária segura, alocação dinâmica via malloc/free, escrita em \"wb\" com fwrite e leitura em \"rb\" testando fread(...) == 1.",
            },
        ],
    },
]
