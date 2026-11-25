"""Módulo 1 — Ponteiros em C (18 subtópicos) para o ADS Study Team v4.0."""
from __future__ import annotations

TOPICS_PONTEIROS = [
    {
        "id": "ptr-1",
        "num": "1.1",
        "title": "Conceito: endereço de memória, bytes, RAM e o que significa 'apontar'",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.1–7.2) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Entenda a memória RAM como um vetor gigante de bytes numerados por endereços hexadecimais e veja que um ponteiro nada mais é do que uma variável cujo conteúdo é um desses endereços.",
        "conceptHtml": (
            "<p>A memória <strong>RAM</strong> pode ser visualizada como uma sequência contígua de gavetas de <strong>1 byte (8 bits)</strong>, "
            "onde cada gaveta possui um número único chamado <strong>endereço de memória</strong> (geralmente exibido em hexadecimal, como <code>0x1000</code>).</p>"
            "<p>Quando declaramos <code>int x = 42;</code> em uma arquitetura de 32/64 bits típica (onde <code>sizeof(int) == 4</code>), o compilador reserva 4 bytes consecutivos "
            "(por exemplo, de <code>0x1000</code> a <code>0x1003</code>) e grava o valor <code>42</code> ali. O endereço da variável é o endereço do seu <strong>primeiro byte</strong> (<code>0x1000</code>).</p>"
            "<p>Uma variável comum guarda um <em>valor</em> (ex.: <code>42</code>). Um <strong>ponteiro</strong> também é uma variável armazenada na RAM (ocupando geralmente 4 bytes em sistemas 32-bit ou 8 bytes em 64-bit), "
            "mas o seu conteúdo é o <strong>endereço de outra variável</strong>. Dizer que <code>p</code> <em>aponta</em> para <code>x</code> significa exatamente que <code>p</code> armazena o endereço de <code>x</code>.</p>"
        ),
        "code": """#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x;

    printf("Valor de x: %d\\n", x);
    printf("Tamanho de int: %zu bytes\\n", sizeof(x));
    printf("Tamanho do ponteiro p: %zu bytes\\n", sizeof(p));
    printf("Endereco armazenado em p: %p\\n", (void *)p);
    return 0;
}""",
        "logicSteps": [
            "A variável inteira x é alocada na Stack ocupando 4 bytes a partir de um endereço base (ex.: 0x1000).",
            "A variável ponteiro p também recebe seu próprio espaço na Stack (ex.: 8 bytes em x86_64 no endereço 0x1008).",
            "O operador & extrai o endereço inicial de x (0x1000) e o grava dentro dos bytes de p.",
            "Assim, p 'aponta' indiretamente para x sem duplicar o valor 42."
        ],
        "pitfall": (
            "Confundir o <strong>endereço do ponteiro</strong> (<code>&amp;p</code>) com o <strong>endereço armazenado no ponteiro</strong> (<code>p</code>). "
            "Todo ponteiro ocupa memória própria e tem seu próprio endereço; o que muda é que seu <em>conteúdo</em> é outro endereço."
        ),
        "memoryDiagram": {
            "caption": "Representação lógica da RAM (Stack): x ocupa 4 bytes em 0x1000 e p guarda o valor 0x1000 em 0x1008.",
            "cells": [
                {"idx": 0, "addr": "0x1000", "val": "42", "tag": "int x (4 bytes)"},
                {"idx": 1, "addr": "0x1008", "val": "0x1000", "tag": "int *p -> aponta para x"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-1",
                "tabLabel": "RAM & Endereços",
                "badge": "1D • Memória",
                "title": "Nascimento de x e do ponteiro p na RAM",
                "desc": "Acompanhe como um inteiro e um ponteiro ocupam endereços distintos na memória.",
                "kind": "1d",
                "codeLines": [
                    "int x = 42;",
                    "int *p = &x;",
                    "x = 99;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"x": "42", "p": "?"},
                        "note": "x é criado em 0x1000 com valor 42 (4 bytes).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "42", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x1008", "label": "p", "val": "LIXO", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"x": "42", "p": "0x1000", "*p": "42"},
                        "note": "p recebe &x (0x1000). Agora p aponta para x.",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "42", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x1008", "label": "p", "val": "0x1000", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"x": "99", "p": "0x1000", "*p": "99"},
                        "note": "x muda para 99; p continua com 0x1000, logo *p agora reflete 99.",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "99", "active": True, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x1008", "label": "p", "val": "0x1000", "active": False, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-2",
        "num": "1.2",
        "title": "Operadores & (endereço de) e * (desreferenciação / conteúdo apontado)",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.3) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Domine os dois operadores fundamentais de ponteiros: & obtém o endereço de um lvalue e * acessa ou modifica o conteúdo no endereço apontado.",
        "conceptHtml": (
            "<p>Em expressões C, os operadores unários <code>&amp;</code> e <code>*</code> são inversos entre si:</p>"
            "<ul>"
            "<li><strong><code>&amp;var</code> (operador de endereço):</strong> retorna o endereço de memória de um objeto (lvalue), gerando um ponteiro do tipo <code>T *</code> se <code>var</code> for do tipo <code>T</code>.</li>"
            "<li><strong><code>*ptr</code> (operador de indireção ou desreferenciação):</strong> segue o endereço armazenado em <code>ptr</code> para ler ou escrever o valor original armazenado lá.</li>"
            "</ul>"
            "<p>Quando <code>p = &amp;x</code>, vale a identidade <code>*&amp;x == x</code> e <code>*p</code> funciona como um apelido direto para <code>x</code>: tanto <code>y = *p;</code> (leitura) quanto <code>*p = 50;</code> (escrita) atuam diretamente na célula de <code>x</code>.</p>"
        ),
        "code": """#include <stdio.h>

int main(void) {
    int a = 10, b = 0;
    int *p = &a;

    b = *p + 5;   /* le o valor apontado por p (10) e soma 5 */
    *p = 30;      /* escreve 30 diretamente na memoria de 'a' */

    printf("a = %d, b = %d, *p = %d\\n", a, b, *p);
    return 0;
}""",
        "logicSteps": [
            "a inicia com 10 e p recebe &a, passando a apontar para a.",
            "Na expressão b = *p + 5, *p desreferencia p, lê 10 e atribui 15 a b.",
            "Na instrução *p = 30, o operador * à esquerda da atribuição altera o conteúdo de a para 30.",
            "Ao final, a e *p valem 30, enquanto b vale 15."
        ],
        "pitfall": (
            "Não confunda o <code>*</code> da <strong>declaração</strong> (<code>int *p;</code>, que apenas diz que <code>p</code> é um ponteiro) "
            "com o <code>*</code> de <strong>desreferenciação</strong> em expressões (<code>*p = 30;</code>). Além disso, nunca tente aplicar <code>&amp;</code> a literais ou expressões temporárias como <code>&amp;10</code> ou <code>&amp;(a + b)</code> — isso causa erro de compilação (não é lvalue)."
        ),
        "memoryDiagram": {
            "caption": "Desreferenciação *p = 30 altera 'a' sem alterar o endereço guardado em 'p'.",
            "cells": [
                {"idx": 0, "addr": "0x2000", "val": "30", "tag": "int a (modificado via *p)"},
                {"idx": 1, "addr": "0x2004", "val": "15", "tag": "int b"},
                {"idx": 2, "addr": "0x2008", "val": "0x2000", "tag": "int *p -> a"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-2",
                "tabLabel": "Operadores & e *",
                "badge": "1D • Indireção",
                "title": "Leitura e escrita via *p",
                "desc": "Observe a diferença entre ler *p e atribuir a *p.",
                "kind": "1d",
                "codeLines": [
                    "int a = 10, b = 0;",
                    "int *p = &a;",
                    "b = *p + 5;",
                    "*p = 30;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"a": "10", "b": "0", "p": "?"},
                        "note": "a = 10 e b = 0 inicializados na Stack.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "a", "val": "10", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "b", "val": "0", "active": True, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "p", "val": "LIXO", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"a": "10", "b": "0", "p": "0x2000", "*p": "10"},
                        "note": "p recebe &a (0x2000).",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "a", "val": "10", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x2004", "label": "b", "val": "0", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "p", "val": "0x2000", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"a": "10", "b": "15", "p": "0x2000", "*p": "10"},
                        "note": "*p retorna 10; b recebe 10 + 5 = 15.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "a", "val": "10", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x2004", "label": "b", "val": "15", "active": True, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "p", "val": "0x2000", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"a": "30", "b": "15", "p": "0x2000", "*p": "30"},
                        "note": "*p = 30 segue o endereço 0x2000 e sobrescreve 'a' com 30.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "a", "val": "30", "active": True, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x2004", "label": "b", "val": "15", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "p", "val": "0x2000", "active": False, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-3",
        "num": "1.3",
        "title": "Declaração e inicialização: int *p = &x;, tipos (int*, char*, float*) e NULL",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.2) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Aprenda a declarar ponteiros tipados corretamente, inicializar com &var ou NULL e entender por que o tipo apontado importa para o compilador.",
        "conceptHtml": (
            "<p>A sintaxe de declaração é <code>tipo *nome;</code>. Embora todos os ponteiros de dados costumem ter o mesmo tamanho em bytes na arquitetura (ex.: 8 bytes em 64 bits), "
            "o <strong>tipo base</strong> (<code>int*</code>, <code>char*</code>, <code>float*</code>) informa ao compilador duas coisas essenciais:</p>"
            "<ol>"
            "<li><strong>Quantos bytes ler/escrever</strong> ao fazer <code>*p</code> (1 byte para <code>char*</code>, 4 bytes para <code>int*</code>/<code>float*</code>, etc.).</li>"
            "<li><strong>Qual o passo da aritmética</strong> ao somar <code>p + 1</code> (salta <code>sizeof(tipo)</code> bytes).</li>"
            "</ol>"
            "<p>Quando o ponteiro ainda não tem um alvo válido, deve-se inicializá-lo com <code>NULL</code> (macro definida em <code>&lt;stddef.h&gt;</code>, <code>&lt;stdio.h&gt;</code> ou <code>&lt;stdlib.h&gt;</code>), "
            "que representa o endereço nulo — garantia da linguagem de que não aponta para nenhum objeto válido.</p>"
        ),
        "code": """#include <stdio.h>

int main(void) {
    int x = 7;
    char letra = 'A';
    float nota = 8.5f;

    int *pi = &x;
    char *pc = &letra;
    float *pf = &nota;
    int *p_vazio = NULL;

    printf("x=%d, letra=%c, nota=%.1f, p_vazio=%p\\n",
           *pi, *pc, *pf, (void *)p_vazio);
    return 0;
}""",
        "logicSteps": [
            "Declarar int *pi = &x vincula o tipo int * ao endereço de uma variável int.",
            "Ponteiros de tipos incompatíveis (ex.: float *pf = &x;) geram aviso/erro de tipo sem cast explícito.",
            "p_vazio = NULL inicializa o ponteiro com valor sentinela seguro (endereço 0).",
            "Ao desreferenciar *pi, *pc e *pf, o compilador interpreta 4 bytes int, 1 byte char e 4 bytes float IEEE-754."
        ],
        "pitfall": (
            "Cuidado com declarações múltiplas na mesma linha! Em <code>int* a, b;</code>, o asterisco liga-se ao identificador, "
            "portanto apenas <code>a</code> é ponteiro (<code>int *</code>) e <code>b</code> é um <code>int</code> comum! "
            "Para declarar dois ponteiros, escreva <code>int *a, *b;</code>."
        ),
        "memoryDiagram": {
            "caption": "Tipos distintos ocupam tamanhos distintos ao serem desreferenciados, embora os ponteiros armazenem endereços.",
            "cells": [
                {"idx": 0, "addr": "0x3000", "val": "7", "tag": "int x (4B) <- pi"},
                {"idx": 1, "addr": "0x3004", "val": "'A'", "tag": "char letra (1B) <- pc"},
                {"idx": 2, "addr": "0x3008", "val": "8.5", "tag": "float nota (4B) <- pf"},
                {"idx": 3, "addr": "0x3010", "val": "NULL (0x0)", "tag": "int *p_vazio"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-3",
                "tabLabel": "Tipos e NULL",
                "badge": "1D • Tipagem",
                "title": "Inicialização tipada e ponteiro NULL",
                "desc": "Veja cada ponteiro apontando para seu tipo correspondente ou para NULL.",
                "kind": "1d",
                "codeLines": [
                    "int x = 7; char c = 'A';",
                    "int *pi = &x;",
                    "char *pc = &c;",
                    "int *pv = NULL;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"x": "7", "c": "'A'"},
                        "note": "x (4 bytes) e c (1 byte) são alocados.",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "x (int)", "val": "7", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x3004", "label": "c (char)", "val": "'A'", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"x": "7", "pi": "0x3000", "*pi": "7"},
                        "note": "pi (int*) guarda 0x3000 e lê 4 bytes.",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "x (int)", "val": "7", "active": False, "ptrs": ["pi"]},
                            {"idx": 1, "addr": "0x3004", "label": "c (char)", "val": "'A'", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x3008", "label": "pi", "val": "0x3000", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"c": "'A'", "pc": "0x3004", "*pc": "'A'"},
                        "note": "pc (char*) guarda 0x3004 e lê 1 byte.",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "x (int)", "val": "7", "active": False, "ptrs": ["pi"]},
                            {"idx": 1, "addr": "0x3004", "label": "c (char)", "val": "'A'", "active": False, "ptrs": ["pc"]},
                            {"idx": 2, "addr": "0x3008", "label": "pi", "val": "0x3000", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x3010", "label": "pc", "val": "0x3004", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"pv": "NULL"},
                        "note": "pv recebe NULL (0x0), indicando explicitamente que não aponta para nada.",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "x (int)", "val": "7", "active": False, "ptrs": ["pi"]},
                            {"idx": 1, "addr": "0x3004", "label": "c (char)", "val": "'A'", "active": False, "ptrs": ["pc"]},
                            {"idx": 2, "addr": "0x3018", "label": "pv", "val": "NULL", "active": True, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-4",
        "num": "1.4",
        "title": "Ponteiros não inicializados (lixo) e ponteiros nulos: verificação antes do uso",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.2–7.3) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Entenda o perigo dos ponteiros selvagens (wild pointers) contendo lixo de memória e aprenda o padrão defensivo de inicialização e checagem com NULL.",
        "conceptHtml": (
            "<p>Variáveis locais em C (armazenadas na Stack) <strong>não são zeradas automaticamente</strong>. "
            "Se você declarar <code>int *p;</code> sem inicializar, <code>p</code> conterá qualquer sequência de bits que havia antes naquela região da memória — "
            "um <strong>ponteiro selvagem (wild pointer)</strong>.</p>"
            "<p>Tentar desreferenciar um ponteiro não inicializado (<code>*p = 10;</code>) provoca <strong>Comportamento Indefinido (Undefined Behavior)</strong>: "
            "pode corromper outra variável silenciosamente ou gerar um <em>Segmentation Fault (SIGSEGV)</em> imediato.</p>"
            "<p>Da mesma forma, desreferenciar um ponteiro <code>NULL</code> também causa falha de segmentação. A diferença crucial é que "
            "<strong><code>NULL</code> é testável</strong> antes do uso: <code>if (p != NULL) { ... }</code> (ou simplesmente <code>if (p)</code>), ao passo que lixo de memória é indistinguível de um endereço real.</p>"
        ),
        "code": """#include <stdio.h>

void imprimir_seguro(const int *p) {
    if (p == NULL) {
        printf("Ponteiro nulo: acesso bloqueado com seguranca.\\n");
        return;
    }
    printf("Valor apontado: %d\\n", *p);
}

int main(void) {
    int valor = 100;
    int *p = NULL;        /* nunca deixe int *p; sem inicializar */

    imprimir_seguro(p);   /* seguro: cai no if (p == NULL) */
    p = &valor;
    imprimir_seguro(p);   /* seguro: p agora aponta para valor */
    return 0;
}""",
        "logicSteps": [
            "Inicializar int *p = NULL elimina o risco de lixo de memória aleatório.",
            "Antes de qualquer desreferenciação *p, verificar if (p != NULL) ou if (p == NULL) return;",
            "Na primeira chamada a imprimir_seguro(p), p é NULL e a função retorna sem executar *p.",
            "Após p = &valor, o teste passa e *p imprime 100 com segurança."
        ],
        "pitfall": (
            "Nunca escreva <code>int *p; if (p != NULL) *p = 5;</code> achando que está seguro! "
            "Um ponteiro não inicializado contém <strong>lixo</strong> (quase nunca é <code>NULL</code>), então o <code>if (p != NULL)</code> "
            "será verdadeiro e você desreferenciará um endereço inválido!"
        ),
        "memoryDiagram": {
            "caption": "Comparação entre ponteiro selvagem (lixo imprevisível) e ponteiro inicializado com NULL.",
            "cells": [
                {"idx": 0, "addr": "0x4000", "val": "0x7FA3B10C (lixo)", "tag": "int *wild (PERIGO!)"},
                {"idx": 1, "addr": "0x4008", "val": "NULL (0x0)", "tag": "int *seguro (testável)"},
                {"idx": 2, "addr": "0x4010", "val": "100", "tag": "int valor"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-4",
                "tabLabel": "Verificação NULL",
                "badge": "1D • Segurança",
                "title": "Guarda defensiva antes da desreferenciação",
                "desc": "Acompanhe o fluxo condicional evitando Segmentation Fault.",
                "kind": "1d",
                "codeLines": [
                    "int valor = 100;",
                    "int *p = NULL;",
                    "if (p != NULL) { *p = 200; }",
                    "p = &valor;",
                    "if (p != NULL) { *p = 200; }"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"valor": "100", "p": "?"},
                        "note": "valor nasce com 100.",
                        "cells": [
                            {"idx": 0, "addr": "0x4010", "label": "valor", "val": "100", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x4018", "label": "p", "val": "LIXO", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"valor": "100", "p": "NULL"},
                        "note": "p é inicializado com NULL.",
                        "cells": [
                            {"idx": 0, "addr": "0x4010", "label": "valor", "val": "100", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x4018", "label": "p", "val": "NULL", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"valor": "100", "p": "NULL"},
                        "note": "p != NULL é falso! O bloco *p = 200 é ignorado sem crash.",
                        "cells": [
                            {"idx": 0, "addr": "0x4010", "label": "valor", "val": "100", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x4018", "label": "p", "val": "NULL", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"valor": "100", "p": "0x4010"},
                        "note": "p passa a apontar para valor (0x4010).",
                        "cells": [
                            {"idx": 0, "addr": "0x4010", "label": "valor", "val": "100", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x4018", "label": "p", "val": "0x4010", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"valor": "200", "p": "0x4010", "*p": "200"},
                        "note": "p != NULL é verdadeiro! *p = 200 altera valor para 200.",
                        "cells": [
                            {"idx": 0, "addr": "0x4010", "label": "valor", "val": "200", "active": True, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x4018", "label": "p", "val": "0x4010", "active": False, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-5",
        "num": "1.5",
        "title": "Impressão de endereços: printf(\"%p\", (void *)p) e o cast obrigatório (void *)",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.3) / C99–C11 §7.21.6.1 (fprintf %p)",
        "summary": "Saiba por que o especificador %p exige um argumento do tipo void * segundo o padrão ISO C e como evitar comportamento indefinido em printf.",
        "conceptHtml": (
            "<p>Para imprimir um endereço de memória no console com <code>printf</code>, o especificador correto do padrão C é <strong><code>%p</code></strong> (exibido tipicamente em hexadecimal, como <code>0x7ffd4a2c</code>).</p>"
            "<p>Pela especificação ISO C99/C11, funções variádicas como <code>printf</code> não realizam conversão automática de ponteiros tipados (como <code>int *</code> ou <code>char *</code>) para <code>void *</code>, "
            "pois <code>printf</code> não conhece o protótipo dos argumentos após a string de formato. Assim, o padrão exige explicitamente que o argumento correspondente a <code>%p</code> seja do tipo <code>void *</code>: "
            "<strong><code>printf(\"%p\", (void *)p);</code></strong>.</p>"
            "<p>Também podemos imprimir o endereço da própria variável ponteiro usando <code>(void *)&amp;p</code>.</p>"
        ),
        "code": """#include <stdio.h>

int main(void) {
    int x = 55;
    int *p = &x;

    printf("Endereco de x (&x): %p\\n", (void *)&x);
    printf("Conteudo de p (p):  %p\\n", (void *)p);
    printf("Endereco de p (&p): %p\\n", (void *)&p);
    printf("Conteudo apontado (*p): %d\\n", *p);
    return 0;
}""",
        "logicSteps": [
            "&x e p possuem o mesmo valor (o endereço de x), mas tipos int * que devem ser convertidos com (void *).",
            "&p retorna o endereço onde a própria variável ponteiro p mora (tipo int **), também convertido com (void *).",
            "Passar p diretamente sem (void *) em %p viola o padrão ISO C (aviso -Wformat / -Wpedantic).",
            "Nunca use %d ou %u para imprimir ponteiros, pois em sistemas 64 bits o endereço tem 8 bytes e será truncado."
        ],
        "pitfall": (
            "Usar <code>printf(\"%d\", p)</code> ou esquecer o cast <code>(void *)</code> com <code>%p</code>. "
            "Em arquiteturas de 64 bits, <code>%d</code> lê apenas 4 bytes e exibe um número negativo sem sentido; "
            "já omitir <code>(void *)</code> é explicitamente <em>Undefined Behavior</em> na norma C (embora alguns compiladores tolerem em x86_64, <code>-Wformat</code> acusa erro/aviso)."
        ),
        "memoryDiagram": {
            "caption": "Três expressões diferentes em printf: (void *)p == (void *)&x, diferente de (void *)&p.",
            "cells": [
                {"idx": 0, "addr": "0x5000", "val": "55", "tag": "x (impresso via *p)"},
                {"idx": 1, "addr": "0x5008", "val": "0x5000", "tag": "p (&p = 0x5008, p = 0x5000)"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-5",
                "tabLabel": "p vs &p vs *p",
                "badge": "1D • Endereços",
                "title": "Distinção entre &x, p, &p e *p",
                "desc": "Veja exatamente o que cada expressão avalia na impressão.",
                "kind": "1d",
                "codeLines": [
                    "int x = 55;",
                    "int *p = &x;",
                    "printf(\"%p\", (void *)p);",
                    "printf(\"%p\", (void *)&p);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"x": "55", "&x": "0x5000"},
                        "note": "x reside em 0x5000 com valor 55.",
                        "cells": [
                            {"idx": 0, "addr": "0x5000", "label": "x", "val": "55", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"x": "55", "p": "0x5000", "&p": "0x5008"},
                        "note": "p reside em 0x5008 e guarda 0x5000.",
                        "cells": [
                            {"idx": 0, "addr": "0x5000", "label": "x", "val": "55", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x5008", "label": "p", "val": "0x5000", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"(void*)p": "0x5000", "saida": "0x5000"},
                        "note": "Imprime o CONTEÚDO de p, que é o endereço de x (0x5000).",
                        "cells": [
                            {"idx": 0, "addr": "0x5000", "label": "x", "val": "55", "active": True, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x5008", "label": "p", "val": "0x5000", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"(void*)&p": "0x5008", "saida": "0x5008"},
                        "note": "Imprime o ENDEREÇO onde a variável p está armazenada (0x5008).",
                        "cells": [
                            {"idx": 0, "addr": "0x5000", "label": "x", "val": "55", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x5008", "label": "p", "val": "0x5000", "active": True, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-6",
        "num": "1.6",
        "title": "Aritmética de ponteiros: p++, p--, p+k, p2-p1, deslocamento proporcional a sizeof(tipo)",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.6) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Compreenda por que somar 1 a um ponteiro não soma 1 byte, e sim sizeof(tipo) bytes, e como subtrair dois ponteiros retorna a distância em elementos.",
        "conceptHtml": (
            "<p>A aritmética de ponteiros é escalonada pelo tamanho do tipo apontado. Se <code>p</code> é do tipo <code>T *</code> e armazena o endereço <code>E</code>, então:</p>"
            "<ul>"
            "<li><strong><code>p + k</code></strong> resulta no endereço <code>E + k * sizeof(T)</code>. Para <code>int *p</code> (4 bytes), <code>p + 2</code> avança <strong>8 bytes</strong>. Para <code>double *d</code> (8 bytes), <code>d + 2</code> avança <strong>16 bytes</strong>.</li>"
            "<li><strong><code>p++</code> / <code>p--</code></strong> avança ou recua o ponteiro exatamente 1 elemento (<code>sizeof(T)</code> bytes).</li>"
            "<li><strong><code>p2 - p1</code></strong> (quando ambos apontam para o mesmo vetor) retorna o número de <strong>elementos</strong> entre eles (do tipo <code>ptrdiff_t</code>), e não a diferença em bytes!</li>"
            "</ul>"
            "<p>Operações proibidas em ponteiros: somar dois ponteiros (<code>p1 + p2</code>), multiplicar ou dividir ponteiros (<code>p * 2</code>).</p>"
        ),
        "code": """#include <stdio.h>
#include <stddef.h>

int main(void) {
    int v[4] = {10, 20, 30, 40};
    int *p1 = &v[0];
    int *p2 = p1 + 3;          /* aponta para v[3] (+ 3 * sizeof(int) bytes) */

    ptrdiff_t dist = p2 - p1;  /* diferenca em elementos: 3 */
    p1++;                      /* agora aponta para v[1] */

    printf("*p1 = %d, *p2 = %d, p2 - p1 = %td\\n", *p1, *p2, p2 - p1);
    printf("Distancia inicial: %td elementos\\n", dist);
    return 0;
}""",
        "logicSteps": [
            "p1 começa apontando para v[0] (ex.: endereço 0x1000).",
            "p2 = p1 + 3 calcula 0x1000 + 3 * 4 = 0x100C, alcançando v[3] (40).",
            "p2 - p1 divide a diferença em bytes (12) por sizeof(int) (4), resultando em 3 elementos.",
            "p1++ avança 4 bytes para 0x1004 (v[1]), fazendo a nova diferença p2 - p1 ser 2."
        ],
        "pitfall": (
            "Em provas de concurso e faculdade, é clássico perguntar: 'Se <code>int *p = 0x1000</code> (com <code>int</code> de 4 bytes), "
            "quanto vale <code>p + 3</code>?' Muitos alunos respondem <code>0x1003</code>, mas a resposta correta é <code>0x100C</code> (1000 + 12 em hexa). "
            "Além disso, cuidado com a precedência: <code>*p++</code> lê <code>*p</code> e depois incrementa o <strong>ponteiro</strong> <code>p</code>; já <code>(*p)++</code> incrementa o <strong>valor</strong> apontado."
        ),
        "memoryDiagram": {
            "caption": "Vetor int v[4] (sizeof(int)=4): cada +1 no ponteiro salta 4 bytes na RAM.",
            "cells": [
                {"idx": 0, "addr": "0x1000", "val": "10", "tag": "v[0]"},
                {"idx": 1, "addr": "0x1004", "val": "20", "tag": "v[1] <- p1 (após p1++)"},
                {"idx": 2, "addr": "0x1008", "val": "30", "tag": "v[2]"},
                {"idx": 3, "addr": "0x100C", "val": "40", "tag": "v[3] <- p2 (p1+3)"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-6",
                "tabLabel": "Aritmética +k e p2-p1",
                "badge": "1D • Aritmética",
                "title": "Deslocamento proporcional a sizeof(int) = 4",
                "desc": "Observe os endereços saltando de 4 em 4 bytes e a subtração de ponteiros.",
                "kind": "1d",
                "codeLines": [
                    "int v[4] = {10, 20, 30, 40};",
                    "int *p1 = v;",
                    "int *p2 = p1 + 3;",
                    "p1++;",
                    "int d = (int)(p2 - p1);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"sizeof(int)": "4"},
                        "note": "Vetor v alocado em blocos contíguos de 4 bytes (0x1000 a 0x100C).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "v[0]", "val": "10", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x1004", "label": "v[1]", "val": "20", "active": True, "ptrs": []},
                            {"idx": 2, "addr": "0x1008", "label": "v[2]", "val": "30", "active": True, "ptrs": []},
                            {"idx": 3, "addr": "0x100C", "label": "v[3]", "val": "40", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"p1": "0x1000", "*p1": "10"},
                        "note": "p1 aponta para v[0] (0x1000).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "v[0]", "val": "10", "active": True, "ptrs": ["p1"]},
                            {"idx": 1, "addr": "0x1004", "label": "v[1]", "val": "20", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x1008", "label": "v[2]", "val": "30", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x100C", "label": "v[3]", "val": "40", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"p1": "0x1000", "p2": "0x100C", "*p2": "40"},
                        "note": "p1 + 3 avança 3 * 4 = 12 bytes -> 0x100C (v[3]).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "v[0]", "val": "10", "active": False, "ptrs": ["p1"]},
                            {"idx": 1, "addr": "0x1004", "label": "v[1]", "val": "20", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x1008", "label": "v[2]", "val": "30", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x100C", "label": "v[3]", "val": "40", "active": True, "ptrs": ["p2"]}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"p1": "0x1004", "*p1": "20", "p2": "0x100C"},
                        "note": "p1++ avança 4 bytes -> 0x1004 (v[1]).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "v[0]", "val": "10", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x1004", "label": "v[1]", "val": "20", "active": True, "ptrs": ["p1"]},
                            {"idx": 2, "addr": "0x1008", "label": "v[2]", "val": "30", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x100C", "label": "v[3]", "val": "40", "active": False, "ptrs": ["p2"]}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"p1": "0x1004", "p2": "0x100C", "d": "2"},
                        "note": "p2 - p1 = (0x100C - 0x1004) / 4 = 8 / 4 = 2 elementos.",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "v[0]", "val": "10", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x1004", "label": "v[1]", "val": "20", "active": True, "ptrs": ["p1"]},
                            {"idx": 2, "addr": "0x1008", "label": "v[2]", "val": "30", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x100C", "label": "v[3]", "val": "40", "active": True, "ptrs": ["p2"]}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-7",
        "num": "1.7",
        "title": "Ponteiros e vetores: v como endereço do 1º elemento e equivalência v[i] == *(v + i)",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.7) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Descubra o decaimento de vetores para ponteiros (array decay), a equivalência exata v[i] == *(v + i) e a diferença entre v e um ponteiro modificável.",
        "conceptHtml": (
            "<p>Em C, na maioria das expressões, o nome de um vetor <code>v</code> <strong>decai</strong> (<em>array-to-pointer decay</em>) para o endereço do seu primeiro elemento: "
            "<strong><code>v == &amp;v[0]</code></strong>. Por definição da linguagem, o operador de subscrito <code>[]</code> é açúcar sintático para aritmética de ponteiros:</p>"
            "<p><code>v[i] &equiv; *(v + i) &equiv; *(i + v) &equiv; i[v]</code> e <code>&amp;v[i] &equiv; v + i</code>.</p>"
            "<p><strong>Atenção à diferença fundamental:</strong> embora <code>v</code> decaia para <code>int *</code>, <code>v</code> <strong>não é uma variável ponteiro</strong>! "
            "Você não pode fazer <code>v++</code> ou <code>v = p</code>, pois <code>v</code> não é um lvalue modificável. Além disso, em <code>sizeof(v)</code> e <code>&amp;v</code>, o vetor <strong>não</strong> decai: "
            "<code>sizeof(v)</code> retorna o tamanho total do vetor em bytes, enquanto <code>sizeof(p)</code> retorna apenas o tamanho do ponteiro.</p>"
        ),
        "code": """#include <stdio.h>

int main(void) {
    int v[4] = {5, 10, 15, 20};
    int *p = v; /* equivalente a int *p = &v[0]; */

    for (int i = 0; i < 4; i++) {
        printf("v[%d]=%d | *(v+%d)=%d | p[%d]=%d | *(p+%d)=%d\\n",
               i, v[i], i, *(v + i), i, p[i], i, *(p + i));
    }
    printf("sizeof(v)=%zu, sizeof(p)=%zu\\n", sizeof(v), sizeof(p));
    return 0;
}""",
        "logicSteps": [
            "int *p = v atribui o endereço &v[0] ao ponteiro modificável p.",
            "Para qualquer índice i, v[i], *(v + i), p[i] e *(p + i) acessam exatamente o mesmo elemento.",
            "sizeof(v) avalia o vetor inteiro (4 * 4 = 16 bytes), pois sizeof não sofre decay.",
            "sizeof(p) avalia apenas o tamanho do ponteiro (4 ou 8 bytes)."
        ],
        "pitfall": (
            "Tentar executar <code>v++</code> em um vetor declarado localmente (<code>int v[4];</code>) causa erro de compilação (<em>lvalue required as increment operand</em>). "
            "Por outro lado, em um parâmetro de função <code>void f(int v[])</code>, o compilador converte <code>int v[]</code> para <code>int *v</code>, e aí sim <code>v++</code> e <code>sizeof(v)</code> comportam-se como ponteiro!"
        ),
        "memoryDiagram": {
            "caption": "Equivalência v[i] == *(v + i) == *(p + i) == p[i] sobre o mesmo bloco contíguo.",
            "cells": [
                {"idx": 0, "addr": "0x2000", "val": "5", "tag": "v[0] / *(v+0) <- v, p"},
                {"idx": 1, "addr": "0x2004", "val": "10", "tag": "v[1] / *(v+1)"},
                {"idx": 2, "addr": "0x2008", "val": "15", "tag": "v[2] / *(v+2)"},
                {"idx": 3, "addr": "0x200C", "val": "20", "tag": "v[3] / *(v+3)"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-7",
                "tabLabel": "v[i] vs *(p+i)",
                "badge": "1D • Vetores",
                "title": "Percurso por ponteiro equivalente ao índice",
                "desc": "Veja p percorrendo o vetor v com *(p + i) e p++.",
                "kind": "1d",
                "codeLines": [
                    "int v[4] = {5, 10, 15, 20};",
                    "int *p = v;",
                    "*(p + 2) = 99;",
                    "p = p + 1;",
                    "p[1] = 77;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"v": "{5,10,15,20}"},
                        "note": "Vetor v criado na memória.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "5", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "10", "active": True, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "15", "active": True, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "20", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"p": "0x2000", "*p": "5"},
                        "note": "p recebe v (&v[0]).",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "5", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "10", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "15", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "20", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"p": "0x2000", "*(p+2)": "99", "v[2]": "99"},
                        "note": "*(p + 2) acessa v[2] e grava 99.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "5", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "10", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "99", "active": True, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "20", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"p": "0x2004", "*p": "10"},
                        "note": "p avança para v[1] (0x2004).",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "5", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "10", "active": True, "ptrs": ["p"]},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "99", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "20", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"p": "0x2004", "p[1]": "77", "v[2]": "77"},
                        "note": "Como p aponta para v[1], p[1] equivale a *(p + 1), ou seja, v[2] = 77!",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "5", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "10", "active": False, "ptrs": ["p"]},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "77", "active": True, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "20", "active": False, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-8",
        "num": "1.8",
        "title": "Ponteiros e strings: percurso de char * até '\\0', diferença entre char s[] (mutável) e char *s (literal read-only)",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.7–7.10) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Percorra strings usando apenas char * e condição *p != '\\0', e evite travamentos ao distinguir arrays mutáveis de literais em memória somente leitura.",
        "conceptHtml": (
            "<p>Em C, uma string é um vetor de caracteres terminado pelo caractere nulo <strong><code>'\\0'</code></strong> (valor ASCII 0). "
            "Podemos percorrer qualquer string com um ponteiro <code>char *p</code> incrementando-o até encontrar o terminador: <code>while (*p != '\\0') { ... p++; }</code>.</p>"
            "<p>Existe uma diferença crítica entre as duas formas abaixo:</p>"
            "<ul>"
            "<li><strong><code>char s[] = \"ADS\";</code></strong> — Cria um <strong>vetor mutável na Stack</strong> de 4 bytes (<code>'A','D','S','\\0'</code>) copiando o literal. Você <strong>pode</strong> fazer <code>s[0] = 'X';</code>, mas <strong>não</strong> pode fazer <code>s++</code>.</li>"
            "<li><strong><code>const char *p = \"ADS\";</code></strong> (ou <code>char *p = \"ADS\";</code>) — Cria um <strong>ponteiro</strong> na Stack que aponta para a string literal armazenada na seção <strong>somente leitura (.rodata)</strong> do executável. Você <strong>pode</strong> fazer <code>p++</code>, mas tentar modificar <code>p[0] = 'X';</code> causa <strong>Undefined Behavior / Segmentation Fault</strong>!</li>"
            "</ul>"
        ),
        "code": """#include <stdio.h>

size_t meu_strlen(const char *s) {
    const char *inicio = s;
    while (*s != '\\0') {
        s++;
    }
    return (size_t)(s - inicio);
}

int main(void) {
    char mutavel[] = "C99";     /* array na Stack: pode alterar caracteres */
    const char *lit = "ADS";    /* ponteiro para .rodata: nao altere *lit */

    mutavel[0] = 'c';
    printf("%s (len=%zu), %s (len=%zu)\\n",
           mutavel, meu_strlen(mutavel), lit, meu_strlen(lit));
    return 0;
}""",
        "logicSteps": [
            "inicio guarda o endereço do primeiro caractere de s.",
            "Enquanto *s != '\\0', o ponteiro s avança 1 byte (sizeof(char) == 1) por iteração.",
            "Quando *s == '\\0', s aponta exatamente para o terminador nulo.",
            "A subtração s - inicio retorna o tamanho da string sem contar o '\\0'."
        ],
        "pitfall": (
            "Escrever <code>char *s = \"ola\"; s[0] = 'O';</code>. Em C, literais de string residem em área protegida de memória; "
            "tentar modificá-los provoca crash (Segmentation Fault) em sistemas modernos. Sempre use <code>const char *s = \"ola\";</code> para literais e <code>char s[] = \"ola\";</code> quando precisar editar."
        ),
        "memoryDiagram": {
            "caption": "char mutavel[] copia bytes para a Stack; const char *lit aponta para .rodata (somente leitura).",
            "cells": [
                {"idx": 0, "addr": "Stack 0x6000", "val": "'c','9','9','\\0'", "tag": "mutavel[] (editável)"},
                {"idx": 1, "addr": "Stack 0x6010", "val": "0x00400800", "tag": "const char *lit"},
                {"idx": 2, "addr": ".rodata 0x400800", "val": "'A','D','S','\\0'", "tag": "Literal (READ-ONLY)"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-8",
                "tabLabel": "Percurso até '\\0'",
                "badge": "1D • Strings",
                "title": "Calculando strlen via ponteiro s - inicio",
                "desc": "Acompanhe o ponteiro s caminhando byte a byte até o '\\0'.",
                "kind": "1d",
                "codeLines": [
                    "char s[] = \"ADS\";",
                    "char *ini = s, *p = s;",
                    "while (*p != '\\0') p++;",
                    "int len = (int)(p - ini);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"s": "\"ADS\""},
                        "note": "Array mutável com 4 bytes ('A','D','S','\\0') na Stack.",
                        "cells": [
                            {"idx": 0, "addr": "0x6000", "label": "s[0]", "val": "'A'", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x6001", "label": "s[1]", "val": "'D'", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x6002", "label": "s[2]", "val": "'S'", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x6003", "label": "s[3]", "val": "'\\0'", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"ini": "0x6000", "p": "0x6000", "*p": "'A'"},
                        "note": "ini e p apontam para o primeiro byte ('A').",
                        "cells": [
                            {"idx": 0, "addr": "0x6000", "label": "s[0]", "val": "'A'", "active": True, "ptrs": ["ini", "p"]},
                            {"idx": 1, "addr": "0x6001", "label": "s[1]", "val": "'D'", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x6002", "label": "s[2]", "val": "'S'", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x6003", "label": "s[3]", "val": "'\\0'", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"ini": "0x6000", "p": "0x6003", "*p": "'\\0'"},
                        "note": "p avança por 'A', 'D', 'S' e para ao encontrar '\\0' em 0x6003.",
                        "cells": [
                            {"idx": 0, "addr": "0x6000", "label": "s[0]", "val": "'A'", "active": False, "ptrs": ["ini"]},
                            {"idx": 1, "addr": "0x6001", "label": "s[1]", "val": "'D'", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x6002", "label": "s[2]", "val": "'S'", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x6003", "label": "s[3]", "val": "'\\0'", "active": True, "ptrs": ["p"]}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"ini": "0x6000", "p": "0x6003", "len": "3"},
                        "note": "len = p - ini = 0x6003 - 0x6000 = 3 caracteres.",
                        "cells": [
                            {"idx": 0, "addr": "0x6000", "label": "s[0]", "val": "'A'", "active": False, "ptrs": ["ini"]},
                            {"idx": 1, "addr": "0x6001", "label": "s[1]", "val": "'D'", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x6002", "label": "s[2]", "val": "'S'", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x6003", "label": "s[3]", "val": "'\\0'", "active": True, "ptrs": ["p"]}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-9",
        "num": "1.9",
        "title": "Passagem de parâmetros por referência: troca(int *a, int *b) modificando o chamador",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.4) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Entenda como simular passagem por referência em C passando endereços por valor, permitindo que uma função altere variáveis do chamador.",
        "conceptHtml": (
            "<p>A linguagem C sempre passa argumentos <strong>por valor</strong> (cópia). Por isso, uma função <code>void troca(int x, int y)</code> recebe apenas cópias locais e não consegue alterar as variáveis originais da <code>main</code>.</p>"
            "<p>Para simular a <strong>passagem por referência</strong>, a função recebe <strong>ponteiros</strong> (<code>int *a, int *b</code>), e o chamador passa os endereços (<code>troca(&amp;x, &amp;y);</code>). "
            "Os endereços são copiados para os parâmetros <code>a</code> e <code>b</code>; quando a função executa <code>*a</code> e <code>*b</code>, ela acessa diretamente a memória da função chamadora!</p>"
        ),
        "code": """#include <stdio.h>

void troca(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 10, y = 25;
    troca(&x, &y);
    printf("x = %d, y = %d\\n", x, y); /* x = 25, y = 10 */
    return 0;
}""",
        "logicSteps": [
            "main chama troca(&x, &y), copiando os endereços 0x1000 e 0x1004 para os parâmetros a e b.",
            "temp lê o conteúdo de *a (10).",
            "*a = *b lê 25 do endereço de y e grava em x.",
            "*b = temp grava 10 no endereço de y; ao retornar, x=25 e y=10 na main."
        ],
        "pitfall": (
            "Trocar os próprios ponteiros dentro da função (<code>int *t = a; a = b; b = t;</code>) em vez de trocar os conteúdos apontados (<code>*a</code> e <code>*b</code>)! "
            "Como <code>a</code> e <code>b</code> são cópias locais dos endereços, reatribuir <code>a = b</code> não altera nada na <code>main</code>."
        ),
        "memoryDiagram": {
            "caption": "Frame de troca() acessando variáveis do frame de main() via ponteiros a e b.",
            "cells": [
                {"idx": 0, "addr": "main: 0x1000", "val": "25 (era 10)", "tag": "int x <- a"},
                {"idx": 1, "addr": "main: 0x1004", "val": "10 (era 25)", "tag": "int y <- b"},
                {"idx": 2, "addr": "troca: 0x0FE0", "val": "0x1000", "tag": "int *a"},
                {"idx": 3, "addr": "troca: 0x0FE8", "val": "0x1004", "tag": "int *b"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-9",
                "tabLabel": "troca(&x, &y)",
                "badge": "1D • Referência",
                "title": "Troca de variáveis entre frames via ponteiros",
                "desc": "Veja como temp, *a e *b alteram x e y do chamador.",
                "kind": "1d",
                "codeLines": [
                    "int x = 10, y = 25;",
                    "/* troca(&x, &y) */ int *a = &x, *b = &y;",
                    "int temp = *a;",
                    "*a = *b;",
                    "*b = temp;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"x": "10", "y": "25"},
                        "note": "x e y criados no frame da main.",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "10", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "25", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"x": "10", "y": "25", "a": "0x1000", "b": "0x1004"},
                        "note": "Parâmetros a e b recebem &x e &y.",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "10", "active": False, "ptrs": ["a"]},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "25", "active": False, "ptrs": ["b"]}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"x": "10", "y": "25", "temp": "10"},
                        "note": "temp salva *a (10).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "10", "active": True, "ptrs": ["a"]},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "25", "active": False, "ptrs": ["b"]},
                            {"idx": 2, "addr": "0x0FD8", "label": "temp", "val": "10", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"x": "25", "y": "25", "temp": "10"},
                        "note": "*a = *b copia 25 para x.",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "25", "active": True, "ptrs": ["a"]},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "25", "active": False, "ptrs": ["b"]},
                            {"idx": 2, "addr": "0x0FD8", "label": "temp", "val": "10", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"x": "25", "y": "10", "temp": "10"},
                        "note": "*b = temp copia 10 para y. Troca concluída!",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "25", "active": False, "ptrs": ["a"]},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "10", "active": True, "ptrs": ["b"]},
                            {"idx": 2, "addr": "0x0FD8", "label": "temp", "val": "10", "active": False, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-10",
        "num": "1.10",
        "title": "Funções que retornam múltiplos valores via ponteiros (ex.: menor e maior de um vetor)",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.4) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Use parâmetros de saída (out-parameters) com ponteiros para retornar dois ou mais resultados simultaneamente a partir de uma única função.",
        "conceptHtml": (
            "<p>Como o comando <code>return</code> de C devolve apenas um único valor (ou nenhum, em funções <code>void</code>), "
            "é padrão idiomático em C receber <strong>ponteiros como parâmetros de saída</strong> (<em>out-parameters</em>).</p>"
            "<p>A função pode ainda reservar o valor de retorno oficial para indicar <strong>status de sucesso/erro</strong> (ex.: retornar <code>0</code> em sucesso e <code>-1</code> se o vetor for vazio ou ponteiro nulo), "
            "enquanto preenche <code>*menor</code> e <code>*maior</code> diretamente na memória do chamador.</p>"
        ),
        "code": """#include <stdio.h>

int min_max(const int *v, int n, int *menor, int *maior) {
    if (v == NULL || n <= 0 || menor == NULL || maior == NULL) {
        return -1;
    }
    *menor = v[0];
    *maior = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < *menor) *menor = v[i];
        if (v[i] > *maior) *maior = v[i];
    }
    return 0;
}

int main(void) {
    int dados[5] = {18, 4, 42, -3, 15};
    int mn, mx;
    if (min_max(dados, 5, &mn, &mx) == 0) {
        printf("Menor = %d, Maior = %d\\n", mn, mx);
    }
    return 0;
}""",
        "logicSteps": [
            "Valida ponteiros e tamanho n <= 0 antes de desreferenciar qualquer argumento.",
            "Inicializa *menor e *maior com o primeiro elemento v[0].",
            "Percorre de i = 1 até n - 1 comparando v[i] com *menor e *maior e atualizando diretamente mn e mx.",
            "Retorna 0 para sinalizar ao chamador que os valores em mn e mx são válidos."
        ],
        "pitfall": (
            "Esquecer de inicializar <code>*menor</code> e <code>*maior</code> com <code>v[0]</code> antes do laço, confiando em lixo que estava em <code>mn</code> e <code>mx</code> na <code>main</code>! "
            "Outro erro clássico é tentar retornar o endereço de uma variável local (<code>int local; return &amp;local;</code>), gerando um ponteiro pendente (dangling) assim que a função termina."
        ),
        "memoryDiagram": {
            "caption": "min_max recebe const int *v (leitura) e escreve os resultados em &mn e &mx.",
            "cells": [
                {"idx": 0, "addr": "0x2000", "val": "{18,4,42,-3,15}", "tag": "dados[5] (const int *v)"},
                {"idx": 1, "addr": "0x2020", "val": "-3", "tag": "mn <- *menor"},
                {"idx": 2, "addr": "0x2024", "val": "42", "tag": "mx <- *maior"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-10",
                "tabLabel": "min_max via Ponteiros",
                "badge": "1D • Out-Params",
                "title": "Retornando menor e maior via parâmetros ponteiro",
                "desc": "Acompanhe as atualizações em *menor (mn) e *maior (mx) ao longo do vetor.",
                "kind": "1d",
                "codeLines": [
                    "int v[4] = {18, 4, 42, -3};",
                    "*menor = v[0]; *maior = v[0];",
                    "/* i=1 (4) */ if (v[1] < *menor) *menor = v[1];",
                    "/* i=2 (42) */ if (v[2] > *maior) *maior = v[2];",
                    "/* i=3 (-3) */ if (v[3] < *menor) *menor = v[3];"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"mn": "?", "mx": "?"},
                        "note": "Vetor dados = {18, 4, 42, -3}; mn e mx ainda sem valor.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "18", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "4", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "42", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "-3", "active": False, "ptrs": []},
                            {"idx": 4, "addr": "0x2020", "label": "mn", "val": "?", "active": False, "ptrs": ["menor"]},
                            {"idx": 5, "addr": "0x2024", "label": "mx", "val": "?", "active": False, "ptrs": ["maior"]}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"*menor": "18", "*maior": "18"},
                        "note": "*menor e *maior inicializados com v[0] = 18.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "18", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "4", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "42", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "-3", "active": False, "ptrs": []},
                            {"idx": 4, "addr": "0x2020", "label": "mn", "val": "18", "active": True, "ptrs": ["menor"]},
                            {"idx": 5, "addr": "0x2024", "label": "mx", "val": "18", "active": True, "ptrs": ["maior"]}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"i": "1", "v[1]": "4", "*menor": "4", "*maior": "18"},
                        "note": "4 < 18 -> *menor atualizado para 4 (mn = 4).",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "18", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "4", "active": True, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "42", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "-3", "active": False, "ptrs": []},
                            {"idx": 4, "addr": "0x2020", "label": "mn", "val": "4", "active": True, "ptrs": ["menor"]},
                            {"idx": 5, "addr": "0x2024", "label": "mx", "val": "18", "active": False, "ptrs": ["maior"]}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"i": "2", "v[2]": "42", "*menor": "4", "*maior": "42"},
                        "note": "42 > 18 -> *maior atualizado para 42 (mx = 42).",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "18", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "4", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "42", "active": True, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "-3", "active": False, "ptrs": []},
                            {"idx": 4, "addr": "0x2020", "label": "mn", "val": "4", "active": False, "ptrs": ["menor"]},
                            {"idx": 5, "addr": "0x2024", "label": "mx", "val": "42", "active": True, "ptrs": ["maior"]}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"i": "3", "v[3]": "-3", "*menor": "-3", "*maior": "42"},
                        "note": "-3 < 4 -> *menor atualizado para -3 (mn = -3).",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "18", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "4", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "42", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "-3", "active": True, "ptrs": []},
                            {"idx": 4, "addr": "0x2020", "label": "mn", "val": "-3", "active": True, "ptrs": ["menor"]},
                            {"idx": 5, "addr": "0x2024", "label": "mx", "val": "42", "active": False, "ptrs": ["maior"]}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-11",
        "num": "1.11",
        "title": "Ponteiro para ponteiro (int **pp): dupla indireção, uso em matrizes dinâmicas e parâmetros",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 / C Completo e Total Cap. 5 (Indireção Múltipla) / Padrão C99–C11",
        "summary": "Domine a dupla indireção (int **pp): quando uma função precisa alterar para onde um ponteiro do chamador aponta, ou na criação de vetores de ponteiros.",
        "conceptHtml": (
            "<p>Se um ponteiro <code>int *p</code> é uma variável na memória que guarda o endereço de um <code>int</code>, então <code>p</code> também tem seu próprio endereço <code>&amp;p</code>. "
            "O tipo de <code>&amp;p</code> é <strong><code>int **</code></strong> (ponteiro para ponteiro para <code>int</code>).</p>"
            "<p>Para chegar ao inteiro original a partir de <code>pp</code>, aplicamos <strong>dupla indireção</strong>:</p>"
            "<ul>"
            "<li><code>pp</code> contém o endereço de <code>p</code>;</li>"
            "<li><code>*pp</code> acessa o próprio ponteiro <code>p</code> (o endereço de <code>x</code>);</li>"
            "<li><code>**pp</code> acessa o inteiro <code>x</code>.</li>"
            "</ul>"
            "<p>Os dois principais usos práticos de <code>T **</code> são: (1) permitir que uma função aloque memória ou redirecione um ponteiro do chamador (ex.: <code>alocar(&amp;ptr, n)</code> ou inserção no início de lista encadeada) e "
            "(2) representar matrizes dinâmicas como um vetor de ponteiros para linhas (<code>int **m</code>).</p>"
        ),
        "code": """#include <stdio.h>
#include <stdlib.h>

int alocar_vetor(int **pp, int n) {
    *pp = malloc((size_t)n * sizeof(**pp));
    if (*pp == NULL) return -1;
    for (int i = 0; i < n; i++) {
        (*pp)[i] = (i + 1) * 10;
    }
    return 0;
}

int main(void) {
    int x = 5;
    int *p = &x;
    int **pp = &p;
    **pp = 88; /* altera x para 88 */

    int *din = NULL;
    if (alocar_vetor(&din, 3) == 0) {
        printf("x=%d, din[1]=%d\\n", x, din[1]);
        free(din);
    }
    return 0;
}""",
        "logicSteps": [
            "pp = &p guarda o endereço da variável ponteiro p.",
            "*pp desreferencia pp e se refere a p; **pp desreferencia duas vezes e altera x para 88.",
            "Na função alocar_vetor(&din, 3), pp recebe &din, portanto *pp = malloc(...) modifica din na main.",
            "Atenção aos parênteses em (*pp)[i]: [] tem precedência maior que *."
        ],
        "pitfall": (
            "Escrever <code>*pp[i]</code> em vez de <code>(*pp)[i]</code>! Como <code>[]</code> tem precedência maior que <code>*</code>, "
            "<code>*pp[i]</code> significa <code>*(pp[i])</code> (avança <code>pp</code> como vetor de ponteiros e desreferencia lixo), causando crash. "
            "Use sempre <code>(*pp)[i]</code> quando quiser indexar o vetor apontado por <code>*pp</code>."
        ),
        "memoryDiagram": {
            "caption": "Cadeia de dupla indireção: pp (0x1010) -> p (0x1008) -> x (0x1000).",
            "cells": [
                {"idx": 0, "addr": "0x1000", "val": "88", "tag": "int x (**pp)"},
                {"idx": 1, "addr": "0x1008", "val": "0x1000", "tag": "int *p (*pp)"},
                {"idx": 2, "addr": "0x1010", "val": "0x1008", "tag": "int **pp"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-11",
                "tabLabel": "Dupla Indireção",
                "badge": "1D • int **pp",
                "title": "Seguindo a cadeia pp -> *pp -> **pp",
                "desc": "Veja a diferença entre pp, *pp e **pp passo a passo.",
                "kind": "1d",
                "codeLines": [
                    "int x = 5, y = 9;",
                    "int *p = &x;",
                    "int **pp = &p;",
                    "**pp = 88;",
                    "*pp = &y;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"x": "5", "y": "9"},
                        "note": "x = 5 (0x1000) e y = 9 (0x1004).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "5", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "9", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"p": "0x1000", "*p": "5"},
                        "note": "p aponta para x (0x1000).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "5", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "9", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x1008", "label": "p", "val": "0x1000", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"pp": "0x1008", "*pp": "0x1000", "**pp": "5"},
                        "note": "pp guarda o endereço de p (0x1008).",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "5", "active": False, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "9", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x1008", "label": "p", "val": "0x1000", "active": False, "ptrs": ["pp"]},
                            {"idx": 3, "addr": "0x1010", "label": "pp", "val": "0x1008", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"x": "88", "*pp": "0x1000", "**pp": "88"},
                        "note": "**pp = 88 atravessa dois ponteiros e altera x para 88.",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "88", "active": True, "ptrs": ["p"]},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "9", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x1008", "label": "p", "val": "0x1000", "active": False, "ptrs": ["pp"]},
                            {"idx": 3, "addr": "0x1010", "label": "pp", "val": "0x1008", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"p": "0x1004", "*pp": "0x1004", "**pp": "9"},
                        "note": "*pp = &y redireciona p para y (0x1004)! Agora **pp vale 9.",
                        "cells": [
                            {"idx": 0, "addr": "0x1000", "label": "x", "val": "88", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x1004", "label": "y", "val": "9", "active": False, "ptrs": ["p"]},
                            {"idx": 2, "addr": "0x1008", "label": "p", "val": "0x1004", "active": True, "ptrs": ["pp"]},
                            {"idx": 3, "addr": "0x1010", "label": "pp", "val": "0x1008", "active": False, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-12",
        "num": "1.12",
        "title": "Ponteiros e matrizes 2D: acesso via *(*(m + i) + j) e passagem para funções",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Entenda como matrizes estáticas 2D são armazenadas em row-major order, a notação *(*(m + i) + j) e por que int m[][COLS] decai para int (*m)[COLS], não para int **.",
        "conceptHtml": (
            "<p>Uma matriz estática <code>int m[2][3]</code> é um <strong>bloco único contíguo de 6 inteiros</strong> organizado linha por linha (<em>row-major order</em>). "
            "O identificador <code>m</code> decai para um <strong>ponteiro para linha</strong>: tipo <code>int (*)[3]</code> (e <strong>NÃO</strong> <code>int **</code>!).</p>"
            "<p>Por isso, <code>m + i</code> salta <code>i</code> linhas inteiras (<code>i * 3 * sizeof(int)</code> bytes). "
            "Ao desreferenciar <code>*(m + i)</code>, obtemos o endereço do início da linha <code>i</code> (tipo <code>int *</code>). Somando <code>+ j</code>, avançamos <code>j</code> colunas e chegamos a:</p>"
            "<p><strong><code>m[i][j] &equiv; *(*(m + i) + j)</code></strong></p>"
            "<p>Na passagem para funções, é obrigatório informar o número de colunas (ou usar VLA em C99): <code>void f(int m[][3], int linhas)</code> ou <code>void f(int (*m)[3], int linhas)</code>.</p>"
        ),
        "code": """#include <stdio.h>

void imprimir_matriz(int (*m)[3], int linhas) {
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%3d ", *(*(m + i) + j));
        }
        printf("\\n");
    }
}

int main(void) {
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};
    *(*(m + 1) + 2) = 99; /* altera m[1][2] de 6 para 99 */
    imprimir_matriz(m, 2);
    return 0;
}""",
        "logicSteps": [
            "m tem tipo int[2][3] e decai para int (*)[3] (ponteiro para array de 3 ints).",
            "m + i desloca i * 12 bytes (assumindo int de 4 bytes e 3 colunas).",
            "*(m + i) obtém o subvetor da linha i, que decai para int * (&m[i][0]).",
            "*(m + i) + j avança j * 4 bytes na linha i; o * externo lê ou escreve m[i][j]."
        ],
        "pitfall": (
            "Passar uma matriz estática <code>int m[2][3]</code> para uma função que espera <code>int **m</code>! "
            "Os tipos são completamente incompatíveis: em <code>int[2][3]</code> não há um vetor de ponteiros armazenado na RAM, apenas 6 inteiros seguidos. "
            "Se forçar com cast <code>(int **)m</code>, o programa tentará ler o inteiro <code>1</code> como um endereço de memória e quebrará."
        ),
        "memoryDiagram": {
            "caption": "Matriz 2x3 em row-major order: m+1 salta 3 inteiros (12 bytes) direto para m[1][0].",
            "cells": [
                {"idx": 0, "addr": "0x7000", "val": "1", "tag": "m[0][0] <- m"},
                {"idx": 1, "addr": "0x7004", "val": "2", "tag": "m[0][1]"},
                {"idx": 2, "addr": "0x7008", "val": "3", "tag": "m[0][2]"},
                {"idx": 3, "addr": "0x700C", "val": "4", "tag": "m[1][0] <- *(m+1)"},
                {"idx": 4, "addr": "0x7010", "val": "5", "tag": "m[1][1]"},
                {"idx": 5, "addr": "0x7014", "val": "99", "tag": "m[1][2] <- *(*(m+1)+2)"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-12",
                "tabLabel": "Matriz 2D *(*(m+i)+j)",
                "badge": "2D • Row-Major",
                "title": "Acesso por aritmética de ponteiros em matriz 2x3",
                "desc": "Observe a navegação por linha *(m + i) e coluna + j.",
                "kind": "2d",
                "codeLines": [
                    "int m[2][3] = {{1,2,3}, {4,5,6}};",
                    "int *linha1 = *(m + 1);",
                    "int val = *(linha1 + 1);",
                    "*(*(m + 1) + 2) = 99;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"m": "0x7000", "sizeof(m[0])": "12"},
                        "note": "Matriz 2x3 inicializada na memória em ordem de linhas.",
                        "grid": [
                            [
                                {"addr": "0x7000", "label": "m[0][0]", "val": "1", "active": False},
                                {"addr": "0x7004", "label": "m[0][1]", "val": "2", "active": False},
                                {"addr": "0x7008", "label": "m[0][2]", "val": "3", "active": False}
                            ],
                            [
                                {"addr": "0x700C", "label": "m[1][0]", "val": "4", "active": False},
                                {"addr": "0x7010", "label": "m[1][1]", "val": "5", "active": False},
                                {"addr": "0x7014", "label": "m[1][2]", "val": "6", "active": False}
                            ]
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"m+1": "0x700C", "linha1": "0x700C"},
                        "note": "m + 1 avança 12 bytes e *(m + 1) retorna &m[1][0] (0x700C).",
                        "grid": [
                            [
                                {"addr": "0x7000", "label": "m[0][0]", "val": "1", "active": False},
                                {"addr": "0x7004", "label": "m[0][1]", "val": "2", "active": False},
                                {"addr": "0x7008", "label": "m[0][2]", "val": "3", "active": False}
                            ],
                            [
                                {"addr": "0x700C", "label": "m[1][0]", "val": "4", "active": True},
                                {"addr": "0x7010", "label": "m[1][1]", "val": "5", "active": False},
                                {"addr": "0x7014", "label": "m[1][2]", "val": "6", "active": False}
                            ]
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"linha1+1": "0x7010", "val": "5"},
                        "note": "*(linha1 + 1) acessa m[1][1] = 5.",
                        "grid": [
                            [
                                {"addr": "0x7000", "label": "m[0][0]", "val": "1", "active": False},
                                {"addr": "0x7004", "label": "m[0][1]", "val": "2", "active": False},
                                {"addr": "0x7008", "label": "m[0][2]", "val": "3", "active": False}
                            ],
                            [
                                {"addr": "0x700C", "label": "m[1][0]", "val": "4", "active": False},
                                {"addr": "0x7010", "label": "m[1][1]", "val": "5", "active": True},
                                {"addr": "0x7014", "label": "m[1][2]", "val": "6", "active": False}
                            ]
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"*(m+1)+2": "0x7014", "m[1][2]": "99"},
                        "note": "*(*(m + 1) + 2) = 99 altera diretamente m[1][2] para 99.",
                        "grid": [
                            [
                                {"addr": "0x7000", "label": "m[0][0]", "val": "1", "active": False},
                                {"addr": "0x7004", "label": "m[0][1]", "val": "2", "active": False},
                                {"addr": "0x7008", "label": "m[0][2]", "val": "3", "active": False}
                            ],
                            [
                                {"addr": "0x700C", "label": "m[1][0]", "val": "4", "active": False},
                                {"addr": "0x7010", "label": "m[1][1]", "val": "5", "active": False},
                                {"addr": "0x7014", "label": "m[1][2]", "val": "99", "active": True}
                            ]
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-13",
        "num": "1.13",
        "title": "Alocação dinâmica de memória (<stdlib.h>): malloc, calloc, realloc, free, sizeof e verificação NULL",
        "pdfRef": "Deitel 6ª Ed. Cap. 12 (12.2–12.3) / C Completo e Total Cap. 5 & 18 / Padrão C99–C11",
        "summary": "Gerencie memória no Heap em tempo de execução com malloc, calloc, realloc e free, usando sizeof para portabilidade e verificando retornos NULL.",
        "conceptHtml": (
            "<p>A memória alocada na Stack tem tamanho fixo e morre ao fim da função. Para blocos cujo tamanho só é conhecido em execução (ou que devem sobreviver à função), usamos o <strong>Heap</strong> via <code>&lt;stdlib.h&gt;</code>:</p>"
            "<ul>"
            "<li><strong><code>malloc(bytes)</code>:</strong> aloca <code>bytes</code> não inicializados (lixo) e retorna <code>void *</code> (ou <code>NULL</code> se faltar memória).</li>"
            "<li><strong><code>calloc(qtd, tam_elem)</code>:</strong> aloca <code>qtd * tam_elem</code> bytes e <strong>zera todos os bits</strong>.</li>"
            "<li><strong><code>realloc(ptr, novo_tam)</code>:</strong> redimensiona um bloco anterior preservando o conteúdo comum; pode mover o bloco para outro endereço. Se falhar, retorna <code>NULL</code> <em>sem</em> liberar o bloco antigo!</li>"
            "<li><strong><code>free(ptr)</code>:</strong> devolve o bloco ao sistema. Chamar <code>free(NULL)</code> é seguro (não faz nada).</li>"
            "</ul>"
            "<p>Use sempre <code>sizeof(*p)</code> ou <code>sizeof(tipo)</code>: <code>int *v = malloc(n * sizeof(*v));</code>.</p>"
        ),
        "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *v = calloc(3, sizeof(*v)); /* {0, 0, 0} */
    if (v == NULL) return 1;

    v[0] = 10; v[1] = 20; v[2] = 30;

    int *tmp = realloc(v, 5 * sizeof(*v));
    if (tmp == NULL) {
        free(v); /* evita perder o ponteiro original se realloc falhar */
        return 1;
    }
    v = tmp;
    v[3] = 40; v[4] = 50;

    for (int i = 0; i < 5; i++) printf("%d ", v[i]);
    free(v);
    v = NULL;
    return 0;
}""",
        "logicSteps": [
            "calloc(3, sizeof(*v)) aloca 3 inteiros zerados no Heap e retorna o endereço base.",
            "Sempre verificar if (v == NULL) antes de acessar v[i].",
            "Ao chamar realloc, atribuir o resultado a um ponteiro temporário tmp antes de sobrescrever v.",
            "Ao término do uso, chamar free(v) e zerar v = NULL."
        ],
        "pitfall": (
            "Fazer <code>v = realloc(v, novo_tam);</code> diretamente! Se <code>realloc</code> falhar e retornar <code>NULL</code>, "
            "você sobrescreve o único ponteiro <code>v</code> que guardava o bloco original, causando um <strong>memory leak</strong> imediato. "
            "Outro erro é esquecer <code>sizeof</code> em <code>malloc(10)</code> achando que alocou 10 <code>int</code>s (alocou apenas 10 bytes = 2 ints e meio!)."
        ),
        "memoryDiagram": {
            "caption": "Ponteiro v na Stack apontando para bloco dinâmico no Heap redimensionado via realloc.",
            "cells": [
                {"idx": 0, "addr": "Stack 0x7FF0", "val": "Heap 0x9000", "tag": "int *v"},
                {"idx": 1, "addr": "Heap 0x9000", "val": "10, 20, 30, 40, 50", "tag": "5 ints (20 bytes)"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-13",
                "tabLabel": "calloc + realloc + free",
                "badge": "1D • Heap",
                "title": "Ciclo de vida no Heap com realloc seguro",
                "desc": "Acompanhe calloc, verificação NULL, realloc via tmp e free.",
                "kind": "1d",
                "codeLines": [
                    "int *v = calloc(2, sizeof(int));",
                    "v[0] = 10; v[1] = 20;",
                    "int *tmp = realloc(v, 3 * sizeof(int));",
                    "if (tmp) { v = tmp; v[2] = 30; }",
                    "free(v); v = NULL;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"v": "0x9000 (Heap)"},
                        "note": "calloc aloca 2 ints zerados no Heap em 0x9000.",
                        "cells": [
                            {"idx": 0, "addr": "0x9000", "label": "v[0]", "val": "0", "active": True, "ptrs": ["v"]},
                            {"idx": 1, "addr": "0x9004", "label": "v[1]", "val": "0", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"v": "0x9000", "v[0]": "10", "v[1]": "20"},
                        "note": "Preenche v[0] e v[1].",
                        "cells": [
                            {"idx": 0, "addr": "0x9000", "label": "v[0]", "val": "10", "active": True, "ptrs": ["v"]},
                            {"idx": 1, "addr": "0x9004", "label": "v[1]", "val": "20", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"v": "0x9000", "tmp": "0x9500"},
                        "note": "realloc move os dados para novo bloco de 3 ints em 0x9500 (v[2] ainda com lixo).",
                        "cells": [
                            {"idx": 0, "addr": "0x9500", "label": "tmp[0]", "val": "10", "active": False, "ptrs": ["tmp"]},
                            {"idx": 1, "addr": "0x9504", "label": "tmp[1]", "val": "20", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x9508", "label": "tmp[2]", "val": "LIXO", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"v": "0x9500", "v[2]": "30"},
                        "note": "v atualizado para tmp e v[2] recebe 30.",
                        "cells": [
                            {"idx": 0, "addr": "0x9500", "label": "v[0]", "val": "10", "active": False, "ptrs": ["v"]},
                            {"idx": 1, "addr": "0x9504", "label": "v[1]", "val": "20", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x9508", "label": "v[2]", "val": "30", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"v": "NULL"},
                        "note": "Bloco 0x9500 liberado com free(v) e ponteiro zerado para NULL.",
                        "cells": [
                            {"idx": 0, "addr": "0x9500", "label": "FREED", "val": "---", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x7FF0", "label": "v (Stack)", "val": "NULL", "active": True, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-14",
        "num": "1.14",
        "title": "Vetores e matrizes dinâmicos no Heap + Memory Leak, Dangling Pointer e Double Free",
        "pdfRef": "Deitel 6ª Ed. Cap. 12 / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Construa matrizes dinâmicas M x N com int **m no Heap, libere na ordem inversa sem vazamentos e identifique os 3 bugs clássicos de memória dinâmica.",
        "conceptHtml": (
            "<p>Para alocar uma matriz dinâmica <code>M x N</code> no Heap:</p>"
            "<ol>"
            "<li>Aloque o vetor de ponteiros das linhas: <code>int **m = malloc(M * sizeof(int *));</code>.</li>"
            "<li>Para cada linha <code>i</code> de <code>0</code> a <code>M - 1</code>, aloque as colunas: <code>m[i] = malloc(N * sizeof(int));</code>.</li>"
            "<li>Na hora de liberar, faça na <strong>ordem inversa</strong>: primeiro <code>free(m[i])</code> em um laço para cada linha, e só depois <code>free(m)</code>!</li>"
            "</ol>"
            "<p>Três armadilhas mortais do Heap:</p>"
            "<ul>"
            "<li><strong>Memory Leak (vazamento):</strong> alocar e perder o ponteiro sem chamar <code>free</code> (ex.: chamar <code>free(m)</code> sem liberar cada <code>m[i]</code> antes).</li>"
            "<li><strong>Dangling Pointer (ponteiro pendente):</strong> continuar usando um ponteiro após <code>free(p)</code> (<em>Use-After-Free</em>). Solução: <code>p = NULL;</code> logo após <code>free(p);</code>.</li>"
            "<li><strong>Double Free:</strong> chamar <code>free(p)</code> duas vezes sobre o mesmo endereço não nulo, corrompendo o gerenciador de Heap.</li>"
            "</ul>"
        ),
        "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int M = 2, N = 3;
    int **m = malloc((size_t)M * sizeof(int *));
    if (!m) return 1;

    for (int i = 0; i < M; i++) {
        m[i] = malloc((size_t)N * sizeof(int));
        if (!m[i]) {
            for (int k = 0; k < i; k++) free(m[k]);
            free(m);
            return 1;
        }
        for (int j = 0; j < N; j++) m[i][j] = i * N + j + 1;
    }

    printf("m[1][2] = %d\\n", m[1][2]);

    /* Liberacao na ordem inversa para evitar Memory Leak */
    for (int i = 0; i < M; i++) {
        free(m[i]);
    }
    free(m);
    m = NULL; /* evita Dangling Pointer e Double Free */
    return 0;
}""",
        "logicSteps": [
            "m recebe um array de M ponteiros (int *) no Heap.",
            "Cada m[i] recebe um array independente de N inteiros no Heap.",
            "Se m[i] falhar no meio, liberamos as linhas 0..i-1 já alocadas e m antes de abortar.",
            "Ao final, liberamos cada linha m[i], depois free(m), e zeramos m = NULL para evitar dangling/double free."
        ],
        "pitfall": (
            "Executar apenas <code>free(m);</code> em uma matriz alocada linha a linha deixa todas as linhas <code>m[0]..m[M-1]</code> órfãs no Heap (<strong>Memory Leak</strong>)! "
            "Por outro lado, chamar <code>free(m)</code> e depois tentar acessar <code>m[0]</code> dentro do laço para liberar as linhas gera <strong>Use-After-Free (Dangling Pointer)</strong>."
        ),
        "memoryDiagram": {
            "caption": "Matriz dinâmica int **m (2x3): m aponta para vetor de 2 ponteiros no Heap, cada um apontando para sua linha.",
            "cells": [
                {"idx": 0, "addr": "Stack", "val": "0xA000", "tag": "int **m"},
                {"idx": 1, "addr": "Heap 0xA000", "val": "[0xA100, 0xA200]", "tag": "m[0], m[1] (int*[])"},
                {"idx": 2, "addr": "Heap 0xA100", "val": "[1, 2, 3]", "tag": "linha 0 (free 1º)"},
                {"idx": 3, "addr": "Heap 0xA200", "val": "[4, 5, 6]", "tag": "linha 1 (free 1º)"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-14",
                "tabLabel": "Matriz Dinâmica 2x3",
                "badge": "2D • Heap & Free",
                "title": "Alocação e liberação inversa de int **m (2x3)",
                "desc": "Veja as linhas sendo alocadas no Heap e liberadas antes do vetor de ponteiros.",
                "kind": "2d",
                "codeLines": [
                    "int **m = malloc(2 * sizeof(int *));",
                    "m[0] = malloc(3 * sizeof(int));",
                    "m[1] = malloc(3 * sizeof(int));",
                    "m[0][1] = 10; m[1][2] = 20;",
                    "free(m[0]); free(m[1]); free(m); m = NULL;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"m": "0xA000", "m[0]": "?", "m[1]": "?"},
                        "note": "Aloca vetor de 2 ponteiros (m[0] e m[1]) em 0xA000.",
                        "grid": [
                            [{"addr": "0xA000", "label": "m[0]", "val": "LIXO", "active": True}],
                            [{"addr": "0xA008", "label": "m[1]", "val": "LIXO", "active": True}]
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"m": "0xA000", "m[0]": "0xA100"},
                        "note": "Linha 0 alocada em 0xA100 (3 inteiros).",
                        "grid": [
                            [
                                {"addr": "0xA100", "label": "m[0][0]", "val": "?", "active": True},
                                {"addr": "0xA104", "label": "m[0][1]", "val": "?", "active": True},
                                {"addr": "0xA108", "label": "m[0][2]", "val": "?", "active": True}
                            ],
                            [
                                {"addr": "0xA008", "label": "m[1]", "val": "LIXO", "active": False}
                            ]
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"m": "0xA000", "m[0]": "0xA100", "m[1]": "0xA200"},
                        "note": "Linha 1 alocada em 0xA200 (3 inteiros).",
                        "grid": [
                            [
                                {"addr": "0xA100", "label": "m[0][0]", "val": "?", "active": False},
                                {"addr": "0xA104", "label": "m[0][1]", "val": "?", "active": False},
                                {"addr": "0xA108", "label": "m[0][2]", "val": "?", "active": False}
                            ],
                            [
                                {"addr": "0xA200", "label": "m[1][0]", "val": "?", "active": True},
                                {"addr": "0xA204", "label": "m[1][1]", "val": "?", "active": True},
                                {"addr": "0xA208", "label": "m[1][2]", "val": "?", "active": True}
                            ]
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"m[0][1]": "10", "m[1][2]": "20"},
                        "note": "Escreve m[0][1] = 10 e m[1][2] = 20 nas linhas independentes.",
                        "grid": [
                            [
                                {"addr": "0xA100", "label": "m[0][0]", "val": "?", "active": False},
                                {"addr": "0xA104", "label": "m[0][1]", "val": "10", "active": True},
                                {"addr": "0xA108", "label": "m[0][2]", "val": "?", "active": False}
                            ],
                            [
                                {"addr": "0xA200", "label": "m[1][0]", "val": "?", "active": False},
                                {"addr": "0xA204", "label": "m[1][1]", "val": "?", "active": False},
                                {"addr": "0xA208", "label": "m[1][2]", "val": "20", "active": True}
                            ]
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"m": "NULL"},
                        "note": "Libera m[0], depois m[1], depois m, e zera m = NULL.",
                        "grid": [
                            [{"addr": "0xA100", "label": "linha 0", "val": "FREED", "active": False}],
                            [{"addr": "0xA200", "label": "linha 1", "val": "FREED", "active": False}],
                            [{"addr": "Stack", "label": "m", "val": "NULL", "active": True}]
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-15",
        "num": "1.15",
        "title": "Ponteiros para funções: declaração, callbacks e exemplo prático com qsort",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.11) / C Completo e Total Cap. 5 & 21 / Padrão C99–C11",
        "summary": "Armazene endereços de funções em ponteiros para criar callbacks, tabelas de despacho e ordenação genérica com qsort(<stdlib.h>).",
        "conceptHtml": (
            "<p>Funções compiladas também residem na memória (segmento de código). Um <strong>ponteiro para função</strong> guarda o endereço de entrada de uma função com assinatura compatível.</p>"
            "<p>Sintaxe: <code>retorno (*nome_ptr)(tipos_parametros);</code> — os parênteses em <code>(*nome_ptr)</code> são <strong>obrigatórios</strong> (sem eles, <code>int *f(int);</code> declara uma função que retorna <code>int *</code>!).</p>"
            "<p>O uso clássico em C é o <strong>callback</strong> na função padrão <code>qsort</code> de <code>&lt;stdlib.h&gt;</code>:</p>"
            "<p><code>void qsort(void *base, size_t nmemb, size_t size, int (*compar)(const void *, const void *));</code></p>"
            "<p>A função de comparação recebe dois ponteiros genéricos <code>const void *</code> e deve retornar negativo se <code>a &lt; b</code>, zero se <code>a == b</code>, ou positivo se <code>a &gt; b</code>.</p>"
        ),
        "code": """#include <stdio.h>
#include <stdlib.h>

int cmp_crescente(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb); /* evita overflow de va - vb */
}

int somar(int x, int y) { return x + y; }

int main(void) {
    int (*op)(int, int) = somar;
    printf("Callback direto: %d\\n", op(3, 4));

    int v[5] = {40, 10, 50, 20, 30};
    qsort(v, 5, sizeof(v[0]), cmp_crescente);
    for (int i = 0; i < 5; i++) printf("%d ", v[i]);
    return 0;
}""",
        "logicSteps": [
            "int (*op)(int, int) = somar declara op como ponteiro para função que recebe (int, int) e retorna int.",
            "op(3, 4) (ou (*op)(3, 4)) invoca a função apontada por op.",
            "qsort recebe o endereço de cmp_crescente como 4º argumento e a chama repetidamente durante o algoritmo.",
            "Dentro de cmp_crescente, fazemos cast de const void * para const int * antes de desreferenciar."
        ],
        "pitfall": (
            "1) Esquecer os parênteses: <code>int *f(int, int);</code> é protótipo de função que retorna <code>int*</code>, não ponteiro para função.<br>"
            "2) Em <code>qsort</code>, retornar <code>*(const int *)a - *(const int *)b</code> pode causar <strong>integer overflow</strong> se houver números muito grandes/negativos (ex.: <code>INT_MAX - (-1)</code>). Prefira <code>(va &gt; vb) - (va &lt; vb)</code>."
        ),
        "memoryDiagram": {
            "caption": "Ponteiro op e parâmetro compar de qsort guardam endereços de código na seção .text.",
            "cells": [
                {"idx": 0, "addr": "Stack", "val": ".text 0x401200", "tag": "int (*op)(int, int) = somar"},
                {"idx": 1, "addr": ".text 0x401200", "val": "somar(x, y)", "tag": "Código da função"},
                {"idx": 2, "addr": ".text 0x401240", "val": "cmp_crescente", "tag": "Callback passado a qsort"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-15",
                "tabLabel": "Callback & qsort",
                "badge": "1D • Funções",
                "title": "Ordenação por qsort usando ponteiro de função",
                "desc": "Veja op chamando somar e qsort ordenando v via cmp_crescente.",
                "kind": "1d",
                "codeLines": [
                    "int (*op)(int, int) = somar;",
                    "int r = op(3, 4);",
                    "int v[4] = {40, 10, 30, 20};",
                    "qsort(v, 4, sizeof(int), cmp_crescente);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"op": "0x401200 (&somar)"},
                        "note": "op aponta para o endereço da função somar na memória de código.",
                        "cells": [
                            {"idx": 0, "addr": "Stack", "label": "op", "val": "&somar", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x401200", "label": ".text", "val": "somar()", "active": False, "ptrs": ["op"]}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"op": "&somar", "r": "7"},
                        "note": "op(3, 4) executa somar(3, 4) e retorna 7.",
                        "cells": [
                            {"idx": 0, "addr": "Stack", "label": "r", "val": "7", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x401200", "label": ".text", "val": "somar()", "active": True, "ptrs": ["op"]}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"v": "{40, 10, 30, 20}"},
                        "note": "Vetor desordenado v antes do qsort.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "40", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "10", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "30", "active": False, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "20", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"compar": "&cmp_crescente", "v": "{10, 20, 30, 40}"},
                        "note": "qsort chama cmp_crescente para comparar pares de elementos e ordena v.",
                        "cells": [
                            {"idx": 0, "addr": "0x2000", "label": "v[0]", "val": "10", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x2004", "label": "v[1]", "val": "20", "active": True, "ptrs": []},
                            {"idx": 2, "addr": "0x2008", "label": "v[2]", "val": "30", "active": True, "ptrs": []},
                            {"idx": 3, "addr": "0x200C", "label": "v[3]", "val": "40", "active": True, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-16",
        "num": "1.16",
        "title": "Ponteiros genéricos (void *) e conversão explícita (cast)",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.10) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Entenda o papel do ponteiro genérico void * para escrever funções polimórficas como memcpy, malloc e impressão genérica, e suas restrições.",
        "conceptHtml": (
            "<p>Um ponteiro <strong><code>void *</code></strong> é um ponteiro genérico capaz de armazenar o endereço de qualquer tipo de dado (<code>int</code>, <code>double</code>, <code>struct</code>), "
            "sendo implicitamente conversível de/para qualquer ponteiro de objeto em C.</p>"
            "<p>Contudo, como o compilador <strong>não sabe o tamanho do tipo apontado</strong> por um <code>void *</code>, duas operações são <strong>proibidas</strong> diretamente sobre <code>void *</code>:</p>"
            "<ol>"
            "<li><strong>Não pode ser desreferenciado:</strong> <code>*p</code> dá erro de compilação! É obrigatório converter (cast) primeiro: <code>*(int *)p</code>.</li>"
            "<li><strong>Não permite aritmética padrão ISO C:</strong> <code>p++</code> ou <code>p + 1</code> é inválido no padrão C (embora o GCC aceite como extensão não portátil tratando <code>sizeof(void) == 1</code>; em código portátil, converta para <code>char *</code> ou <code>unsigned char *</code> para avançar byte a byte).</li>"
            "</ol>"
        ),
        "code": """#include <stdio.h>

void imprimir_generico(const void *dado, char tipo) {
    if (tipo == 'i') {
        printf("int: %d\\n", *(const int *)dado);
    } else if (tipo == 'd') {
        printf("double: %.2f\\n", *(const double *)dado);
    } else if (tipo == 'c') {
        printf("char: %c\\n", *(const char *)dado);
    }
}

int main(void) {
    int a = 42;
    double b = 3.14;
    void *gen = &a;
    imprimir_generico(gen, 'i');
    gen = &b;
    imprimir_generico(gen, 'd');
    return 0;
}""",
        "logicSteps": [
            "void *gen aceita &a (int *) e depois &b (double *) sem erro de tipo.",
            "Não é possível fazer *gen diretamente porque void não possui tamanho definido.",
            "Na função imprimir_generico, o parâmetro 'tipo' guia o cast explícito: *(const int *)dado ou *(const double *)dado.",
            "Após o cast para o ponteiro concreto, a desreferenciação lê o número exato de bytes."
        ],
        "pitfall": (
            "Fazer cast para o tipo errado (ex.: passar <code>&amp;b</code> que é <code>double *</code> e ler com <code>*(int *)dado</code>) "
            "interpreta os primeiros 4 bytes da representação IEEE-754 de ponto flutuante como um inteiro, produzindo lixo silencioso ou violação de <em>strict aliasing</em>."
        ),
        "memoryDiagram": {
            "caption": "O mesmo void *gen aponta sucessivamente para 4 bytes (int) e 8 bytes (double); o cast define como ler.",
            "cells": [
                {"idx": 0, "addr": "0x8000", "val": "42 (4B)", "tag": "int a"},
                {"idx": 1, "addr": "0x8008", "val": "3.14 (8B)", "tag": "double b"},
                {"idx": 2, "addr": "0x8010", "val": "0x8000 -> 0x8008", "tag": "void *gen"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-16",
                "tabLabel": "void * e Cast",
                "badge": "1D • Genérico",
                "title": "Reaproveitando void *gen com casts explícitos",
                "desc": "Veja como gen aponta para tipos distintos e requer cast para leitura.",
                "kind": "1d",
                "codeLines": [
                    "int a = 42; double b = 3.14;",
                    "void *gen = &a;",
                    "int x = *(int *)gen;",
                    "gen = &b;",
                    "double y = *(double *)gen;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"a": "42", "b": "3.14"},
                        "note": "a (4 bytes) e b (8 bytes) alocados na Stack.",
                        "cells": [
                            {"idx": 0, "addr": "0x8000", "label": "a (int)", "val": "42", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x8008", "label": "b (double)", "val": "3.14", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"gen": "0x8000"},
                        "note": "gen recebe &a implicitamente como void *.",
                        "cells": [
                            {"idx": 0, "addr": "0x8000", "label": "a (int)", "val": "42", "active": False, "ptrs": ["gen"]},
                            {"idx": 1, "addr": "0x8008", "label": "b (double)", "val": "3.14", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x8010", "label": "gen", "val": "0x8000", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"gen": "0x8000", "x": "42"},
                        "note": "Cast (int *)gen permite ler os 4 bytes de a -> x = 42.",
                        "cells": [
                            {"idx": 0, "addr": "0x8000", "label": "a (int)", "val": "42", "active": True, "ptrs": ["gen"]},
                            {"idx": 1, "addr": "0x8008", "label": "b (double)", "val": "3.14", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x8010", "label": "gen", "val": "0x8000", "active": False, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"gen": "0x8008"},
                        "note": "gen agora recebe &b (0x8008).",
                        "cells": [
                            {"idx": 0, "addr": "0x8000", "label": "a (int)", "val": "42", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x8008", "label": "b (double)", "val": "3.14", "active": False, "ptrs": ["gen"]},
                            {"idx": 2, "addr": "0x8010", "label": "gen", "val": "0x8008", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"gen": "0x8008", "y": "3.14"},
                        "note": "Cast (double *)gen lê os 8 bytes de b -> y = 3.14.",
                        "cells": [
                            {"idx": 0, "addr": "0x8000", "label": "a (int)", "val": "42", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x8008", "label": "b (double)", "val": "3.14", "active": True, "ptrs": ["gen"]},
                            {"idx": 2, "addr": "0x8010", "label": "gen", "val": "0x8008", "active": False, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-17",
        "num": "1.17",
        "title": "Ponteiros com const: const int *p vs int *const p vs const int *const p",
        "pdfRef": "Deitel 6ª Ed. Cap. 7 (7.5) / C Completo e Total Cap. 5 / Padrão C99–C11",
        "summary": "Leia declarações com const da direita para a esquerda e nunca mais confunda ponteiro para dado constante com ponteiro constante.",
        "conceptHtml": (
            "<p>A regra de ouro em C para decifrar qualificadores <code>const</code> é <strong>ler da direita para a esquerda</strong> em relação ao asterisco <code>*</code>:</p>"
            "<ul>"
            "<li><strong><code>const int *p</code></strong> (ou <code>int const *p</code>): <em>ponteiro para int constante</em>. Você <strong>pode</strong> mudar para onde <code>p</code> aponta (<code>p = &amp;y;</code>), mas <strong>não</strong> pode alterar o valor via <code>*p</code> (<code>*p = 10;</code> é erro!).</li>"
            "<li><strong><code>int *const p</code>:</strong> <em>ponteiro constante para int</em>. O endereço em <code>p</code> é fixo (<code>p = &amp;y;</code> é erro!), mas você <strong>pode</strong> alterar o valor apontado (<code>*p = 10;</code> é válido!).</li>"
            "<li><strong><code>const int *const p</code>:</strong> <em>ponteiro constante para int constante</em>. Nem <code>p</code> nem <code>*p</code> podem ser modificados.</li>"
            "</ul>"
        ),
        "code": """#include <stdio.h>

int main(void) {
    int a = 10, b = 20;

    const int *p1 = &a;       /* dado somente-leitura, ponteiro movel */
    p1 = &b;                  /* OK */
    /* *p1 = 30; -> ERRO de compilacao */

    int *const p2 = &a;       /* ponteiro fixo, dado editavel */
    *p2 = 30;                 /* OK: altera 'a' para 30 */
    /* p2 = &b;  -> ERRO de compilacao */

    const int *const p3 = &b; /* ambos fixos */
    printf("a=%d, *p1=%d, *p2=%d, *p3=%d\\n", a, *p1, *p2, *p3);
    return 0;
}""",
        "logicSteps": [
            "const antes do * protege o dado apontado (*p não pode ser escrito).",
            "const depois do * protege o próprio ponteiro (p deve ser inicializado na declaração e não pode ser reatribuído).",
            "const nos dois lados trava tanto o endereço quanto a escrita indireta.",
            "Em parâmetros de funções de leitura (ex.: imprimir(const int *v)), usar const int * garante que a função não altere o vetor do chamador."
        ],
        "pitfall": (
            "Esquecer de inicializar um <code>int *const p</code> na declaração! Como <code>p</code> é constante, "
            "ele não pode receber um endereço depois (<code>int *const p; p = &amp;a;</code> falha na compilação). "
            "Outro detalhe sutil: <code>const int *p = &amp;a;</code> não torna <code>a</code> imutável — <code>a = 99;</code> continua válido, apenas a janela <code>*p</code> é somente leitura."
        ),
        "memoryDiagram": {
            "caption": "O cadeado (const) antes do * tranca o alvo; depois do * tranca o próprio ponteiro.",
            "cells": [
                {"idx": 0, "addr": "0x3000", "val": "30 (editável via *p2)", "tag": "int a"},
                {"idx": 1, "addr": "0x3004", "val": "20 (bloqueado em *p1/*p3)", "tag": "int b"},
                {"idx": 2, "addr": "0x3008", "val": "0x3000 -> 0x3004", "tag": "const int *p1 (ponteiro móvel)"},
                {"idx": 3, "addr": "0x3010", "val": "0x3000 [FIXO]", "tag": "int *const p2"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-17",
                "tabLabel": "Regras do const",
                "badge": "1D • const",
                "title": "Comparando const int *p1 e int *const p2",
                "desc": "Veja quais operações são permitidas em cada tipo de ponteiro.",
                "kind": "1d",
                "codeLines": [
                    "int a = 10, b = 20;",
                    "const int *p1 = &a;",
                    "p1 = &b; /* OK: p1 move */",
                    "int *const p2 = &a;",
                    "*p2 = 30; /* OK: *p2 muda */"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"a": "10", "b": "20"},
                        "note": "a = 10 e b = 20 declarados.",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "a", "val": "10", "active": True, "ptrs": []},
                            {"idx": 1, "addr": "0x3004", "label": "b", "val": "20", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"p1": "0x3000", "*p1": "10 (RO)"},
                        "note": "p1 é ponteiro móvel para dado read-only (*p1 travado).",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "a", "val": "10", "active": False, "ptrs": ["p1"]},
                            {"idx": 1, "addr": "0x3004", "label": "b", "val": "20", "active": False, "ptrs": []},
                            {"idx": 2, "addr": "0x3008", "label": "p1", "val": "0x3000", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"p1": "0x3004", "*p1": "20 (RO)"},
                        "note": "p1 = &b é válido porque o ponteiro p1 NÃO é const.",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "a", "val": "10", "active": False, "ptrs": []},
                            {"idx": 1, "addr": "0x3004", "label": "b", "val": "20", "active": False, "ptrs": ["p1"]},
                            {"idx": 2, "addr": "0x3008", "label": "p1", "val": "0x3004", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"p2": "0x3000 (FIXO)", "*p2": "10"},
                        "note": "p2 nasce preso a 0x3000 (não pode apontar para b).",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "a", "val": "10", "active": False, "ptrs": ["p2"]},
                            {"idx": 1, "addr": "0x3004", "label": "b", "val": "20", "active": False, "ptrs": ["p1"]},
                            {"idx": 2, "addr": "0x3010", "label": "p2 (const)", "val": "0x3000", "active": True, "ptrs": []}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"a": "30", "p2": "0x3000 (FIXO)", "*p2": "30"},
                        "note": "*p2 = 30 é válido e altera 'a' para 30.",
                        "cells": [
                            {"idx": 0, "addr": "0x3000", "label": "a", "val": "30", "active": True, "ptrs": ["p2"]},
                            {"idx": 1, "addr": "0x3004", "label": "b", "val": "20", "active": False, "ptrs": ["p1"]},
                            {"idx": 2, "addr": "0x3010", "label": "p2 (const)", "val": "0x3000", "active": False, "ptrs": []}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "ptr-18",
        "num": "1.18",
        "title": "Ponteiros e structs (operador ->), introdução a estruturas dinâmicas, erros comuns e Valgrind / ASan",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 & 12 / C Completo e Total Cap. 7 & 18 / Padrão C99–C11",
        "summary": "Conecte ponteiros a structs com o operador seta (->), construa nós auto-referenciados para listas encadeadas/pilhas/filas e use AddressSanitizer e Valgrind.",
        "conceptHtml": (
            "<p>Ao ter um ponteiro <code>Aluno *p</code> para uma struct, acessar um campo exigiria <code>(*p).nota</code> (os parênteses são necessários porque <code>.</code> tem precedência maior que <code>*</code>). "
            "Para simplificar, C oferece o <strong>operador seta <code>-&gt;</code></strong>: <strong><code>p-&gt;campo &equiv; (*p).campo</code></strong>.</p>"
            "<p>Com ponteiros dentro de structs (<strong>structs auto-referenciadas</strong>), construímos estruturas dinâmicas onde cada nó aponta para o próximo:</p>"
            "<ul>"
            "<li><strong>Lista encadeada:</strong> sequência de nós ligados por <code>prox</code> terminando em <code>NULL</code>.</li>"
            "<li><strong>Pilha (LIFO) e Fila (FIFO):</strong> implementadas com ponteiros <code>topo</code> ou <code>inicio</code>/<code>fim</code>.</li>"
            "</ul>"
            "<p>Para caçar erros silenciosos (<em>memory leak</em>, <em>out-of-bounds</em>, <em>use-after-free</em>, <em>double free</em>), compile com <strong>AddressSanitizer</strong> (<code>gcc -g -fsanitize=address,undefined prog.c</code>) ou execute sob <strong>Valgrind</strong> (<code>valgrind --leak-check=full ./prog</code>).</p>"
        ),
        "code": """#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *prox;
} No;

int main(void) {
    No *n1 = malloc(sizeof(No));
    No *n2 = malloc(sizeof(No));
    if (!n1 || !n2) { free(n1); free(n2); return 1; }

    n1->dado = 10; n1->prox = n2;
    n2->dado = 20; n2->prox = NULL;

    for (No *cur = n1; cur != NULL; cur = cur->prox) {
        printf("%d -> ", cur->dado);
    }
    printf("NULL\\n");

    free(n2);
    free(n1);
    return 0;
}""",
        "logicSteps": [
            "struct No contém um ponteiro struct No *prox capaz de guardar o endereço do próximo nó.",
            "n1->dado = 10 equivale a (*n1).dado = 10, acessando o campo via ponteiro.",
            "n1->prox = n2 encadeia o primeiro nó ao segundo; n2->prox = NULL encerra a lista.",
            "Ao liberar a lista, guarde o próximo antes de dar free(cur) para evitar Use-After-Free."
        ],
        "pitfall": (
            "1) Escrever <code>*p.campo</code> sem parênteses: o compilador interpreta como <code>*(p.campo)</code> e dá erro, pois <code>p</code> é ponteiro e não struct.<br>"
            "2) Em lista encadeada, fazer <code>free(cur); cur = cur-&gt;prox;</code> lê <code>cur-&gt;prox</code> <em>depois</em> da memória liberada (<strong>Use-After-Free</strong>)! Salve <code>No *prox = cur-&gt;prox; free(cur); cur = prox;</code>. Use <code>-fsanitize=address</code> para detectar na hora."
        ),
        "memoryDiagram": {
            "caption": "Lista encadeada no Heap: n1 (0xB000) aponta via prox para n2 (0xB020), que aponta para NULL.",
            "cells": [
                {"idx": 0, "addr": "Heap 0xB000", "val": "{dado: 10, prox: 0xB020}", "tag": "No *n1"},
                {"idx": 1, "addr": "Heap 0xB020", "val": "{dado: 20, prox: NULL}", "tag": "No *n2"}
            ]
        },
        "tracers": [
            {
                "id": "tr-ptr-18",
                "tabLabel": "Operador -> e Lista",
                "badge": "1D • Lista Encadeada",
                "title": "Encadeamento de nós com operador ->",
                "desc": "Acompanhe cur percorrendo n1 -> n2 -> NULL.",
                "kind": "1d",
                "codeLines": [
                    "No *n1 = malloc(sizeof(No));",
                    "No *n2 = malloc(sizeof(No));",
                    "n1->dado = 10; n1->prox = n2;",
                    "n2->dado = 20; n2->prox = NULL;",
                    "No *cur = n1; cur = cur->prox;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"n1": "0xB000"},
                        "note": "Nó n1 alocado no Heap em 0xB000.",
                        "cells": [
                            {"idx": 0, "addr": "0xB000", "label": "n1", "val": "{dado: ?, prox: ?}", "active": True, "ptrs": ["n1"]}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"n1": "0xB000", "n2": "0xB020"},
                        "note": "Nó n2 alocado no Heap em 0xB020.",
                        "cells": [
                            {"idx": 0, "addr": "0xB000", "label": "n1", "val": "{dado: ?, prox: ?}", "active": False, "ptrs": ["n1"]},
                            {"idx": 1, "addr": "0xB020", "label": "n2", "val": "{dado: ?, prox: ?}", "active": True, "ptrs": ["n2"]}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"n1->dado": "10", "n1->prox": "0xB020"},
                        "note": "n1 recebe dado 10 e seu campo prox aponta para n2 (0xB020).",
                        "cells": [
                            {"idx": 0, "addr": "0xB000", "label": "n1", "val": "{10, -> 0xB020}", "active": True, "ptrs": ["n1"]},
                            {"idx": 1, "addr": "0xB020", "label": "n2", "val": "{dado: ?, prox: ?}", "active": False, "ptrs": ["n2"]}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"n2->dado": "20", "n2->prox": "NULL"},
                        "note": "n2 recebe dado 20 e prox = NULL, encerrando a lista.",
                        "cells": [
                            {"idx": 0, "addr": "0xB000", "label": "n1", "val": "{10, -> 0xB020}", "active": False, "ptrs": ["n1"]},
                            {"idx": 1, "addr": "0xB020", "label": "n2", "val": "{20, NULL}", "active": True, "ptrs": ["n2"]}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"cur": "0xB020", "cur->dado": "20"},
                        "note": "cur inicia em n1 (0xB000) e avança via cur = cur->prox para n2 (0xB020).",
                        "cells": [
                            {"idx": 0, "addr": "0xB000", "label": "n1", "val": "{10, -> 0xB020}", "active": False, "ptrs": ["n1"]},
                            {"idx": 1, "addr": "0xB020", "label": "n2", "val": "{20, NULL}", "active": True, "ptrs": ["n2", "cur"]}
                        ]
                    }
                ]
            }
        ]
    }
]
