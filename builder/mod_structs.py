"""Módulo 2: Structs, Unions, Enums e Registros em C — Conteúdo completo (2.1 a 2.18)."""
from __future__ import annotations

TOPICS_STRUCTS = [
    {
        "id": "strc-1",
        "num": "2.1",
        "title": "Conceito: Tipo Composto Heterogêneo (Registro)",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.1–10.2) • Lista PDF: Ex. 1, 5",
        "summary": (
            "Uma struct (estrutura ou registro) agrupa sob um único nome várias variáveis "
            "de tipos diferentes, armazenadas em posições contíguas de memória."
        ),
        "conceptHtml": (
            "<p>Enquanto um <strong>vetor (array)</strong> armazena vários elementos do "
            "<em>mesmo</em> tipo, uma <code>struct</code> permite reunir dados "
            "<strong>heterogêneos</strong> (como <code>int</code>, <code>float</code> e "
            "<code>char[]</code>) que descrevem uma mesma entidade do mundo real — por exemplo, "
            "um aluno, um produto ou um ponto no plano.</p>"
            "<ul>"
            "<li><strong>Homogêneo (vetor):</strong> <code>float notas[3];</code> — todos os campos têm o mesmo tipo.</li>"
            "<li><strong>Heterogêneo (struct):</strong> reúne matrícula (<code>int</code>), nome (<code>char[40]</code>) e média (<code>float</code>) em um único bloco lógico.</li>"
            "<li><strong>Benefício em ATP:</strong> facilita passar vários dados relacionados para funções e gravar registros inteiros em arquivos binários (<code>fwrite</code>).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "/* Modelo de registro (molde): ainda nao aloca memoria */\n"
            "struct Aluno {\n"
            "    int matricula;\n"
            "    char nome[20];\n"
            "    float media;\n"
            "};\n"
            "\n"
            "int main(void) {\n"
            "    struct Aluno a1 = {101, \"Ana\", 8.5f};\n"
            "    printf(\"%d - %s: %.1f\\n\", a1.matricula, a1.nome, a1.media);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Definir a struct apenas descreve o layout (molde) do novo tipo composto para o compilador, sem reservar memória ainda.",
            "Ao declarar a variável a1 do tipo struct Aluno, o compilador aloca espaço contíguo para matricula, nome e media.",
            "Cada membro conserva seu próprio tipo e ocupa sua própria faixa de bytes dentro da mesma variável composta."
        ],
        "pitfall": (
            "Confundir definição do tipo com criação de variável: escrever apenas "
            "<code>struct Aluno { ... };</code> não reserva memória; é preciso declarar uma variável "
            "como <code>struct Aluno a1;</code> para guardar dados."
        ),
        "tracers": [
            {
                "id": "tr-strc-1",
                "tabLabel": "Memória do Registro",
                "badge": "Stack • Contíguo",
                "title": "Anatomia de uma struct em memória",
                "desc": "Veja como os campos heterogêneos de a1 ficam agrupados em sequência.",
                "kind": "1d",
                "codeLines": [
                    "struct Aluno { int mat; char nome[8]; float media; };",
                    "struct Aluno a1;",
                    "a1.mat = 101;",
                    "a1.media = 8.5f;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"molde": "struct Aluno (16 B)"},
                        "note": "O compilador registra o layout do tipo struct Aluno (nenhum byte alocado em execução).",
                        "cells": []
                    },
                    {
                        "line": 1,
                        "vars": {"a1": "{?, ?, ?}"},
                        "note": "Variável local a1 é alocada na stack a partir de 0x1000 com lixo de memória.",
                        "cells": [
                            {"addr": "0x1000", "label": "a1.mat", "val": "?", "changed": True},
                            {"addr": "0x1004", "label": "a1.nome", "val": "\"???\"", "changed": True},
                            {"addr": "0x100C", "label": "a1.media", "val": "?", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"a1.mat": "101"},
                        "note": "Campo inteiro a1.mat recebe 101 sem afetar os outros membros.",
                        "cells": [
                            {"addr": "0x1000", "label": "a1.mat", "val": "101", "changed": True},
                            {"addr": "0x1004", "label": "a1.nome", "val": "\"???\"", "changed": False},
                            {"addr": "0x100C", "label": "a1.media", "val": "?", "changed": False}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"a1.mat": "101", "a1.media": "8.5"},
                        "note": "Campo float a1.media recebe 8.5f no deslocamento correspondente.",
                        "cells": [
                            {"addr": "0x1000", "label": "a1.mat", "val": "101", "changed": False},
                            {"addr": "0x1004", "label": "a1.nome", "val": "\"???\"", "changed": False},
                            {"addr": "0x100C", "label": "a1.media", "val": "8.5", "changed": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-2",
        "num": "2.2",
        "title": "Declaração e Criação de Variáveis struct",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.2) • Lista PDF: Ex. 1, 3, 4",
        "summary": (
            "Aprenda as três formas de declarar structs em C, incluindo o ponto e vírgula "
            "obrigatório ao final da chave de fechamento."
        ),
        "conceptHtml": (
            "<p>Em C, a palavra-chave <code>struct</code> pode ser usada para definir uma "
            "<strong>tag</strong> (nome do molde) e depois declarar variáveis usando "
            "<code>struct NomeTag var;</code>.</p>"
            "<ul>"
            "<li><strong>Forma 1 (separada — recomendada):</strong> define <code>struct Ponto { int x; int y; };</code> no topo e declara <code>struct Ponto p1, p2;</code> nas funções.</li>"
            "<li><strong>Forma 2 (junto à definição):</strong> <code>struct Ponto { int x; int y; } p1, p2;</code> define o tipo e já cria variáveis globais ou locais.</li>"
            "<li><strong>Forma 3 (anônima):</strong> <code>struct { int x; int y; } cfg;</code> cria variável única, mas impede reutilizar o tipo depois.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "struct Ponto {\n"
            "    int x;\n"
            "    int y;\n"
            "}; /* ';' obrigatorio! */\n"
            "\n"
            "int main(void) {\n"
            "    struct Ponto p1, p2;\n"
            "    p1.x = 3; p1.y = 4;\n"
            "    p2.x = 10; p2.y = 20;\n"
            "    printf(\"p1=(%d,%d) p2=(%d,%d)\\n\", p1.x, p1.y, p2.x, p2.y);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "A tag Ponto identifica a estrutura no espaço de nomes de tags (por isso em C sem typedef é obrigatório escrever struct Ponto).",
            "O ponto e vírgula após '}' encerra a declaração; esquecê-lo faz o compilador interpretar o próximo identificador como variável.",
            "p1 e p2 são instâncias independentes: alterar p1.x não modifica p2.x."
        ],
        "pitfall": (
            "Esquecer o <code>;</code> após <code>}</code> ou tentar declarar apenas "
            "<code>Ponto p1;</code> sem <code>struct</code> (em C puro, diferente de C++, a tag sozinha não vira nome de tipo sem <code>typedef</code>)."
        ),
        "tracers": [
            {
                "id": "tr-strc-2",
                "tabLabel": "Instâncias Independentes",
                "badge": "Stack • 2 variáveis",
                "title": "Criação de p1 e p2 do tipo struct Ponto",
                "desc": "Cada variável struct Ponto recebe seu próprio par (x, y) na memória.",
                "kind": "1d",
                "codeLines": [
                    "struct Ponto p1, p2;",
                    "p1.x = 3; p1.y = 4;",
                    "p2.x = 10; p2.y = 20;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"p1": "{?, ?}", "p2": "{?, ?}"},
                        "note": "Alocadas duas instâncias distintas na stack: p1 (0x2000) e p2 (0x2008).",
                        "cells": [
                            {"addr": "0x2000", "label": "p1.x", "val": "?", "changed": True},
                            {"addr": "0x2004", "label": "p1.y", "val": "?", "changed": True},
                            {"addr": "0x2008", "label": "p2.x", "val": "?", "changed": True},
                            {"addr": "0x200C", "label": "p2.y", "val": "?", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"p1": "{3, 4}", "p2": "{?, ?}"},
                        "note": "Atribuição aos campos de p1 deixa p2 intacta.",
                        "cells": [
                            {"addr": "0x2000", "label": "p1.x", "val": "3", "changed": True},
                            {"addr": "0x2004", "label": "p1.y", "val": "4", "changed": True},
                            {"addr": "0x2008", "label": "p2.x", "val": "?", "changed": False},
                            {"addr": "0x200C", "label": "p2.y", "val": "?", "changed": False}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"p1": "{3, 4}", "p2": "{10, 20}"},
                        "note": "p2 recebe suas próprias coordenadas (10, 20).",
                        "cells": [
                            {"addr": "0x2000", "label": "p1.x", "val": "3", "changed": False},
                            {"addr": "0x2004", "label": "p1.y", "val": "4", "changed": False},
                            {"addr": "0x2008", "label": "p2.x", "val": "10", "changed": True},
                            {"addr": "0x200C", "label": "p2.y", "val": "20", "changed": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-3",
        "num": "2.3",
        "title": "typedef: Simplificando Nomes de Tipos",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.6) • Lista PDF: Ex. 39, 40, 54",
        "summary": (
            "typedef cria um sinônimo (alias) para um tipo existente, dispensando repetir "
            "a palavra struct em toda declaração e assinatura de função."
        ),
        "conceptHtml": (
            "<p><code>typedef</code> não cria um tipo novo na memória; ele cria um "
            "<strong>apelido</strong> para um tipo já existente, tornando o código mais limpo e legível.</p>"
            "<ul>"
            "<li><strong>Sem tag (mais comum):</strong> <code>typedef struct { int dia, mes, ano; } Data;</code> — permite declarar <code>Data hoje;</code>.</li>"
            "<li><strong>Com tag + alias (obrigatório em listas encadeadas):</strong> <code>typedef struct no { int dado; struct no *prox; } No;</code> — dentro da struct ainda usamos <code>struct no *</code> porque <code>No</code> só passa a existir ao final da declaração.</li>"
            "<li><strong>Atenção à ordem:</strong> em <code>typedef struct { ... } Aluno;</code>, <code>Aluno</code> é um <em>nome de tipo</em>, não uma variável!</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "typedef struct {\n"
            "    int numerador;\n"
            "    int denominador;\n"
            "} FRACAO; /* Ex. 54 do PDF */\n"
            "\n"
            "typedef struct no {\n"
            "    int valor;\n"
            "    struct no *prox; /* dentro usa a tag 'struct no' */\n"
            "} No;\n"
            "\n"
            "int main(void) {\n"
            "    FRACAO f1 = {3, 4};\n"
            "    No n1 = {10, NULL};\n"
            "    printf(\"%d/%d e no=%d\\n\", f1.numerador, f1.denominador, n1.valor);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "No primeiro typedef, FRACAO vira sinônimo da struct anônima com numerador e denominador.",
            "No segundo typedef, a tag 'no' é necessária para que o ponteiro prox possa referenciar 'struct no' antes do alias No ser concluído.",
            "Na função main, FRACAO f1 e No n1 substituem 'struct ...' com exatamente o mesmo layout em memória."
        ],
        "pitfall": (
            "Escrever <code>typedef struct { int x; } Ponto;</code> e achar que <code>Ponto</code> "
            "é uma variável global (tentando fazer <code>Ponto.x = 5;</code>). Com <code>typedef</code>, "
            "o identificador no final é um <strong>tipo</strong>, não uma variável."
        ),
        "tracers": [
            {
                "id": "tr-strc-3",
                "tabLabel": "Alias typedef",
                "badge": "Compilação + Stack",
                "title": "Como typedef mapeia FRACAO para struct",
                "desc": "FRACAO f1 ocupa exatamente o mesmo espaço que struct sem typedef.",
                "kind": "1d",
                "codeLines": [
                    "typedef struct { int num; int den; } FRACAO;",
                    "FRACAO f1 = {3, 4};",
                    "f1.num = 6;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"alias": "FRACAO -> struct {int num, den}"},
                        "note": "FRACAO é registrado na tabela de tipos do compilador (0 bytes alocados).",
                        "cells": []
                    },
                    {
                        "line": 1,
                        "vars": {"f1.num": "3", "f1.den": "4"},
                        "note": "f1 nasce inicializada com 3/4 na stack.",
                        "cells": [
                            {"addr": "0x3000", "label": "f1.num", "val": "3", "changed": True},
                            {"addr": "0x3004", "label": "f1.den", "val": "4", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"f1.num": "6", "f1.den": "4"},
                        "note": "Acesso normal via operador ponto altera numerador para 6.",
                        "cells": [
                            {"addr": "0x3000", "label": "f1.num", "val": "6", "changed": True},
                            {"addr": "0x3004", "label": "f1.den", "val": "4", "changed": False}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-4",
        "num": "2.4",
        "title": "Acesso aos Membros: Operador . vs Operador ->",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.4) • Lista PDF: Ex. 31, 32, 45",
        "summary": (
            "Use o ponto (.) quando tiver a variável struct em mãos, e a seta (->) quando "
            "tiver um ponteiro para a struct."
        ),
        "conceptHtml": (
            "<p>A regra de ouro em C para acessar um campo de uma estrutura depende exclusivamente "
            "do tipo da expressão à esquerda:</p>"
            "<ul>"
            "<li><strong>Variável ou elemento de vetor (<code>s.campo</code>):</strong> use o operador ponto <code>.</code> (ex.: <code>s.referencia</code>, <code>turma[0].nota</code>).</li>"
            "<li><strong>Ponteiro para struct (<code>ps-&gt;campo</code>):</strong> use o operador seta <code>-&gt;</code>, que é um atalho exato para <code>(*ps).campo</code>.</li>"
            "<li><strong>Precedência crítica:</strong> o operador <code>.</code> tem precedência maior que <code>*</code>! Escrever <code>*ps.valor</code> significa <code>*(ps.valor)</code> e gera erro de compilação; os parênteses em <code>(*ps).valor</code> são obrigatórios.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "struct Sensor {\n"
            "    int referencia;\n"
            "    float valor_medido;\n"
            "};\n"
            "\n"
            "void entra_dados(struct Sensor *s) {\n"
            "    /* Ex. 32 do PDF: s eh ponteiro, entao usa-se seta -> */\n"
            "    s->referencia = 42;\n"
            "    (*s).valor_medido = 27.5f; /* equivalente a s->valor_medido */\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    struct Sensor sen;\n"
            "    struct Sensor *ps = &sen;\n"
            "    entra_dados(ps);\n"
            "    printf(\"Ref=%d Valor=%.1f\\n\", sen.referencia, ps->valor_medido);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "sen é uma variável struct Sensor direta, logo seus campos são acessados com sen.referencia.",
            "ps armazena &sen (endereço da struct); para acessar via ps, usa-se ps->valor_medido.",
            "Em scanf(\"%d\", &s->referencia), o operador -> tem maior precedência que &, portanto &s->referencia equivale a &(s->referencia), obtendo o endereço do campo."
        ],
        "pitfall": (
            "Misturar os operadores (<code>ps.referencia</code> ou <code>sen-&gt;referencia</code>) "
            "ou esquecer parênteses em <code>(*s).valor</code> ao não usar <code>-&gt;</code>."
        ),
        "tracers": [
            {
                "id": "tr-strc-4",
                "tabLabel": "Ponto . vs Seta ->",
                "badge": "Ponteiro + Struct",
                "title": "Acesso direto (sen.) vs indireto (ps->)",
                "desc": "ps guarda o endereço de sen; ps->valor_medido desreferencia ps e acessa o campo.",
                "kind": "1d",
                "codeLines": [
                    "struct Sensor sen = {10, 12.0f};",
                    "struct Sensor *ps = &sen;",
                    "sen.referencia = 42;",
                    "ps->valor_medido = 27.5f;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"sen.ref": "10", "sen.val": "12.0"},
                        "note": "sen nasce em 0x4000 com referencia=10 e valor_medido=12.0.",
                        "cells": [
                            {"addr": "0x4000", "label": "sen.referencia", "val": "10", "changed": True},
                            {"addr": "0x4004", "label": "sen.valor_medido", "val": "12.0", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"ps": "0x4000 (&sen)"},
                        "note": "Ponteiro ps (0x4010) aponta para o início de sen (0x4000).",
                        "cells": [
                            {"addr": "0x4000", "label": "sen.referencia", "val": "10", "changed": False},
                            {"addr": "0x4004", "label": "sen.valor_medido", "val": "12.0", "changed": False},
                            {"addr": "0x4010", "label": "ps", "val": "0x4000 -> sen", "changed": True, "ptr": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"sen.ref": "42"},
                        "note": "Acesso direto com ponto altera sen.referencia para 42.",
                        "cells": [
                            {"addr": "0x4000", "label": "sen.referencia", "val": "42", "changed": True},
                            {"addr": "0x4004", "label": "sen.valor_medido", "val": "12.0", "changed": False},
                            {"addr": "0x4010", "label": "ps", "val": "0x4000 -> sen", "changed": False, "ptr": True}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"sen.val": "27.5", "ps->val": "27.5"},
                        "note": "ps->valor_medido segue 0x4000 + offset 4 e altera sen.valor_medido para 27.5.",
                        "cells": [
                            {"addr": "0x4000", "label": "sen.referencia", "val": "42", "changed": False},
                            {"addr": "0x4004", "label": "sen.valor_medido", "val": "27.5", "changed": True},
                            {"addr": "0x4010", "label": "ps", "val": "0x4000 -> sen", "changed": False, "ptr": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-5",
        "num": "2.5",
        "title": "Inicialização: Lista, Designada e Campo a Campo",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.3) • Padrão C99+",
        "summary": (
            "Structs podem ser inicializadas na declaração por ordem (lista), por nome de "
            "campo (designada C99) ou preenchidas posteriormente campo a campo."
        ),
        "conceptHtml": (
            "<p>Existem três maneiras principais de preencher uma variável <code>struct</code>:</p>"
            "<ul>"
            "<li><strong>Lista posicional:</strong> <code>Pessoa p = {\"Ana\", 20};</code> — os valores devem seguir a ordem exata da declaração. Campos omitidos ao final recebem <code>0</code> (ou <code>NULL</code>).</li>"
            "<li><strong>Inicialização designada (C99):</strong> <code>Pessoa p = {.idade = 20, .nome = \"Ana\"};</code> — independe da ordem e deixa o código autoexplicativo.</li>"
            "<li><strong>Atribuição após declarar:</strong> <code>p.idade = 20;</code> funciona, mas para arrays de <code>char</code> é obrigatório usar <code>strcpy(p.nome, \"Ana\")</code> (nunca <code>p.nome = \"Ana\"</code>!).</li>"
            "<li><strong>Zero-init idiomático:</strong> <code>Pessoa p = {0};</code> zera todos os bytes/campos da struct.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "\n"
            "typedef struct {\n"
            "    char nome[20];\n"
            "    int idade;\n"
            "    float altura;\n"
            "} Pessoa;\n"
            "\n"
            "int main(void) {\n"
            "    /* 1) Lista posicional (altura omitida -> 0.0) */\n"
            "    Pessoa a = {\"Bia\", 19};\n"
            "    /* 2) Inicializacao designada (C99) */\n"
            "    Pessoa b = {.idade = 20, .nome = \"Ana\", .altura = 1.65f};\n"
            "    /* 3) Campo a campo */\n"
            "    Pessoa c;\n"
            "    strcpy(c.nome, \"Leo\");\n"
            "    c.idade = 22;\n"
            "    c.altura = 1.78f;\n"
            "    printf(\"%s %.2f | %s %.2f | %s %.2f\\n\",\n"
            "           a.nome, a.altura, b.nome, b.altura, c.nome, c.altura);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Na lista posicional, omitir um campo do final faz o compilador zerá-lo automaticamente (altura = 0.0f).",
            "Na inicialização designada (.campo = valor), a ordem não importa e campos omitidos também são zerados.",
            "Após a declaração, não é possível usar chaves diretamente sem cast composto: strings exigem strcpy e escalares usam '='."
        ],
        "pitfall": (
            "Tentar atribuir <code>c = {\"Leo\", 22, 1.78f};</code> em uma linha separada da declaração "
            "(sem cast composto <code>(Pessoa){...}</code>) ou tentar <code>c.nome = \"Leo\";</code> com <code>=</code> em vez de <code>strcpy</code>."
        ),
        "tracers": [
            {
                "id": "tr-strc-5",
                "tabLabel": "Formas de Inicializar",
                "badge": "C99 • Zero-fill",
                "title": "Lista posicional vs inicialização designada",
                "desc": "Campos omitidos em inicializadores parciais são zerados pelo compilador.",
                "kind": "1d",
                "codeLines": [
                    "Pessoa a = {\"Bia\", 19};",
                    "Pessoa b = {.idade = 20, .nome = \"Ana\"};",
                    "b.altura = 1.65f;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"a.nome": "\"Bia\"", "a.idade": "19", "a.altura": "0.0"},
                        "note": "altura foi omitida na lista de 'a', portanto recebe 0.0 automaticamente (não fica lixo!).",
                        "cells": [
                            {"addr": "0x5000", "label": "a.nome", "val": "\"Bia\"", "changed": True},
                            {"addr": "0x5014", "label": "a.idade", "val": "19", "changed": True},
                            {"addr": "0x5018", "label": "a.altura", "val": "0.0", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"b.nome": "\"Ana\"", "b.idade": "20", "b.altura": "0.0"},
                        "note": "Designada permite declarar .idade antes de .nome; .altura começa zerada.",
                        "cells": [
                            {"addr": "0x5020", "label": "b.nome", "val": "\"Ana\"", "changed": True},
                            {"addr": "0x5034", "label": "b.idade", "val": "20", "changed": True},
                            {"addr": "0x5038", "label": "b.altura", "val": "0.0", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"b.nome": "\"Ana\"", "b.idade": "20", "b.altura": "1.65"},
                        "note": "Atribuição campo a campo atualiza apenas b.altura.",
                        "cells": [
                            {"addr": "0x5020", "label": "b.nome", "val": "\"Ana\"", "changed": False},
                            {"addr": "0x5034", "label": "b.idade", "val": "20", "changed": False},
                            {"addr": "0x5038", "label": "b.altura", "val": "1.65", "changed": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-6",
        "num": "2.6",
        "title": "Leitura e Impressão de Structs (fgets e Buffer)",
        "pdfRef": "Deitel 6ª Ed. Cap. 8/10 • Lista PDF: Ex. 15, 23, 44",
        "summary": (
            "Como ler strings com espaços usando fgets e limpar o '\\n' residual deixado "
            "por scanf anterior sem recorrer a gets() ou fflush(stdin)."
        ),
        "conceptHtml": (
            "<p>Ao ler campos mistos de uma struct (números com <code>scanf</code> e strings "
            "com <code>fgets</code>), o clássico bug do \"pulo de leitura\" ocorre porque "
            "<code>scanf(\"%d\", &amp;x)</code> deixa o <code>'\\n'</code> (Enter) no buffer de entrada.</p>"
            "<ul>"
            "<li><strong>Limpeza portável de buffer:</strong> use um laço <code>int c; while ((c = getchar()) != '\\n' &amp;&amp; c != EOF) {}</code> após o <code>scanf</code> numérico antes de chamar <code>fgets</code>.</li>"
            "<li><strong>Remover o '\\n' do <code>fgets</code>:</strong> <code>fgets</code> inclui a quebra de linha na string; remova com <code>s[strcspn(s, \"\\n\")] = '\\0';</code>.</li>"
            "<li><strong>Por que evitar <code>gets()</code> e <code>fflush(stdin)</code>?</strong> <code>gets()</code> foi removida do C11 por causar buffer overflow; <code>fflush(stdin)</code> tem comportamento indefinido no padrão C (embora apareça em listas antigas como o Ex. 15 do PDF).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "\n"
            "typedef struct {\n"
            "    int codigo;\n"
            "    char descricao[61];\n"
            "} Compromisso;\n"
            "\n"
            "void limpa_buffer(void) {\n"
            "    int c;\n"
            "    while ((c = getchar()) != '\\n' && c != EOF) {}\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    Compromisso comp;\n"
            "    scanf(\"%d\", &comp.codigo);\n"
            "    limpa_buffer(); /* consome o '\\n' deixado pelo scanf */\n"
            "    if (fgets(comp.descricao, sizeof(comp.descricao), stdin) != NULL) {\n"
            "        comp.descricao[strcspn(comp.descricao, \"\\n\")] = '\\0';\n"
            "    }\n"
            "    printf(\"[%d] %s\\n\", comp.codigo, comp.descricao);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "scanf(\"%d\", &comp.codigo) lê os dígitos do código, mas para ao encontrar o '\\n', deixando-o em stdin.",
            "limpa_buffer() consome caracteres restantes até o '\\n' (inclusive), preparando stdin para a leitura de texto.",
            "fgets lê com segurança até sizeof(comp.descricao)-1 chars e strcspn substitui o '\\n' final por '\\0'."
        ],
        "pitfall": (
            "Chamar <code>fgets</code> logo após <code>scanf(\"%d\", ...)</code> sem limpar o "
            "buffer: o <code>fgets</code> lê imediatamente o <code>'\\n'</code> pendente e "
            "grava uma string vazia sem deixar o usuário digitar."
        ),
        "tracers": [
            {
                "id": "tr-strc-6",
                "tabLabel": "Buffer stdin + fgets",
                "badge": "I/O Seguro",
                "title": "Consumo do '\\n' entre scanf e fgets",
                "desc": "Acompanhe o conteúdo do buffer stdin e dos campos de comp.",
                "kind": "1d",
                "codeLines": [
                    "scanf(\"%d\", &comp.codigo);",
                    "limpa_buffer();",
                    "fgets(comp.descricao, 61, stdin);",
                    "comp.descricao[strcspn(comp.descricao, \"\\n\")] = '\\0';"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"stdin": "\"\\nProva ATP\\n\"", "comp.codigo": "7"},
                        "note": "Usuário digitou '7\\nProva ATP\\n'. scanf leu 7 e deixou '\\n' na frente do buffer.",
                        "cells": [
                            {"addr": "stdin", "label": "buffer", "val": "'\\n' P r o v a ...", "changed": True},
                            {"addr": "0x6000", "label": "comp.codigo", "val": "7", "changed": True},
                            {"addr": "0x6004", "label": "comp.descricao", "val": "\"???\"", "changed": False}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"stdin": "\"Prova ATP\\n\"", "comp.codigo": "7"},
                        "note": "limpa_buffer() descarta o '\\n' pendente.",
                        "cells": [
                            {"addr": "stdin", "label": "buffer", "val": "P r o v a   A T P '\\n'", "changed": True},
                            {"addr": "0x6000", "label": "comp.codigo", "val": "7", "changed": False},
                            {"addr": "0x6004", "label": "comp.descricao", "val": "\"???\"", "changed": False}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"comp.descricao": "\"Prova ATP\\n\""},
                        "note": "fgets lê a linha inteira, mantendo o '\\n' antes do '\\0'.",
                        "cells": [
                            {"addr": "stdin", "label": "buffer", "val": "(vazio)", "changed": True},
                            {"addr": "0x6000", "label": "comp.codigo", "val": "7", "changed": False},
                            {"addr": "0x6004", "label": "comp.descricao", "val": "\"Prova ATP\\n\"", "changed": True}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"comp.descricao": "\"Prova ATP\""},
                        "note": "strcspn encontra o índice do '\\n' e o troca por '\\0', limpando a string.",
                        "cells": [
                            {"addr": "0x6000", "label": "comp.codigo", "val": "7", "changed": False},
                            {"addr": "0x6004", "label": "comp.descricao", "val": "\"Prova ATP\\0\"", "changed": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-7",
        "num": "2.7",
        "title": "Atribuição Direta entre Structs (b = a) e Cópia Rasa",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.2) • Lista PDF: Ex. 44",
        "summary": (
            "Ao contrário de vetores, uma struct pode ser atribuída diretamente a outra do "
            "mesmo tipo (b = a), copiando todos os campos byte a byte — inclusive ponteiros!"
        ),
        "conceptHtml": (
            "<p>Em C, fazer <code>b = a;</code> entre duas variáveis do <strong>mesmo tipo "
            "struct</strong> copia todos os membros de <code>a</code> para <code>b</code> — "
            "inclusive arrays internos declarados dentro da struct (como <code>char nome[40]</code>).</p>"
            "<ul>"
            "<li><strong>Vantagem em ordenação:</strong> trocar dois registros fica simples (<code>tmp = v[i]; v[i] = v[j]; v[j] = tmp;</code>).</li>"
            "<li><strong>Cuidado — Cópia Rasa (Shallow Copy):</strong> se a struct tiver um <em>ponteiro</em> (<code>char *nome;</code>), <code>b = a</code> copia apenas o endereço guardado no ponteiro, fazendo <code>a.nome</code> e <code>b.nome</code> apontarem para a mesma região do heap!</li>"
            "<li><strong>Tipos incompatíveis:</strong> mesmo que duas structs tenham campos idênticos, se forem definições distintas sem o mesmo tipo, <code>b = a</code> não compila.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n"
            "\n"
            "typedef struct { int id; char nome[16]; } Fixo;\n"
            "typedef struct { int id; char *nome; } Dinamico;\n"
            "\n"
            "int main(void) {\n"
            "    Fixo f1 = {1, \"Ana\"}, f2;\n"
            "    f2 = f1; /* copia o array nome inteiro! */\n"
            "    f2.nome[0] = 'E'; /* f1.nome continua \"Ana\" */\n"
            "\n"
            "    Dinamico d1 = {2, malloc(16)}, d2;\n"
            "    strcpy(d1.nome, \"Bia\");\n"
            "    d2 = d1; /* COPIA RASA: d2.nome aponta para o MESMO buffer! */\n"
            "    d2.nome[0] = 'L'; /* altera d1.nome tambem -> \"Lia\"! */\n"
            "    printf(\"f1=%s f2=%s | d1=%s d2=%s\\n\", f1.nome, f2.nome, d1.nome, d2.nome);\n"
            "    free(d1.nome); /* nao dar free(d2.nome) -> double free! */\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Em Fixo, nome[16] mora dentro da própria struct; logo f2 = f1 duplica os 16 bytes e f1/f2 são independentes.",
            "Em Dinamico, nome é apenas um endereço (4 ou 8 bytes); d2 = d1 copia o endereço, gerando aliasing.",
            "Alterar *d2.nome altera d1.nome e dar free em ambos causaria double free (comportamento indefinido)."
        ],
        "pitfall": (
            "Usar <code>b = a</code> em structs que possuem ponteiros alocados com <code>malloc</code> "
            "e depois chamar <code>free</code> nos dois (double free) ou assumir que editar um não afeta o outro."
        ),
        "tracers": [
            {
                "id": "tr-strc-7",
                "tabLabel": "Cópia Rasa vs Array",
                "badge": "Aliasing • Heap",
                "title": "Por que d2 = d1 compartilha o ponteiro interno",
                "desc": "Compare o efeito de alterar o caractere 0 após b = a.",
                "kind": "1d",
                "codeLines": [
                    "Dinamico d1 = {2, malloc(16)}; strcpy(d1.nome, \"Bia\");",
                    "Dinamico d2 = d1;",
                    "d2.nome[0] = 'L';"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"d1.id": "2", "d1.nome": "0x9000"},
                        "note": "d1.nome aponta para o bloco 0x9000 no heap contendo \"Bia\".",
                        "cells": [
                            {"addr": "0x7000", "label": "d1.id", "val": "2", "changed": True},
                            {"addr": "0x7004", "label": "d1.nome", "val": "0x9000", "changed": True, "ptr": True},
                            {"addr": "0x9000", "label": "heap", "val": "\"Bia\"", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"d2.id": "2", "d2.nome": "0x9000"},
                        "note": "d2 = d1 copia os bytes da struct: d2.nome recebe o MESMO endereço 0x9000.",
                        "cells": [
                            {"addr": "0x7004", "label": "d1.nome", "val": "0x9000", "changed": False, "ptr": True},
                            {"addr": "0x7014", "label": "d2.nome", "val": "0x9000", "changed": True, "ptr": True},
                            {"addr": "0x9000", "label": "heap", "val": "\"Bia\"", "changed": False}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"*d1.nome": "\"Lia\"", "*d2.nome": "\"Lia\""},
                        "note": "Alterar via d2.nome modifica 0x9000, afetando d1.nome simultaneamente!",
                        "cells": [
                            {"addr": "0x7004", "label": "d1.nome", "val": "0x9000", "changed": False, "ptr": True},
                            {"addr": "0x7014", "label": "d2.nome", "val": "0x9000", "changed": False, "ptr": True},
                            {"addr": "0x9000", "label": "heap", "val": "\"Lia\"", "changed": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-8",
        "num": "2.8",
        "title": "Vetores de Structs (Tabelas em Memória)",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.7) • Lista PDF: Ex. 2, 5, 9, 17, 22",
        "summary": (
            "Um vetor de structs organiza múltiplos registros homogêneos em posições contíguas, "
            "como linhas de uma tabela em memória."
        ),
        "conceptHtml": (
            "<p>Para cadastrar 5 alunos, 100 contatos da agenda ou N produtos de um estoque, "
            "declaramos um <strong>vetor de structs</strong>: <code>Aluno turma[5];</code>.</p>"
            "<ul>"
            "<li><strong>Indexação + ponto:</strong> <code>turma[i]</code> é uma variável do tipo <code>Aluno</code>, portanto seus campos usam ponto: <code>turma[i].nota</code>.</li>"
            "<li><strong>String dentro de vetor de struct:</strong> <code>turma[i].nome[0]</code> acessa o primeiro caractere do nome do aluno <code>i</code>.</li>"
            "<li><strong>Endereçamento em scanf:</strong> <code>scanf(\"%f\", &amp;turma[i].nota);</code> — lembre do <code>&amp;</code> em campos escalares, mas <strong>não</strong> em arrays de char (<code>turma[i].nome</code> já decai para ponteiro).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#define N 3\n"
            "\n"
            "typedef struct {\n"
            "    int cod;\n"
            "    char nome[16];\n"
            "    float preco;\n"
            "    int qtd;\n"
            "} Produto;\n"
            "\n"
            "int main(void) {\n"
            "    Produto est[N] = {\n"
            "        {10, \"Teclado\", 120.0f, 5},\n"
            "        {20, \"Mouse\",    65.0f, 12},\n"
            "        {30, \"Cabo USB\", 25.0f, 30}\n"
            "    };\n"
            "    for (int i = 0; i < N; i++) {\n"
            "        printf(\"#%d %-10s R$ %.2f (qtd: %d)\\n\",\n"
            "               est[i].cod, est[i].nome, est[i].preco, est[i].qtd);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "est[N] aloca N blocos consecutivos de sizeof(Produto) bytes na memória.",
            "No laço for, est[i] seleciona a linha i da tabela e o operador '.' acessa a coluna (campo) desejada.",
            "A inicialização pode usar listas aninhadas entre chaves para cada elemento do vetor."
        ],
        "pitfall": (
            "Colocar o índice depois do campo (<code>turma.nome[i]</code> em vez de <code>turma[i].nome</code>) "
            "ou esquecer que índices em C vão de <code>0</code> a <code>N-1</code>."
        ),
        "tracers": [
            {
                "id": "tr-strc-8",
                "tabLabel": "Tabela 2D de Structs",
                "badge": "Array • Registros",
                "title": "Vetor est[3] representado como tabela",
                "desc": "Cada linha i representa um Produto completo; cada coluna representa um campo.",
                "kind": "2d",
                "codeLines": [
                    "Produto est[3] = {{10,\"Teclado\",120,5}, {20,\"Mouse\",65,12}, {30,\"Cabo\",25,30}};",
                    "est[1].qtd -= 2;",
                    "est[2].preco = 29.0f;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"N": "3"},
                        "note": "Tabela est[3] inicializada com 3 produtos em memória contígua.",
                        "grid": [
                            [{"label": "[0].cod", "val": "10", "changed": True}, {"label": "[0].nome", "val": "\"Teclado\"", "changed": True}, {"label": "[0].preco", "val": "120", "changed": True}, {"label": "[0].qtd", "val": "5", "changed": True}],
                            [{"label": "[1].cod", "val": "20", "changed": True}, {"label": "[1].nome", "val": "\"Mouse\"", "changed": True}, {"label": "[1].preco", "val": "65", "changed": True}, {"label": "[1].qtd", "val": "12", "changed": True}],
                            [{"label": "[2].cod", "val": "30", "changed": True}, {"label": "[2].nome", "val": "\"Cabo\"", "changed": True}, {"label": "[2].preco", "val": "25", "changed": True}, {"label": "[2].qtd", "val": "30", "changed": True}]
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"est[1].qtd": "10"},
                        "note": "Venda de 2 mouses atualiza apenas a célula est[1].qtd para 10.",
                        "grid": [
                            [{"label": "[0].cod", "val": "10", "changed": False}, {"label": "[0].nome", "val": "\"Teclado\"", "changed": False}, {"label": "[0].preco", "val": "120", "changed": False}, {"label": "[0].qtd", "val": "5", "changed": False}],
                            [{"label": "[1].cod", "val": "20", "changed": False}, {"label": "[1].nome", "val": "\"Mouse\"", "changed": False}, {"label": "[1].preco", "val": "65", "changed": False}, {"label": "[1].qtd", "val": "10", "changed": True}],
                            [{"label": "[2].cod", "val": "30", "changed": False}, {"label": "[2].nome", "val": "\"Cabo\"", "changed": False}, {"label": "[2].preco", "val": "25", "changed": False}, {"label": "[2].qtd", "val": "30", "changed": False}]
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"est[2].preco": "29.0"},
                        "note": "Reajuste altera est[2].preco para 29.0.",
                        "grid": [
                            [{"label": "[0].cod", "val": "10", "changed": False}, {"label": "[0].nome", "val": "\"Teclado\"", "changed": False}, {"label": "[0].preco", "val": "120", "changed": False}, {"label": "[0].qtd", "val": "5", "changed": False}],
                            [{"label": "[1].cod", "val": "20", "changed": False}, {"label": "[1].nome", "val": "\"Mouse\"", "changed": False}, {"label": "[1].preco", "val": "65", "changed": False}, {"label": "[1].qtd", "val": "10", "changed": False}],
                            [{"label": "[2].cod", "val": "30", "changed": False}, {"label": "[2].nome", "val": "\"Cabo\"", "changed": False}, {"label": "[2].preco", "val": "29.0", "changed": True}, {"label": "[2].qtd", "val": "30", "changed": False}]
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-9",
        "num": "2.9",
        "title": "Operações em Vetores: Busca, Ordenação, Filtros e Médias",
        "pdfRef": "Lista PDF: Ex. 2, 6, 13, 17, 28, 43, 44",
        "summary": (
            "Padrões clássicos de prova sobre vetores de structs: busca por código ou string "
            "(strcmp), ordenação por campo (Bubble/Selection Sort com troca inteira), filtros e acumuladores."
        ),
        "conceptHtml": (
            "<p>Quase todo problema de ATP com vetores de structs combina quatro operações:</p>"
            "<ul>"
            "<li><strong>Busca:</strong> para campo numérico use <code>v[i].cod == alvo</code>; para texto use <code>strcmp(v[i].nome, alvo) == 0</code> (nunca <code>==</code> entre strings!).</li>"
            "<li><strong>Ordenação por nome ou nota:</strong> compare o critério (<code>strcmp(v[j].nome, v[j+1].nome) &gt; 0</code> ou <code>v[j].media &lt; v[j+1].media</code>) e troque a <em>struct inteira</em> com variável auxiliar <code>tmp</code>.</li>"
            "<li><strong>Extremos (maior/menor):</strong> guarde o <em>índice</em> <code>idxMaior = 0</code> e compare <code>v[i].media &gt; v[idxMaior].media</code> a partir de <code>i = 1</code>.</li>"
            "<li><strong>Filtros e médias:</strong> conte quantos atendem à condição antes de dividir a soma para evitar divisão por zero!</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "\n"
            "typedef struct { char nome[20]; float media; } Aluno;\n"
            "\n"
            "void ordenar_por_nome(Aluno v[], int n) {\n"
            "    for (int i = 0; i < n - 1; i++) {\n"
            "        for (int j = 0; j < n - 1 - i; j++) {\n"
            "            if (strcmp(v[j].nome, v[j + 1].nome) > 0) {\n"
            "                Aluno tmp = v[j];\n"
            "                v[j] = v[j + 1];\n"
            "                v[j + 1] = tmp;\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
            "\n"
            "int buscar_nome(const Aluno v[], int n, const char *alvo) {\n"
            "    for (int i = 0; i < n; i++) {\n"
            "        if (strcmp(v[i].nome, alvo) == 0) return i;\n"
            "    }\n"
            "    return -1;\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    Aluno t[3] = {{\"Carlos\", 7.0f}, {\"Ana\", 9.5f}, {\"Bruno\", 5.5f}};\n"
            "    ordenar_por_nome(t, 3);\n"
            "    int pos = buscar_nome(t, 3, \"Bruno\");\n"
            "    printf(\"Bruno na pos %d (media %.1f)\\n\", pos, t[pos].media);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "strcmp(a, b) > 0 indica que 'a' vem depois de 'b' na ordem alfabética (tabela ASCII).",
            "A troca usa Aluno tmp = v[j], preservando a correspondência entre nome e média de cada aluno.",
            "buscar_nome retorna o índice encontrado ou -1 quando não há ocorrência, permitindo validar antes de acessar t[pos]."
        ],
        "pitfall": (
            "Comparar strings com <code>v[i].nome == alvo</code> (compara endereços e sempre falha) "
            "ou ordenar apenas o vetor de médias sem trocar o campo <code>nome</code> junto."
        ),
        "tracers": [
            {
                "id": "tr-strc-9",
                "tabLabel": "Ordenação de Structs",
                "badge": "Bubble Sort • Swap",
                "title": "Troca completa de registros por nome",
                "desc": "Quando strcmp > 0, o registro inteiro (nome + media) muda de posição.",
                "kind": "2d",
                "codeLines": [
                    "/* t = [(\"Carlos\",7.0), (\"Ana\",9.5), (\"Bruno\",5.5)] */",
                    "if (strcmp(t[0].nome, t[1].nome) > 0) swap(t[0], t[1]);",
                    "if (strcmp(t[1].nome, t[2].nome) > 0) swap(t[1], t[2]);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"i": "0"},
                        "note": "Estado inicial fora de ordem alfabética.",
                        "grid": [
                            [{"label": "t[0].nome", "val": "\"Carlos\"", "changed": True}, {"label": "t[0].media", "val": "7.0", "changed": True}],
                            [{"label": "t[1].nome", "val": "\"Ana\"", "changed": True}, {"label": "t[1].media", "val": "9.5", "changed": True}],
                            [{"label": "t[2].nome", "val": "\"Bruno\"", "changed": True}, {"label": "t[2].media", "val": "5.5", "changed": True}]
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"strcmp(\"Carlos\",\"Ana\")": "> 0"},
                        "note": "\"Carlos\" > \"Ana\": t[0] e t[1] são trocados por completo.",
                        "grid": [
                            [{"label": "t[0].nome", "val": "\"Ana\"", "changed": True}, {"label": "t[0].media", "val": "9.5", "changed": True}],
                            [{"label": "t[1].nome", "val": "\"Carlos\"", "changed": True}, {"label": "t[1].media", "val": "7.0", "changed": True}],
                            [{"label": "t[2].nome", "val": "\"Bruno\"", "changed": False}, {"label": "t[2].media", "val": "5.5", "changed": False}]
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"strcmp(\"Carlos\",\"Bruno\")": "> 0"},
                        "note": "\"Carlos\" > \"Bruno\": t[1] e t[2] trocam; vetor fica ordenado: Ana, Bruno, Carlos.",
                        "grid": [
                            [{"label": "t[0].nome", "val": "\"Ana\"", "changed": False}, {"label": "t[0].media", "val": "9.5", "changed": False}],
                            [{"label": "t[1].nome", "val": "\"Bruno\"", "changed": True}, {"label": "t[1].media", "val": "5.5", "changed": True}],
                            [{"label": "t[2].nome", "val": "\"Carlos\"", "changed": True}, {"label": "t[2].media", "val": "7.0", "changed": True}]
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-10",
        "num": "2.10",
        "title": "Structs e Funções: Valor, Referência e Retorno",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.5) • Lista PDF: Ex. 32, 37, 39, 54",
        "summary": (
            "Structs são passadas por valor por padrão (cópia completa); para alterar o original "
            "ou evitar cópia pesada, passe ponteiro (const ou mutável). Funções também podem retornar structs."
        ),
        "conceptHtml": (
            "<p>Diferente de vetores (que decaem para ponteiros), uma <code>struct</code> inteira "
            "passada como argumento vai <strong>por valor</strong> (cópia de todos os campos).</p>"
            "<ul>"
            "<li><strong>Por valor (<code>void imprime(Ponto p)</code>):</strong> alterações em <code>p</code> não afetam quem chamou; útil para structs pequenas.</li>"
            "<li><strong>Por referência com ponteiro (<code>void le(Ponto *p)</code>):</strong> altera a variável original usando <code>-&gt;</code> e evita copiar structs grandes.</li>"
            "<li><strong>Somente leitura eficiente (<code>void imprime(const Cadastro *c)</code>):</strong> zero cópia + garantia do compilador de não modificação.</li>"
            "<li><strong>Retorno de struct (<code>FRACAO soma(FRACAO a, FRACAO b)</code>):</strong> ideal para devolver múltiplos valores empacotados (como no Ex. 37/54 do PDF).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "typedef struct { int x, y; } Ponto;\n"
            "\n"
            "void dobra_copia(Ponto p) {\n"
            "    p.x *= 2; p.y *= 2; /* altera apenas a copia local */\n"
            "}\n"
            "\n"
            "void dobra_ref(Ponto *p) {\n"
            "    p->x *= 2; p->y *= 2; /* altera a struct original */\n"
            "}\n"
            "\n"
            "Ponto soma_pontos(Ponto a, Ponto b) {\n"
            "    Ponto res = {a.x + b.x, a.y + b.y};\n"
            "    return res;\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    Ponto p = {2, 3};\n"
            "    dobra_copia(p);         /* p continua (2, 3) */\n"
            "    dobra_ref(&p);          /* p vira (4, 6) */\n"
            "    Ponto q = soma_pontos(p, (Ponto){1, 1});\n"
            "    printf(\"p=(%d,%d) q=(%d,%d)\\n\", p.x, p.y, q.x, q.y);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "dobra_copia(p) recebe uma cópia independente no stack frame da função; ao retornar, a cópia é descartada.",
            "dobra_ref(&p) recebe o endereço de p e modifica diretamente p.x e p.y usando ->.",
            "soma_pontos devolve uma nova struct Ponto construída localmente, permitindo retornar x e y juntos."
        ],
        "pitfall": (
            "Passar struct por valor esperando que a função altere o original (ex.: função de leitura "
            "<code>void le(Aluno a)</code> sem <code>*</code>). Em C puro, também não existe <code>Data &amp;D</code> "
            "(isso é referência de C++, como aparece por engano em alguns enunciados adaptados como Ex. 40)."
        ),
        "tracers": [
            {
                "id": "tr-strc-10",
                "tabLabel": "Valor vs Ponteiro",
                "badge": "Stack Frames",
                "title": "Comparação entre dobra_copia(p) e dobra_ref(&p)",
                "desc": "Veja por que apenas dobra_ref modifica p na main.",
                "kind": "1d",
                "codeLines": [
                    "Ponto p = {2, 3};",
                    "dobra_copia(p); /* param p_copia = {2, 3} -> {4, 6} */",
                    "dobra_ref(&p);  /* param ptr = &p -> altera p */"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"main.p": "{2, 3}"},
                        "note": "p nasce em main no endereço 0x8000.",
                        "cells": [
                            {"addr": "0x8000", "label": "main.p.x", "val": "2", "changed": True},
                            {"addr": "0x8004", "label": "main.p.y", "val": "3", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"main.p": "{2, 3}", "copia": "{4, 6}"},
                        "note": "dobra_copia altera apenas o frame temporário (0x8100); main.p permanece {2, 3}.",
                        "cells": [
                            {"addr": "0x8000", "label": "main.p.x", "val": "2", "changed": False},
                            {"addr": "0x8004", "label": "main.p.y", "val": "3", "changed": False},
                            {"addr": "0x8100", "label": "copia.x (temp)", "val": "4", "changed": True},
                            {"addr": "0x8104", "label": "copia.y (temp)", "val": "6", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"main.p": "{4, 6}", "ptr": "0x8000"},
                        "note": "dobra_ref recebe 0x8000 e altera main.p diretamente para {4, 6}.",
                        "cells": [
                            {"addr": "0x8000", "label": "main.p.x", "val": "4", "changed": True},
                            {"addr": "0x8004", "label": "main.p.y", "val": "6", "changed": True},
                            {"addr": "0x8120", "label": "ptr", "val": "0x8000 -> p", "changed": True, "ptr": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-11",
        "num": "2.11",
        "title": "Structs Aninhadas (Composição de Registros)",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 • Lista PDF: Ex. 7, 8, 15, 22, 40, 52",
        "summary": (
            "Uma struct pode conter outra struct como membro (ex.: Data dentro de Compromisso, "
            "Endereco dentro de Cadastro), encadeando pontos no acesso."
        ),
        "conceptHtml": (
            "<p>Para evitar repetir campos como <code>dia, mes, ano</code> ou <code>rua, cep, cidade</code> "
            "em várias estruturas, definimos structs menores e as reutilizamos como membros (composição).</p>"
            "<ul>"
            "<li><strong>Ordem de definição:</strong> a struct interna (<code>Data</code>, <code>Endereco</code>) deve ser declarada <em>antes</em> da struct externa (<code>Pessoa</code>, <code>Compromisso</code>).</li>"
            "<li><strong>Acesso encadeado:</strong> usa-se ponto para cada nível: <code>p.nasc.ano</code> ou <code>agenda[i].data.mes</code>.</li>"
            "<li><strong>Misto com ponteiro:</strong> se <code>pp</code> é ponteiro para <code>Pessoa</code>, o campo interno <code>nasc</code> é um valor dentro dela, logo o acesso é <code>pp-&gt;nasc.ano</code> (seta primeiro, ponto depois!).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "typedef struct { int dia, mes, ano; } Data;\n"
            "typedef struct { int hora, min, seg; } Horario;\n"
            "\n"
            "typedef struct {\n"
            "    Data data;\n"
            "    Horario hora;\n"
            "    char texto[40];\n"
            "} Compromisso; /* Ex. 7 e 15 do PDF */\n"
            "\n"
            "int main(void) {\n"
            "    Compromisso c = {{25, 11, 2026}, {19, 30, 0}, \"Prova de ATP\"};\n"
            "    Compromisso *pc = &c;\n"
            "    printf(\"%02d/%02d/%d %02d:%02d - %s\\n\",\n"
            "           c.data.dia, c.data.mes, c.data.ano,\n"
            "           pc->hora.hora, pc->hora.min, pc->texto);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Data e Horario são definidos primeiro para que o compilador conheça seus tamanhos ao montar Compromisso.",
            "Na inicialização, chaves aninhadas {{25, 11, 2026}, {19, 30, 0}, ...} preenchem cada sub-struct ordenadamente.",
            "pc é ponteiro para Compromisso, mas pc->hora é uma struct (não ponteiro), por isso o segundo acesso usa ponto (pc->hora.hora)."
        ],
        "pitfall": (
            "Declarar a struct externa antes da interna, ou escrever <code>pc-&gt;hora-&gt;min</code> "
            "quando <code>hora</code> é uma struct embutida por valor (não um ponteiro)."
        ),
        "tracers": [
            {
                "id": "tr-strc-11",
                "tabLabel": "Acesso Encadeado",
                "badge": "Composição",
                "title": "Acesso a subcampos via c.data.mes e pc->hora.min",
                "desc": "Veja a hierarquia contígua dos sub-registros dentro de Compromisso.",
                "kind": "1d",
                "codeLines": [
                    "Compromisso c = {{25, 11, 2026}, {19, 30, 0}, \"Prova\"};",
                    "Compromisso *pc = &c;",
                    "pc->data.dia = 26;",
                    "c.hora.min = 45;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"c.data": "25/11/2026", "c.hora": "19:30:00"},
                        "note": "Sub-structs data e hora ficam embutidas dentro do bloco de c (0x9100).",
                        "cells": [
                            {"addr": "0x9100", "label": "c.data.dia", "val": "25", "changed": True},
                            {"addr": "0x9104", "label": "c.data.mes", "val": "11", "changed": True},
                            {"addr": "0x9108", "label": "c.data.ano", "val": "2026", "changed": True},
                            {"addr": "0x910C", "label": "c.hora.hora", "val": "19", "changed": True},
                            {"addr": "0x9110", "label": "c.hora.min", "val": "30", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"pc": "0x9100"},
                        "note": "pc aponta para o início de c.",
                        "cells": [
                            {"addr": "0x9100", "label": "c.data.dia", "val": "25", "changed": False},
                            {"addr": "0x9110", "label": "c.hora.min", "val": "30", "changed": False},
                            {"addr": "0x9150", "label": "pc", "val": "0x9100 -> c", "changed": True, "ptr": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"c.data.dia": "26"},
                        "note": "pc->data acessa a struct interna e .dia altera o dia para 26.",
                        "cells": [
                            {"addr": "0x9100", "label": "c.data.dia", "val": "26", "changed": True},
                            {"addr": "0x9110", "label": "c.hora.min", "val": "30", "changed": False},
                            {"addr": "0x9150", "label": "pc", "val": "0x9100 -> c", "changed": False, "ptr": True}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"c.hora.min": "45"},
                        "note": "Acesso direto c.hora.min altera os minutos para 45.",
                        "cells": [
                            {"addr": "0x9100", "label": "c.data.dia", "val": "26", "changed": False},
                            {"addr": "0x9110", "label": "c.hora.min", "val": "45", "changed": True},
                            {"addr": "0x9150", "label": "pc", "val": "0x9100 -> c", "changed": False, "ptr": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-12",
        "num": "2.12",
        "title": "Structs com Vetores e Strings como Membros",
        "pdfRef": "Lista PDF: Ex. 1, 14, 39, 41",
        "summary": (
            "Uma struct pode conter vetores numéricos (ex.: float notas[3]) e strings de tamanho "
            "fixo (char nome[31]), exigindo cuidado com o '\\0' e funções de string.h."
        ),
        "conceptHtml": (
            "<p>Quando colocamos um vetor dentro de uma struct — como <code>float notas[3];</code> "
            "ou <code>char titulo[31];</code> (30 letras + 1 byte para o terminador <code>'\\0'</code>) "
            "— o array faz parte do tamanho total da struct.</p>"
            "<ul>"
            "<li><strong>Espaço para o <code>'\\0'</code>:</strong> se o enunciado pede \"máximo 15 letras\" (Ex. 12, 13, 14), declare <code>char campo[16];</code> para caber o <code>'\\0'</code>!</li>"
            "<li><strong>Manipulação de strings:</strong> use <code>strcpy</code>/<code>strncpy</code> para atribuir e <code>strcmp</code> para comparar.</li>"
            "<li><strong>Serialização segura:</strong> structs com arrays fixos (sem ponteiros) podem ser gravadas e lidas diretamente em arquivo binário com <code>fwrite</code>/<code>fread</code>.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "\n"
            "typedef struct {\n"
            "    int matricula;\n"
            "    char nome[16]; /* ate 15 letras + '\\0' */\n"
            "    float notas[3];\n"
            "    float media;\n"
            "} Aluno;\n"
            "\n"
            "float calcula_media(const Aluno *a) {\n"
            "    float soma = 0.0f;\n"
            "    for (int i = 0; i < 3; i++) soma += a->notas[i];\n"
            "    return soma / 3.0f;\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    Aluno al;\n"
            "    al.matricula = 2026;\n"
            "    strcpy(al.nome, \"Mariana\");\n"
            "    al.notas[0] = 7.0f; al.notas[1] = 8.5f; al.notas[2] = 8.5f;\n"
            "    al.media = calcula_media(&al);\n"
            "    printf(\"%s -> media %.2f\\n\", al.nome, al.media);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "char nome[16] reserva 16 bytes dentro de Aluno para armazenar até 15 caracteres úteis mais o terminador '\\0'.",
            "a->notas[i] combina '->' (pois 'a' é ponteiro) com '[i]' (indexação do vetor interno).",
            "Como os vetores são internos à struct, sizeof(Aluno) inclui todos os 16 chars e os 3 floats."
        ],
        "pitfall": (
            "Declarar <code>char nome[15]</code> para \"15 letras\" e causar estouro de 1 byte ao "
            "gravar o <code>'\\0'</code>, ou tentar atribuir <code>al.nome = \"Mariana\"</code> com <code>=</code>."
        ),
        "tracers": [
            {
                "id": "tr-strc-12",
                "tabLabel": "Array Dentro da Struct",
                "badge": "Membros Vetoriais",
                "title": "Preenchimento de notas[3] e cálculo de média",
                "desc": "Veja a->notas[i] acumulando as três provas de Mariana.",
                "kind": "1d",
                "codeLines": [
                    "strcpy(al.nome, \"Mariana\");",
                    "al.notas[0] = 7.0f; al.notas[1] = 8.5f; al.notas[2] = 8.5f;",
                    "al.media = calcula_media(&al);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"al.nome": "\"Mariana\""},
                        "note": "strcpy copia M-a-r-i-a-n-a-'\\0' para dentro dos bytes de al.nome.",
                        "cells": [
                            {"addr": "0xA004", "label": "al.nome", "val": "\"Mariana\\0\"", "changed": True},
                            {"addr": "0xA014", "label": "notas[0..2]", "val": "[?, ?, ?]", "changed": False},
                            {"addr": "0xA020", "label": "al.media", "val": "?", "changed": False}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"notas": "[7.0, 8.5, 8.5]"},
                        "note": "As três notas ocupam 3 floats consecutivos dentro da própria struct.",
                        "cells": [
                            {"addr": "0xA004", "label": "al.nome", "val": "\"Mariana\\0\"", "changed": False},
                            {"addr": "0xA014", "label": "notas[0..2]", "val": "[7.0, 8.5, 8.5]", "changed": True},
                            {"addr": "0xA020", "label": "al.media", "val": "?", "changed": False}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"al.media": "8.0"},
                        "note": "calcula_media(&al) soma 24.0 / 3 = 8.0 e armazena em al.media.",
                        "cells": [
                            {"addr": "0xA004", "label": "al.nome", "val": "\"Mariana\\0\"", "changed": False},
                            {"addr": "0xA014", "label": "notas[0..2]", "val": "[7.0, 8.5, 8.5]", "changed": False},
                            {"addr": "0xA020", "label": "al.media", "val": "8.0", "changed": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-13",
        "num": "2.13",
        "title": "Structs com Ponteiros Internos (Deep Copy e Deep Free)",
        "pdfRef": "Lista PDF: Ex. 19, 20, 50 • Memória ADS (Lição #1)",
        "summary": (
            "Quando uma struct possui ponteiros para dados dinâmicos (ex.: char *str ou Filme *filmes), "
            "copiar e liberar exige clonar e desalocar os blocos apontados (deep copy / deep free)."
        ),
        "conceptHtml": (
            "<p>Nos exercícios de Livro de Receitas (Ex. 19), Diretores/Filmes (Ex. 20) e String "
            "com tamanho + ponteiro (Ex. 50), a struct não guarda os dados em si, mas sim um "
            "<strong>ponteiro para um bloco no heap</strong>.</p>"
            "<ul>"
            "<li><strong>Deep Copy (cópia profunda):</strong> aloque novo bloco com <code>malloc</code> para o destino e copie o conteúdo com <code>memcpy</code>/<code>strcpy</code>.</li>"
            "<li><strong>Deep Free (liberação na ordem inversa):</strong> libere <em>primeiro</em> os ponteiros internos (<code>free(d.filmes)</code>) e só <em>depois</em> o ponteiro da struct externa (se houver).</li>"
            "<li><strong>Nunca serialize diretamente em arquivo binário:</strong> <code>fwrite(&amp;s, sizeof(s), 1, f)</code> gravaria o endereço de memória (inútil ao reabrir o programa!), não o texto apontado.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n"
            "\n"
            "typedef struct {\n"
            "    int tam;\n"
            "    char *dados; /* Ex. 50 do PDF */\n"
            "} MinhaStr;\n"
            "\n"
            "MinhaStr cria_str(const char *orig) {\n"
            "    MinhaStr s;\n"
            "    s.tam = (int)strlen(orig);\n"
            "    s.dados = malloc((size_t)s.tam + 1);\n"
            "    if (s.dados) strcpy(s.dados, orig);\n"
            "    return s;\n"
            "}\n"
            "\n"
            "MinhaStr clona_str(const MinhaStr *orig) {\n"
            "    return cria_str(orig->dados); /* deep copy: novo malloc! */\n"
            "}\n"
            "\n"
            "void libera_str(MinhaStr *s) {\n"
            "    free(s->dados); /* deep free */\n"
            "    s->dados = NULL;\n"
            "    s->tam = 0;\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    MinhaStr a = cria_str(\"ADS\");\n"
            "    MinhaStr b = clona_str(&a);\n"
            "    b.dados[0] = 'X'; /* a.dados segue \"ADS\" */\n"
            "    printf(\"%s (%d) | %s (%d)\\n\", a.dados, a.tam, b.dados, b.tam);\n"
            "    libera_str(&a);\n"
            "    libera_str(&b);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "cria_str calcula strlen(orig) e aloca tam + 1 bytes no heap para incluir '\\0'.",
            "clona_str faz deep copy: b.dados recebe um endereço diferente no heap, evitando compartilhamento com a.dados.",
            "libera_str chama free(s->dados) e zera o ponteiro (NULL) para prevenir dangling pointers e double free."
        ],
        "pitfall": (
            "Dar <code>free(diretor)</code> antes de dar <code>free(diretor-&gt;filmes)</code> "
            "(causa vazamento de memória dos filmes) ou usar <code>b = a</code> em vez de deep copy."
        ),
        "tracers": [
            {
                "id": "tr-strc-13",
                "tabLabel": "Deep Copy no Heap",
                "badge": "Stack + Heap",
                "title": "Separação de buffers em clona_str(&a)",
                "desc": "a.dados e b.dados apontam para blocos independentes no heap.",
                "kind": "1d",
                "codeLines": [
                    "MinhaStr a = cria_str(\"ADS\");",
                    "MinhaStr b = clona_str(&a);",
                    "b.dados[0] = 'X';",
                    "libera_str(&a); libera_str(&b);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"a.tam": "3", "a.dados": "0xH100"},
                        "note": "cria_str aloca 4 bytes em 0xH100 no heap com \"ADS\".",
                        "cells": [
                            {"addr": "stack:a", "label": "a.dados", "val": "0xH100", "changed": True, "ptr": True},
                            {"addr": "0xH100", "label": "heap A", "val": "\"ADS\"", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"b.tam": "3", "b.dados": "0xH200"},
                        "note": "clona_str faz novo malloc em 0xH200 e copia \"ADS\" (deep copy).",
                        "cells": [
                            {"addr": "stack:a", "label": "a.dados", "val": "0xH100", "changed": False, "ptr": True},
                            {"addr": "0xH100", "label": "heap A", "val": "\"ADS\"", "changed": False},
                            {"addr": "stack:b", "label": "b.dados", "val": "0xH200", "changed": True, "ptr": True},
                            {"addr": "0xH200", "label": "heap B", "val": "\"ADS\"", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"*a.dados": "\"ADS\"", "*b.dados": "\"XDS\""},
                        "note": "Alterar b.dados[0] modifica apenas 0xH200; a.dados segue intacto.",
                        "cells": [
                            {"addr": "0xH100", "label": "heap A", "val": "\"ADS\"", "changed": False},
                            {"addr": "0xH200", "label": "heap B", "val": "\"XDS\"", "changed": True}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"a.dados": "NULL", "b.dados": "NULL"},
                        "note": "Ambos os blocos são liberados sem double free e ponteiros zerados.",
                        "cells": [
                            {"addr": "stack:a", "label": "a.dados", "val": "NULL", "changed": True, "ptr": True},
                            {"addr": "stack:b", "label": "b.dados", "val": "NULL", "changed": True, "ptr": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-14",
        "num": "2.14",
        "title": "Ponteiros para Structs e Vetores Dinâmicos (malloc + cria)",
        "pdfRef": "Deitel 6ª Ed. Cap. 12 • Lista PDF: Ex. 12, 35, 38",
        "summary": (
            "Aloque uma única struct (padrão fábrica struct Produto* cria(...)) ou um vetor "
            "de N structs em tempo de execução usando malloc/calloc e sizeof(*p)."
        ),
        "conceptHtml": (
            "<p>Quando o tamanho do cadastro só é conhecido em tempo de execução (<code>scanf(\"%d\", &amp;n)</code>) "
            "ou quando queremos construir um objeto no heap e devolver seu ponteiro (como no Ex. 35 do PDF), "
            "usamos alocação dinâmica:</p>"
            "<ul>"
            "<li><strong>1 struct no heap (função <code>cria</code>):</strong> <code>struct produto *p = malloc(sizeof(*p));</code> — sempre valide <code>if (p == NULL)</code> antes de usar <code>p-&gt;</code>!</li>"
            "<li><strong>Vetor dinâmico de N structs:</strong> <code>Carro *v = calloc((size_t)n, sizeof(*v));</code> — <code>calloc</code> já zera todos os campos e retorna um ponteiro que pode ser indexado como <code>v[i].preco</code>.</li>"
            "<li><strong>Liberação obrigatória:</strong> tudo que nasce com <code>malloc</code>/<code>calloc</code> deve terminar com <code>free(p)</code>.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n"
            "\n"
            "struct produto {\n"
            "    int codigo;\n"
            "    char nome[51];\n"
            "    int quantidade;\n"
            "    float preco;\n"
            "};\n"
            "\n"
            "/* Ex. 35(b) do PDF: fabrica dinamica no heap */\n"
            "struct produto *cria(int cod, const char *nome, int quant, float preco) {\n"
            "    struct produto *p = malloc(sizeof(*p));\n"
            "    if (p == NULL) return NULL;\n"
            "    p->codigo = cod;\n"
            "    strncpy(p->nome, nome, 50);\n"
            "    p->nome[50] = '\\0';\n"
            "    p->quantidade = quant;\n"
            "    p->preco = preco;\n"
            "    return p;\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    struct produto *prod = cria(101, \"SSD 1TB\", 8, 349.90f);\n"
            "    if (prod != NULL) {\n"
            "        printf(\"%d %s R$ %.2f\\n\", prod->codigo, prod->nome, prod->preco);\n"
            "        free(prod);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "malloc(sizeof(*p)) calcula automaticamente o tamanho completo de struct produto sem risco de erro manual.",
            "Se malloc retornar NULL (falta de memória), cria devolve NULL em vez de tentar escrever em endereço inválido.",
            "strncpy(..., 50) + p->nome[50] = '\\0' garante que nomes longos não estourem o buffer de 51 bytes."
        ],
        "pitfall": (
            "Esquecer <code>sizeof(struct produto)</code> e fazer <code>malloc(sizeof(struct produto *))</code> "
            "(aloca apenas 8 bytes do ponteiro em vez dos ~64 bytes da struct, corrompendo o heap)."
        ),
        "tracers": [
            {
                "id": "tr-strc-14",
                "tabLabel": "Fábrica cria() no Heap",
                "badge": "malloc + free",
                "title": "Retorno de ponteiro para struct alocada no heap",
                "desc": "O objeto sobrevive ao retorno da função cria() até que main chame free().",
                "kind": "1d",
                "codeLines": [
                    "struct produto *p = malloc(sizeof(*p));",
                    "p->codigo = 101; p->preco = 349.90f;",
                    "return p; /* recebido por prod em main */",
                    "free(prod); prod = NULL;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"p": "0xH500"},
                        "note": "malloc reserva ~64 bytes no heap em 0xH500 e devolve o endereço para p.",
                        "cells": [
                            {"addr": "stack:p", "label": "cria::p", "val": "0xH500", "changed": True, "ptr": True},
                            {"addr": "0xH500", "label": "heap.codigo", "val": "?", "changed": True},
                            {"addr": "0xH53C", "label": "heap.preco", "val": "?", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"p->codigo": "101", "p->preco": "349.90"},
                        "note": "Campos no heap são inicializados via seta ->.",
                        "cells": [
                            {"addr": "stack:p", "label": "cria::p", "val": "0xH500", "changed": False, "ptr": True},
                            {"addr": "0xH500", "label": "heap.codigo", "val": "101", "changed": True},
                            {"addr": "0xH53C", "label": "heap.preco", "val": "349.90", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"prod": "0xH500"},
                        "note": "Frame de cria() some, mas 0xH500 permanece vivo no heap e agora prod aponta para ele.",
                        "cells": [
                            {"addr": "stack:prod", "label": "main::prod", "val": "0xH500", "changed": True, "ptr": True},
                            {"addr": "0xH500", "label": "heap.codigo", "val": "101", "changed": False},
                            {"addr": "0xH53C", "label": "heap.preco", "val": "349.90", "changed": False}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"prod": "NULL"},
                        "note": "free(prod) devolve 0xH500 ao sistema e prod = NULL evita uso após liberação.",
                        "cells": [
                            {"addr": "stack:prod", "label": "main::prod", "val": "NULL", "changed": True, "ptr": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-15",
        "num": "2.15",
        "title": "union: Compartilhamento de Memória e Tagged Union",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.8) • Lista PDF: Ex. 34, 47",
        "summary": (
            "Enquanto struct soma o espaço de todos os campos, union faz todos os membros "
            "compartilharem o mesmo endereço, ocupando apenas o tamanho do maior membro."
        ),
        "conceptHtml": (
            "<p>Uma <code>union</code> (união) tem sintaxe parecida com <code>struct</code>, "
            "mas com semântica de memória oposta: apenas <strong>um membro é válido por vez</strong>.</p>"
            "<ul>"
            "<li><strong>Tamanho:</strong> <code>sizeof(union)</code> é igual ao maior membro (mais eventual alinhamento), economizando RAM quando um registro tem variantes mutuamente exclusivas (como Contrato Individual <em>ou</em> Coletivo no Ex. 34 do PDF).</li>"
            "<li><strong>Sobrescrita:</strong> gravar em um campo da <code>union</code> sobrescreve os bytes dos demais campos.</li>"
            "<li><strong>Tagged Union (Padrão Ouro):</strong> envolva a <code>union</code> dentro de uma <code>struct</code> junto de uma etiqueta (<code>char tipo</code> ou <code>enum</code>) para saber qual membro ler com segurança!</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "typedef struct { int num; char cpf[15]; float renda; } Individual;\n"
            "typedef struct { int num; char cnpj[19]; int qtdMasc; } Coletivo;\n"
            "\n"
            "typedef union {\n"
            "    Individual ind;\n"
            "    Coletivo col;\n"
            "} DadosContrato; /* ocupa max(sizeof(ind), sizeof(col)) */\n"
            "\n"
            "typedef struct {\n"
            "    char tipo; /* 'I' ou 'C' (tag) */\n"
            "    DadosContrato dados;\n"
            "} Contrato;\n"
            "\n"
            "int main(void) {\n"
            "    Contrato c;\n"
            "    c.tipo = 'I';\n"
            "    c.dados.ind = (Individual){1001, \"123.456.789-00\", 4500.0f};\n"
            "    if (c.tipo == 'I')\n"
            "        printf(\"Contrato %d CPF %s\\n\", c.dados.ind.num, c.dados.ind.cpf);\n"
            "    printf(\"sizeof(union)=%zu\\n\", sizeof(DadosContrato));\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Individual e Coletivo começam exatamente no mesmo offset (deslocamento 0) dentro de DadosContrato.",
            "Se você escrever em c.dados.ind e depois escrever em c.dados.col, os bytes antigos de ind são corrompidos.",
            "O campo c.tipo ('I' ou 'C') funciona como discriminador (tag) para escolher o ramo correto no if/switch."
        ],
        "pitfall": (
            "Ler um membro da <code>union</code> diferente do último que foi gravado (type punning "
            "acidental) ou assumir que <code>sizeof(union)</code> soma o tamanho de todos os membros."
        ),
        "tracers": [
            {
                "id": "tr-strc-15",
                "tabLabel": "Sobreposição na Union",
                "badge": "Memória Compartilhada",
                "title": "union Valor { int i; float f; } no mesmo endereço",
                "desc": "Escrever em u.f sobrescreve os mesmos 4 bytes onde u.i estava guardado.",
                "kind": "1d",
                "codeLines": [
                    "union Valor { int i; float f; } u;",
                    "u.i = 65;",
                    "u.f = 3.5f; /* sobrescreve u.i! */"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"sizeof(u)": "4 bytes"},
                        "note": "u ocupa apenas 4 bytes (tamanho do maior membro, não 8 bytes).",
                        "cells": [
                            {"addr": "0xB000..0xB003", "label": "u.i / u.f", "val": "????", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"u.i": "65"},
                        "note": "Os 4 bytes em 0xB000 guardam o inteiro 65 (0x00000041).",
                        "cells": [
                            {"addr": "0xB000..0xB003", "label": "u.i (ativo)", "val": "65 (0x00000041)", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"u.f": "3.5", "u.i": "1080033280 (lixo!)"},
                        "note": "Gravar 3.5f (IEEE-754: 0x40600000) no mesmo endereço destrói o antigo valor de u.i.",
                        "cells": [
                            {"addr": "0xB000..0xB003", "label": "u.f (ativo)", "val": "3.5 (0x40600000)", "changed": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-16",
        "num": "2.16",
        "title": "enum: Constantes Nomeadas e Uso com Structs",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.11) • Lista PDF: Ex. 33, 46",
        "summary": (
            "enum cria um conjunto de constantes inteiras nomeadas (0, 1, 2... por padrão ou com "
            "valores explícitos), substituindo 'números mágicos' em structs."
        ),
        "conceptHtml": (
            "<p>No Ex. 33 do PDF (sócios de um clube), campos como estado civil (1=Casado, 2=Solteiro...), "
            "turno (1=Manhã, 2=Tarde, 3=Noite) e atividade ficam muito mais legíveis com <code>enum</code>.</p>"
            "<ul>"
            "<li><strong>Numeração padrão:</strong> o primeiro item vale <code>0</code> e os seguintes incrementam de 1 em 1.</li>"
            "<li><strong>Valor inicial customizado:</strong> <code>typedef enum { MANHA = 1, TARDE, NOITE } Turno;</code> faz <code>TARDE = 2</code> e <code>NOITE = 3</code> automaticamente!</li>"
            "<li><strong>Integração com <code>switch</code> e <code>struct</code>:</strong> campos <code>enum</code> são armazenados como inteiros e lidos/comparados por nome simbólico (<code>if (s.turno == MANHA)</code>).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "typedef enum { CASADO = 1, SOLTEIRO, DIVORCIADO, VIUVO } EstadoCivil;\n"
            "typedef enum { MANHA = 1, TARDE, NOITE } Turno;\n"
            "\n"
            "typedef struct {\n"
            "    int matricula;\n"
            "    EstadoCivil est_civil;\n"
            "    Turno turno;\n"
            "} Socio; /* Baseado no Ex. 33 do PDF */\n"
            "\n"
            "int main(void) {\n"
            "    Socio s = {501, CASADO, NOITE};\n"
            "    if (s.est_civil == CASADO && s.turno == NOITE) {\n"
            "        printf(\"Socio %d: Casado, turno %d (Noite)\\n\", s.matricula, s.turno);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "CASADO recebe 1 explicitamente; SOLTEIRO, DIVORCIADO e VIUVO recebem 2, 3 e 4 automaticamente.",
            "Na struct Socio, os campos est_civil e turno ocupam espaço de um inteiro (tipicamente 4 bytes).",
            "A leitura via scanf(\"%d\", (int*)&s.turno) pode ler o número, mas o código usa nomes claros como NOITE."
        ],
        "pitfall": (
            "Tentar imprimir o <em>nome</em> do enumerador com <code>printf(\"%s\", s.turno)</code> "
            "(<code>enum</code> é um inteiro em C; <code>%s</code> causaria crash! Use um vetor de strings ou <code>switch</code> para exibir o texto)."
        ),
        "tracers": [
            {
                "id": "tr-strc-16",
                "tabLabel": "Constantes Enum",
                "badge": "Inteiros Nomeados",
                "title": "Mapeamento de enum em uma struct Socio",
                "desc": "Cada constante enum é resolvida para um valor inteiro em tempo de compilação.",
                "kind": "1d",
                "codeLines": [
                    "typedef enum { CASADO = 1, SOLTEIRO, DIVORCIADO } EstadoCivil;",
                    "typedef enum { MANHA = 1, TARDE, NOITE } Turno;",
                    "Socio s = {501, CASADO, NOITE};"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"CASADO": "1", "SOLTEIRO": "2", "DIVORCIADO": "3"},
                        "note": "Constantes recebem 1, 2, 3 automaticamente.",
                        "cells": []
                    },
                    {
                        "line": 1,
                        "vars": {"MANHA": "1", "TARDE": "2", "NOITE": "3"},
                        "note": "NOITE é avaliada pelo compilador como o inteiro 3.",
                        "cells": []
                    },
                    {
                        "line": 2,
                        "vars": {"s.matricula": "501", "s.est_civil": "1 (CASADO)", "s.turno": "3 (NOITE)"},
                        "note": "Em memória, s armazena os inteiros 501, 1 e 3.",
                        "cells": [
                            {"addr": "0xC000", "label": "s.matricula", "val": "501", "changed": True},
                            {"addr": "0xC004", "label": "s.est_civil", "val": "1 (CASADO)", "changed": True},
                            {"addr": "0xC008", "label": "s.turno", "val": "3 (NOITE)", "changed": True}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-17",
        "num": "2.17",
        "title": "Campos de Bits (Bit Fields), Alinhamento e sizeof (Padding)",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 (Seção 10.10) • Arquitetura x86/x64",
        "summary": (
            "Entenda por que sizeof(struct) costuma ser maior que a soma dos campos (padding de "
            "alinhamento) e como bit fields compactam flags em poucos bits."
        ),
        "conceptHtml": (
            "<p>A CPU lê memória de forma mais rápida quando tipos de 4 bytes (<code>int</code>) "
            "estão em endereços múltiplos de 4, e tipos de 8 bytes (<code>double</code>) em múltiplos de 8. "
            "Por isso, o compilador insere bytes invisíveis de enchimento chamados <strong>padding</strong>:</p>"
            "<ul>"
            "<li><strong>Efeito da ordem dos campos:</strong> <code>struct A { char c; int x; char d; };</code> gasta <strong>12 bytes</strong> (1 + 3 pad + 4 + 1 + 3 pad), mas reordenar para <code>{ int x; char c; char d; }</code> reduz para <strong>8 bytes</strong>!</li>"
            "<li><strong>Sempre use <code>sizeof(MinhaStruct)</code>:</strong> nunca some manualmente os tamanhos para usar em <code>malloc</code> ou <code>fread</code>.</li>"
            "<li><strong>Campos de bits (Bit Fields):</strong> <code>unsigned ativo : 1; unsigned nivel : 3;</code> compacta múltiplos valores pequenos dentro de uma mesma palavra de memória (<code>sizeof</code> = 4 bytes para várias flags).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "\n"
            "struct Desalinhada { char a; int b; char c; }; /* tipico: 12 bytes */\n"
            "struct Otimizada   { int b; char a; char c; }; /* tipico: 8 bytes */\n"
            "\n"
            "typedef struct {\n"
            "    unsigned int ativo : 1; /* 0..1 (1 bit) */\n"
            "    unsigned int tipo  : 2; /* 0..3 (2 bits) */\n"
            "    unsigned int mes   : 4; /* 0..15 (4 bits) */\n"
            "} Flags;\n"
            "\n"
            "int main(void) {\n"
            "    Flags f = {1, 2, 11};\n"
            "    printf(\"Desalinhada=%zu | Otimizada=%zu | Flags=%zu\\n\",\n"
            "           sizeof(struct Desalinhada),\n"
            "           sizeof(struct Otimizada),\n"
            "           sizeof(Flags));\n"
            "    printf(\"ativo=%u tipo=%u mes=%u\\n\", f.ativo, f.tipo, f.mes);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Em Desalinhada, após 'char a' (1 byte), o compilador insere 3 bytes de padding para que 'int b' comece em múltiplo de 4; ao final insere mais 3 bytes para que o tamanho total seja múltiplo de 4.",
            "Em Otimizada, colocar o int primeiro agrupa os dois chars juntos, eliminando o padding intermediário (4 + 1 + 1 + 2 pad = 8 bytes).",
            "Na struct Flags, ativo (1 bit), tipo (2 bits) e mes (4 bits) cabem todos nos primeiros 7 bits de um único unsigned int."
        ],
        "pitfall": (
            "Tentar obter o endereço de um bit field (<code>&amp;f.ativo</code>) — erro de compilação, "
            "pois ponteiros em C apontam para bytes, não para bits individuais — ou somar tamanhos na mão ignorando padding."
        ),
        "tracers": [
            {
                "id": "tr-strc-17",
                "tabLabel": "Padding vs Otimizada",
                "badge": "Alinhamento • sizeof",
                "title": "Comparação byte a byte de padding em Desalinhada vs Otimizada",
                "desc": "Veja como a ordem dos membros muda sizeof() de 12 para 8 bytes.",
                "kind": "1d",
                "codeLines": [
                    "struct Desalinhada { char a; int b; char c; }; /* 12 B */",
                    "struct Otimizada   { int b; char a; char c; }; /* 8 B */",
                    "Flags f = {1, 2, 11}; /* 7 bits em 4 B */"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"sizeof(Desalinhada)": "12 bytes (6 úteis + 6 padding)"},
                        "note": "Padding após 'a' (bytes 1..3) e após 'c' (bytes 9..11) garante alinhamento de 4 em 4.",
                        "cells": [
                            {"addr": "+0", "label": "char a", "val": "1 B", "changed": True},
                            {"addr": "+1..+3", "label": "PADDING", "val": "3 B (lixo)", "changed": True},
                            {"addr": "+4..+7", "label": "int b", "val": "4 B", "changed": True},
                            {"addr": "+8", "label": "char c", "val": "1 B", "changed": True},
                            {"addr": "+9..+11", "label": "PADDING", "val": "3 B (lixo)", "changed": True}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"sizeof(Otimizada)": "8 bytes (6 úteis + 2 padding)"},
                        "note": "Reordenando do maior tipo para o menor, os dois chars ficam contíguos e sobram só 2 bytes de padding.",
                        "cells": [
                            {"addr": "+0..+3", "label": "int b", "val": "4 B", "changed": True},
                            {"addr": "+4", "label": "char a", "val": "1 B", "changed": True},
                            {"addr": "+5", "label": "char c", "val": "1 B", "changed": True},
                            {"addr": "+6..+7", "label": "PADDING", "val": "2 B", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"sizeof(Flags)": "4 bytes", "bits usados": "7 de 32"},
                        "note": "Bit fields empacotam ativo(1b), tipo(2b) e mes(4b) dentro da mesma palavra de 32 bits.",
                        "cells": [
                            {"addr": "bit 0", "label": "ativo:1", "val": "1", "changed": True},
                            {"addr": "bits 1..2", "label": "tipo:2", "val": "2 (10b)", "changed": True},
                            {"addr": "bits 3..6", "label": "mes:4", "val": "11 (1011b)", "changed": True},
                            {"addr": "bits 7..31", "label": "livres", "val": "25 bits", "changed": False}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "strc-18",
        "num": "2.18",
        "title": "Estruturas Autorreferenciadas, Aplicações e Erros Comuns",
        "pdfRef": "Deitel 6ª Ed. Cap. 10 e 12 • Lista PDF: Ex. 3, 17, 41, 48",
        "summary": (
            "Uma struct autorreferenciada contém um ponteiro para si mesma (struct No *prox), "
            "base de listas encadeadas, pilhas e filas — além do checklist final dos 4 erros clássicos."
        ),
        "conceptHtml": (
            "<p>Uma struct <strong>não pode conter uma instância de si mesma</strong> por valor "
            "(seria tamanho infinito!), mas <strong>pode conter um ponteiro</strong> para o próprio "
            "tipo (<code>struct No *prox;</code>), pois todo ponteiro tem tamanho fixo.</p>"
            "<ul>"
            "<li><strong>Aplicações clássicas da lista:</strong> Agenda ordenada (Ex. 3), Estoque (Ex. 17), Pilha push/pop (Ex. 48) e Lista Encadeada (Ex. 41).</li>"
            "<li><strong>Checklist dos 4 erros clássicos em Structs:</strong>"
            "<ol>"
            "<li>Esquecer o <code>;</code> após a chave de fechamento <code>}</code> da struct.</li>"
            "<li>Confundir <code>.</code> (variável) com <code>-&gt;</code> (ponteiro).</li>"
            "<li>Comparar duas structs com <code>if (a == b)</code> — C não permite <code>==</code> entre structs por causa do padding! Compare campo a campo (e strings com <code>strcmp</code>).</li>"
            "<li>Atribuir strings com <code>a.nome = \"Ana\"</code> — use <code>strcpy(a.nome, \"Ana\")</code>.</li>"
            "</ol></li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "\n"
            "typedef struct No {\n"
            "    int dado;\n"
            "    struct No *prox; /* ponteiro para o mesmo tipo */\n"
            "} No;\n"
            "\n"
            "int main(void) {\n"
            "    No *n1 = malloc(sizeof(No));\n"
            "    No *n2 = malloc(sizeof(No));\n"
            "    if (!n1 || !n2) { free(n1); free(n2); return 1; }\n"
            "    n1->dado = 10; n1->prox = n2;\n"
            "    n2->dado = 20; n2->prox = NULL;\n"
            "\n"
            "    for (No *p = n1; p != NULL; p = p->prox) {\n"
            "        printf(\"%d -> \", p->dado);\n"
            "    }\n"
            "    printf(\"NULL\\n\");\n"
            "    free(n2); free(n1);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "struct No *prox é válido porque o ponteiro ocupa tamanho fixo (4 ou 8 bytes) independentemente de struct No.",
            "n1->prox guarda o endereço de n2; n2->prox recebe NULL para marcar o fim da lista encadeada.",
            "O percurso usa p = p->prox até p == NULL, visitando nós em posições arbitrárias do heap."
        ],
        "pitfall": (
            "Tentar declarar <code>struct No prox;</code> sem o asterisco <code>*</code> (erro: tipo incompleto), "
            "comparar structs com <code>n1 == n2</code> (inválido em C) ou esquecer de liberar todos os nós na lista."
        ),
        "tracers": [
            {
                "id": "tr-strc-18",
                "tabLabel": "Lista Encadeada (No *)",
                "badge": "Autorreferenciada",
                "title": "Ligação de nós n1 -> n2 -> NULL no heap",
                "desc": "Acompanhe o ponteiro de percurso p avançando com p = p->prox.",
                "kind": "1d",
                "codeLines": [
                    "n1->dado = 10; n1->prox = n2;",
                    "n2->dado = 20; n2->prox = NULL;",
                    "No *p = n1;",
                    "p = p->prox; /* p agora aponta para n2 */",
                    "p = p->prox; /* p vira NULL: fim */"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"n1": "0xH010", "n1->prox": "0xH020"},
                        "note": "n1 (0xH010) armazena dado=10 e aponta para n2 (0xH020).",
                        "cells": [
                            {"addr": "0xH010", "label": "n1 {dado,prox}", "val": "{10, 0xH020}", "changed": True, "ptr": True},
                            {"addr": "0xH020", "label": "n2 {dado,prox}", "val": "{?, ?}", "changed": False}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"n2->dado": "20", "n2->prox": "NULL"},
                        "note": "n2 fecha a cadeia apontando para NULL.",
                        "cells": [
                            {"addr": "0xH010", "label": "n1 {dado,prox}", "val": "{10, 0xH020}", "changed": False, "ptr": True},
                            {"addr": "0xH020", "label": "n2 {dado,prox}", "val": "{20, NULL}", "changed": True}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"p": "0xH010 (n1)", "imprime": "10 ->"},
                        "note": "p inicia em n1 e lê p->dado == 10.",
                        "cells": [
                            {"addr": "0xH010", "label": "n1 (p)", "val": "{10, 0xH020}", "changed": True, "ptr": True},
                            {"addr": "0xH020", "label": "n2", "val": "{20, NULL}", "changed": False}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"p": "0xH020 (n2)", "imprime": "20 ->"},
                        "note": "p = p->prox salta para 0xH020 e lê p->dado == 20.",
                        "cells": [
                            {"addr": "0xH010", "label": "n1", "val": "{10, 0xH020}", "changed": False},
                            {"addr": "0xH020", "label": "n2 (p)", "val": "{20, NULL}", "changed": True, "ptr": True}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"p": "NULL", "imprime": "NULL"},
                        "note": "p = p->prox recebe NULL e encerra o laço for.",
                        "cells": [
                            {"addr": "stack:p", "label": "p", "val": "NULL (fim)", "changed": True}
                        ]
                    }
                ]
            }
        ]
    }
]
