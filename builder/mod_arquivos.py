"""Módulo 3 — Arquivos em C (TOPICS_ARQUIVOS: 17 tópicos, arq-1 a arq-17)."""
from __future__ import annotations

TOPICS_ARQUIVOS = [
    {
        "id": "arq-1",
        "num": "3.1",
        "title": "Conceito: Persistência, Memória vs. Armazenamento e Texto vs. Binário",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.1–11.2) · C Completo e Total Cap. 8",
        "summary": (
            "Variáveis em RAM são voláteis e desaparecem quando o programa termina; arquivos em disco garantem "
            "persistência como fluxos (streams) de bytes, organizados em formato texto (ASCII/UTF-8 legível) ou "
            "binário (espelho bruto dos bytes da memória)."
        ),
        "conceptHtml": (
            "<p>Em C, toda variável comum (<code>int</code>, <code>double</code>, <code>struct</code>) vive na "
            "<strong>memória principal (RAM)</strong>, que é rápida, porém <em>volátil</em>: ao encerrar o processo ou "
            "desligar o computador, os dados são perdidos. Para alcançar <strong>persistência</strong>, gravamos esses "
            "dados em <strong>armazenamento secundário</strong> (SSD/HD) através de <strong>arquivos</strong>.</p>"
            "<p>Para a biblioteca padrão C, um arquivo é um <strong>fluxo sequencial de bytes</strong> (<em>stream</em>) "
            "terminado por um marcador lógico de fim de arquivo (<code>EOF</code>). Existem duas formas principais de "
            "interpretar esses bytes (Deitel Cap. 11.2):</p>"
            "<ul>"
            "<li><strong>Arquivo Texto:</strong> armazena caracteres codificados (ex.: ASCII). O inteiro <code>12345</code> "
            "vira 5 bytes (<code>'1','2','3','4','5'</code>) e quebras de linha sofrem tradução de plataforma "
            "(<code>\\n</code> &harr; <code>\\r\\n</code> no Windows). É legível por humanos, porém exige conversão (parsing/formatação).</li>"
            "<li><strong>Arquivo Binário:</strong> grava exatamente a representação interna da RAM sem tradução de caracteres. "
            "O inteiro <code>12345</code> (<code>0x00003039</code> em 32 bits) ocupa sempre 4 bytes fixos, independentemente "
            "do número de dígitos. É compacto e mais rápido para I/O em lote, mas não é legível em editores de texto comuns.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    int valor = 12345; // 4 bytes na RAM (0x39 0x30 0x00 0x00 em little-endian)\n\n"
            "    FILE *ft = fopen(\"num.txt\", \"w\");\n"
            "    if (ft != NULL) {\n"
            "        fprintf(ft, \"%d\\n\", valor); // Texto: '1','2','3','4','5','\\n' (6+ bytes)\n"
            "        fclose(ft);\n"
            "    }\n\n"
            "    FILE *fb = fopen(\"num.bin\", \"wb\");\n"
            "    if (fb != NULL) {\n"
            "        fwrite(&valor, sizeof(int), 1, fb); // Binario: exatos 4 bytes crus\n"
            "        fclose(fb);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "O inteiro valor = 12345 ocupa 4 bytes fixos na RAM em formato binário (complemento de dois).",
            "Ao gravar com fprintf em num.txt, o valor é convertido para dígitos ASCII ('1','2','3','4','5'), consumindo 5 bytes mais a quebra de linha.",
            "Ao gravar com fwrite em num.bin, os 4 bytes brutos da RAM são copiados sem conversão, preservando tamanho fixo de registro."
        ],
        "pitfall": (
            "Achar que 'arquivo binário' não contém texto ou que 'int' ocupa sempre 2 ou 4 bytes iguais no texto e no binário: "
            "no texto, 1000000000 gasta 10 bytes (10 dígitos), enquanto em binário um int de 32 bits gasta sempre 4 bytes."
        ),
        "tracers": [
            {
                "id": "tr-arq-1",
                "tabLabel": "Texto vs Binário",
                "badge": "1D · Bytes em Disco",
                "title": "Comparação de Bytes: RAM vs num.txt vs num.bin",
                "desc": "Acompanhe quantos bytes e qual representação são gravados para int valor = 12345.",
                "kind": "1d",
                "codeLines": [
                    "int valor = 12345;",
                    "fprintf(ft, \"%d\\n\", valor);",
                    "fwrite(&valor, sizeof(int), 1, fb);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"valor": "12345", "RAM": "4 bytes (0x39 0x30 0x00 0x00)"},
                        "note": "Na RAM, 12345 está em little-endian (4 bytes).",
                        "cells": [
                            {"label": "RAM[0]", "val": "0x39", "state": "active"},
                            {"label": "RAM[1]", "val": "0x30", "state": "active"},
                            {"label": "RAM[2]", "val": "0x00", "state": "active"},
                            {"label": "RAM[3]", "val": "0x00", "state": "active"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"valor": "12345", "num.txt": "6 bytes (ASCII)"},
                        "note": "fprintf converte o inteiro para caracteres ASCII legíveis ('1'..'5' + '\\n').",
                        "cells": [
                            {"label": "txt[0]", "val": "'1' (0x31)", "state": "modified"},
                            {"label": "txt[1]", "val": "'2' (0x32)", "state": "modified"},
                            {"label": "txt[2]", "val": "'3' (0x33)", "state": "modified"},
                            {"label": "txt[3]", "val": "'4' (0x34)", "state": "modified"},
                            {"label": "txt[4]", "val": "'5' (0x35)", "state": "modified"},
                            {"label": "txt[5]", "val": "'\\n' (0x0A)", "state": "modified"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"valor": "12345", "num.bin": "4 bytes (brutos)"},
                        "note": "fwrite copia exatamente os 4 bytes da RAM para num.bin sem conversão.",
                        "cells": [
                            {"label": "bin[0]", "val": "0x39", "state": "active"},
                            {"label": "bin[1]", "val": "0x30", "state": "active"},
                            {"label": "bin[2]", "val": "0x00", "state": "active"},
                            {"label": "bin[3]", "val": "0x00", "state": "active"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-2",
        "num": "3.2",
        "title": "Ponteiro FILE * e Biblioteca <stdio.h>",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.3) · C Completo e Total Cap. 8",
        "summary": (
            "Em C, todo arquivo aberto é manipulado por meio de um ponteiro FILE *, estrutura definida em <stdio.h> "
            "que guarda descritor do SO, ponteiro para buffer de E/S, posição atual e flags de erro/EOF."
        ),
        "conceptHtml": (
            "<p>Ao trabalhar com arquivos em C, o programador não acessa diretamente os setores do disco nem cria "
            "variáveis do tipo <code>FILE</code> por valor. A biblioteca <code>&lt;stdio.h&gt;</code> define o tipo "
            "opaco <code>FILE</code> (um apelido via <code>typedef struct</code>), e todas as funções de E/S recebem ou "
            "retornam um ponteiro <code>FILE *</code>.</p>"
            "<p>De acordo com Deitel (Cap. 11.3) e Schildt (Cap. 8), a estrutura <code>FILE</code> mantém internamente o "
            "<strong>Bloco de Controle de Arquivo (FCB)</strong> do stream em espaço de usuário, contendo:</p>"
            "<ul>"
            "<li><strong>Descritor de arquivo (fd):</strong> identificador numérico fornecido pelo sistema operacional.</li>"
            "<li><strong>Buffer e ponteiro de buffer:</strong> área em RAM para agrupar leituras/escritas e reduzir chamadas de sistema.</li>"
            "<li><strong>Indicador de posição (cursor):</strong> deslocamento do próximo byte a ser lido ou gravado.</li>"
            "<li><strong>Flags de estado:</strong> bits indicando modo de abertura, ocorrência de erro (<code>ferror</code>) e fim de arquivo (<code>feof</code>).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    FILE *fp = NULL; // Boa prática: inicializar com NULL\n"
            "    fp = fopen(\"log.txt\", \"w\");\n"
            "    if (fp == NULL) {\n"
            "        return 1;\n"
            "    }\n"
            "    // fp aponta para uma struct FILE alocada e gerenciada por <stdio.h>\n"
            "    fputs(\"Sistema iniciado\\n\", fp);\n"
            "    fclose(fp);\n"
            "    fp = NULL; // Evita ponteiro pendente (dangling pointer)\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "FILE *fp declara um ponteiro para a estrutura de controle de fluxo definida em <stdio.h>, inicializado com NULL.",
            "fopen aloca/inicializa o objeto FILE interno e retorna seu endereço em fp (ou NULL em caso de falha).",
            "Após fclose(fp), a estrutura FILE é liberada; atribuir fp = NULL impede uso acidental posterior."
        ],
        "pitfall": (
            "Declarar 'FILE fp;' em vez de 'FILE *fp;' ou tentar copiar '*fp1 = *fp2;' manualmente. O tipo FILE é opaco "
            "e gerenciado exclusivamente pela libc; manipule sempre via FILE *."
        ),
        "tracers": [
            {
                "id": "tr-arq-2",
                "tabLabel": "Ciclo do FILE *",
                "badge": "1D · Ponteiro & FCB",
                "title": "Ciclo de Vida do Ponteiro FILE *fp",
                "desc": "Veja como fp transita de NULL para a struct FILE gerenciada pelo sistema e retorna a NULL após fclose.",
                "kind": "1d",
                "codeLines": [
                    "FILE *fp = NULL;",
                    "fp = fopen(\"log.txt\", \"w\");",
                    "fputs(\"OK\\n\", fp);",
                    "fclose(fp); fp = NULL;"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"fp": "NULL", "estado": "sem stream"},
                        "note": "fp nasce apontando para NULL, evitando lixo de memória.",
                        "cells": [
                            {"label": "fp", "val": "NULL", "state": "normal"},
                            {"label": "FILE struct", "val": "(não alocada)", "state": "normal"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"fp": "0x55a0", "fd": "3", "flags": "WRITE", "pos": "0"},
                        "note": "fopen retorna endereço da struct FILE alocada pela biblioteca padrão.",
                        "cells": [
                            {"label": "fp", "val": "0x55a0", "state": "active"},
                            {"label": "fd", "val": "3", "state": "modified"},
                            {"label": "buffer", "val": "[vazio]", "state": "normal"},
                            {"label": "pos", "val": "0", "state": "normal"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"fp": "0x55a0", "buffer": "'O','K','\\n'", "pos": "3"},
                        "note": "fputs escreve os bytes no buffer associado à struct FILE e avança pos para 3.",
                        "cells": [
                            {"label": "fp", "val": "0x55a0", "state": "active"},
                            {"label": "fd", "val": "3", "state": "normal"},
                            {"label": "buffer", "val": "\"OK\\n\"", "state": "modified"},
                            {"label": "pos", "val": "3", "state": "modified"}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"fp": "NULL", "estado": "fechado"},
                        "note": "fclose descarrega o buffer para o disco, fecha fd=3 e libera a struct FILE.",
                        "cells": [
                            {"label": "fp", "val": "NULL", "state": "normal"},
                            {"label": "FILE struct", "val": "(liberada)", "state": "eof"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-3",
        "num": "3.3",
        "title": "Abertura e Fechamento: fopen, fclose e Verificação Obrigatória de NULL",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.4–11.5) · C Completo e Total Cap. 8",
        "summary": (
            "fopen(caminho, modo) abre o stream e retorna NULL se falhar; testar if (fp == NULL) antes de qualquer I/O "
            "evita falha de segmentação, e fclose(fp) descarrega buffers e libera o descritor."
        ),
        "conceptHtml": (
            "<p>A função <code>FILE *fopen(const char *nome, const char *modo)</code> estabelece a ligação entre o programa "
            "e o arquivo físico no sistema operacional. Ela pode falhar por diversos motivos: arquivo inexistente no modo "
            "leitura, falta de permissão, diretório inválido ou limite de descritores abertos atingido.</p>"
            "<p>Quando falha, <code>fopen</code> retorna <code>NULL</code>. Passar um ponteiro <code>NULL</code> para "
            "<code>fprintf</code>, <code>fgets</code>, <code>fread</code> ou <code>fclose</code> provoca "
            "<strong>comportamento indefinido</strong> (geralmente <em>Segmentation Fault</em>). Por isso, a verificação "
            "imediata é obrigatória (Deitel Cap. 11.4).</p>"
            "<p>Ao finalizar o uso, <code>int fclose(FILE *fp)</code> realiza três ações essenciais: envia ao disco quaisquer "
            "dados pendentes no buffer (<em>flush</em>), fecha o descritor no sistema operacional e libera a memória da "
            "estrutura <code>FILE</code>. Retorna <code>0</code> em caso de sucesso ou <code>EOF</code> em erro.</p>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"dados.txt\", \"r\");\n"
            "    if (fp == NULL) {\n"
            "        perror(\"Erro ao abrir dados.txt\");\n"
            "        return EXIT_FAILURE;\n"
            "    }\n\n"
            "    int x = 0;\n"
            "    if (fscanf(fp, \"%d\", &x) == 1) {\n"
            "        printf(\"Valor lido: %d\\n\", x);\n"
            "    }\n\n"
            "    if (fclose(fp) == EOF) {\n"
            "        perror(\"Erro ao fechar dados.txt\");\n"
            "        return EXIT_FAILURE;\n"
            "    }\n"
            "    return EXIT_SUCCESS;\n"
            "}"
        ),
        "logicSteps": [
            "fopen tenta abrir dados.txt no modo leitura (\"r\"); se o arquivo não existir, retorna NULL.",
            "O bloco if (fp == NULL) intercepta a falha antes de qualquer operação de leitura, exibe diagnóstico com perror e encerra.",
            "Após a leitura, fclose(fp) libera o recurso do SO e seu retorno é verificado contra EOF para garantir integridade."
        ],
        "pitfall": (
            "Chamar fclose(fp) dentro de um tratamento de erro quando fp já é NULL! Chamar fclose(NULL) causa crash "
            "(Segmentation Fault). Só chame fclose(fp) se fp != NULL."
        ),
        "tracers": [
            {
                "id": "tr-arq-3",
                "tabLabel": "Fluxo Seguro",
                "badge": "1D · Guarda NULL",
                "title": "Rastreio de Abertura com Falha vs Sucesso",
                "desc": "Observe a decisão do fluxo quando fopen falha (retorna NULL) versus quando abre normalmente.",
                "kind": "1d",
                "codeLines": [
                    "FILE *fp = fopen(\"dados.txt\", \"r\");",
                    "if (fp == NULL) { perror(\"Erro\"); return 1; }",
                    "fscanf(fp, \"%d\", &x);",
                    "fclose(fp);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"arquivo": "\"dados.txt\" (inexistente)", "fp": "NULL"},
                        "note": "Cenário A: arquivo não existe no disco; fopen(\"dados.txt\", \"r\") retorna NULL.",
                        "cells": [
                            {"label": "fp", "val": "NULL", "state": "eof"},
                            {"label": "errno", "val": "ENOENT", "state": "modified"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"fp": "NULL", "desvio": "true -> return 1"},
                        "note": "A guarda if (fp == NULL) captura o erro e evita chamar fscanf(NULL, ...).",
                        "cells": [
                            {"label": "fp", "val": "NULL", "state": "eof"},
                            {"label": "saída", "val": "EXIT_FAILURE (1)", "state": "active"}
                        ]
                    },
                    {
                        "line": 0,
                        "vars": {"arquivo": "\"dados.txt\" (contém 42)", "fp": "0x5610"},
                        "note": "Cenário B: arquivo existe; fopen retorna endereço válido 0x5610.",
                        "cells": [
                            {"label": "fp", "val": "0x5610", "state": "active"},
                            {"label": "conteúdo", "val": "\"42\"", "state": "normal"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"fp": "0x5610", "x": "42"},
                        "note": "fscanf lê com segurança usando o ponteiro válido fp e preenche x = 42.",
                        "cells": [
                            {"label": "fp", "val": "0x5610", "state": "normal"},
                            {"label": "x", "val": "42", "state": "modified"}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"fclose(fp)": "0 (sucesso)"},
                        "note": "fclose fecha o arquivo e retorna 0.",
                        "cells": [
                            {"label": "retorno", "val": "0", "state": "active"},
                            {"label": "descritor", "val": "liberado", "state": "normal"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-4",
        "num": "3.4",
        "title": "Modos de Abertura: r, w, a, r+, w+, a+ e Binários (rb, wb, ab, r+b)",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.4) · C Completo e Total Cap. 8",
        "summary": (
            "O modo define operações permitidas (leitura/escrita), se cria arquivo ausente, se trunca o conteúdo anterior "
            "para zero bytes e se trata o fluxo como texto ou binário ('b')."
        ),
        "conceptHtml": (
            "<p>A tabela de modos de <code>fopen</code> (Deitel Fig. 11.6) controla quatro propriedades críticas:</p>"
            "<ul>"
            "<li><code>\"r\"</code> / <code>\"rb\"</code>: apenas leitura. Arquivo <strong>deve existir</strong> (retorna <code>NULL</code> se não existir).</li>"
            "<li><code>\"w\"</code> / <code>\"wb\"</code>: apenas escrita. Cria se não existir; <strong>APAGA (trunca para 0 bytes)</strong> se já existir!</li>"
            "<li><code>\"a\"</code> / <code>\"ab\"</code>: acréscimo (<em>append</em>). Cria se não existir; preserva conteúdo e força toda escrita para o <strong>fim do arquivo</strong>.</li>"
            "<li><code>\"r+\"</code> / <code>\"r+b\"</code> (ou <code>\"rb+\"</code>): leitura e escrita. Arquivo <strong>deve existir</strong>; não apaga conteúdo. Ideal para atualização in-loco de registros.</li>"
            "<li><code>\"w+\"</code> / <code>\"w+b\"</code>: leitura e escrita. Cria ou <strong>zera</strong> arquivo existente.</li>"
            "<li><code>\"a+\"</code> / <code>\"a+b\"</code>: leitura em qualquer ponto (via <code>fseek</code>), mas toda escrita vai sempre para o fim do arquivo.</li>"
            "</ul>"
            "<p>O sufixo <code>b</code> desativa a tradução de quebras de linha (<code>\\n</code> &harr; <code>\\r\\n</code>) "
            "e caracteres de controle no Windows, garantindo leitura exata de bytes.</p>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    // 1) Criar/zerar arquivo de texto\n"
            "    FILE *f1 = fopen(\"notas.txt\", \"w\");\n"
            "    if (f1) { fputs(\"10.0\\n\", f1); fclose(f1); }\n\n"
            "    // 2) Anexar sem apagar o que já existe\n"
            "    FILE *f2 = fopen(\"notas.txt\", \"a\");\n"
            "    if (f2) { fputs(\"8.5\\n\", f2); fclose(f2); }\n\n"
            "    // 3) Abrir binário existente para leitura e alteração pontual\n"
            "    FILE *fb = fopen(\"produtos.dat\", \"r+b\");\n"
            "    if (fb == NULL) {\n"
            "        // Se não existir ainda, r+b falha e retorna NULL!\n"
            "        fb = fopen(\"produtos.dat\", \"w+b\");\n"
            "    }\n"
            "    if (fb) fclose(fb);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "O modo \"w\" cria notas.txt ou descarta todo o conteúdo prévio antes de escrever \"10.0\\n\".",
            "O modo \"a\" preserva \"10.0\\n\" e grava \"8.5\\n\" obrigatoriamente ao final do arquivo.",
            "Para atualizar um arquivo binário sem apagá-lo, tenta-se \"r+b\"; somente se retornar NULL cria-se com \"w+b\"."
        ],
        "pitfall": (
            "Usar \"w\" ou \"w+b\" para atualizar um registro existente: ao abrir em modo \"w\", o arquivo inteiro é "
            "imediatamente truncado para 0 bytes antes mesmo do primeiro fwrite/fprintf!"
        ),
        "tracers": [
            {
                "id": "tr-arq-4",
                "tabLabel": "Matriz de Modos",
                "badge": "2D · Tabela Comparativa",
                "title": "Efeito dos Modos de Abertura no Arquivo",
                "desc": "Simule a abertura de um arquivo existente com 20 bytes nos modos \"r\", \"w\", \"a\" e \"r+b\".",
                "kind": "2d",
                "codeLines": [
                    "fopen(\"arq\", \"r\");",
                    "fopen(\"arq\", \"w\");",
                    "fopen(\"arq\", \"a\");",
                    "fopen(\"arq\", \"r+b\");"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"modo": "\"r\"", "se_nao_existe": "NULL", "trunca": "Não"},
                        "note": "Modo \"r\" abre somente para leitura no offset 0; retorna NULL se não existir.",
                        "grid": [
                            [
                                {"label": "Modo", "val": "\"r\"", "state": "active"},
                                {"label": "Lê?", "val": "Sim", "state": "active"},
                                {"label": "Escreve?", "val": "Não", "state": "normal"},
                                {"label": "Cria?", "val": "Não", "state": "eof"},
                                {"label": "Trunca?", "val": "Não", "state": "normal"}
                            ],
                            [
                                {"label": "Cursor inicial", "val": "0", "state": "normal"},
                                {"label": "Bytes prévios", "val": "20 preservados", "state": "active"},
                                {"label": "Tipo", "val": "Texto", "state": "normal"}
                            ]
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"modo": "\"w\"", "se_nao_existe": "Cria", "trunca": "SIM (0 bytes)"},
                        "note": "PERIGO: modo \"w\" zera os 20 bytes existentes imediatamente na abertura!",
                        "grid": [
                            [
                                {"label": "Modo", "val": "\"w\"", "state": "active"},
                                {"label": "Lê?", "val": "Não", "state": "normal"},
                                {"label": "Escreve?", "val": "Sim", "state": "active"},
                                {"label": "Cria?", "val": "Sim", "state": "modified"},
                                {"label": "Trunca?", "val": "SIM (0B)", "state": "eof"}
                            ],
                            [
                                {"label": "Cursor inicial", "val": "0", "state": "normal"},
                                {"label": "Bytes prévios", "val": "APAGADOS", "state": "eof"},
                                {"label": "Tipo", "val": "Texto", "state": "normal"}
                            ]
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"modo": "\"a\"", "se_nao_existe": "Cria", "trunca": "Não"},
                        "note": "Modo \"a\" preserva os 20 bytes e posiciona escritas no fim (offset 20).",
                        "grid": [
                            [
                                {"label": "Modo", "val": "\"a\"", "state": "active"},
                                {"label": "Lê?", "val": "Não", "state": "normal"},
                                {"label": "Escreve?", "val": "Só no fim", "state": "modified"},
                                {"label": "Cria?", "val": "Sim", "state": "modified"},
                                {"label": "Trunca?", "val": "Não", "state": "normal"}
                            ],
                            [
                                {"label": "Cursor escrita", "val": "20 (EOF)", "state": "modified"},
                                {"label": "Bytes prévios", "val": "20 preservados", "state": "active"},
                                {"label": "Tipo", "val": "Texto", "state": "normal"}
                            ]
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"modo": "\"r+b\"", "se_nao_existe": "NULL", "trunca": "Não"},
                        "note": "Modo \"r+b\" lê e escreve em binário sem truncar, permitindo atualizar registros com fseek.",
                        "grid": [
                            [
                                {"label": "Modo", "val": "\"r+b\"", "state": "active"},
                                {"label": "Lê?", "val": "Sim", "state": "active"},
                                {"label": "Escreve?", "val": "Sim", "state": "active"},
                                {"label": "Cria?", "val": "Não", "state": "eof"},
                                {"label": "Trunca?", "val": "Não", "state": "normal"}
                            ],
                            [
                                {"label": "Cursor inicial", "val": "0", "state": "normal"},
                                {"label": "Bytes prévios", "val": "20 preservados", "state": "active"},
                                {"label": "Tipo", "val": "Binário", "state": "modified"}
                            ]
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-5",
        "num": "3.5",
        "title": "Arquivos de Texto — Escrita: fprintf, fputs e fputc",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.4) · C Completo e Total Cap. 8",
        "summary": (
            "fputc grava um caractere por vez, fputs grava uma string literal sem adicionar '\\n' automático, e fprintf "
            "grava dados formatados usando especificadores (%d, %.2f, %s)."
        ),
        "conceptHtml": (
            "<p>Para escrever em arquivos de texto, <code>&lt;stdio.h&gt;</code> disponibiliza três níveis de granularidade "
            "(Schildt Cap. 8):</p>"
            "<ul>"
            "<li><code>int fputc(int ch, FILE *fp)</code>: escreve um único caractere (convertido para <code>unsigned char</code>). "
            "Retorna o caractere escrito ou <code>EOF</code> em erro.</li>"
            "<li><code>int fputs(const char *str, FILE *fp)</code>: escreve a string terminada em <code>'\\0'</code> (sem "
            "gravar o <code>'\\0'</code> e <strong>sem inserir <code>'\\n'</code></strong> automaticamente, ao contrário de <code>puts</code>). "
            "Retorna valor não-negativo em sucesso ou <code>EOF</code> em erro.</li>"
            "<li><code>int fprintf(FILE *fp, const char *fmt, ...)</code>: funciona como <code>printf</code>, direcionando "
            "a saída formatada para <code>fp</code>. Retorna o número de caracteres gravados (ou negativo se falhar).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"relatorio.txt\", \"w\");\n"
            "    if (!fp) return 1;\n\n"
            "    fputc('#', fp);                  // Grava 1 caractere\n"
            "    fputs(\" Relatório ADS\\n\", fp); // Grava string (\\n explícito!)\n"
            "    int qtd = 3;\n"
            "    double media = 8.75;\n"
            "    fprintf(fp, \"Alunos=%d;Media=%.2f\\n\", qtd, media);\n\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "fputc('#', fp) grava o byte '#' na posição 0 do fluxo.",
            "fputs(\" Relatório ADS\\n\", fp) grava os caracteres da string sem o terminador '\\0', exigindo '\\n' explícito.",
            "fprintf formata inteiros e ponto flutuante como texto ASCII e escreve no mesmo stream sequencial."
        ],
        "pitfall": (
            "Confundir puts(s) com fputs(s, fp): puts acrescenta '\\n' no final em stdout, mas fputs NÃO acrescenta '\\n' "
            "no arquivo. Outro erro é passar formato dinâmico do usuário direto como format string: fprintf(fp, str) em vez de fputs(str, fp)."
        ),
        "tracers": [
            {
                "id": "tr-arq-5",
                "tabLabel": "Escrita Sequencial",
                "badge": "1D · Cursor de Saída",
                "title": "Avanço do Cursor com fputc, fputs e fprintf",
                "desc": "Acompanhe os bytes gravados no buffer de saída a cada chamada.",
                "kind": "1d",
                "codeLines": [
                    "fputc('#', fp);",
                    "fputs(\" OK\\n\", fp);",
                    "fprintf(fp, \"N=%d\", 7);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"cursor": "1", "retorno_fputc": "'#' (35)"},
                        "note": "fputc grava '#' no offset 0 e move o cursor para 1.",
                        "cells": [
                            {"label": "[0]", "val": "'#'", "state": "modified"},
                            {"label": "[1]", "val": "_", "state": "active"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"cursor": "4", "retorno_fputs": ">= 0"},
                        "note": "fputs grava ' ', 'O', 'K', '\\n' (sem '\\0'). Cursor avança para 4.",
                        "cells": [
                            {"label": "[0]", "val": "'#'", "state": "normal"},
                            {"label": "[1]", "val": "' '", "state": "modified"},
                            {"label": "[2]", "val": "'O'", "state": "modified"},
                            {"label": "[3]", "val": "'K'", "state": "modified"},
                            {"label": "[4]", "val": "'\\n'", "state": "modified"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"cursor": "8", "retorno_fprintf": "3"},
                        "note": "fprintf converte 7 para '7' e escreve \"N=7\" (3 bytes), retornando 3.",
                        "cells": [
                            {"label": "[0..4]", "val": "\"# OK\\n\"", "state": "normal"},
                            {"label": "[5]", "val": "'N'", "state": "modified"},
                            {"label": "[6]", "val": "'='", "state": "modified"},
                            {"label": "[7]", "val": "'7'", "state": "modified"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-6",
        "num": "3.6",
        "title": "Arquivos de Texto — Leitura: fscanf, fgets e fgetc",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.5) · C Completo e Total Cap. 8",
        "summary": (
            "fgetc retorna int (para distinguir 0..255 de EOF), fgets lê até n-1 caracteres ou '\\n' evitando estouro "
            "de buffer, e fscanf lê campos formatados retornando a quantidade de itens convertidos."
        ),
        "conceptHtml": (
            "<p>Cada função de leitura em modo texto tem um contrato próprio (Deitel Cap. 11.5; Schildt Cap. 8):</p>"
            "<ul>"
            "<li><code>int fgetc(FILE *fp)</code>: lê 1 byte e retorna como <code>unsigned char</code> promovido a <code>int</code>, "
            "ou <code>EOF</code> (geralmente <code>-1</code>) no fim/erro. Guardar o retorno em <code>char</code> é bug clássico!</li>"
            "<li><code>char *fgets(char *buf, int n, FILE *fp)</code>: lê no máximo <code>n - 1</code> caracteres, parando após "
            "consumir um <code>'\\n'</code> (que fica no buffer se couber!) ou no <code>EOF</code>, e sempre adiciona <code>'\\0'</code>. "
            "Retorna <code>buf</code> ou <code>NULL</code> quando não lê nada (EOF/erro).</li>"
            "<li><code>int fscanf(FILE *fp, const char *fmt, ...)</code>: pula espaços em branco iniciais (exceto <code>%c</code>/<code>%[...]</code>), "
            "converte campos e retorna o <strong>número de variáveis preenchidas com sucesso</strong> (ou <code>EOF</code> se acabar antes do primeiro campo).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"alunos.txt\", \"r\");\n"
            "    if (!fp) return 1;\n\n"
            "    char linha[128];\n"
            "    while (fgets(linha, sizeof(linha), fp) != NULL) {\n"
            "        linha[strcspn(linha, \"\\r\\n\")] = '\\0'; // Remove quebra de linha\n"
            "        int id;\n"
            "        double nota;\n"
            "        if (sscanf(linha, \"%d %lf\", &id, &nota) == 2) {\n"
            "            printf(\"ID=%d Nota=%.1f\\n\", id, nota);\n"
            "        }\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "fgets lê uma linha inteira com limite seguro sizeof(linha), mantendo o '\\n' no buffer quando houver espaço.",
            "strcspn localiza '\\r' ou '\\n' e substitui por '\\0', limpando a string lida.",
            "sscanf analisa a linha já em memória e só processa o registro se retornar exatamente 2 conversões."
        ],
        "pitfall": (
            "Declarar 'char c; while ((c = fgetc(fp)) != EOF)': em arquiteturas com char sem sinal (unsigned char), c "
            "nunca vale -1 (loop infinito); em char com sinal, o byte 0xFF (ÿ) vira -1 e encerra o arquivo antes da hora! Use sempre int c."
        ),
        "tracers": [
            {
                "id": "tr-arq-6",
                "tabLabel": "fgets + sscanf",
                "badge": "1D · Buffer de Linha",
                "title": "Leitura Segura com fgets e Remoção do \\n",
                "desc": "Veja o conteúdo do array linha[] ao ler \"101 9.5\\n\" com fgets e limpar o '\\n'.",
                "kind": "1d",
                "codeLines": [
                    "fgets(linha, sizeof(linha), fp);",
                    "linha[strcspn(linha, \"\\r\\n\")] = '\\0';",
                    "sscanf(linha, \"%d %lf\", &id, &nota);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"retorno_fgets": "linha", "strlen": "8"},
                        "note": "fgets lê '1','0','1',' ','9','.','5','\\n' e grava '\\0' ao final.",
                        "cells": [
                            {"label": "[0]", "val": "'1'", "state": "modified"},
                            {"label": "[1]", "val": "'0'", "state": "modified"},
                            {"label": "[2]", "val": "'1'", "state": "modified"},
                            {"label": "[3]", "val": "' '", "state": "modified"},
                            {"label": "[4..6]", "val": "\"9.5\"", "state": "modified"},
                            {"label": "[7]", "val": "'\\n'", "state": "active"},
                            {"label": "[8]", "val": "'\\0'", "state": "normal"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"strcspn": "7", "strlen": "7"},
                        "note": "strcspn retorna índice 7 ('\\n'), que é substituído por '\\0'.",
                        "cells": [
                            {"label": "[0..2]", "val": "\"101\"", "state": "normal"},
                            {"label": "[3]", "val": "' '", "state": "normal"},
                            {"label": "[4..6]", "val": "\"9.5\"", "state": "normal"},
                            {"label": "[7]", "val": "'\\0'", "state": "modified"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"id": "101", "nota": "9.5", "retorno_sscanf": "2"},
                        "note": "sscanf extrai ambos os campos e retorna 2.",
                        "cells": [
                            {"label": "id", "val": "101", "state": "active"},
                            {"label": "nota", "val": "9.5", "state": "active"},
                            {"label": "ret", "val": "2", "state": "modified"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-7",
        "num": "3.7",
        "title": "Fim de Arquivo: feof, Retornos de Leitura e o Erro de while(!feof(fp))",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.5) · C Completo e Total Cap. 8",
        "summary": (
            "Em C, feof(fp) NÃO prevê o fim do arquivo: ela só retorna verdadeiro DEPOIS que uma leitura já tentou ler "
            "além do último byte e falhou. Por isso, while (!feof(fp)) duplica ou processa lixo na última iteração."
        ),
        "conceptHtml": (
            "<p>Um dos erros mais cobrados em provas de ADS e entrevistas é escrever <code>while (!feof(fp))</code> para "
            "controlar um laço de leitura. Por que isso falha?</p>"
            "<p>A flag de fim de arquivo dentro de <code>FILE</code> começa zerada mesmo quando o cursor já está exatamente "
            "sobre o último byte válido do arquivo (ou logo após ele). A função <code>feof(fp)</code> apenas consulta essa "
            "flag — ela <strong>não espia o próximo byte no disco</strong>. Somente quando uma função de leitura (<code>fgetc</code>, "
            "<code>fgets</code>, <code>fscanf</code>, <code>fread</code>) tenta ler e encontra o fim do fluxo é que a flag é ligada.</p>"
            "<p><strong>Regra de ouro:</strong> controle o laço sempre pelo <strong>retorno da função de leitura</strong>:</p>"
            "<ul>"
            "<li><code>while ((c = fgetc(fp)) != EOF)</code></li>"
            "<li><code>while (fgets(buf, sizeof buf, fp) != NULL)</code></li>"
            "<li><code>while (fscanf(fp, \"%d\", &x) == 1)</code></li>"
            "<li><code>while (fread(&reg, sizeof reg, 1, fp) == 1)</code></li>"
            "</ul>"
            "<p>Use <code>feof(fp)</code> apenas <em>depois</em> que o laço terminar, para distinguir se parou por fim normal "
            "do arquivo ou por erro de hardware/I/O (<code>ferror(fp)</code>).</p>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"nums.txt\", \"r\");\n"
            "    if (!fp) return 1;\n\n"
            "    int x, soma = 0;\n"
            "    // ERRADO: while (!feof(fp)) { fscanf(fp, \"%d\", &x); soma += x; } // Soma o último 2x!\n\n"
            "    // CORRETO: testar o retorno da própria leitura\n"
            "    while (fscanf(fp, \"%d\", &x) == 1) {\n"
            "        soma += x;\n"
            "    }\n\n"
            "    if (feof(fp)) {\n"
            "        printf(\"Fim normal. Soma = %d\\n\", soma);\n"
            "    } else if (ferror(fp)) {\n"
            "        perror(\"Erro durante leitura\");\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Na forma errada, após ler o último inteiro '20', feof(fp) ainda é 0; o laço entra mais uma vez, fscanf falha sem alterar x, e soma recebe 20 pela segunda vez.",
            "Na forma correta, while (fscanf(fp, \"%d\", &x) == 1) falha imediatamente quando não há mais inteiros (retorna EOF ou 0) e sai antes de acumular.",
            "Fora do laço, feof(fp) confirma que a parada ocorreu por término natural dos dados, e ferror(fp) descarta falha de leitura."
        ],
        "pitfall": (
            "Usar while (!feof(fp)) com fscanf ou fread: se o arquivo tem '10 20', na 3ª volta !feof(fp) ainda é verdadeiro, "
            "fscanf retorna EOF sem mexer em x (que ainda vale 20), e o programa processa '20' duplicado!"
        ),
        "tracers": [
            {
                "id": "tr-arq-7",
                "tabLabel": "Bug while(!feof)",
                "badge": "1D · Flag EOF",
                "title": "Por que while(!feof(fp)) Duplica o Último Valor",
                "desc": "Compare a flag feof(fp) passo a passo lendo o arquivo \"10 20\".",
                "kind": "1d",
                "codeLines": [
                    "while (!feof(fp)) {",
                    "  fscanf(fp, \"%d\", &x);",
                    "  soma += x;",
                    "}"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"cursor": "0 ('1')", "feof(fp)": "0", "x": "?", "soma": "0"},
                        "note": "Início: cursor em '1'. feof(fp) é 0. Entra no laço.",
                        "cells": [
                            {"label": "arq[0..1]", "val": "\"10\"", "state": "active"},
                            {"label": "arq[2]", "val": "' '", "state": "normal"},
                            {"label": "arq[3..4]", "val": "\"20\"", "state": "normal"},
                            {"label": "EOF", "val": "(fim)", "state": "normal"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"cursor": "2 (' ')", "feof(fp)": "0", "x": "10", "soma": "10"},
                        "note": "fscanf lê 10 (ret=1). soma = 10. Ainda há dados.",
                        "cells": [
                            {"label": "arq[0..1]", "val": "\"10\"", "state": "normal"},
                            {"label": "arq[2]", "val": "' '", "state": "active"},
                            {"label": "arq[3..4]", "val": "\"20\"", "state": "normal"},
                            {"label": "EOF", "val": "(fim)", "state": "normal"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"cursor": "5 (fim)", "feof(fp)": "0 (!)", "x": "20", "soma": "30"},
                        "note": "fscanf lê 20 e para exatamente ao final. Como ainda NÃO tentou ler além do fim, feof(fp) CONTINUA 0!",
                        "cells": [
                            {"label": "arq[0..1]", "val": "\"10\"", "state": "normal"},
                            {"label": "arq[3..4]", "val": "\"20\"", "state": "modified"},
                            {"label": "EOF", "val": "cursor aqui, flag=0!", "state": "active"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"cursor": "5 (fim)", "feof(fp)": "1 (ligou agora)", "fscanf_ret": "EOF", "x": "20 (intocado!)"},
                        "note": "!feof(fp) era 1 e entrou na 3ª volta! fscanf tenta ler, encontra EOF, liga flag=1 e NÃO altera x.",
                        "cells": [
                            {"label": "x", "val": "20 (lixo antigo)", "state": "eof"},
                            {"label": "feof(fp)", "val": "1", "state": "eof"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"x": "20", "soma": "50 (ERRO! deveria ser 30)"},
                        "note": "BUG: soma += x soma 20 novamente! Se o laço testasse fscanf(...) == 1, teria parado antes.",
                        "cells": [
                            {"label": "soma", "val": "50 (DUPLICADO)", "state": "eof"},
                            {"label": "correto", "val": "30", "state": "active"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-8",
        "num": "3.8",
        "title": "Arquivos Binários: fwrite e fread (Sintaxe, Contagem de Blocos e Eficiência)",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.7–11.9) · C Completo e Total Cap. 8",
        "summary": (
            "fwrite e fread transferem blocos contíguos de memória diretamente entre RAM e disco sem formatação, "
            "recebendo ponteiro, tamanho do item, quantidade de itens e FILE *, e retornando quantos itens foram transferidos."
        ),
        "conceptHtml": (
            "<p>Para I/O binária em bloco, <code>&lt;stdio.h&gt;</code> fornece (Deitel Cap. 11.7):</p>"
            "<p><code>size_t fwrite(const void *ptr, size_t tam, size_t qtd, FILE *fp);</code><br>"
            "<code>size_t fread(void *ptr, size_t tam, size_t qtd, FILE *fp);</code></p>"
            "<ul>"
            "<li><code>ptr</code>: endereço base na RAM do objeto ou vetor a gravar/preencher.</li>"
            "<li><code>tam</code>: tamanho em bytes de <strong>um</strong> elemento (geralmente <code>sizeof(Tipo)</code>).</li>"
            "<li><code>qtd</code>: número de elementos consecutivos a transferir (total de bytes = <code>tam * qtd</code>).</li>"
            "<li><strong>Retorno:</strong> o número de <strong>elementos</strong> (não bytes!) efetivamente gravados/lidos. Se retornar "
            "menos que <code>qtd</code>, ocorreu fim de arquivo (em <code>fread</code>) ou erro de gravação.</li>"
            "</ul>"
            "<p>Gravar um vetor inteiro de 1000 inteiros com uma única chamada <code>fwrite(v, sizeof(int), 1000, fp)</code> "
            "é ordens de grandeza mais eficiente do que 1000 chamadas a <code>fprintf</code>, pois elimina parsing e reduz chamadas internas.</p>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    int v[4] = {10, 20, 30, 40};\n"
            "    FILE *fp = fopen(\"vetor.bin\", \"wb\");\n"
            "    if (!fp) return 1;\n\n"
            "    size_t gravados = fwrite(v, sizeof(int), 4, fp);\n"
            "    fclose(fp);\n"
            "    if (gravados != 4) return 1;\n\n"
            "    int lidos[4] = {0};\n"
            "    fp = fopen(\"vetor.bin\", \"rb\");\n"
            "    if (!fp) return 1;\n"
            "    size_t qtd = fread(lidos, sizeof(int), 4, fp);\n"
            "    printf(\"Blocos lidos: %zu (lidos[2]=%d)\\n\", qtd, lidos[2]);\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "fwrite(v, sizeof(int), 4, fp) grava 4 blocos de 4 bytes (16 bytes no total) em uma única operação.",
            "O retorno gravados é comparado com 4 (quantidade de elementos solicitada), não com 16 (bytes).",
            "fread(lidos, sizeof(int), 4, fp) lê os 4 inteiros de volta para o vetor lidos[] e retorna 4."
        ],
        "pitfall": (
            "Testar 'if (fread(&x, sizeof(x), 1, fp) != sizeof(x))' — fread retorna a contagem de BLOCOS (1), e não de bytes! "
            "Se sizeof(x) == 4, comparar com sizeof(x) sempre acusará falso erro."
        ),
        "tracers": [
            {
                "id": "tr-arq-8",
                "tabLabel": "Blocos fwrite/fread",
                "badge": "1D · Transferência em Lote",
                "title": "Transferência de Vetor com fwrite e fread",
                "desc": "Veja a transferência de 4 elementos sizeof(int)=4 bytes entre RAM e arquivo binário.",
                "kind": "1d",
                "codeLines": [
                    "int v[4] = {10, 20, 30, 40};",
                    "size_t g = fwrite(v, sizeof(int), 4, fp);",
                    "size_t q = fread(lidos, sizeof(int), 4, fp);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"sizeof(int)": "4", "qtd": "4", "total_bytes": "16"},
                        "note": "Vetor v ocupa 16 bytes contíguos na RAM.",
                        "cells": [
                            {"label": "v[0]", "val": "10 (4B)", "state": "active"},
                            {"label": "v[1]", "val": "20 (4B)", "state": "active"},
                            {"label": "v[2]", "val": "30 (4B)", "state": "active"},
                            {"label": "v[3]", "val": "40 (4B)", "state": "active"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"g (blocos)": "4", "bytes_no_disco": "16"},
                        "note": "fwrite copia os 4 blocos de uma só vez e retorna g = 4 (elementos).",
                        "cells": [
                            {"label": "off 0..3", "val": "10", "state": "modified"},
                            {"label": "off 4..7", "val": "20", "state": "modified"},
                            {"label": "off 8..11", "val": "30", "state": "modified"},
                            {"label": "off 12..15", "val": "40", "state": "modified"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"q (blocos)": "4", "lidos[2]": "30"},
                        "note": "fread preenche lidos[0..3] em bloco e retorna q = 4.",
                        "cells": [
                            {"label": "lidos[0]", "val": "10", "state": "active"},
                            {"label": "lidos[1]", "val": "20", "state": "active"},
                            {"label": "lidos[2]", "val": "30", "state": "active"},
                            {"label": "lidos[3]", "val": "40", "state": "active"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-9",
        "num": "3.9",
        "title": "Gravação e Leitura de Structs em Arquivos Binários e de Texto",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.7–11.9) · C Completo e Total Cap. 8",
        "summary": (
            "Structs sem ponteiros podem ser gravadas integralmente com fwrite/fread em tamanho fixo (permitindo acesso "
            "aleatório por índice), enquanto em texto exigem serialização campo a campo com fprintf/fscanf ou fgets."
        ),
        "conceptHtml": (
            "<p>Ao persistir registros compostos (<code>struct</code>), há duas estratégias clássicas:</p>"
            "<ul>"
            "<li><strong>Binário (registro de tamanho fixo):</strong> <code>fwrite(&amp;aluno, sizeof(Aluno), 1, fp)</code> "
            "grava todos os campos de uma só vez. Cada registro ocupa exatamente <code>sizeof(Aluno)</code> bytes, o que "
            "habilita pular diretamente para o registro <code>i</code> com <code>fseek</code>.</li>"
            "<li><strong>Texto (serialização campo a campo):</strong> usa <code>fprintf(fp, \"%d;%s;%.2f\\n\", a.id, a.nome, a.nota)</code> "
            "e leitura via <code>fgets</code> + <code>sscanf</code>/<code>strtok</code>. É legível e portável entre arquiteturas.</li>"
            "</ul>"
            "<p><strong>Regra fundamental de ponteiros em structs:</strong> NUNCA grave com <code>fwrite</code> uma struct que "
            "contenha ponteiros (ex.: <code>char *nome</code> ou <code>struct No *prox</code>)! O <code>fwrite</code> gravaria "
            "apenas o <em>endereço de memória</em> daquela execução, que será lixo inválido na próxima vez que o programa rodar. "
            "Para binário direto, use vetores fixos dentro da struct (ex.: <code>char nome[50]</code>) ou serialize o conteúdo apontado.</p>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n\n"
            "typedef struct {\n"
            "    int id;\n"
            "    char nome[40]; // Vetor fixo (NUNCA char *nome para fwrite direto!)\n"
            "    double nota;\n"
            "} Aluno;\n\n"
            "int main(void) {\n"
            "    Aluno a = {101, \"Maria Silva\", 9.2};\n\n"
            "    // Binário: registro completo em 1 chamada\n"
            "    FILE *fb = fopen(\"alunos.dat\", \"wb\");\n"
            "    if (fb) {\n"
            "        fwrite(&a, sizeof(Aluno), 1, fb);\n"
            "        fclose(fb);\n"
            "    }\n\n"
            "    // Texto: serialização explícita campo a campo\n"
            "    FILE *ft = fopen(\"alunos.txt\", \"w\");\n"
            "    if (ft) {\n"
            "        fprintf(ft, \"%d;%s;%.2f\\n\", a.id, a.nome, a.nota);\n"
            "        fclose(ft);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Aluno usa char nome[40] embutido (sem ponteiros externos), tornando os bytes da struct autossuficientes para fwrite.",
            "fwrite(&a, sizeof(Aluno), 1, fb) grava id, nome[40], eventuais bytes de alinhamento (padding) e nota em alunos.dat.",
            "fprintf serializa os valores legíveis em alunos.txt separados por ';', independente de padding ou tamanho de struct."
        ],
        "pitfall": (
            "Gravar uma struct com campo 'char *nome' usando fwrite(&s, sizeof(s), 1, fp): o texto do nome NÃO vai para o "
            "arquivo, apenas o endereço hexadecimal de memória (ex.: 0x55b012), causando crash ao ler em outra execução."
        ),
        "tracers": [
            {
                "id": "tr-arq-9",
                "tabLabel": "Struct em Disco",
                "badge": "2D · Binário vs Ponteiro",
                "title": "Layout de Struct Segura vs Struct com Ponteiro",
                "desc": "Compare o que vai para o arquivo binário quando a struct usa char nome[40] versus char *nome.",
                "kind": "2d",
                "codeLines": [
                    "typedef struct { int id; char nome[40]; double nota; } AlunoFixo;",
                    "typedef struct { int id; char *nome; double nota; } AlunoPtr;",
                    "fwrite(&a, sizeof(a), 1, fb);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"tipo": "AlunoFixo", "sizeof": "56 bytes (com padding)"},
                        "note": "AlunoFixo contém os 40 bytes de caracteres diretamente dentro da própria struct.",
                        "grid": [
                            [
                                {"label": "id (4B)", "val": "101", "state": "active"},
                                {"label": "nome[40] (40B)", "val": "\"Maria Silva\\0...\"", "state": "active"},
                                {"label": "padding (4B)", "val": "alinhamento", "state": "normal"},
                                {"label": "nota (8B)", "val": "9.2", "state": "active"}
                            ]
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"tipo": "AlunoPtr", "problema": "grava endereço 0x7f10"},
                        "note": "PERIGO: em AlunoPtr, o campo nome guarda apenas um ponteiro; \"Maria\" fica fora da struct (no heap/rodata).",
                        "grid": [
                            [
                                {"label": "id (4B+4B pad)", "val": "101", "state": "normal"},
                                {"label": "nome (8B ptr)", "val": "0x7f10 (ENDEREÇO!)", "state": "eof"},
                                {"label": "nota (8B)", "val": "9.2", "state": "normal"}
                            ],
                            [
                                {"label": "Fora da struct", "val": "0x7f10 -> \"Maria Silva\" (NÃO GRAVADO!)", "state": "eof"}
                            ]
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"AlunoFixo": "Válido ao reler", "AlunoPtr": "Dangling pointer ao reler"},
                        "note": "Ao reabrir o arquivo em outro processo, 0x7f10 não contém mais \"Maria\" — somente AlunoFixo funciona com fwrite direto.",
                        "grid": [
                            [
                                {"label": "AlunoFixo no disco", "val": "101 + \"Maria Silva\" + 9.2", "state": "modified"},
                                {"label": "AlunoPtr no disco", "val": "101 + 0x7f10 (LIXO) + 9.2", "state": "eof"}
                            ]
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-10",
        "num": "3.10",
        "title": "Acesso Aleatório: fseek, ftell, rewind e Cálculo de Tamanho",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.6, 11.8) · C Completo e Total Cap. 8",
        "summary": (
            "fseek reposiciona o cursor usando SEEK_SET, SEEK_CUR ou SEEK_END; ftell retorna o offset atual em bytes; "
            "rewind volta ao início; e fseek(..., 0, SEEK_END) + ftell() mede o tamanho de arquivos binários."
        ),
        "conceptHtml": (
            "<p>Em arquivos de registro fixo (especialmente binários), não é necessário ler do início até o registro desejado: "
            "podemos realizar <strong>acesso direto (aleatório)</strong> (Deitel Cap. 11.8):</p>"
            "<ul>"
            "<li><code>int fseek(FILE *fp, long offset, int origem)</code>: move o cursor para <code>origem + offset</code>. "
            "Origens padrão: <code>SEEK_SET</code> (0, início), <code>SEEK_CUR</code> (1, posição atual) e <code>SEEK_END</code> (2, fim). "
            "Retorna <code>0</code> no sucesso.</li>"
            "<li><code>long ftell(FILE *fp)</code>: informa o deslocamento atual em bytes desde o início (ou <code>-1L</code> em erro).</li>"
            "<li><code>void rewind(FILE *fp)</code>: equivalente a <code>fseek(fp, 0L, SEEK_SET)</code>, além de limpar as flags de erro/EOF.</li>"
            "</ul>"
            "<p>Para acessar o registro de índice <code>idx</code> (0-based): <code>fseek(fp, (long)idx * sizeof(Reg), SEEK_SET)</code>. "
            "Para calcular o tamanho total em bytes de um arquivo aberto em modo binário: <code>fseek(fp, 0L, SEEK_END); long bytes = ftell(fp);</code> "
            "e a quantidade de registros é <code>bytes / sizeof(Reg)</code>.</p>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "typedef struct { int id; double preco; } Item;\n\n"
            "int main(void) {\n"
            "    FILE *fp = fopen(\"itens.dat\", \"rb\");\n"
            "    if (!fp) return 1;\n\n"
            "    fseek(fp, 0L, SEEK_END);\n"
            "    long tamanho = ftell(fp);\n"
            "    long total_itens = tamanho / (long)sizeof(Item);\n\n"
            "    if (total_itens >= 3) {\n"
            "        // Acesso direto ao 3º registro (índice 2)\n"
            "        fseek(fp, 2L * (long)sizeof(Item), SEEK_SET);\n"
            "        Item it;\n"
            "        if (fread(&it, sizeof(Item), 1, fp) == 1) {\n"
            "            printf(\"Item[2]: id=%d preco=%.2f\\n\", it.id, it.preco);\n"
            "        }\n"
            "    }\n"
            "    rewind(fp); // Volta ao byte 0\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "fseek(fp, 0L, SEEK_END) posiciona o cursor exatamente após o último byte do arquivo.",
            "ftell(fp) devolve o total de bytes; dividindo por sizeof(Item) obtém-se a quantidade de registros gravados.",
            "fseek(fp, 2L * sizeof(Item), SEEK_SET) salta os 2 primeiros registros em O(1) e posiciona no índice 2; rewind(fp) retorna ao byte 0."
        ],
        "pitfall": (
            "Usar fseek com offset negativo em SEEK_SET (posição inválida), esquecer de multiplicar o índice por sizeof(Tipo), "
            "ou usar fseek/ftell com offsets arbitrários em arquivos TEXTO no Windows (onde \\r\\n faz bytes em disco diferirem de caracteres lidos)."
        ),
        "tracers": [
            {
                "id": "tr-arq-10",
                "tabLabel": "Cursor Aleatório",
                "badge": "1D · fseek / ftell",
                "title": "Saltando entre Registros com fseek, ftell e rewind",
                "desc": "Suponha sizeof(Item)=16 e 4 registros no arquivo (64 bytes). Veja a posição do cursor.",
                "kind": "1d",
                "codeLines": [
                    "fseek(fp, 0L, SEEK_END);",
                    "long tamanho = ftell(fp);",
                    "fseek(fp, 2L * sizeof(Item), SEEK_SET);",
                    "fread(&it, sizeof(Item), 1, fp);",
                    "rewind(fp);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"origem": "SEEK_END", "offset": "0", "cursor": "64"},
                        "note": "Cursor salta diretamente para o fim do arquivo (byte 64).",
                        "cells": [
                            {"label": "Reg[0] (0..15)", "val": "id=1", "state": "normal"},
                            {"label": "Reg[1] (16..31)", "val": "id=2", "state": "normal"},
                            {"label": "Reg[2] (32..47)", "val": "id=3", "state": "normal"},
                            {"label": "Reg[3] (48..63)", "val": "id=4", "state": "normal"},
                            {"label": "EOF (64)", "val": "CURSOR", "state": "active"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"tamanho": "64", "total_itens": "64 / 16 = 4"},
                        "note": "ftell retorna 64; 64 / 16 = 4 registros.",
                        "cells": [
                            {"label": "tamanho", "val": "64 bytes", "state": "modified"},
                            {"label": "total_itens", "val": "4", "state": "modified"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"origem": "SEEK_SET", "offset": "32", "cursor": "32"},
                        "note": "fseek posiciona no byte 2 * 16 = 32 (início de Reg[2]).",
                        "cells": [
                            {"label": "Reg[0]", "val": "0..15", "state": "normal"},
                            {"label": "Reg[1]", "val": "16..31", "state": "normal"},
                            {"label": "Reg[2] (32..47)", "val": "CURSOR -> id=3", "state": "active"},
                            {"label": "Reg[3]", "val": "48..63", "state": "normal"}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"it.id": "3", "cursor_apos_fread": "48"},
                        "note": "fread lê Reg[2] (bytes 32..47) e avança cursor automaticamente para 48.",
                        "cells": [
                            {"label": "Reg[2]", "val": "LIDO", "state": "modified"},
                            {"label": "cursor", "val": "48 (Reg[3])", "state": "active"}
                        ]
                    },
                    {
                        "line": 4,
                        "vars": {"cursor": "0", "feof": "0", "ferror": "0"},
                        "note": "rewind(fp) devolve o cursor ao byte 0 e limpa flags de estado.",
                        "cells": [
                            {"label": "Reg[0] (0..15)", "val": "CURSOR", "state": "active"},
                            {"label": "Reg[1..3]", "val": "16..63", "state": "normal"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-11",
        "num": "3.11",
        "title": "Operações sobre Arquivos: remove, rename e Temporários (tmpfile)",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.9–11.10) · C Completo e Total Cap. 8",
        "summary": (
            "remove apaga um arquivo pelo nome e rename o renomeia/move (ambos retornam 0 no sucesso); tmpfile() cria "
            "um arquivo binário temporário exclusivo (modo wb+) que é apagado automaticamente ao fechar."
        ),
        "conceptHtml": (
            "<p>A biblioteca <code>&lt;stdio.h&gt;</code> oferece operações de manipulação no sistema de arquivos "
            "(Schildt Cap. 8):</p>"
            "<ul>"
            "<li><code>int remove(const char *caminho)</code>: remove o arquivo do disco. Retorna <code>0</code> em sucesso ou "
            "valor diferente de zero em erro (por exemplo, arquivo aberto no Windows ou inexistente).</li>"
            "<li><code>int rename(const char *antigo, const char *novo)</code>: renomeia o arquivo. Muito usada no padrão "
            "<strong>arquivo temporário + substituição</strong> para exclusão física ou edição segura. Retorna <code>0</code> no sucesso.</li>"
            "<li><code>FILE *tmpfile(void)</code>: cria um arquivo temporário com nome único aberto em modo <code>\"wb+\"</code>. "
            "Ele é <strong>automaticamente removido</strong> pelo sistema quando <code>fclose</code> é chamado ou quando o programa termina normalmente.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    // Padrão seguro de atualização/remoção em arquivo\n"
            "    FILE *orig = fopen(\"lista.txt\", \"r\");\n"
            "    FILE *temp = fopen(\"lista.tmp\", \"w\");\n"
            "    if (!orig || !temp) {\n"
            "        if (orig) fclose(orig);\n"
            "        if (temp) fclose(temp);\n"
            "        return 1;\n"
            "    }\n"
            "    // Copia filtrando dados...\n"
            "    fputs(\"linha mantida\\n\", temp);\n"
            "    fclose(orig); // Obrigatório fechar ANTES de remove/rename!\n"
            "    fclose(temp);\n\n"
            "    if (remove(\"lista.txt\") == 0) {\n"
            "        rename(\"lista.tmp\", \"lista.txt\");\n"
            "    }\n\n"
            "    // Arquivo temporário efêmero (wb+ auto-removido ao fechar)\n"
            "    FILE *scratch = tmpfile();\n"
            "    if (scratch) {\n"
            "        fputs(\"cache\", scratch);\n"
            "        rewind(scratch);\n"
            "        fclose(scratch); // Apagado automaticamente do disco\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Os dados válidos são copiados de orig (lista.txt) para um arquivo auxiliar temp (lista.tmp).",
            "Ambos os streams são fechados com fclose ANTES de manipular os nomes no sistema de arquivos.",
            "remove(\"lista.txt\") apaga o antigo e rename(\"lista.tmp\", \"lista.txt\") promove o novo; tmpfile() gera área efêmera em \"wb+\"."
        ],
        "pitfall": (
            "Chamar remove(\"lista.txt\") ou rename(\"lista.tmp\", \"lista.txt\") com os arquivos ainda abertos! No Windows "
            "o SO bloqueia a operação e retorna erro diferente de zero; além disso, verificar != 0 evita perder dados."
        ),
        "tracers": [
            {
                "id": "tr-arq-11",
                "tabLabel": "Substituição Segura",
                "badge": "1D · Sistema de Arquivos",
                "title": "Sequência Atômica: Cópia -> fclose -> remove -> rename",
                "desc": "Acompanhe os arquivos no diretório durante a substituição via temporário.",
                "kind": "1d",
                "codeLines": [
                    "FILE *temp = fopen(\"lista.tmp\", \"w\");",
                    "fclose(orig); fclose(temp);",
                    "remove(\"lista.txt\");",
                    "rename(\"lista.tmp\", \"lista.txt\");"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"orig": "aberto (r)", "temp": "aberto (w)"},
                        "note": "Existem dois arquivos no diretório; registros válidos são gravados em lista.tmp.",
                        "cells": [
                            {"label": "lista.txt", "val": "antigo (aberto)", "state": "normal"},
                            {"label": "lista.tmp", "val": "novo (aberto)", "state": "modified"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"orig": "fechado", "temp": "fechado"},
                        "note": "Ambos são fechados: buffers descarregados e travas do SO liberadas.",
                        "cells": [
                            {"label": "lista.txt", "val": "antigo (fechado)", "state": "active"},
                            {"label": "lista.tmp", "val": "novo (fechado)", "state": "active"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"remove_ret": "0 (sucesso)"},
                        "note": "remove apaga lista.txt antigo. Se falhasse, lista.tmp ainda preservaria os dados.",
                        "cells": [
                            {"label": "lista.txt", "val": "(removido)", "state": "eof"},
                            {"label": "lista.tmp", "val": "novo (intacto)", "state": "modified"}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"rename_ret": "0 (sucesso)"},
                        "note": "rename transforma lista.tmp no novo lista.txt.",
                        "cells": [
                            {"label": "lista.txt", "val": "novo (ativo!)", "state": "active"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-12",
        "num": "3.12",
        "title": "Tratamento de Erros: perror, ferror, clearerr e errno (<errno.h>)",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 · C Completo e Total Cap. 8",
        "summary": (
            "errno (<errno.h>) guarda o código numérico do último erro de sistema; perror imprime a descrição legível "
            "para stderr; ferror testa falha no stream e clearerr limpa as flags de erro e EOF."
        ),
        "conceptHtml": (
            "<p>Para diagnosticar falhas de E/S com precisão profissional em C, combinamos quatro mecanismos:</p>"
            "<ul>"
            "<li><code>errno</code> (em <code>&lt;errno.h&gt;</code>): variável global/thread-local preenchida por funções como "
            "<code>fopen</code>, <code>remove</code> e <code>rename</code> quando falham (ex.: <code>ENOENT</code> = arquivo não "
            "encontrado, <code>EACCES</code> = permissão negada). Pode ser convertida em string com <code>strerror(errno)</code> (<code>&lt;string.h&gt;</code>).</li>"
            "<li><code>void perror(const char *msg)</code>: imprime <code>msg: &lt;descrição do errno&gt;\\n</code> diretamente "
            "em <code>stderr</code>.</li>"
            "<li><code>int ferror(FILE *fp)</code>: retorna valor diferente de zero se ocorreu erro de leitura ou escrita naquele stream.</li>"
            "<li><code>void clearerr(FILE *fp)</code>: zera tanto o indicador de erro (<code>ferror</code>) quanto o de fim de arquivo (<code>feof</code>) do stream.</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <errno.h>\n"
            "#include <string.h>\n\n"
            "int main(void) {\n"
            "    errno = 0;\n"
            "    FILE *fp = fopen(\"inexistente.dat\", \"rb\");\n"
            "    if (fp == NULL) {\n"
            "        fprintf(stderr, \"Código errno=%d (%s)\\n\", errno, strerror(errno));\n"
            "        perror(\"Detalhes via perror\");\n"
            "        return 1;\n"
            "    }\n\n"
            "    int c = fgetc(fp);\n"
            "    if (c == EOF && ferror(fp)) {\n"
            "        perror(\"Falha física de leitura\");\n"
            "        clearerr(fp); // Reseta flags ferror e feof para nova tentativa\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Quando fopen falha, ela retorna NULL e ajusta errno para o código específico do sistema operacional.",
            "strerror(errno) traduz o código numérico em texto e perror imprime o prefixo seguido da mensagem de erro em stderr.",
            "Em um stream aberto, ferror(fp) distingue falha real de simples fim de arquivo, e clearerr(fp) limpa as duas flags."
        ],
        "pitfall": (
            "Chamar printf() ou outras funções de biblioteca ANTES de perror() ou ler errno: outra chamada bem-sucedida ou "
            "com erro interno pode sobrescrever errno antes de você capturá-lo! Salve ou imprima o erro imediatamente."
        ),
        "tracers": [
            {
                "id": "tr-arq-12",
                "tabLabel": "Flags & errno",
                "badge": "1D · Diagnóstico",
                "title": "Estado de errno, ferror e feof com clearerr",
                "desc": "Acompanhe como errno e as flags do stream reagem a erros e à chamada de clearerr.",
                "kind": "1d",
                "codeLines": [
                    "errno = 0; fp = fopen(\"inexistente.dat\", \"rb\");",
                    "perror(\"Falha\");",
                    "/* ... stream aberto atinge EOF ... */",
                    "clearerr(fp);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"fp": "NULL", "errno": "2 (ENOENT)"},
                        "note": "fopen falha por arquivo ausente; SO grava ENOENT em errno.",
                        "cells": [
                            {"label": "fp", "val": "NULL", "state": "eof"},
                            {"label": "errno", "val": "ENOENT", "state": "modified"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"stderr": "\"Falha: No such file or directory\""},
                        "note": "perror consulta errno imediatamente e envia a mensagem para stderr.",
                        "cells": [
                            {"label": "stderr", "val": "Falha: No such file...", "state": "active"},
                            {"label": "errno", "val": "ENOENT", "state": "normal"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"feof(fp)": "1", "ferror(fp)": "0"},
                        "note": "Em um stream aberto após atingir fim do arquivo, flag EOF está ativa (1).",
                        "cells": [
                            {"label": "flag EOF", "val": "1", "state": "eof"},
                            {"label": "flag ERR", "val": "0", "state": "normal"}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"feof(fp)": "0", "ferror(fp)": "0"},
                        "note": "clearerr(fp) zera ambas as flags (EOF e ERR) do stream.",
                        "cells": [
                            {"label": "flag EOF", "val": "0", "state": "active"},
                            {"label": "flag ERR", "val": "0", "state": "active"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-13",
        "num": "3.13",
        "title": "Buffer de E/S: fflush, setvbuf e o Efeito de Não Fechar o Arquivo",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 · C Completo e Total Cap. 8",
        "summary": (
            "Streams usam buffer em RAM (_IOFBF, _IOLBF, _IONBF) para agrupar operações de disco. Esquecer fclose pode "
            "deixar dados presos no buffer sem gravação; fflush força a descarga imediata."
        ),
        "conceptHtml": (
            "<p>Acessar o disco a cada <code>fputc</code> seria milhares de vezes mais lento do que acessar a RAM. Por isso, "
            "a biblioteca padrão associa um <strong>buffer</strong> a cada <code>FILE *</code>:</p>"
            "<ul>"
            "<li><strong>Totalmente bufferizado (<code>_IOFBF</code>):</strong> padrão para arquivos em disco; só grava no SO quando o buffer enche, chama-se <code>fflush(fp)</code> ou <code>fclose(fp)</code>.</li>"
            "<li><strong>Bufferizado por linha (<code>_IOLBF</code>):</strong> comum em <code>stdout</code> no terminal; descarrega ao encontrar <code>'\\n'</code> ou encher.</li>"
            "<li><strong>Sem buffer (<code>_IONBF</code>):</strong> padrão para <code>stderr</code>; escreve imediatamente, ideal para logs de falha.</li>"
            "</ul>"
            "<p>A função <code>int setvbuf(FILE *fp, char *buf, int modo, size_t tam)</code> configura o buffer <strong>antes</strong> de qualquer leitura/escrita no stream. "
            "Já <code>int fflush(FILE *fp)</code> força a descarga do buffer de saída para o disco (ou, em streams <code>\"r+\"</code>/<code>\"w+\"</code>, sincroniza saída antes de ler). "
            "Se o programa travar (<code>abort</code>/queda de energia) ou esquecer <code>fclose</code>, o conteúdo ainda no buffer pode se perder e gerar arquivo vazio ou truncado!</p>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    FILE *log = fopen(\"audit.log\", \"w\");\n"
            "    if (!log) return 1;\n\n"
            "    // Configura buffer de linha para gravar cada evento completo ao receber '\\n'\n"
            "    setvbuf(log, NULL, _IOLBF, 0);\n\n"
            "    fprintf(log, \"Passo 1 concluido\"); // Ainda no buffer (sem '\\n')\n"
            "    fflush(log);                        // Força gravação imediata no disco!\n"
            "    fprintf(log, \"\\nPasso 2 concluido\\n\");\n\n"
            "    fclose(log); // Sempre fechar para garantir flush final e liberar descritor\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "setvbuf altera o modo de bufferização logo após fopen e antes de qualquer escrita.",
            "fprintf sem '\\n' deixa os bytes acumulados apenas na RAM do buffer do processo.",
            "fflush(log) descarrega os bytes pendentes para o sistema operacional imediatamente; fclose realiza o flush final."
        ],
        "pitfall": (
            "Usar fflush(stdin) para limpar buffer de teclado: o padrão C (ISO C) define fflush() APENAS para streams de saída "
            "ou atualização; em streams de entrada como stdin o comportamento é indefinido (não portável)."
        ),
        "tracers": [
            {
                "id": "tr-arq-13",
                "tabLabel": "RAM Buffer vs Disco",
                "badge": "2D · Fluxo de Buffer",
                "title": "Dados no Buffer em RAM vs Persistência Real no Disco",
                "desc": "Veja quando os bytes saem do buffer em RAM e realmente chegam ao arquivo audit.log.",
                "kind": "2d",
                "codeLines": [
                    "FILE *log = fopen(\"audit.log\", \"w\");",
                    "fprintf(log, \"Passo 1\");",
                    "fflush(log);",
                    "fclose(log);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"buffer_RAM": "vazio", "disco": "0 bytes"},
                        "note": "Arquivo aberto com buffer vazio em RAM.",
                        "grid": [
                            [{"label": "Buffer RAM", "val": "[        ]", "state": "normal"}],
                            [{"label": "Disco (audit.log)", "val": "0 bytes", "state": "normal"}]
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"buffer_RAM": "\"Passo 1\" (7B)", "disco": "0 bytes (!)"} ,
                        "note": "ATENÇÃO: após fprintf, \"Passo 1\" está SÓ na RAM! Se o programa abortar aqui, o arquivo fica com 0 bytes.",
                        "grid": [
                            [{"label": "Buffer RAM", "val": "\"Passo 1\"", "state": "modified"}],
                            [{"label": "Disco (audit.log)", "val": "0 bytes (ainda vazio!)", "state": "eof"}]
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"buffer_RAM": "vazio", "disco": "\"Passo 1\" (7B)"},
                        "note": "fflush(log) envia o conteúdo do buffer para o SO/disco e esvazia o buffer.",
                        "grid": [
                            [{"label": "Buffer RAM", "val": "[vazio]", "state": "normal"}],
                            [{"label": "Disco (audit.log)", "val": "\"Passo 1\" (7 bytes)", "state": "active"}]
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"estado": "fechado com segurança"},
                        "note": "fclose faz o flush final automático e libera o descritor.",
                        "grid": [
                            [{"label": "Buffer RAM", "val": "(liberado)", "state": "normal"}],
                            [{"label": "Disco (audit.log)", "val": "7 bytes garantidos", "state": "active"}]
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-14",
        "num": "3.14",
        "title": "Fluxos Padrão: stdin, stdout, stderr e Redirecionamento no Terminal",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.2) · C Completo e Total Cap. 8",
        "summary": (
            "Todo programa C já inicia com três streams abertos automaticamente: stdin (entrada padrão), stdout (saída "
            "padrão) e stderr (erro padrão, sem buffer), que podem ser redirecionados pelo shell (<, >, 2>)."
        ),
        "conceptHtml": (
            "<p>Antes mesmo de você chamar <code>fopen</code>, o ambiente de execução abre três ponteiros <code>FILE *</code> "
            "globais definidos em <code>&lt;stdio.h&gt;</code> (Deitel Cap. 11.2):</p>"
            "<ul>"
            "<li><code>stdin</code>: entrada padrão (normalmente o teclado). Funções como <code>scanf</code> e <code>getchar</code> são atalhos para <code>fscanf(stdin, ...)</code> e <code>fgetc(stdin)</code>.</li>"
            "<li><code>stdout</code>: saída padrão (normalmente a tela). <code>printf(...)</code> equivale a <code>fprintf(stdout, ...)</code>.</li>"
            "<li><code>stderr</code>: saída padrão de erro (também na tela por padrão, mas <strong>sem buffer</strong> para aparecer na hora mesmo em falhas).</li>"
            "</ul>"
            "<p><strong>Redirecionamento no terminal (shell):</strong> sem mudar uma linha do código C, o usuário pode conectar arquivos aos fluxos padrão:</p>"
            "<ul>"
            "<li><code>./prog &lt; entrada.txt &gt; saida.txt</code> redireciona <code>stdin</code> e <code>stdout</code>.</li>"
            "<li><code>./prog &gt; saida.txt 2&gt; erros.log</code> separa saída normal (<code>stdout</code>) de diagnósticos (<code>stderr</code>)!</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(void) {\n"
            "    int n;\n"
            "    // Lê de stdin (teclado ou arquivo via '< entrada.txt')\n"
            "    while (fscanf(stdin, \"%d\", &n) == 1) {\n"
            "        if (n < 0) {\n"
            "            fprintf(stderr, \"Aviso: valor negativo ignorado (%d)\\n\", n);\n"
            "            continue;\n"
            "        }\n"
            "        fprintf(stdout, \"Dobro: %d\\n\", n * 2);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "fscanf(stdin, ...) lê do fluxo padrão de entrada, permitindo teste interativo ou via redirecionamento '<'.",
            "Valores válidos vão para stdout via fprintf(stdout, ...), podendo ser capturados com '>' ou pipe '|'.",
            "Mensagens de aviso vão para stderr, permanecendo visíveis no console ou isoladas com '2>' sem contaminar stdout."
        ],
        "pitfall": (
            "Imprimir mensagens de erro com printf() (stdout) em vez de fprintf(stderr, ...): quando alguém redireciona a "
            "saída do programa para um arquivo CSV/JSON (> dados.csv), o erro vai parar dentro do arquivo de dados!"
        ),
        "tracers": [
            {
                "id": "tr-arq-14",
                "tabLabel": "Redirecionamento",
                "badge": "2D · stdin/stdout/stderr",
                "title": "Roteamento com ./prog < in.txt > out.txt 2> err.log",
                "desc": "Veja para onde vai cada linha quando stdin lê '5' e '-3' com redirecionamento no terminal.",
                "kind": "2d",
                "codeLines": [
                    "while (fscanf(stdin, \"%d\", &n) == 1) {",
                    "  if (n < 0) fprintf(stderr, \"Aviso: %d\\n\", n);",
                    "  else fprintf(stdout, \"Dobro: %d\\n\", n * 2);",
                    "}"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"n": "5", "origem": "in.txt (stdin)"},
                        "note": "Primeira leitura de stdin (redirecionado de in.txt) retorna n = 5.",
                        "grid": [
                            [{"label": "stdin (in.txt)", "val": "[5] -3", "state": "active"}],
                            [{"label": "stdout (out.txt)", "val": "(vazio)", "state": "normal"}],
                            [{"label": "stderr (err.log)", "val": "(vazio)", "state": "normal"}]
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"n": "5", "destino": "stdout -> out.txt"},
                        "note": "5 >= 0: fprintf envia \"Dobro: 10\\n\" para out.txt.",
                        "grid": [
                            [{"label": "stdin (in.txt)", "val": "5 [-3]", "state": "normal"}],
                            [{"label": "stdout (out.txt)", "val": "Dobro: 10", "state": "modified"}],
                            [{"label": "stderr (err.log)", "val": "(vazio)", "state": "normal"}]
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"n": "-3", "destino": "stderr -> err.log"},
                        "note": "-3 < 0: mensagem de erro vai para err.log sem sujar out.txt!",
                        "grid": [
                            [{"label": "stdin (in.txt)", "val": "5 -3 [EOF]", "state": "normal"}],
                            [{"label": "stdout (out.txt)", "val": "Dobro: 10", "state": "normal"}],
                            [{"label": "stderr (err.log)", "val": "Aviso: -3", "state": "eof"}]
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-15",
        "num": "3.15",
        "title": "Argumentos de Linha de Comando: int argc, char *argv[] para Arquivos",
        "pdfRef": "Deitel 6ª Ed. Cap. 14 · C Completo e Total Cap. 6 & 8",
        "summary": (
            "argc informa a quantidade de argumentos passados na chamada do executável e argv[] guarda as strings (argv[0] "
            "é o nome do programa, argv[1], argv[2]... são os caminhos de arquivos de entrada e saída)."
        ),
        "conceptHtml": (
            "<p>Programas utilitários em C (como <code>cp</code>, <code>grep</code>, <code>wc</code>) não pedem nomes de "
            "arquivos com <code>scanf</code>: eles recebem esses nomes diretamente via <code>int main(int argc, char *argv[])</code>.</p>"
            "<ul>"
            "<li><code>argc</code> (<em>argument count</em>): inteiro &ge; 1 indicando quantos argumentos existem.</li>"
            "<li><code>argv</code> (<em>argument vector</em>): vetor de ponteiros para strings terminado em <code>argv[argc] == NULL</code>. "
            "<code>argv[0]</code> contém o nome/caminho do próprio executável; <code>argv[1]</code> é o 1º parâmetro, <code>argv[2]</code> o 2º, e assim por diante.</li>"
            "</ul>"
            "<p><strong>Regra de validação obrigatória:</strong> antes de acessar <code>argv[1]</code> ou <code>argv[2]</code>, "
            "verifique <code>if (argc &lt; 3)</code> (ou <code>argc != 3</code>) e imprima a forma de uso em <code>stderr</code>. "
            "Acessar <code>argv[i]</code> quando <code>i &gt;= argc</code> acessa <code>NULL</code> ou memória inválida!</p>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "int main(int argc, char *argv[]) {\n"
            "    if (argc != 3) {\n"
            "        fprintf(stderr, \"Uso: %s <origem> <destino>\\n\", argv[0]);\n"
            "        return 1;\n"
            "    }\n\n"
            "    FILE *in = fopen(argv[1], \"rb\");\n"
            "    if (!in) { perror(argv[1]); return 1; }\n\n"
            "    FILE *out = fopen(argv[2], \"wb\");\n"
            "    if (!out) { perror(argv[2]); fclose(in); return 1; }\n\n"
            "    int ch;\n"
            "    while ((ch = fgetc(in)) != EOF) {\n"
            "        fputc(ch, out);\n"
            "    }\n"
            "    fclose(in);\n"
            "    fclose(out);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "Valida-se argc != 3 antes de ler argv[1] e argv[2], exibindo a sintaxe esperada com argv[0] em stderr.",
            "argv[1] é passado diretamente a fopen(..., \"rb\") como arquivo de origem; argv[2] como destino em \"wb\".",
            "Se a abertura de out falhar, in (que já foi aberto!) é fechado com fclose(in) para evitar vazamento de descritor."
        ],
        "pitfall": (
            "Esquecer que argv[0] é o nome do programa! Para 2 arquivos (origem e destino), argc deve ser 3 (não 2). Além disso, "
            "se out falhar no fopen, esquecer fclose(in) vaza o primeiro descritor."
        ),
        "tracers": [
            {
                "id": "tr-arq-15",
                "tabLabel": "Vetor argv[]",
                "badge": "1D · argc & argv",
                "title": "Execução: ./copia dados.bin backup.bin",
                "desc": "Inspecione argc e cada ponteiro de argv[] durante a validação e abertura dos arquivos.",
                "kind": "1d",
                "codeLines": [
                    "int main(int argc, char *argv[]) {",
                    "  if (argc != 3) return 1;",
                    "  FILE *in = fopen(argv[1], \"rb\");",
                    "  FILE *out = fopen(argv[2], \"wb\");"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"argc": "3", "argv[0]": "\"./copia\""},
                        "note": "O shell preenche argc = 3 e um vetor argv com 4 posições (terminando em NULL).",
                        "cells": [
                            {"label": "argv[0]", "val": "\"./copia\"", "state": "normal"},
                            {"label": "argv[1]", "val": "\"dados.bin\"", "state": "active"},
                            {"label": "argv[2]", "val": "\"backup.bin\"", "state": "active"},
                            {"label": "argv[3]", "val": "NULL", "state": "normal"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"argc != 3": "false"},
                        "note": "argc é 3, então a validação passa e o programa segue.",
                        "cells": [
                            {"label": "argc", "val": "3 == 3 (OK)", "state": "modified"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"argv[1]": "\"dados.bin\"", "in": "0x55c0"},
                        "note": "fopen abre argv[1] (\"dados.bin\") para leitura binária.",
                        "cells": [
                            {"label": "in", "val": "0x55c0 -> dados.bin", "state": "active"}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"argv[2]": "\"backup.bin\"", "out": "0x55e0"},
                        "note": "fopen abre argv[2] (\"backup.bin\") para escrita binária.",
                        "cells": [
                            {"label": "in", "val": "0x55c0 -> dados.bin", "state": "normal"},
                            {"label": "out", "val": "0x55e0 -> backup.bin", "state": "modified"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-16",
        "num": "3.16",
        "title": "Algoritmos Clássicos e CSV: Contadores, Transformações, Busca e strtok/sscanf",
        "pdfRef": "Deitel 6ª Ed. Cap. 8 & 11 · C Completo e Total Cap. 8",
        "summary": (
            "Padrões recorrentes em provas: contar linhas/palavras/chars (máquina de estados), copiar/concatenar/converter "
            "maiúsculas-minúsculas, buscar palavras com strstr, gerar relatórios e fazer parsing de CSV com fgets + strtok/sscanf."
        ),
        "conceptHtml": (
            "<p>A maior parte das questões práticas de arquivos em C combina streams com manipulação de strings (<code>&lt;string.h&gt;</code> "
            "e <code>&lt;ctype.h&gt;</code>):</p>"
            "<ul>"
            "<li><strong>Contar caracteres, palavras e linhas (estilo <code>wc</code>):</strong> leia com <code>int ch = fgetc(fp)</code>. "
            "Cada byte incrementa <code>chars</code>; <code>ch == '\\n'</code> incrementa <code>linhas</code>; e uma flag "
            "<code>em_palavra</code> detecta transições de espaço (<code>isspace(ch)</code>) para não-espaço.</li>"
            "<li><strong>Copiar / Concatenar / Maiúsculas:</strong> copiar usa <code>fgetc/fputc</code> (ou blocos <code>fread/fwrite</code>); "
            "concatenar abre o destino em <code>\"a\"</code> (ou <code>\"ab\"</code>); converter caixa aplica <code>toupper((unsigned char)ch)</code>.</li>"
            "<li><strong>Buscar palavra e gerar relatório:</strong> leia linha a linha com <code>fgets</code>, teste com <code>strstr(linha, termo) != NULL</code> "
            "e grave as ocorrências e totais em um arquivo de relatório com <code>fprintf</code>.</li>"
            "<li><strong>Leitura de CSV:</strong> leia a linha com <code>fgets</code>, remova <code>\\r\\n</code> e separe os campos por "
            "<code>\",\"</code> ou <code>\";\"</code> usando <code>strtok(linha, \";\")</code> (ou <code>sscanf(linha, \"%49[^;];%d;%lf\", ...)</code> "
            "para evitar falhas com campos vazios).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "#include <stdlib.h>\n\n"
            "int main(void) {\n"
            "    FILE *csv = fopen(\"vendas.csv\", \"r\");\n"
            "    FILE *rel = fopen(\"resumo.txt\", \"w\");\n"
            "    if (!csv || !rel) { if (csv) fclose(csv); if (rel) fclose(rel); return 1; }\n\n"
            "    char linha[128];\n"
            "    fgets(linha, sizeof(linha), csv); // Descarta cabeçalho\n"
            "    double total = 0.0;\n"
            "    int linhas = 0;\n\n"
            "    while (fgets(linha, sizeof(linha), csv) != NULL) {\n"
            "        linha[strcspn(linha, \"\\r\\n\")] = '\\0';\n"
            "        char *prod = strtok(linha, \";\");\n"
            "        char *qtd_s = strtok(NULL, \";\");\n"
            "        char *preco_s = strtok(NULL, \";\");\n"
            "        if (prod && qtd_s && preco_s) {\n"
            "            int qtd = atoi(qtd_s);\n"
            "            double preco = atof(preco_s);\n"
            "            total += qtd * preco;\n"
            "            linhas++;\n"
            "            fprintf(rel, \"%-15s | %3d x %6.2f\\n\", prod, qtd, preco);\n"
            "        }\n"
            "    }\n"
            "    fprintf(rel, \"TOTAL (%d itens): R$ %.2f\\n\", linhas, total);\n"
            "    fclose(csv); fclose(rel);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "A primeira chamada fgets pula a linha de cabeçalho do CSV antes do laço principal.",
            "Cada linha subsequente tem '\\r\\n' removido e é quebrada in-loco por strtok usando ';' como delimitador.",
            "Após validar os 3 ponteiros (prod, qtd_s, preco_s), os números são convertidos e o relatório formatado é escrito em resumo.txt."
        ],
        "pitfall": (
            "Esquecer que strtok() MODIFICA a string original substituindo delimitadores por '\\0', além de colapsar dois "
            "delimitadores seguidos (ex.: \"A;;10\" trata \";;\" como um único separador). Para campos vazios em CSV, prefira sscanf com scanset ou strsep/ponteiro manual."
        ),
        "tracers": [
            {
                "id": "tr-arq-16",
                "tabLabel": "Tokenização CSV",
                "badge": "1D · strtok in-loco",
                "title": "Fatiamento de Linha CSV com strtok(linha, \";\")",
                "desc": "Veja como strtok insere '\\0' dentro do array linha[] e retorna ponteiros para cada coluna.",
                "kind": "1d",
                "codeLines": [
                    "// linha = \"Mouse;2;45.50\"",
                    "char *prod = strtok(linha, \";\");",
                    "char *qtd_s = strtok(NULL, \";\");",
                    "char *preco_s = strtok(NULL, \";\");"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"linha": "\"Mouse;2;45.50\""},
                        "note": "Buffer inicial após remover o '\\n'.",
                        "cells": [
                            {"label": "[0..4]", "val": "Mouse", "state": "normal"},
                            {"label": "[5]", "val": "';'", "state": "normal"},
                            {"label": "[6]", "val": "'2'", "state": "normal"},
                            {"label": "[7]", "val": "';'", "state": "normal"},
                            {"label": "[8..12]", "val": "45.50", "state": "normal"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"prod": "&linha[0] (\"Mouse\")"},
                        "note": "strtok encontra o 1º ';' no índice 5, troca-o por '\\0' e devolve o início.",
                        "cells": [
                            {"label": "[0..4]", "val": "Mouse", "state": "active"},
                            {"label": "[5]", "val": "'\\0'", "state": "modified"},
                            {"label": "[6]", "val": "'2'", "state": "normal"},
                            {"label": "[7]", "val": "';'", "state": "normal"},
                            {"label": "[8..12]", "val": "45.50", "state": "normal"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"qtd_s": "&linha[6] (\"2\")"},
                        "note": "strtok(NULL, \";\") retoma após o índice 5, troca ';' do índice 7 por '\\0' e devolve \"2\".",
                        "cells": [
                            {"label": "[0..4]", "val": "Mouse", "state": "normal"},
                            {"label": "[5]", "val": "'\\0'", "state": "normal"},
                            {"label": "[6]", "val": "'2'", "state": "active"},
                            {"label": "[7]", "val": "'\\0'", "state": "modified"},
                            {"label": "[8..12]", "val": "45.50", "state": "normal"}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"preco_s": "&linha[8] (\"45.50\")", "total": "91.00"},
                        "note": "Último token aponta para \"45.50\" até o '\\0' final.",
                        "cells": [
                            {"label": "[0..5]", "val": "Mouse\\0", "state": "normal"},
                            {"label": "[6..7]", "val": "2\\0", "state": "normal"},
                            {"label": "[8..12]", "val": "45.50", "state": "active"}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "arq-17",
        "num": "3.17",
        "title": "CRUD em Arquivos, Ordenação/Busca e Armadilhas Avançadas",
        "pdfRef": "Deitel 6ª Ed. Cap. 11 (11.8–11.10) · C Completo e Total Cap. 8",
        "summary": (
            "CRUD em binário combina append (Create), leitura sequencial (Read), fseek+r+b (Update) e exclusão lógica "
            "(flag ativo=0) ou física (cópia para temp + remove + rename), evitando falhas de fflush/fseek e portabilidade."
        ),
        "conceptHtml": (
            "<p>Implementar um <strong>CRUD completo</strong> (Cadastrar, Listar, Buscar, Alterar, Excluir) sobre arquivos "
            "exige domínio de quatro conceitos fundamentais (Deitel Cap. 11.10):</p>"
            "<ul>"
            "<li><strong>Exclusão Lógica vs. Física:</strong> na <em>lógica</em>, a struct possui um campo <code>int ativo</code>; "
            "basta marcar <code>ativo = 0</code> e sobrescrever o registro no mesmo offset com <code>fseek</code> + <code>fwrite</code> (O(1), "
            "mas deixa espaço morto). Na <em>física</em>, copiam-se apenas os registros ativos para um arquivo temporário, fecham-se "
            "ambos e faz-se <code>remove</code> + <code>rename</code> (compacta o arquivo).</li>"
            "<li><strong>Ordenação e Busca em Arquivo:</strong> para arquivos pequenos/médios, carrega-se o vetor de structs em RAM, "
            "ordena-se (ex.: <code>qsort</code>) e regrava; se já ordenado por ID no arquivo binário, é possível fazer "
            "<strong>busca binária direta no disco</strong> com <code>fseek(fp, mid * sizeof(Reg), SEEK_SET)</code> em O(log n)!</li>"
            "<li><strong>Alternância Leitura/Escrita em modos <code>+</code> (<code>r+</code>, <code>r+b</code>):</strong> pelo padrão ANSI/ISO C, "
            "após uma leitura NÃO se pode escrever imediatamente sem antes chamar <code>fseek</code>/<code>rewind</code>; e após "
            "uma escrita NÃO se pode ler sem chamar <code>fseek</code> ou <code>fflush</code>!</li>"
            "<li><strong>Portabilidade binária:</strong> arquivos gravados com <code>fwrite(&amp;struct)</code> dependem de "
            "<em>padding</em> do compilador, tamanho de <code>int</code>/<code>long</code> e ordem de bytes (<em>endianness</em>: little vs big-endian).</li>"
            "</ul>"
        ),
        "code": (
            "#include <stdio.h>\n\n"
            "typedef struct { int id; char nome[32]; double saldo; int ativo; } Conta;\n\n"
            "int atualizar_saldo(const char *arq, int id_alvo, double novo_saldo) {\n"
            "    FILE *fp = fopen(arq, \"r+b\"); // NUNCA \"w+b\" para alterar!\n"
            "    if (!fp) return 0;\n"
            "    Conta c;\n"
            "    long idx = 0;\n"
            "    while (fread(&c, sizeof(Conta), 1, fp) == 1) {\n"
            "        if (c.ativo && c.id == id_alvo) {\n"
            "            c.saldo = novo_saldo;\n"
            "            // Obrigatório reposicionar antes de escrever após fread!\n"
            "            fseek(fp, idx * (long)sizeof(Conta), SEEK_SET);\n"
            "            fwrite(&c, sizeof(Conta), 1, fp);\n"
            "            fflush(fp); // Garante sincronização se houver nova leitura\n"
            "            fclose(fp);\n"
            "            return 1;\n"
            "        }\n"
            "        idx++;\n"
            "    }\n"
            "    fclose(fp);\n"
            "    return 0;\n"
            "}"
        ),
        "logicSteps": [
            "O arquivo é aberto em \"r+b\" para permitir leitura e sobrescrita pontual sem apagar registros existentes.",
            "Após fread encontrar o registro desejado, o cursor avançou para idx + 1; fseek recua exatamente para idx * sizeof(Conta).",
            "fwrite sobrescreve o registro in-loco e fflush/fclose garante persistência sem comportamento indefinido na troca leitura->escrita."
        ],
        "pitfall": (
            "1) Esquecer o fseek antes do fwrite após encontrar o registro com fread: o programa sobrescreve o PRÓXIMO registro "
            "(e viola a regra ANSI C de alternância R/W em modo '+'); 2) usar \"w\" por engano e apagar o banco; 3) esquecer fclose."
        ),
        "tracers": [
            {
                "id": "tr-arq-17",
                "tabLabel": "Update in-loco (r+b)",
                "badge": "1D · CRUD Binário",
                "title": "Por que Recuar com fseek Antes do fwrite na Alteração",
                "desc": "Acompanhe o cursor ao buscar id=20 (idx=1) e alterar o saldo sem corromper o registro vizinho.",
                "kind": "1d",
                "codeLines": [
                    "while (fread(&c, sizeof(Conta), 1, fp) == 1)",
                    "  // Achou id == 20 no idx = 1!",
                    "  fseek(fp, idx * sizeof(Conta), SEEK_SET);",
                    "  fwrite(&c, sizeof(Conta), 1, fp);"
                ],
                "steps": [
                    {
                        "line": 0,
                        "vars": {"idx": "0", "cursor_apos_fread": "1 * sizeof"},
                        "note": "1º fread lê Reg[0] (id=10). Cursor fica no início de Reg[1]. Não é o alvo; idx vira 1.",
                        "cells": [
                            {"label": "Reg[0] (id=10)", "val": "lido", "state": "normal"},
                            {"label": "Reg[1] (id=20)", "val": "CURSOR AQUI", "state": "active"},
                            {"label": "Reg[2] (id=30)", "val": "intacto", "state": "normal"}
                        ]
                    },
                    {
                        "line": 1,
                        "vars": {"idx": "1", "c.id": "20", "cursor_apos_fread": "2 * sizeof (!)"},
                        "note": "2º fread lê Reg[1] (id=20), MAS avança o cursor para Reg[2]! Escrever agora corromperia Reg[2]!",
                        "cells": [
                            {"label": "Reg[0] (id=10)", "val": "ok", "state": "normal"},
                            {"label": "Reg[1] (id=20)", "val": "alvo na RAM", "state": "modified"},
                            {"label": "Reg[2] (id=30)", "val": "PERIGO: CURSOR AQUI", "state": "eof"}
                        ]
                    },
                    {
                        "line": 2,
                        "vars": {"idx": "1", "fseek_offset": "1 * sizeof(Conta)"},
                        "note": "fseek recua o cursor de volta para o início de Reg[1] (e cumpre a troca leitura->escrita).",
                        "cells": [
                            {"label": "Reg[0] (id=10)", "val": "ok", "state": "normal"},
                            {"label": "Reg[1] (id=20)", "val": "CURSOR RECUADO", "state": "active"},
                            {"label": "Reg[2] (id=30)", "val": "protegido", "state": "normal"}
                        ]
                    },
                    {
                        "line": 3,
                        "vars": {"c.saldo": "atualizado", "cursor_apos_fwrite": "2 * sizeof"},
                        "note": "fwrite sobrescreve exatamente Reg[1] no disco; Reg[0] e Reg[2] permanecem intactos.",
                        "cells": [
                            {"label": "Reg[0] (id=10)", "val": "ok", "state": "normal"},
                            {"label": "Reg[1] (id=20)", "val": "ATUALIZADO!", "state": "modified"},
                            {"label": "Reg[2] (id=30)", "val": "intacto", "state": "normal"}
                        ]
                    }
                ]
            }
        ]
    }
]
