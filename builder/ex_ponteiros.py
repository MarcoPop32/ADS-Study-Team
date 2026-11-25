"""Exercícios (30 MCQs, 10 Certo/Errado e 2 Clássicos) do Módulo 1 — Ponteiros."""
from __future__ import annotations

MCQ_PONTEIROS = [
    {
        "id": "q-ptr-1",
        "category": "ponteiros",
        "subtopic": "1.1 Conceito e RAM",
        "level": "Básico",
        "title": "Natureza de um ponteiro na memória RAM",
        "stem": "Em uma máquina de 64 bits onde int ocupa 4 bytes e ponteiros ocupam 8 bytes, considere: int x = 42; int *p = &x;. O que está armazenado diretamente nos bytes pertencentes à variável p?",
        "code": "int x = 42;\nint *p = &x;",
        "options": [
            "Uma cópia do valor inteiro 42 ocupando 4 bytes.",
            "O endereço de memória do primeiro byte ocupado pela variável x.",
            "A soma dos 4 bytes que compõem a variável x.",
            "O endereço do último byte de x somado a sizeof(int).",
            "Apenas o identificador textual \"x\" na tabela de símbolos."
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: p armazena o endereço inicial (primeiro byte) de x na RAM.",
        "steps": [
            "Em C, cada variável ocupa um bloco contíguo de bytes na RAM e é identificada pelo endereço do seu menor byte (primeiro byte).",
            "O operador & retorna o endereço inicial de x, que é gravado como conteúdo dentro dos 8 bytes da variável ponteiro p."
        ],
        "optionExplanations": [
            "Incorreta: p não duplica o valor 42; ele guarda um endereço.",
            "Correta: ponteiros armazenam endereços de memória, especificamente o endereço do primeiro byte do objeto apontado.",
            "Incorreta: endereços não são somas dos conteúdos dos bytes.",
            "Incorreta: o endereço de um objeto é sempre o de seu primeiro byte, não o último + sizeof.",
            "Incorreta: em tempo de execução em C compilado, ponteiros guardam endereços numéricos, não nomes de variáveis."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x;
    printf("Endereco de x = %p, conteudo de p = %p\\n", (void *)&x, (void *)p);
    return 0;
}"""
    },
    {
        "id": "q-ptr-2",
        "category": "ponteiros",
        "subtopic": "1.2 Operadores & e *",
        "level": "Básico",
        "title": "Leitura e escrita com & e *",
        "stem": "Qual será a saída exata impressa pelo programa em C abaixo?",
        "code": """#include <stdio.h>
int main(void) {
    int a = 5, b = 12;
    int *p = &a;
    *p = *p + b;
    p = &b;
    *p = a - 2;
    printf("%d %d", a, b);
    return 0;
}""",
        "options": [
            "5 12",
            "17 12",
            "17 15",
            "5 15",
            "12 10"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: a vira 17 e em seguida b recebe 17 - 2 = 15.",
        "steps": [
            "Inicialmente p aponta para a (5). A linha *p = *p + b calcula 5 + 12 = 17 e grava em a.",
            "Depois p = &b redireciona p para b. A linha *p = a - 2 calcula 17 - 2 = 15 e grava em b."
        ],
        "optionExplanations": [
            "Incorreta: tanto a quanto b são modificados via *p.",
            "Incorreta: b também é alterado na linha *p = a - 2 após p apontar para &b.",
            "Correta: a passa a valer 17 na 1ª escrita indireta e b passa a valer 15 na 2ª.",
            "Incorreta: a foi atualizado antes de p ser redirecionado para &b.",
            "Incorreta: *p + b soma 5 + 12 = 17, não substitui por 12."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int a = 5, b = 12;
    int *p = &a;
    *p = *p + b; /* a = 17 */
    p = &b;
    *p = a - 2;  /* b = 15 */
    printf("%d %d\\n", a, b);
    return 0;
}"""
    },
    {
        "id": "q-ptr-3",
        "category": "ponteiros",
        "subtopic": "1.2 Operadores & e *",
        "level": "Básico",
        "title": "Identidade entre * e &",
        "stem": "Considerando int k = 9; int *ptr = &k;, qual das expressões abaixo NÃO equivale ao valor 9 nem compila como alternativa válida para obter k?",
        "code": "int k = 9;\nint *ptr = &k;",
        "options": [
            "*&k",
            "*ptr",
            "&*ptr == &k ? 9 : 0",
            "&*k",
            "*( &k )"
        ],
        "correct": 3,
        "gabaritoResumo": "Letra D: &*k é inválido pois k não é ponteiro para ser desreferenciado com *.",
        "steps": [
            "Em &*k, o operador unário * é aplicado primeiro a k (da direita para a esquerda).",
            "Como k é int (e não ponteiro), *k gera erro de compilação (invalid type argument of unary '*')."
        ],
        "optionExplanations": [
            "Incorreta: *&k aplica & (endereço) e depois * (desreferencia), resultando em k (9).",
            "Incorreta: *ptr acessa o valor apontado k (9).",
            "Incorreta: &*ptr equivale a ptr, que é igual a &k, logo a expressão ternária resulta em 9.",
            "Correta: k é inteiro comum, portanto *k é inválido em C.",
            "Incorreta: *(&k) é idêntico a *&k, resultando em 9."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int k = 9;
    int *ptr = &k;
    printf("%d %d %d\\n", *&k, *ptr, *(&k));
    return 0;
}"""
    },
    {
        "id": "q-ptr-4",
        "category": "ponteiros",
        "subtopic": "1.3 Declaração e inicialização",
        "level": "Básico",
        "title": "Armadilha na declaração múltipla de ponteiros",
        "stem": "Considere a linha em C: int* a, b; seguida de int x = 10;. Sobre os tipos reais de 'a' e 'b' definidos pelo compilador, assinale a alternativa correta.",
        "code": "int* a, b;",
        "options": [
            "Tanto 'a' quanto 'b' são ponteiros para int (int *).",
            "'a' é um ponteiro para int (int *), mas 'b' é uma variável int comum.",
            "'a' é int comum e 'b' é ponteiro para int (int *).",
            "A sintaxe int* a, b; é proibida pelo padrão ISO C e não compila.",
            "Ambos são ponteiros genéricos void * até serem inicializados."
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: o asterisco vincula-se apenas ao declarador 'a', deixando 'b' como int.",
        "steps": [
            "Na gramática de C, o modificador * pertence ao declarador individual, e não ao especificador de tipo base int.",
            "Portanto, int* a, b; é interpretado exatamente como int *a; int b;. Para dois ponteiros, escreve-se int *a, *b;."
        ],
        "optionExplanations": [
            "Incorreta: b não possui asterisco na frente, logo não é ponteiro.",
            "Correta: apenas a é int *, enquanto b é um int simples.",
            "Incorreta: é o inverso (a tem *, b não tem).",
            "Incorreta: a sintaxe compila perfeitamente em C, sendo justamente uma armadilha famosa.",
            "Incorreta: C possui tipagem estática; o tipo é decidido na compilação."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int x = 10;
    int *a = &x, *b = &x; /* ambos ponteiros */
    printf("%d %d\\n", *a, *b);
    return 0;
}"""
    },
    {
        "id": "q-ptr-5",
        "category": "ponteiros",
        "subtopic": "1.3 Declaração e inicialização",
        "level": "Básico",
        "title": "Por que o tipo do ponteiro importa",
        "stem": "Em uma arquitetura de 64 bits, sizeof(char *), sizeof(int *) e sizeof(double *) valem todos 8 bytes. Por que, mesmo assim, C exige ponteiros tipados em vez de usar apenas um tipo único de ponteiro?",
        "options": [
            "Porque ponteiros para double ocupam mais registradores na CPU que ponteiros para char.",
            "Porque o tipo base informa quantos bytes ler/escrever em *p e o passo em bytes da aritmética p + 1.",
            "Porque ponteiros char * só podem apontar para memória Heap, e int * apenas para a Stack.",
            "Porque apenas ponteiros int * podem receber o valor NULL.",
            "Porque sizeof(p) varia dinamicamente conforme o valor apontado."
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: o tipo determina quantos bytes *p acessa e o salto de p + 1.",
        "steps": [
            "Todos os ponteiros de dados guardam um endereço de memória (geralmente 8 bytes em 64 bits).",
            "O tipo base (char, int, double) define como interpretar os bytes a partir daquele endereço (1, 4 ou 8 bytes) e quanto avançar em p++."
        ],
        "optionExplanations": [
            "Incorreta: endereços têm a mesma largura de barramento.",
            "Correta: tamanho de leitura/escrita na desreferenciação e escala da aritmética dependem do tipo base.",
            "Incorreta: qualquer tipo de ponteiro pode apontar para Stack, Heap ou dados globais.",
            "Incorreta: qualquer ponteiro em C pode ser inicializado com NULL.",
            "Incorreta: sizeof de um ponteiro é constante em tempo de compilação."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    char c = 'Z';
    double d = 2.5;
    char *pc = &c;
    double *pd = &d;
    printf("sizeof(pc)=%zu, sizeof(*pc)=%zu, sizeof(*pd)=%zu\\n",
           sizeof(pc), sizeof(*pc), sizeof(*pd));
    return 0;
}"""
    },
    {
        "id": "q-ptr-6",
        "category": "ponteiros",
        "subtopic": "1.4 Ponteiros não inicializados e NULL",
        "level": "Básico",
        "title": "Ponteiro selvagem (lixo) versus NULL",
        "stem": "Analise o trecho de código abaixo dentro de uma função e assinale a afirmação correta sobre seu comportamento:",
        "code": """void exemplo(void) {
    int *p;
    if (p != NULL) {
        *p = 10;
    }
}""",
        "options": [
            "É totalmente seguro, pois variáveis locais do tipo ponteiro são automaticamente inicializadas com NULL em C.",
            "O teste if (p != NULL) evita qualquer falha, pois lixo de memória sempre é convertido para NULL.",
            "Há risco grave de Comportamento Indefinido / Segmentation Fault, pois p contém lixo de memória e quase nunca será NULL.",
            "Não compila porque C proíbe comparar ponteiros com NULL.",
            "O compilador aloca um inteiro automaticamente na Stack quando *p = 10 é executado."
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: p local não inicializado contém lixo (raramente NULL), passando pelo if e desreferenciando endereço inválido.",
        "steps": [
            "Variáveis locais automáticas (sem static) não são inicializadas pelo compilador em C; p nasce com bits residuais da Stack.",
            "Como esses bits aleatórios dificilmente são zero (NULL), p != NULL avalia como verdadeiro e *p = 10 escreve em endereço desconhecido."
        ],
        "optionExplanations": [
            "Incorreta: apenas variáveis globais ou static recebem inicialização implícita zero/NULL.",
            "Incorreta: lixo de memória não vira NULL; ele passa no teste p != NULL.",
            "Correta: é o clássico wild pointer causando Undefined Behavior.",
            "Incorreta: comparar ponteiro com NULL é padrão e recomendado após inicialização explícita.",
            "Incorreta: C nunca aloca memória automaticamente ao desreferenciar um ponteiro."
        ],
        "solutionCode": """#include <stdio.h>

void exemplo_seguro(void) {
    int *p = NULL;
    if (p != NULL) {
        *p = 10;
    } else {
        printf("Ponteiro nulo verificado com seguranca.\\n");
    }
}

int main(void) {
    exemplo_seguro();
    return 0;
}"""
    },
    {
        "id": "q-ptr-7",
        "category": "ponteiros",
        "subtopic": "1.5 Impressão de endereços (%p)",
        "level": "Básico",
        "title": "Uso correto de printf com %p",
        "stem": "De acordo com o padrão ISO C (C99/C11), qual chamada de printf está estritamente em conformidade para imprimir o endereço armazenado em double *pd?",
        "code": "double d = 3.14;\ndouble *pd = &d;",
        "options": [
            "printf(\"%d\", pd);",
            "printf(\"%p\", pd);",
            "printf(\"%p\", (void *)pd);",
            "printf(\"%x\", *pd);",
            "printf(\"%p\", (void *)*pd);"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: %p exige exatamente um argumento convertido para void *.",
        "steps": [
            "Em funções variádicas como printf, não há conversão implícita de double * para void *.",
            "O padrão ISO C define que o especificador %p espera um ponteiro do tipo void *, portanto o cast (void *)pd é obrigatório."
        ],
        "optionExplanations": [
            "Incorreta: %d espera int e trunca ponteiros de 64 bits (UB).",
            "Incorreta: passar double * sem cast (void *) viola o padrão para %p (-Wformat).",
            "Correta: (void *)pd atende exatamente ao contrato de %p.",
            "Incorreta: *pd é um double (3.14), não um endereço.",
            "Incorreta: não se pode converter um double (*pd) para (void *)."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    double d = 3.14;
    double *pd = &d;
    printf("Endereco: %p\\n", (void *)pd);
    return 0;
}"""
    },
    {
        "id": "q-ptr-8",
        "category": "ponteiros",
        "subtopic": "1.5 Impressão de endereços (%p)",
        "level": "Intermediário",
        "title": "Comparando endereços: &x, p e &p",
        "stem": "Suponha que x esteja no endereço 0x1000 e p (declarado como int *p = &x;) esteja no endereço 0x1008. O que imprime printf(\"%p %p\", (void *)p, (void *)&p);?",
        "code": "int x = 10;\nint *p = &x;\nprintf(\"%p %p\", (void *)p, (void *)&p);",
        "options": [
            "0x1000 0x1000",
            "0x1008 0x1000",
            "0x1000 0x1008",
            "10 0x1000",
            "0x1008 0x1008"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: p contém 0x1000 (&x) e &p é o endereço do próprio ponteiro (0x1008).",
        "steps": [
            "A expressão (void *)p lê o conteúdo armazenado dentro de p, que é &x = 0x1000.",
            "A expressão (void *)&p obtém o endereço onde a variável p reside na memória, que é 0x1008."
        ],
        "optionExplanations": [
            "Incorreta: p e &p só seriam iguais se o ponteiro apontasse para si mesmo (o que exigiria cast).",
            "Incorreta: inverte a ordem de p e &p.",
            "Correta: conteúdo de p (0x1000) seguido do endereço de p (0x1008).",
            "Incorreta: 10 é *p, não p.",
            "Incorreta: o conteúdo de p é 0x1000, não 0x1008."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int x = 10;
    int *p = &x;
    printf("p=%p &p=%p\\n", (void *)p, (void *)&p);
    return 0;
}"""
    },
    {
        "id": "q-ptr-9",
        "category": "ponteiros",
        "subtopic": "1.6 Aritmética de ponteiros",
        "level": "Intermediário",
        "title": "Deslocamento proporcional a sizeof(tipo)",
        "stem": "Em um sistema onde sizeof(short) == 2 e sizeof(double) == 8, se short *ps = (short *)0x2000 e double *pd = (double *)0x3000, quais serão os endereços resultantes de ps + 3 e pd + 2?",
        "options": [
            "0x2003 e 0x3002",
            "0x2006 e 0x3010",
            "0x200C e 0x3008",
            "0x2006 e 0x3008",
            "0x2002 e 0x3008"
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: ps + 3 soma 3*2=6 (0x2006) e pd + 2 soma 2*8=16=0x10 (0x3010).",
        "steps": [
            "ps + 3 = 0x2000 + 3 * sizeof(short) = 0x2000 + 6 = 0x2006.",
            "pd + 2 = 0x3000 + 2 * sizeof(double) = 0x3000 + 16 decimal = 0x3000 + 0x10 = 0x3010."
        ],
        "optionExplanations": [
            "Incorreta: ignora a multiplicação por sizeof(tipo).",
            "Correta: +6 bytes para short*3 e +16 bytes (0x10 em hexadecimal) para double*2.",
            "Incorreta: usa sizeof(int)=4 em vez de sizeof(short)=2 e sizeof(double)=8.",
            "Incorreta: erra o deslocamento de pd + 2 (8 bytes seria pd + 1).",
            "Incorreta: confunde a quantidade de elementos com bytes."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    short vs[5] = {0};
    double vd[4] = {0};
    short *ps = vs;
    double *pd = vd;
    printf("delta ps+3 = %td bytes\\n", (char *)(ps + 3) - (char *)ps);
    printf("delta pd+2 = %td bytes\\n", (char *)(pd + 2) - (char *)pd);
    return 0;
}"""
    },
    {
        "id": "q-ptr-10",
        "category": "ponteiros",
        "subtopic": "1.6 Aritmética de ponteiros",
        "level": "Intermediário",
        "title": "Precedência *p++ vs (*p)++ e subtração p2 - p1",
        "stem": "Analise o código abaixo e determine o que será impresso na saída padrão:",
        "code": """#include <stdio.h>
int main(void) {
    int v[] = {10, 20, 30, 40};
    int *p1 = v;
    int *p2 = &v[3];
    int a = *p1++;
    int b = (*p1)++;
    printf("%d %d %d %td", a, b, *p1, p2 - p1);
    return 0;
}""",
        "options": [
            "10 20 21 2",
            "20 21 21 2",
            "10 21 21 2",
            "10 20 30 1",
            "10 20 21 8"
        ],
        "correct": 0,
        "gabaritoResumo": "Letra A: *p1++ retorna 10 e avança p1 para v[1]; (*p1)++ retorna 20 e incrementa v[1] para 21; p2 - p1 vale 2.",
        "steps": [
            "Em int a = *p1++, o sufixo ++ aplica-se a p1 após ler *p1: a recebe 10 e p1 passa a apontar para v[1] (20).",
            "Em int b = (*p1)++, os parênteses incrementam o conteúdo v[1] pós-leitura: b recebe 20 e v[1] (logo *p1) passa a ser 21.",
            "p2 aponta para v[3] e p1 para v[1], então p2 - p1 = 3 - 1 = 2 elementos."
        ],
        "optionExplanations": [
            "Correta: a=10, b=20, *p1=21 e diferença de 2 elementos.",
            "Incorreta: *p1++ é pós-incremento, portanto lê v[0]=10 antes de avançar p1.",
            "Incorreta: (*p1)++ é pós-incremento do valor apontado, então b recebe 20 antes de v[1] virar 21.",
            "Incorreta: (*p1)++ não move o ponteiro p1 para v[2].",
            "Incorreta: p2 - p1 retorna distância em elementos (2), não em bytes (8)."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int v[] = {10, 20, 30, 40};
    int *p1 = v;
    int *p2 = &v[3];
    int a = *p1++;
    int b = (*p1)++;
    printf("%d %d %d %td\\n", a, b, *p1, p2 - p1);
    return 0;
}"""
    },
    {
        "id": "q-ptr-11",
        "category": "ponteiros",
        "subtopic": "1.7 Ponteiros e vetores",
        "level": "Básico",
        "title": "Equivalência v[i] == *(v + i) e operador sizeof",
        "stem": "Dado int v[5] = {2, 4, 6, 8, 10}; int *p = v; em um ambiente onde sizeof(int) == 4 e sizeof(int *) == 8, qual alternativa é FALSA?",
        "code": "int v[5] = {2, 4, 6, 8, 10};\nint *p = v;",
        "options": [
            "*(v + 2) resulta em 6.",
            "p[3] resulta em 8.",
            "&v[4] é igual a p + 4.",
            "sizeof(v) é igual a sizeof(p), ambos valendo 8.",
            "2[v] compila em C e resulta em 6."
        ],
        "correct": 3,
        "gabaritoResumo": "Letra D é falsa: sizeof(v) vale 20 bytes (5 * 4), enquanto sizeof(p) vale 8 bytes.",
        "steps": [
            "O vetor v não sofre array decay quando é operando direto de sizeof, logo sizeof(v) = 5 * 4 = 20.",
            "Já p é uma variável ponteiro isolada, logo sizeof(p) = 8.",
            "Além disso, 2[v] equivale a *(2 + v) == *(v + 2) == 6 em C."
        ],
        "optionExplanations": [
            "Incorreta (afirmação verdadeira): *(v + 2) == v[2] == 6.",
            "Incorreta (afirmação verdadeira): p[3] == *(p + 3) == v[3] == 8.",
            "Incorreta (afirmação verdadeira): &v[4] == v + 4 == p + 4.",
            "Correta (afirmação falsa pedida): sizeof(v) = 20 != sizeof(p) = 8.",
            "Incorreta (afirmação verdadeira): pela comutatividade da soma, i[v] == *(i + v) == v[i]."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int v[5] = {2, 4, 6, 8, 10};
    int *p = v;
    printf("sizeof(v)=%zu, sizeof(p)=%zu, 2[v]=%d\\n", sizeof(v), sizeof(p), 2[v]);
    return 0;
}"""
    },
    {
        "id": "q-ptr-12",
        "category": "ponteiros",
        "subtopic": "1.7 Ponteiros e vetores",
        "level": "Intermediário",
        "title": "Array estático vs ponteiro em parâmetro de função",
        "stem": "Sobre a operação de incremento ++ no identificador de um vetor, considere o código abaixo. O que ocorre na compilação de f1 e f2?",
        "code": """void f1(int v[]) {
    v++;
}
void f2(void) {
    int v[3] = {1, 2, 3};
    v++;
}""",
        "options": [
            "Ambas as funções compilam sem erros.",
            "Ambas falham na compilação porque vetores são constantes.",
            "f1 compila (pois int v[] em parâmetro decai para int *v), mas f2 falha na compilação (v é array não-modificável).",
            "f2 compila, mas f1 falha porque parâmetros [] são somente leitura.",
            "f1 compila apenas se escrevermos v[0]++; no lugar de v++;."
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: em parâmetros, int v[] é ajustado para int *v (modificável); em f2, v é um array real (não é lvalue modificável).",
        "steps": [
            "Em listas de parâmetros de funções C, int v[] é automaticamente ajustado pelo compilador para int *v, uma variável ponteiro local que aceita v++.",
            "Dentro de f2, int v[3] declara um array propriamente dito; o nome v não é uma variável ponteiro mutável, portanto v++ gera erro de compilação."
        ],
        "optionExplanations": [
            "Incorreta: f2 não compila.",
            "Incorreta: f1 compila porque parâmetros array viram ponteiros.",
            "Correta: diferencia exatamente array parameter adjustment de um array local.",
            "Incorreta: é o oposto.",
            "Incorreta: v++ em f1 é perfeitamente válido em C padrão."
        ],
        "solutionCode": """#include <stdio.h>

void f1(int v[]) {
    v++; /* valido: v eh int * */
    printf("Segundo elemento: %d\\n", *v);
}

int main(void) {
    int arr[3] = {10, 20, 30};
    f1(arr);
    return 0;
}"""
    },
    {
        "id": "q-ptr-13",
        "category": "ponteiros",
        "subtopic": "1.8 Ponteiros e strings",
        "level": "Básico",
        "title": "Percurso de string com char * até '\\0'",
        "stem": "Qual é a saída impressa pelo programa abaixo?",
        "code": """#include <stdio.h>
int main(void) {
    char s[] = "PONTEIRO";
    char *p = s + 3;
    while (*p != '\\0') {
        putchar(*p);
        p++;
    }
    return 0;
}""",
        "options": [
            "PONT",
            "TEIRO",
            "EIRO",
            "NTEIRO",
            "PONTEIRO"
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: s + 3 aponta para o índice 3 ('T') e p++ percorre até encontrar '\\0', imprimindo TEIRO.",
        "steps": [
            "Os índices da string \"PONTEIRO\" são: 0='P', 1='O', 2='N', 3='T', 4='E', 5='I', 6='R', 7='O', 8='\\0'.",
            "p = s + 3 posiciona p no caractere 'T' (índice 3). O laço imprime cada caractere e avança p++ até *p == '\\0'."
        ],
        "optionExplanations": [
            "Incorreta: s + 3 não começa do início e não para no meio.",
            "Correta: inicia em s[3] ('T') e segue até o terminador nulo '\\0'.",
            "Incorreta: 'E' está em s + 4, não s + 3.",
            "Incorreta: 'N' está em s + 2.",
            "Incorreta: só imprimiria toda a string se p começasse em s + 0."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    char s[] = "PONTEIRO";
    char *p = s + 3;
    while (*p != '\\0') {
        putchar(*p);
        p++;
    }
    putchar('\\n');
    return 0;
}"""
    },
    {
        "id": "q-ptr-14",
        "category": "ponteiros",
        "subtopic": "1.8 Ponteiros e strings",
        "level": "Intermediário",
        "title": "char s[] mutável vs char *s literal read-only",
        "stem": "Considere as duas declarações abaixo em C. Assinale a alternativa correta sobre tentar alterar o primeiro caractere para 'X':",
        "code": """char a[] = "ads";
char *b = "ads";""",
        "options": [
            "a[0] = 'X'; e b[0] = 'X'; são ambas válidas e seguras.",
            "a[0] = 'X'; é inválida porque vetores não podem ser modificados; b[0] = 'X'; é válida.",
            "a[0] = 'X'; é válida (array na Stack), enquanto b[0] = 'X'; causa Comportamento Indefinido (geralmente Segmentation Fault) por tentar escrever em string literal somente-leitura.",
            "Nenhuma das duas permite alteração porque strings em C são sempre imutáveis.",
            "b = \"nova\"; causa erro de compilação, mas b[0] = 'X'; funciona."
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: char a[] copia os caracteres para um vetor editável na Stack; char *b aponta para o literal em seção somente-leitura.",
        "steps": [
            "char a[] = \"ads\"; cria um array de 4 bytes mutáveis na Stack contendo 'a','d','s','\\0'. Logo a[0] = 'X' é seguro.",
            "char *b = \"ads\"; faz b apontar para o literal constante alocado pelo compilador (em .rodata). Tentar escrever em b[0] viola proteção de memória."
        ],
        "optionExplanations": [
            "Incorreta: modificar string literal via b[0] é Undefined Behavior.",
            "Incorreta: é exatamente o contrário.",
            "Correta: distingue memória mutável da Stack de literal read-only.",
            "Incorreta: strings em arrays char[] são perfeitamente mutáveis.",
            "Incorreta: b = \"nova\"; apenas muda o endereço apontado por b, o que é válido."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    char a[] = "ads";
    const char *b = "ads"; /* const protege contra escrita acidental */
    a[0] = 'X';
    printf("%s | %s\\n", a, b);
    return 0;
}"""
    },
    {
        "id": "q-ptr-15",
        "category": "ponteiros",
        "subtopic": "1.9 Passagem por referência",
        "level": "Básico",
        "title": "Modificando variáveis do chamador via ponteiros",
        "stem": "Qual assinatura e corpo implementam corretamente uma função dobrar_e_somar que dobra o primeiro argumento no chamador e acumula o segundo nele?",
        "options": [
            "void dobrar_e_somar(int a, int b) { a = 2 * a + b; }",
            "void dobrar_e_somar(int *a, int b) { *a = 2 * (*a) + b; }",
            "void dobrar_e_somar(int *a, int b) { a = 2 * a + b; }",
            "int *dobrar_e_somar(int a, int b) { int r = 2 * a + b; return &r; }",
            "void dobrar_e_somar(int *a, int *b) { *a = 2 * a + *b; }"
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: recebe int *a para alterar o chamador e desreferencia *a na leitura e escrita.",
        "steps": [
            "Para alterar a variável do chamador, o primeiro parâmetro deve ser ponteiro (int *a).",
            "Tanto na leitura (2 * (*a)) quanto na escrita (*a = ...) é preciso desreferenciar 'a'."
        ],
        "optionExplanations": [
            "Incorreta: passagem por valor altera apenas a cópia local de a.",
            "Correta: desreferencia *a corretamente na leitura e atribuição.",
            "Incorreta: tenta multiplicar ponteiro (2 * a), o que não compila.",
            "Incorreta: retorna endereço de variável local r (dangling pointer).",
            "Incorreta: 2 * a tenta multiplicar um ponteiro por 2."
        ],
        "solutionCode": """#include <stdio.h>

void dobrar_e_somar(int *a, int b) {
    *a = 2 * (*a) + b;
}

int main(void) {
    int x = 10;
    dobrar_e_somar(&x, 5);
    printf("x = %d\\n", x); /* 25 */
    return 0;
}"""
    },
    {
        "id": "q-ptr-16",
        "category": "ponteiros",
        "subtopic": "1.9 Passagem por referência",
        "level": "Intermediário",
        "title": "Erro clássico na função troca",
        "stem": "Um estudante escreveu a função troca_errada abaixo. Ao executar main, o que será impresso?",
        "code": """#include <stdio.h>
void troca_errada(int *a, int *b) {
    int *tmp = a;
    a = b;
    b = tmp;
}
int main(void) {
    int x = 3, y = 7;
    troca_errada(&x, &y);
    printf("%d %d", x, y);
    return 0;
}""",
        "options": [
            "7 3",
            "3 7",
            "7 7",
            "3 3",
            "Erro de compilação na linha int *tmp = a;"
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: troca_errada apenas troca as cópias locais dos ponteiros a e b, deixando x=3 e y=7 intactos.",
        "steps": [
            "Os ponteiros a e b são passados por valor (são cópias dos endereços &x e &y no frame de troca_errada).",
            "Como *a e *b nunca são escritos, os valores originais x=3 e y=7 na main permanecem inalterados."
        ],
        "optionExplanations": [
            "Incorreta: os valores apontados não foram trocados.",
            "Correta: x continua 3 e y continua 7.",
            "Incorreta: nenhuma escrita foi feita na memória de x ou y.",
            "Incorreta: nenhuma escrita foi feita na memória de x ou y.",
            "Incorreta: int *tmp = a; compila normalmente."
        ],
        "solutionCode": """#include <stdio.h>

void troca_correta(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main(void) {
    int x = 3, y = 7;
    troca_correta(&x, &y);
    printf("%d %d\\n", x, y);
    return 0;
}"""
    },
    {
        "id": "q-ptr-17",
        "category": "ponteiros",
        "subtopic": "1.10 Múltiplos retornos via ponteiros",
        "level": "Intermediário",
        "title": "Divisão inteira retornando quociente, resto e status",
        "stem": "Considere a função div_segura abaixo. Qual chamada na main obtém corretamente quociente q e resto r de 17 dividido por 5?",
        "code": """int div_segura(int num, int den, int *q, int *r) {
    if (den == 0 || !q || !r) return -1;
    *q = num / den;
    *r = num % den;
    return 0;
}""",
        "options": [
            "int q, r; div_segura(17, 5, q, r);",
            "int *q, *r; div_segura(17, 5, q, r);",
            "int q, r; div_segura(17, 5, &q, &r);",
            "int q = 0, r = 0; div_segura(17, 5, *q, *r);",
            "int q[2]; div_segura(17, 5, q, q);"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: declara variáveis int q, r e passa seus endereços &q e &r.",
        "steps": [
            "Os parâmetros *q e *r exigem endereços válidos de inteiros existentes no chamador.",
            "Declarar int q, r; e passar &q, &r garante espaço alocado na Stack para receber os dois resultados."
        ],
        "optionExplanations": [
            "Incorreta: passa int em vez de int * (erro de tipo).",
            "Incorreta: q e r são ponteiros não inicializados (wild pointers).",
            "Correta: passa &q e &r apontando para inteiros válidos.",
            "Incorreta: *q é inválido pois q é int, não ponteiro.",
            "Incorreta: passar q para ambos faz *r sobrescrever *q em q[0]."
        ],
        "solutionCode": """#include <stdio.h>

int div_segura(int num, int den, int *q, int *r) {
    if (den == 0 || !q || !r) return -1;
    *q = num / den;
    *r = num % den;
    return 0;
}

int main(void) {
    int q, r;
    if (div_segura(17, 5, &q, &r) == 0) {
        printf("q=%d, r=%d\\n", q, r);
    }
    return 0;
}"""
    },
    {
        "id": "q-ptr-18",
        "category": "ponteiros",
        "subtopic": "1.11 Ponteiro para ponteiro (int **pp)",
        "level": "Intermediário",
        "title": "Rastreando dupla indireção",
        "stem": "Qual será a saída do programa abaixo?",
        "code": """#include <stdio.h>
int main(void) {
    int x = 4, y = 10;
    int *p = &x;
    int **pp = &p;
    **pp += 3;
    *pp = &y;
    *p *= 2;
    printf("%d %d", x, y);
    return 0;
}""",
        "options": [
            "4 10",
            "7 10",
            "7 20",
            "14 10",
            "4 20"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: **pp += 3 altera x para 7; *pp = &y redireciona p para y; *p *= 2 dobra y para 20.",
        "steps": [
            "Inicialmente pp -> p -> x (4). **pp += 3 soma 3 em x, ficando x = 7.",
            "*pp = &y altera o conteúdo de p para &y.",
            "Em seguida *p *= 2 atua sobre y, passando y de 10 para 20."
        ],
        "optionExplanations": [
            "Incorreta: ambos x e y são modificados.",
            "Incorreta: y também é dobrado via *p *= 2.",
            "Correta: x = 7 e y = 20.",
            "Incorreta: antes de dobrar *p, p já havia sido redirecionado para &y.",
            "Incorreta: **pp += 3 alterou x para 7 antes do redirecionamento."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int x = 4, y = 10;
    int *p = &x;
    int **pp = &p;
    **pp += 3;
    *pp = &y;
    *p *= 2;
    printf("%d %d\\n", x, y);
    return 0;
}"""
    },
    {
        "id": "q-ptr-19",
        "category": "ponteiros",
        "subtopic": "1.11 Ponteiro para ponteiro (int **pp)",
        "level": "Avançado",
        "title": "Precedência em (*pp)[i] dentro de função alocadora",
        "stem": "Uma função void cria_arr(int **pp, int n) aloca n inteiros com *pp = malloc(n * sizeof(int));. Para atribuir o valor 99 ao elemento de índice 2 dentro de cria_arr, qual expressão está correta?",
        "options": [
            "*pp[2] = 99;",
            "(*pp)[2] = 99;",
            "**pp[2] = 99;",
            "pp[2] = 99;",
            "&(*pp)[2] = 99;"
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: parênteses em (*pp)[2] garantem que pp seja desreferenciado antes da indexação [2].",
        "steps": [
            "O operador [] possui precedência maior que o operador unário *.",
            "Sem parênteses, *pp[2] é lido como *(pp[2]), acessando fora da variável ponteiro do chamador; com (*pp)[2], primeiro obtemos o ponteiro int* alocado e depois indexamos [2]."
        ],
        "optionExplanations": [
            "Incorreta: *pp[2] equivale a *(pp[2]), causando acesso inválido de memória.",
            "Correta: (*pp)[2] ou *((*pp) + 2) acessa o 3º elemento do vetor alocado.",
            "Incorreta: aplica dupla indireção após indexar pp[2].",
            "Incorreta: pp[2] tem tipo int *, incompatível com 99.",
            "Incorreta: o resultado de &... não é um lvalue modificável."
        ],
        "solutionCode": """#include <stdio.h>
#include <stdlib.h>

void cria_arr(int **pp, int n) {
    *pp = malloc((size_t)n * sizeof(int));
    if (*pp != NULL && n > 2) {
        (*pp)[2] = 99;
    }
}

int main(void) {
    int *v = NULL;
    cria_arr(&v, 4);
    if (v) {
        printf("v[2] = %d\\n", v[2]);
        free(v);
    }
    return 0;
}"""
    },
    {
        "id": "q-ptr-20",
        "category": "ponteiros",
        "subtopic": "1.12 Ponteiros e matrizes 2D",
        "level": "Intermediário",
        "title": "Acesso via *(*(m + i) + j)",
        "stem": "Dada a matriz int m[3][4] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};, qual valor é obtido pela expressão *(*(m + 2) + 1)?",
        "code": "int m[3][4] = {\n    {1, 2, 3, 4},\n    {5, 6, 7, 8},\n    {9, 10, 11, 12}\n};",
        "options": [
            "6",
            "7",
            "10",
            "11",
            "3"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: *(*(m + 2) + 1) equivale a m[2][1], cujo valor é 10.",
        "steps": [
            "Pela equivalência de matrizes 2D, *(*(m + i) + j) é idêntico a m[i][j].",
            "Com i = 2 (terceira linha: {9, 10, 11, 12}) e j = 1 (segunda coluna), obtemos 10."
        ],
        "optionExplanations": [
            "Incorreta: 6 é m[1][1].",
            "Incorreta: 7 é m[1][2].",
            "Correta: m[2][1] = 10.",
            "Incorreta: 11 é m[2][2].",
            "Incorreta: 3 é m[0][2]."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int m[3][4] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
    printf("%d\\n", *(*(m + 2) + 1));
    return 0;
}"""
    },
    {
        "id": "q-ptr-21",
        "category": "ponteiros",
        "subtopic": "1.12 Ponteiros e matrizes 2D",
        "level": "Avançado",
        "title": "Passagem de matriz estática 2D para função",
        "stem": "Para passar uma matriz declarada como int mat[4][5]; para uma função processar( ... , int linhas), qual tipo de parâmetro corresponde exatamente ao decaimento de mat?",
        "options": [
            "int **m",
            "int *m[5]",
            "int (*m)[5]",
            "int m[4][]",
            "void **m"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: int (*m)[5] é um ponteiro para um array de 5 inteiros, tipo exato do decay de int[4][5].",
        "steps": [
            "Um array 2D int[4][5] é um vetor de 4 arrays de 5 ints.",
            "Ao decair, ele vira ponteiro para o seu primeiro elemento (um array de 5 ints): int (*m)[5], equivalente a int m[][5]."
        ],
        "optionExplanations": [
            "Incorreta: int ** é ponteiro para ponteiro, incompatível com matriz contígua estática.",
            "Incorreta: int *m[5] é um array de 5 ponteiros para int (sem parênteses!).",
            "Correta: int (*m)[5] é ponteiro para linha de 5 ints.",
            "Incorreta: em C, apenas a 1ª dimensão pode ser omitida; o número de colunas é obrigatório.",
            "Incorreta: void ** também é incompatível."
        ],
        "solutionCode": """#include <stdio.h>

void processar(int (*m)[5], int linhas) {
    printf("Ultimo elemento: %d\\n", m[linhas - 1][4]);
}

int main(void) {
    int mat[4][5] = {0};
    mat[3][4] = 77;
    processar(mat, 4);
    return 0;
}"""
    },
    {
        "id": "q-ptr-22",
        "category": "ponteiros",
        "subtopic": "1.13 Alocação dinâmica (<stdlib.h>)",
        "level": "Intermediário",
        "title": "Diferença entre malloc e calloc",
        "stem": "Qual alternativa descreve corretamente a diferença entre malloc e calloc da biblioteca <stdlib.h>?",
        "options": [
            "malloc aloca na Stack e calloc aloca no Heap.",
            "malloc inicializa todos os bytes com zero; calloc deixa lixo de memória.",
            "malloc recebe o total de bytes em 1 argumento e deixa memória não inicializada; calloc recebe (qtd, tamanho) e inicializa todos os bits com zero.",
            "calloc não pode retornar NULL em caso de falta de memória.",
            "Blocos criados com calloc não devem ser liberados com free."
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: malloc(bytes) deixa lixo; calloc(n, tam) zera os bits da região alocada.",
        "steps": [
            "Ambas as funções alocam memória dinamicamente no Heap e retornam NULL se falharem.",
            "A assinatura malloc(size_t size) não zera o bloco, enquanto calloc(size_t nmemb, size_t size) zera todos os bytes."
        ],
        "optionExplanations": [
            "Incorreta: ambas alocam no Heap.",
            "Incorreta: é exatamente o inverso.",
            "Correta: assinatura e inicialização com zero estão exatas.",
            "Incorreta: ambas retornam NULL se não houver memória suficiente.",
            "Incorreta: todo bloco de malloc, calloc ou realloc deve ser liberado com free."
        ],
        "solutionCode": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *a = malloc(4 * sizeof(*a));
    int *b = calloc(4, sizeof(*b));
    if (a && b) {
        printf("b[0]=%d, b[3]=%d\\n", b[0], b[3]);
    }
    free(a);
    free(b);
    return 0;
}"""
    },
    {
        "id": "q-ptr-23",
        "category": "ponteiros",
        "subtopic": "1.13 Alocação dinâmica (<stdlib.h>)",
        "level": "Avançado",
        "title": "Uso seguro de realloc",
        "stem": "Por que a escrita direta p = realloc(p, novo_tam); é considerada má prática em código C robusto?",
        "options": [
            "Porque realloc exige que p seja primeiro liberado com free(p).",
            "Porque se realloc falhar e retornar NULL, o ponteiro original p é sobrescrito por NULL, causando vazamento do bloco antigo que não foi liberado.",
            "Porque realloc sempre dobra o tamanho e ignora o argumento novo_tam.",
            "Porque realloc só funciona para ponteiros char *.",
            "Porque realloc copia apenas o primeiro elemento do bloco antigo."
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: em caso de falha, realloc retorna NULL sem liberar o bloco antigo; sobrescrever p perde sua única referência.",
        "steps": [
            "Quando não há memória para expandir/realocar, realloc retorna NULL e mantém o bloco original intacto.",
            "Se atribuirmos direto em p, perdemos o endereço do bloco original (memory leak). Deve-se usar um ponteiro temporário tmp."
        ],
        "optionExplanations": [
            "Incorreta: nunca se deve dar free antes de passar p ao realloc (seria use-after-free).",
            "Correta: padrão seguro é tmp = realloc(p, tam); if (tmp != NULL) p = tmp;.",
            "Incorreta: realloc tenta alocar exatamente novo_tam bytes.",
            "Incorreta: funciona com qualquer bloco alocado dinamicamente via void *.",
            "Incorreta: preserva os dados existentes até o menor entre tamanho antigo e novo."
        ],
        "solutionCode": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = malloc(2 * sizeof(*p));
    if (!p) return 1;
    p[0] = 1; p[1] = 2;

    int *tmp = realloc(p, 4 * sizeof(*p));
    if (!tmp) {
        free(p);
        return 1;
    }
    p = tmp;
    p[2] = 3; p[3] = 4;
    free(p);
    return 0;
}"""
    },
    {
        "id": "q-ptr-24",
        "category": "ponteiros",
        "subtopic": "1.14 Matriz dinâmica no Heap",
        "level": "Intermediário",
        "title": "Ordem correta de liberação de matriz dinâmica int **m",
        "stem": "Uma matriz dinâmica de L linhas e C colunas foi alocada com um vetor de L ponteiros em m e L chamadas malloc(C * sizeof(int)) para cada m[i]. Qual código libera toda a memória sem memory leak nem use-after-free?",
        "options": [
            "free(m);",
            "free(m); for (int i = 0; i < L; i++) free(m[i]);",
            "for (int i = 0; i < L; i++) free(m[i]); free(m);",
            "for (int i = 0; i < C; i++) free(m[i]); free(m);",
            "free(*m); free(m);"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: libera cada uma das L linhas m[i] primeiro e só depois libera o vetor de ponteiros m.",
        "steps": [
            "Cada m[i] (para i de 0 até L-1) aponta para um bloco independente no Heap.",
            "Devemos liberar todos os m[i] enquanto m ainda é válido, e por último executar free(m)."
        ],
        "optionExplanations": [
            "Incorreta: deixa todas as L linhas vazando no Heap (memory leak).",
            "Incorreta: acessa m[i] após free(m), configurando Use-After-Free.",
            "Correta: liberação na ordem inversa à alocação.",
            "Incorreta: itera até C (colunas) em vez de L (linhas).",
            "Incorreta: free(*m) libera apenas a linha 0 (m[0]), vazando as linhas 1..L-1."
        ],
        "solutionCode": """#include <stdlib.h>

void liberar_matriz(int **m, int L) {
    if (!m) return;
    for (int i = 0; i < L; i++) {
        free(m[i]);
    }
    free(m);
}

int main(void) {
    int L = 3, C = 4;
    int **m = malloc((size_t)L * sizeof(int *));
    if (!m) return 1;
    for (int i = 0; i < L; i++) m[i] = calloc((size_t)C, sizeof(int));
    liberar_matriz(m, L);
    return 0;
}"""
    },
    {
        "id": "q-ptr-25",
        "category": "ponteiros",
        "subtopic": "1.14 Bugs no Heap",
        "level": "Avançado",
        "title": "Identificando Memory Leak, Dangling Pointer e Double Free",
        "stem": "Analise os dois trechos abaixo. Quais anomalias de memória ocorrem no Trecho 1 e no Trecho 2, respectivamente?",
        "code": """/* Trecho 1 */
int *p = malloc(sizeof(int));
*p = 10;
free(p);
*p = 20;

/* Trecho 2 */
int *q = malloc(sizeof(int));
free(q);
free(q);""",
        "options": [
            "Memory Leak no Trecho 1 e Null Pointer Dereference no Trecho 2.",
            "Dangling Pointer (Use-After-Free) no Trecho 1 e Double Free no Trecho 2.",
            "Double Free no Trecho 1 e Memory Leak no Trecho 2.",
            "Stack Overflow no Trecho 1 e Dangling Pointer no Trecho 2.",
            "Nenhum erro no Trecho 1 e Memory Leak no Trecho 2."
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: escrever após free(p) é Dangling Pointer / Use-After-Free; chamar free(q) duas vezes sem zerar q é Double Free.",
        "steps": [
            "No Trecho 1, após free(p), p continua guardando o endereço antigo (dangling pointer) e *p = 20 comete Use-After-Free.",
            "No Trecho 2, q não foi zerado com NULL após o primeiro free(q); o segundo free(q) causa Double Free."
        ],
        "optionExplanations": [
            "Incorreta: no Trecho 1 não há leak (free foi chamado), há acesso após liberação.",
            "Correta: Use-After-Free (ponteiro pendente) no Trecho 1 e Double Free no Trecho 2.",
            "Incorreta: inverte e troca os nomes dos bugs.",
            "Incorreta: não envolve estouro de pilha.",
            "Incorreta: ambos os trechos têm Undefined Behavior grave."
        ],
        "solutionCode": """#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int));
    if (p) {
        *p = 10;
        free(p);
        p = NULL; /* evita Dangling Pointer e Double Free */
    }
    free(p); /* free(NULL) eh seguro */
    return 0;
}"""
    },
    {
        "id": "q-ptr-26",
        "category": "ponteiros",
        "subtopic": "1.15 Ponteiros para funções e qsort",
        "level": "Avançado",
        "title": "Declaração de ponteiro para função e comparador do qsort",
        "stem": "Assinale a declaração correta de uma variável 'cmp' que seja um ponteiro para função com a assinatura exigida pelo 4º parâmetro de qsort (recebe dois const void * e retorna int):",
        "options": [
            "int *cmp(const void *, const void *);",
            "int (*cmp)(const void *, const void *);",
            "void (*cmp)(const int *, const int *);",
            "int *(cmp)(const void *, const void *);",
            "int (*cmp[])(void);"
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: parênteses em (*cmp) garantem que cmp é um ponteiro para função retornando int.",
        "steps": [
            "Sem parênteses em torno de *cmp, int *cmp(...) declara uma função que retorna int *.",
            "O comparador de qsort recebe (const void *, const void *) e retorna int: int (*cmp)(const void *, const void *)."
        ],
        "optionExplanations": [
            "Incorreta: declara protótipo de função que retorna int *.",
            "Correta: assinatura exata do callback de comparação de qsort.",
            "Incorreta: retorno e tipos dos parâmetros não correspondem a qsort.",
            "Incorreta: os parênteses em (cmp) não envolvem o *, continuando função retornando int *.",
            "Incorreta: declara array de ponteiros para função sem parâmetros."
        ],
        "solutionCode": """#include <stdio.h>
#include <stdlib.h>

int decrescente(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (vb > va) - (vb < va);
}

int main(void) {
    int (*cmp)(const void *, const void *) = decrescente;
    int v[] = {3, 9, 1, 5};
    qsort(v, 4, sizeof(v[0]), cmp);
    printf("%d %d %d %d\\n", v[0], v[1], v[2], v[3]);
    return 0;
}"""
    },
    {
        "id": "q-ptr-27",
        "category": "ponteiros",
        "subtopic": "1.16 Ponteiros genéricos (void *)",
        "level": "Intermediário",
        "title": "Restrições de void * no padrão C",
        "stem": "Dado float f = 2.5f; void *g = &f;, qual expressão lê corretamente o valor 2.5f a partir de g sem erros de compilação no padrão ISO C?",
        "code": "float f = 2.5f;\nvoid *g = &f;",
        "options": [
            "*g",
            "(float)*g",
            "*(float *)g",
            "*(void *)g",
            "(float *)g"
        ],
        "correct": 2,
        "gabaritoResumo": "Letra C: é obrigatório converter g para (float *) antes de aplicar o operador *.",
        "steps": [
            "Em C, não se pode desreferenciar diretamente um void * porque o tipo void não tem tamanho nem representação.",
            "Primeiro aplicamos o cast para ponteiro tipado (float *)g e depois desreferenciamos com *."
        ],
        "optionExplanations": [
            "Incorreta: desreferenciar void * diretamente é erro de compilação.",
            "Incorreta: ainda tenta desreferenciar *g antes do cast.",
            "Correta: converte void * para float * e lê os 4 bytes do float.",
            "Incorreta: tenta desreferenciar void *.",
            "Incorreta: retorna apenas o endereço convertido para float *, não o valor 2.5f."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    float f = 2.5f;
    void *g = &f;
    printf("%.1f\\n", *(float *)g);
    return 0;
}"""
    },
    {
        "id": "q-ptr-28",
        "category": "ponteiros",
        "subtopic": "1.17 Ponteiros com const",
        "level": "Avançado",
        "title": "const int *p vs int *const p",
        "stem": "Considere as declarações abaixo. Quais linhas provocam ERRO de compilação?",
        "code": """int x = 1, y = 2;
const int *p1 = &x;
int *const p2 = &x;
p1 = &y;     /* Linha A */
*p1 = 10;    /* Linha B */
p2 = &y;     /* Linha C */
*p2 = 20;    /* Linha D */""",
        "options": [
            "Linhas A e D",
            "Linhas B e C",
            "Linhas A e C",
            "Linhas B e D",
            "Apenas Linha C"
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: p1 não pode alterar *p1 (Linha B), e p2 não pode ser redirecionado (Linha C).",
        "steps": [
            "const int *p1: ponteiro para inteiro constante -> p1 = &y (Linha A) é OK; *p1 = 10 (Linha B) é ERRO.",
            "int *const p2: ponteiro constante para inteiro -> p2 = &y (Linha C) é ERRO; *p2 = 20 (Linha D) é OK."
        ],
        "optionExplanations": [
            "Incorreta: ambas as linhas A e D são válidas.",
            "Correta: B viola const no dado apontado por p1, e C viola const no próprio ponteiro p2.",
            "Incorreta: A é válida.",
            "Incorreta: D é válida.",
            "Incorreta: B também falha na compilação."
        ],
        "solutionCode": """#include <stdio.h>

int main(void) {
    int x = 1, y = 2;
    const int *p1 = &x;
    int *const p2 = &x;
    p1 = &y;
    *p2 = 20;
    printf("*p1=%d, *p2=%d\\n", *p1, *p2);
    return 0;
}"""
    },
    {
        "id": "q-ptr-29",
        "category": "ponteiros",
        "subtopic": "1.18 Ponteiros e structs (->)",
        "level": "Intermediário",
        "title": "Acesso a campos com -> e (*p).campo",
        "stem": "Dada a struct typedef struct { int id; float nota; } Aluno; e as declarações Aluno a = {10, 8.0f}; Aluno *pa = &a;, qual expressão NÃO é equivalente a acessar o campo nota?",
        "code": "typedef struct { int id; float nota; } Aluno;\nAluno a = {10, 8.0f};\nAluno *pa = &a;",
        "options": [
            "a.nota",
            "pa->nota",
            "(*pa).nota",
            "*pa.nota",
            "(&a)->nota"
        ],
        "correct": 3,
        "gabaritoResumo": "Letra D: *pa.nota falha na compilação porque . tem precedência maior que *.",
        "steps": [
            "O operador ponto (.) tem precedência maior que o operador unário *.",
            "Logo *pa.nota é interpretado como *(pa.nota), gerando erro pois pa é um ponteiro e não uma struct."
        ],
        "optionExplanations": [
            "Incorreta: a é struct, portanto a.nota é válido.",
            "Incorreta: pa->nota é a forma padrão para ponteiro de struct.",
            "Incorreta: (*pa).nota usa parênteses corretamente e equivale a pa->nota.",
            "Correta: sem parênteses, *pa.nota tenta aplicar . no ponteiro pa e dá erro.",
            "Incorreta: (&a) é Aluno *, logo (&a)->nota é equivalente a a.nota."
        ],
        "solutionCode": """#include <stdio.h>

typedef struct { int id; float nota; } Aluno;

int main(void) {
    Aluno a = {10, 8.0f};
    Aluno *pa = &a;
    printf("%.1f %.1f %.1f\\n", a.nota, pa->nota, (*pa).nota);
    return 0;
}"""
    },
    {
        "id": "q-ptr-30",
        "category": "ponteiros",
        "subtopic": "1.18 Listas dinâmicas e ASan/Valgrind",
        "level": "Avançado",
        "title": "Liberação segura de lista encadeada e sanitizadores",
        "stem": "Ao liberar todos os nós de uma lista encadeada com ponteiro No *head, qual laço evita Use-After-Free (detectado pelo AddressSanitizer / Valgrind)?",
        "options": [
            "while (head != NULL) { free(head); head = head->prox; }",
            "while (head != NULL) { No *prox = head->prox; free(head); head = prox; }",
            "for (No *p = head; p != NULL; p = p->prox) free(p);",
            "free(head); head = NULL;",
            "while (head->prox != NULL) { free(head->prox); }"
        ],
        "correct": 1,
        "gabaritoResumo": "Letra B: salva head->prox em variável temporária antes de executar free(head).",
        "steps": [
            "Após chamar free(head), ler head->prox é Use-After-Free (Undefined Behavior).",
            "A solução correta salva No *prox = head->prox; antes de liberar head e só então avança head = prox."
        ],
        "optionExplanations": [
            "Incorreta: acessa head->prox após free(head) (Use-After-Free).",
            "Correta: preserva o endereço do próximo nó antes do free.",
            "Incorreta: o passo p = p->prox do for executa após free(p) (Use-After-Free).",
            "Incorreta: libera apenas o 1º nó, vazando o restante da lista.",
            "Incorreta: loop infinito e double free se head->prox não for NULL."
        ],
        "solutionCode": """#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *prox;
} No;

void liberar_lista(No *head) {
    while (head != NULL) {
        No *prox = head->prox;
        free(head);
        head = prox;
    }
}

int main(void) {
    No *n = malloc(sizeof(No));
    if (n) { n->dado = 1; n->prox = NULL; liberar_lista(n); }
    return 0;
}"""
    }
]

CE_PONTEIROS = [
    {
        "id": "ce-ptr-1",
        "category": "ponteiros",
        "subtopic": "1.3 / 1.4 Inicialização e NULL",
        "statement": "Em C, toda variável local do tipo ponteiro declarada dentro de uma função (sem o especificador static) é automaticamente inicializada pelo compilador com o valor NULL.",
        "answer": False,
        "steps": [
            "Variáveis locais automáticas na Stack não recebem inicialização implícita em C.",
            "Um ponteiro local declarado apenas como int *p; contém lixo de memória (wild pointer) até receber um endereço válido ou NULL explicitamente."
        ],
        "keyPoint": "Sempre inicialize ponteiros locais com &var, malloc/calloc ou NULL."
    },
    {
        "id": "ce-ptr-2",
        "category": "ponteiros",
        "subtopic": "1.6 Aritmética de ponteiros",
        "statement": "Se p1 e p2 apontam para elementos distintos de um mesmo vetor int v[10], a expressão p2 - p1 retorna a quantidade de elementos de diferença entre eles (tipo ptrdiff_t), e não a diferença bruta em bytes.",
        "answer": True,
        "steps": [
            "A subtração de ponteiros do mesmo tipo em um mesmo array divide automaticamente a diferença de endereços em bytes por sizeof(*p1).",
            "Por exemplo, entre &v[5] e &v[2], p2 - p1 resulta em 3 elementos (e não 12 bytes)."
        ],
        "keyPoint": "p2 - p1 calcula (end_p2 - end_p1) / sizeof(tipo), retornando distância em elementos."
    },
    {
        "id": "ce-ptr-3",
        "category": "ponteiros",
        "subtopic": "1.7 Ponteiros e vetores",
        "statement": "Dado um vetor local int v[10];, a expressão v++ é válida em C porque o nome do vetor é internamente uma variável ponteiro do tipo int *.",
        "answer": False,
        "steps": [
            "Embora v decaia para &v[0] na maioria das expressões, v é um objeto array e não uma variável ponteiro modificável.",
            "Executar v++ em um array local gera erro de compilação (lvalue required as increment operand)."
        ],
        "keyPoint": "Nome de array decai para ponteiro rvalue; apenas uma variável ponteiro (int *p = v) aceita p++."
    },
    {
        "id": "ce-ptr-4",
        "category": "ponteiros",
        "subtopic": "1.8 Ponteiros e strings",
        "statement": "Ao declarar char *s = \"ADS\";, tentar alterar o primeiro caractere com s[0] = 'X'; provoca comportamento indefinido (em geral Segmentation Fault), pois literais de string residem em área de memória somente-leitura.",
        "answer": True,
        "steps": [
            "Diferente de char s[] = \"ADS\"; (que copia os bytes para um vetor mutável na Stack), char *s = \"ADS\"; apenas aponta para o literal em .rodata.",
            "Por boas práticas, declara-se const char *s = \"ADS\"; para o compilador barrar tentativas de escrita."
        ],
        "keyPoint": "Use char s[] para strings mutáveis e const char *s para literais somente-leitura."
    },
    {
        "id": "ce-ptr-5",
        "category": "ponteiros",
        "subtopic": "1.5 Impressão com %p",
        "statement": "Segundo o padrão ISO C99/C11, para imprimir o endereço armazenado em qualquer ponteiro p (como int *p) usando printf com %p, deve-se realizar o cast explícito para (void *), escrevendo printf(\"%p\", (void *)p);.",
        "answer": True,
        "steps": [
            "Como printf é uma função variádica, o compilador não converte automaticamente int * para void * após a string de formato.",
            "A norma C determina que o argumento de %p seja exatamente void *, tornando (void *)p obrigatório para portabilidade."
        ],
        "keyPoint": "Sempre faça cast (void *) ao imprimir ponteiros com %p em printf."
    },
    {
        "id": "ce-ptr-6",
        "category": "ponteiros",
        "subtopic": "1.12 Matrizes 2D",
        "statement": "Uma matriz estática declarada como int mat[3][4]; pode ser passada diretamente sem avisos ou erros para uma função com assinatura void f(int **m, int lin, int col);.",
        "answer": False,
        "steps": [
            "mat[3][4] é um bloco único contíguo de 12 inteiros e decai para int (*)[4] (ponteiro para array de 4 ints).",
            "Já int **m espera um ponteiro para ponteiros (como em matrizes dinâmicas alocadas linha a linha). Os tipos são incompatíveis."
        ],
        "keyPoint": "Matriz estática 2D decai para int (*)[COLS], nunca para int **."
    },
    {
        "id": "ce-ptr-7",
        "category": "ponteiros",
        "subtopic": "1.13 Alocação dinâmica",
        "statement": "Em C padrão, chamar free(NULL); causa falha de segmentação imediata e deve ser sempre evitado.",
        "answer": False,
        "steps": [
            "O padrão ISO C garante explicitamente que free(NULL) é uma operação segura que não faz nada (no-op).",
            "Por isso, zerar o ponteiro com p = NULL; logo após free(p); também previne acidentes de Double Free."
        ],
        "keyPoint": "free(NULL) é garantidamente seguro pelo padrão C; o perigo real é free() em endereço já liberado (Double Free)."
    },
    {
        "id": "ce-ptr-8",
        "category": "ponteiros",
        "subtopic": "1.16 Ponteiro genérico void *",
        "statement": "Um ponteiro genérico void *p pode ser desreferenciado diretamente com *p sem necessidade de cast, desde que aponte para uma variável int válida.",
        "answer": False,
        "steps": [
            "O tipo void é um tipo incompleto sem tamanho definido.",
            "O compilador não sabe quantos bytes ler em *p e proíbe a desreferenciação direta, exigindo cast explícito como *(int *)p."
        ],
        "keyPoint": "void * armazena qualquer endereço, mas exige cast para tipo concreto antes de *."
    },
    {
        "id": "ce-ptr-9",
        "category": "ponteiros",
        "subtopic": "1.17 Ponteiros com const",
        "statement": "Na declaração int *const p = &x;, é permitido alterar o valor de x através de *p = 50;, mas é proibido alterar o endereço guardado em p através de p = &y;.",
        "answer": True,
        "steps": [
            "Lendo da direita para a esquerda: p é um ponteiro constante (const depois de *) para um int mutável.",
            "Portanto o endereço em p é imutável após a inicialização, mas o inteiro apontado pode ser modificado via *p."
        ],
        "keyPoint": "const antes de * trava *p; const depois de * trava p."
    },
    {
        "id": "ce-ptr-10",
        "category": "ponteiros",
        "subtopic": "1.14 / 1.18 Heap e Valgrind",
        "statement": "Ferramentas como Valgrind e AddressSanitizer (-fsanitize=address) conseguem detectar em tempo de execução tanto vazamentos de memória (memory leaks) quanto leituras/escritas após free (use-after-free).",
        "answer": True,
        "steps": [
            "AddressSanitizer instrumenta os acessos de memória em compilação, acusando imediatamente use-after-free, double free e buffer overflow, além de integrar o LeakSanitizer.",
            "Valgrind executa o binário em máquina virtual rastreando cada alocação malloc/calloc e cada acesso à RAM."
        ],
        "keyPoint": "Compile sempre seus testes em C com -g -fsanitize=address,undefined para detectar bugs de ponteiros."
    }
]

CLASSICAL_PONTEIROS = [
    {
        "id": "cls-ptr-1",
        "module": "Ponteiros",
        "source": "Clássico de Entrevistas & Provas de C (Two Pointers In-Place)",
        "title": "Inversão de vetor in-place usando dois ponteiros (*ini e *fim)",
        "problem": (
            "Implemente uma função void inverter_vetor(int *v, int n) que inverta a ordem dos elementos de um vetor de inteiros "
            "no próprio lugar (in-place, complexidade de espaço O(1), sem vetor auxiliar), utilizando exclusivamente dois ponteiros "
            "(ini apontando para o início e fim apontando para o último elemento) e aritmética de ponteiros."
        ),
        "idea": (
            "Inicialize int *ini = v; e int *fim = v + n - 1;. Enquanto ini < fim, troque os valores apontados (*ini e *fim) "
            "usando uma variável auxiliar temp, avance ini++ (1 elemento à direita) e recue fim-- (1 elemento à esquerda). "
            "Quando ini >= fim, os ponteiros se cruzaram ou encontraram no meio e o vetor está invertido."
        ),
        "code": """#include <stdio.h>

void inverter_vetor(int *v, int n) {
    if (v == NULL || n <= 1) return;

    int *ini = v;
    int *fim = v + n - 1;

    while (ini < fim) {
        int temp = *ini;
        *ini = *fim;
        *fim = temp;
        ini++;
        fim--;
    }
}

int main(void) {
    int v[5] = {10, 20, 30, 40, 50};
    inverter_vetor(v, 5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", v[i]);
    }
    printf("\\n");
    return 0;
}""",
        "trace": (
            "Vetor inicial: [10, 20, 30, 40, 50] (n = 5).\n"
            "• Passo 0: ini = &v[0] (*ini=10), fim = &v[4] (*fim=50). ini < fim -> troca 10 e 50 -> [50, 20, 30, 40, 10]; ini=&v[1], fim=&v[3].\n"
            "• Passo 1: ini = &v[1] (*ini=20), fim = &v[3] (*fim=40). ini < fim -> troca 20 e 40 -> [50, 40, 30, 20, 10]; ini=&v[2], fim=&v[2].\n"
            "• Passo 2: ini == fim (&v[2]). Condição ini < fim é falsa; laço encerra com resultado [50, 40, 30, 20, 10]."
        )
    },
    {
        "id": "cls-ptr-2",
        "module": "Ponteiros",
        "source": "Clássico de Estrutura de Dados / ADS",
        "title": "Matriz dinâmica M x N com int **m, soma de linhas e diagonal + free sem Memory Leak",
        "problem": (
            "Escreva funções em C para: (1) alocar dinamicamente uma matriz de inteiros M x N usando int **m (tratando falhas de malloc com rollback parcial), "
            "(2) calcular a soma de cada linha e a soma da diagonal principal (quando M == N), e (3) liberar completamente a matriz do Heap sem causar memory leak."
        ),
        "idea": (
            "Aloque primeiramente o vetor de M ponteiros (int **m = malloc(M * sizeof(int *))). Em seguida, para cada linha i, aloque N inteiros com calloc/malloc; "
            "se uma linha i falhar, libere imediatamente as linhas 0..i-1 e m antes de retornar NULL. Para somar linhas e diagonal, use m[i][j] (ou *(*(m + i) + j)). "
            "Na liberação, percorra 0..M-1 dando free(m[i]) e por fim dê free(m)."
        ),
        "code": """#include <stdio.h>
#include <stdlib.h>

int **alocar_matriz(int M, int N) {
    int **m = malloc((size_t)M * sizeof(int *));
    if (m == NULL) return NULL;

    for (int i = 0; i < M; i++) {
        m[i] = calloc((size_t)N, sizeof(int));
        if (m[i] == NULL) {
            for (int k = 0; k < i; k++) free(m[k]);
            free(m);
            return NULL;
        }
    }
    return m;
}

void liberar_matriz(int **m, int M) {
    if (m == NULL) return;
    for (int i = 0; i < M; i++) {
        free(m[i]);
    }
    free(m);
}

int main(void) {
    int M = 3, N = 3;
    int **mat = alocar_matriz(M, N);
    if (!mat) return 1;

    int val = 1;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            *(*(mat + i) + j) = val++;
        }
    }

    int soma_diag = 0;
    for (int i = 0; i < M; i++) {
        int soma_linha = 0;
        for (int j = 0; j < N; j++) soma_linha += mat[i][j];
        printf("Soma linha %d = %d\\n", i, soma_linha);
        soma_diag += mat[i][i];
    }
    printf("Soma diagonal principal = %d\\n", soma_diag);

    liberar_matriz(mat, M);
    mat = NULL;
    return 0;
}""",
        "trace": (
            "Matriz 3x3 preenchida sequencialmente com 1..9:\n"
            "  Linha 0: [1, 2, 3] -> soma_linha = 6\n"
            "  Linha 1: [4, 5, 6] -> soma_linha = 15\n"
            "  Linha 2: [7, 8, 9] -> soma_linha = 24\n"
            "• Diagonal principal: mat[0][0] + mat[1][1] + mat[2][2] = 1 + 5 + 9 = 15.\n"
            "• Liberação: free(mat[0]), free(mat[1]), free(mat[2]), depois free(mat) e mat = NULL -> 0 bytes vazados no Valgrind."
        )
    }
]
