"""Banco de exercícios de Structs, Unions e Enums: 30 MCQs, 10 Certo/Errado e 2 Problemas Clássicos."""
from __future__ import annotations

MCQ_STRUCTS = [
    {
        "id": "q-strc-1",
        "category": "structs",
        "subtopic": "2.1 Conceito e Registro",
        "level": "Básico",
        "title": "Diferença fundamental entre vetor e struct",
        "stem": (
            "Sobre a estrutura de dados heterogênea (struct) em C, assinale a alternativa CORRETA."
        ),
        "code": "",
        "options": [
            "Uma struct armazena exclusivamente elementos de um mesmo tipo básico.",
            "Definir uma struct reserva imediatamente memória na stack para todos os campos.",
            "Uma struct agrupa membros que podem possuir tipos diferentes sob um único nome.",
            "Não é possível declarar vetores dentro de uma struct em C.",
            "Membros de uma struct são acessados por índice numérico inteiro, como a[0]."
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: isso descreve um vetor (array), que é homogêneo.",
            "Errado: a definição cria apenas o molde (tipo); a memória só é alocada ao declarar uma variável.",
            "Correto: structs são registros compostos heterogêneos que agrupam campos de tipos distintos.",
            "Errado: arrays como char nome[40] e float notas[3] são muito comuns dentro de structs.",
            "Errado: os campos são acessados pelo nome usando '.' ou '->', não por índice."
        ],
        "steps": [
            "Identifique que arrays são homogêneos (mesmo tipo) e structs são heterogêneas (tipos diversos).",
            "Confirme que definir 'struct X { ... };' descreve o formato sem alocar bytes até existir uma variável."
        ],
        "gabaritoResumo": "Struct é um tipo composto heterogêneo cujos membros têm nomes e tipos próprios.",
        "solutionCode": (
            "struct Aluno {\n"
            "    int matricula;\n"
            "    char nome[30];\n"
            "    float media;\n"
            "};"
        )
    },
    {
        "id": "q-strc-2",
        "category": "structs",
        "subtopic": "2.2 Declaração e Variáveis",
        "level": "Básico",
        "title": "Ponto e vírgula ao final da definição de struct",
        "stem": (
            "Observe o trecho em C abaixo. Por que ele falha na compilação?"
        ),
        "code": (
            "struct Ponto {\n"
            "    int x;\n"
            "    int y;\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    struct Ponto p = {1, 2};\n"
            "    return 0;\n"
            "}"
        ),
        "options": [
            "Porque falta o operador typedef antes da palavra struct.",
            "Porque não é permitido inicializar uma struct usando chaves na declaração.",
            "Porque falta o ponto e vírgula ';' logo após a chave de fechamento '}' da struct.",
            "Porque os campos x e y deveriam ser declarados em uma única linha.",
            "Porque struct Ponto não pode ser declarada fora da função main."
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: typedef é opcional; declarar 'struct Ponto p' é perfeitamente válido em C.",
            "Errado: inicialização em lista {1, 2} é válida na declaração.",
            "Correto: toda declaração de struct deve terminar com ';' após '}', pois entre '}' e ';' poderiam existir nomes de variáveis.",
            "Errado: campos podem ficar na mesma linha ou em linhas separadas.",
            "Errado: structs são normalmente declaradas em escopo global para serem visíveis a todas as funções."
        ],
        "steps": [
            "Verifique a linha 4 do código: após '}' não há ';'.",
            "Sem ';', o compilador tenta interpretar 'int main' como uma variável do tipo struct Ponto."
        ],
        "gabaritoResumo": "A definição de uma struct exige ';' imediatamente após a chave de fechamento '}'.",
        "solutionCode": (
            "struct Ponto {\n"
            "    int x;\n"
            "    int y;\n"
            "};\n"
            "int main(void) {\n"
            "    struct Ponto p = {1, 2};\n"
            "    return p.x;\n"
            "}"
        )
    },
    {
        "id": "q-strc-3",
        "category": "structs",
        "subtopic": "2.2 Declaração e Variáveis",
        "level": "Básico",
        "title": "Declaração sem typedef em C",
        "stem": (
            "Considerando 'struct Retangulo { float base; float alt; };', qual declaração de "
            "variável compila em C padrão (ISO C99/C11)?"
        ),
        "code": "",
        "options": [
            "Retangulo r;",
            "struct r Retangulo;",
            "struct Retangulo r;",
            "typedef Retangulo r;",
            "new struct Retangulo r;"
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: em C puro (diferente de C++), sem typedef o nome 'Retangulo' sozinho não é um tipo.",
            "Errado: inverte a tag com o nome da variável.",
            "Correto: sem typedef, deve-se incluir a palavra-chave 'struct' antes da tag.",
            "Errado: typedef cria alias de tipo, não declara variável.",
            "Errado: 'new' não existe em C."
        ],
        "steps": [
            "Em C, nomes após 'struct' ficam no namespace de tags.",
            "Portanto, sem typedef, é obrigatório prefixar com 'struct': struct Retangulo r;."
        ],
        "gabaritoResumo": "Sem typedef, variáveis devem ser declaradas com 'struct NomeTag var;'.",
        "solutionCode": (
            "struct Retangulo { float base; float alt; };\n"
            "int main(void) {\n"
            "    struct Retangulo r = {3.0f, 4.0f};\n"
            "    return (int)(r.base * r.alt);\n"
            "}"
        )
    },
    {
        "id": "q-strc-4",
        "category": "structs",
        "subtopic": "2.3 typedef",
        "level": "Básico",
        "title": "Uso correto de typedef com struct",
        "stem": (
            "Analise o trecho abaixo (baseado no Ex. 54 do PDF) e assinale o que ocorre ao compilar:"
        ),
        "code": (
            "typedef struct _frac {\n"
            "    int numerador, denominador;\n"
            "} FRACAO;\n"
            "\n"
            "int main(void) {\n"
            "    FRACAO f = {1, 2};\n"
            "    FRACAO.numerador = 3;\n"
            "    return 0;\n"
            "}"
        ),
        "options": [
            "Compila e altera f.numerador para 3.",
            "Falha porque FRACAO é um nome de tipo (alias), e não uma variável.",
            "Falha porque não é permitido usar _frac como tag junto de typedef.",
            "Compila, mas gera comportamento indefinido em tempo de execução.",
            "Falha porque struct com typedef não aceita dois campos na mesma linha."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: FRACAO.numerador é inválido porque FRACAO é um tipo.",
            "Correto: com typedef, o identificador antes do ';' torna-se um sinônimo do tipo, não uma variável.",
            "Errado: usar tag (_frac) junto com alias (FRACAO) é totalmente válido em C.",
            "Errado: é um erro de compilação, não de execução.",
            "Errado: 'int numerador, denominador;' é válido dentro de structs."
        ],
        "steps": [
            "Observe a palavra 'typedef' no início da declaração.",
            "Logo, FRACAO é um tipo (como int) e apenas variáveis como 'f' podem usar '.numerador'."
        ],
        "gabaritoResumo": "Com typedef, o nome final é um alias de tipo, jamais uma variável.",
        "solutionCode": (
            "typedef struct _frac { int numerador, denominador; } FRACAO;\n"
            "int main(void) {\n"
            "    FRACAO f = {1, 2};\n"
            "    f.numerador = 3;\n"
            "    return f.numerador;\n"
            "}"
        )
    },
    {
        "id": "q-strc-5",
        "category": "structs",
        "subtopic": "2.4 Acesso: . vs ->",
        "level": "Básico",
        "title": "Operador seta (->) e precedência com *",
        "stem": (
            "Dado 'struct Sensor *s;' apontando para uma struct válida (Ex. 32 do PDF), "
            "qual expressão acessa CORRETAMENTE o campo 'valor_medido'?"
        ),
        "code": (
            "struct Sensor {\n"
            "    int referencia;\n"
            "    float valor_medido;\n"
            "};"
        ),
        "options": [
            "s.valor_medido",
            "*s.valor_medido",
            "(*s).valor_medido",
            "&s->valor_medido",
            "s->*valor_medido"
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: s é ponteiro, não variável struct; '.' exige struct ou union à esquerda.",
            "Errado: '.' tem precedência maior que '*', então *s.valor_medido tenta *(s.valor_medido).",
            "Correto: (*s).valor_medido desreferencia o ponteiro primeiro e depois acessa o campo, equivalendo a s->valor_medido.",
            "Errado: &s->valor_medido retorna o endereço (float *), não o valor float.",
            "Errado: sintaxe inválida em C."
        ],
        "steps": [
            "Como s é ponteiro, podemos usar s->valor_medido ou (*s).valor_medido.",
            "Lembre que '.' precede '*', tornando os parênteses em (*s) indispensáveis."
        ],
        "gabaritoResumo": "s->campo é exatamente equivalente a (*s).campo.",
        "solutionCode": (
            "struct Sensor { int referencia; float valor_medido; };\n"
            "float le_valor(const struct Sensor *s) {\n"
            "    return (*s).valor_medido; /* igual a s->valor_medido */\n"
            "}"
        )
    },
    {
        "id": "q-strc-6",
        "category": "structs",
        "subtopic": "2.4 Acesso: . vs ->",
        "level": "Intermediário",
        "title": "Precedência de &s->campo no scanf",
        "stem": (
            "Na função 'void entra_dados(struct Sensor *s)' (Ex. 32 do PDF), qual chamada de "
            "scanf lê corretamente o campo inteiro 'referencia'?"
        ),
        "code": (
            "struct Sensor {\n"
            "    int referencia;\n"
            "    float valor_medido;\n"
            "};"
        ),
        "options": [
            "scanf(\"%d\", s->referencia);",
            "scanf(\"%d\", &s->referencia);",
            "scanf(\"%d\", s.&referencia);",
            "scanf(\"%d\", *s->referencia);",
            "scanf(\"%d\", &s.referencia);"
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: passa o valor int de referencia em vez do endereço.",
            "Correto: '->' tem precedência maior que '&', logo &s->referencia significa &(s->referencia), passando int *.",
            "Errado: sintaxe inválida após '->'.",
            "Errado: tenta desreferenciar um int.",
            "Errado: s é ponteiro, então s.referencia não compila."
        ],
        "steps": [
            "scanf(\"%d\", ...) espera um ponteiro int *.",
            "O membro inteiro é s->referencia; aplicando '&', obtemos &(s->referencia) = &s->referencia."
        ],
        "gabaritoResumo": "Para ler membro escalar via ponteiro de struct, use &ptr->campo.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "struct Sensor { int referencia; float valor_medido; };\n"
            "void entra_dados(struct Sensor *s) {\n"
            "    scanf(\"%d\", &s->referencia);\n"
            "    scanf(\"%f\", &s->valor_medido);\n"
            "}"
        )
    },
    {
        "id": "q-strc-7",
        "category": "structs",
        "subtopic": "2.5 Inicialização Designada",
        "level": "Intermediário",
        "title": "Inicialização designada e campos omitidos (C99)",
        "stem": (
            "Qual será a saída produzida pelo programa C99 abaixo?"
        ),
        "code": (
            "#include <stdio.h>\n"
            "typedef struct { char nome[12]; int idade; float nota; } Aluno;\n"
            "int main(void) {\n"
            "    Aluno a = {.nota = 9.0f, .nome = \"Ana\"};\n"
            "    printf(\"%s %d %.1f\\n\", a.nome, a.idade, a.nota);\n"
            "    return 0;\n"
            "}"
        ),
        "options": [
            "Erro de compilação porque os campos estão fora de ordem.",
            "Erro de compilação porque .idade não foi inicializado.",
            "Ana 0 9.0",
            "Ana <lixo> 9.0 (comportamento indefinido em a.idade)",
            "9.0 Ana 0"
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: inicialização designada (.campo = valor) permite qualquer ordem desde C99.",
            "Errado: campos omitidos em inicializadores são permitidos.",
            "Correto: na inicialização parcial de structs, todo membro omitido é automaticamente zerado (0 para int).",
            "Errado: só fica lixo se NÃO houver inicializador nenhum ('Aluno a;').",
            "Errado: a ordem dos argumentos no printf imprime nome, idade, nota."
        ],
        "steps": [
            "Inicialização designada ({.nota = 9.0f, .nome = \"Ana\"}) associa valores pelo nome do campo.",
            "O campo .idade omitido recebe 0 garantido pelo padrão C99."
        ],
        "gabaritoResumo": "Na inicialização designada, a ordem é livre e campos omitidos são zerados.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { char nome[12]; int idade; float nota; } Aluno;\n"
            "int main(void) {\n"
            "    Aluno a = {.nota = 9.0f, .nome = \"Ana\"};\n"
            "    printf(\"%s %d %.1f\\n\", a.nome, a.idade, a.nota);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-8",
        "category": "structs",
        "subtopic": "2.6 Leitura e Limpeza de Buffer",
        "level": "Intermediário",
        "title": "Bug do '\\n' entre scanf e fgets",
        "stem": (
            "Um aluno lê o código numérico de um produto com scanf(\"%d\", &p.cod); e, "
            "na linha seguinte, chama fgets(p.nome, 30, stdin);, mas o programa pula a leitura do nome. "
            "Qual é a causa e a correção portável em C padrão?"
        ),
        "code": "",
        "options": [
            "fgets não aceita membros de struct; deve-se usar gets(p.nome).",
            "scanf deixou '\\n' no buffer stdin; deve-se consumir até '\\n' com while ((c = getchar()) != '\\n' && c != EOF) {}.",
            "Deve-se usar fflush(stdin), que é garantido pelo padrão ISO C em todos os sistemas.",
            "scanf consome o '\\n', mas fgets precisa de &p.nome em vez de p.nome.",
            "O tamanho 30 é pequeno demais para stdin; basta trocar por sizeof(int)."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: fgets aceita qualquer char *, inclusive campos de struct; gets foi removida em C11 por insegurança.",
            "Correto: scanf(\"%d\") deixa o Enter ('\\n') em stdin; limpar com getchar() em laço é portável e seguro.",
            "Errado: fflush(stdin) tem comportamento indefinido no padrão ISO C (falha no Linux/GCC).",
            "Errado: p.nome já decai para char *; &p.nome teria tipo char (*)[30].",
            "Errado: o problema é o caractere residual no buffer, não o tamanho do buffer."
        ],
        "steps": [
            "scanf(\"%d\") para de ler ao encontrar o '\\n', deixando-o em stdin.",
            "A solução portável consome caracteres até '\\n' ou EOF usando getchar() antes de chamar fgets()."
        ],
        "gabaritoResumo": "Consuma o '\\n' residual com laço getchar() antes de fgets(); evite gets() e fflush(stdin).",
        "solutionCode": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "void limpa_buf(void) { int c; while ((c = getchar()) != '\\n' && c != EOF) {} }\n"
            "typedef struct { int cod; char nome[30]; } Prod;\n"
            "int main(void) {\n"
            "    Prod p;\n"
            "    if (scanf(\"%d\", &p.cod) == 1) {\n"
            "        limpa_buf();\n"
            "        fgets(p.nome, sizeof(p.nome), stdin);\n"
            "        p.nome[strcspn(p.nome, \"\\n\")] = '\\0';\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-9",
        "category": "structs",
        "subtopic": "2.6 Leitura e Limpeza de Buffer",
        "level": "Básico",
        "title": "Removendo o '\\n' capturado por fgets",
        "stem": (
            "Ao ler 'p.nome' com fgets(p.nome, sizeof(p.nome), stdin), qual linha remove com "
            "segurança o eventual '\\n' ao final da string?"
        ),
        "code": "",
        "options": [
            "p.nome[strlen(p.nome)] = '\\0';",
            "p.nome[strcspn(p.nome, \"\\n\")] = '\\0';",
            "strcpy(p.nome, \"\\n\");",
            "p.nome[0] = '\\0';",
            "strcmp(p.nome, \"\\n\");"
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: strlen(p.nome) aponta para onde já está o '\\0', não para o '\\n'.",
            "Correto: strcspn retorna o índice do primeiro '\\n' (ou do '\\0' se não houver '\\n'), zerando-o sem risco de índice negativo.",
            "Errado: substituiria o nome inteiro por \"\\n\".",
            "Errado: apagaria a string inteira deixando-a vazia.",
            "Errado: strcmp apenas compara e não altera a string."
        ],
        "steps": [
            "strcspn(s, \"\\n\") devolve a quantidade de caracteres antes do primeiro '\\n' (ou o tamanho total se não houver '\\n').",
            "Escrever '\\0' nessa posição remove o '\\n' sem acessar posição -1 mesmo quando a entrada foi truncada."
        ],
        "gabaritoResumo": "p.nome[strcspn(p.nome, \"\\n\")] = '\\0'; é o idioma mais seguro para remover '\\n'.",
        "solutionCode": (
            "#include <string.h>\n"
            "void tira_newline(char *s) {\n"
            "    s[strcspn(s, \"\\n\")] = '\\0';\n"
            "}"
        )
    },
    {
        "id": "q-strc-10",
        "category": "structs",
        "subtopic": "2.7 Atribuição Direta e Cópia Rasa",
        "level": "Intermediário",
        "title": "Atribuição b = a entre structs com vetor fixo",
        "stem": (
            "O que imprime o código abaixo?"
        ),
        "code": (
            "#include <stdio.h>\n"
            "typedef struct { int id; char tag[8]; } Item;\n"
            "int main(void) {\n"
            "    Item a = {1, \"ABC\"}, b;\n"
            "    b = a;\n"
            "    b.tag[0] = 'Z';\n"
            "    printf(\"%s %s\\n\", a.tag, b.tag);\n"
            "    return 0;\n"
            "}"
        ),
        "options": [
            "Erro de compilação: structs não aceitam o operador '='.",
            "ZBC ZBC",
            "ABC ZBC",
            "ABC ABC",
            "Erro de compilação: arrays dentro de struct não podem ser copiados com '='."
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: C permite atribuir duas structs do mesmo tipo com '='.",
            "Errado: isso aconteceria se 'tag' fosse char * (ponteiro), não char tag[8] (array embutido).",
            "Correto: b = a copia todos os bytes de 'a' para 'b', incluindo os 8 chars de tag; editar b.tag não afeta a.tag.",
            "Errado: b.tag[0] foi alterado para 'Z'.",
            "Errado: arrays soltos não aceitam '=', mas arrays encapsulados em uma struct são copiados junto com ela."
        ],
        "steps": [
            "tag[8] está embutida dentro da struct Item.",
            "b = a copia os bytes completos de a para b em memória separada.",
            "Alterar b.tag[0] muda apenas b, mantendo a.tag = \"ABC\"."
        ],
        "gabaritoResumo": "b = a copia arrays fixos internos por valor; a e b ficam independentes.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { int id; char tag[8]; } Item;\n"
            "int main(void) {\n"
            "    Item a = {1, \"ABC\"}, b = a;\n"
            "    b.tag[0] = 'Z';\n"
            "    printf(\"%s %s\\n\", a.tag, b.tag);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-11",
        "category": "structs",
        "subtopic": "2.7 Atribuição Direta e Cópia Rasa",
        "level": "Avançado",
        "title": "Risco de cópia rasa (shallow copy) com ponteiros internos",
        "stem": (
            "Considere 'typedef struct { char *nome; int tam; } Texto;'. Se 't1.nome' foi "
            "alocado com malloc e executamos 'Texto t2 = t1;', qual afirmação é VERDADEIRA?"
        ),
        "code": "",
        "options": [
            "t2.nome recebe automaticamente um novo bloco via malloc implícito.",
            "t1.nome e t2.nome apontam para o mesmo endereço no heap; dar free nos dois causa double free.",
            "t2 = t1 não compila quando a struct possui ponteiros.",
            "Alterar t2.nome[0] nunca afeta t1.nome[0].",
            "fwrite(&t1, sizeof(t1), 1, fp) grava o texto completo de t1.nome no arquivo."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: C nunca faz alocação implícita em atribuição de struct.",
            "Correto: '=' faz cópia rasa (copia o valor do endereço armazenado no ponteiro), gerando aliasing e risco de double free.",
            "Errado: compila normalmente, o que pode esconder o bug.",
            "Errado: como ambos apontam para o mesmo buffer, alterar via t2 afeta t1.",
            "Errado: fwrite gravaria apenas o endereço de memória do ponteiro, não os caracteres."
        ],
        "steps": [
            "t2 = t1 copia campo a campo: copia o ponteiro t1.nome (o endereço), não os dados apontados.",
            "Portanto t1.nome == t2.nome; liberar ambos gera double free."
        ],
        "gabaritoResumo": "Atribuir structs com ponteiros faz cópia rasa (mesmo endereço no heap).",
        "solutionCode": (
            "#include <stdlib.h>\n"
            "#include <string.h>\n"
            "typedef struct { char *nome; int tam; } Texto;\n"
            "Texto deep_copy(const Texto *orig) {\n"
            "    Texto novo;\n"
            "    novo.tam = orig->tam;\n"
            "    novo.nome = malloc((size_t)novo.tam + 1);\n"
            "    if (novo.nome) strcpy(novo.nome, orig->nome);\n"
            "    return novo;\n"
            "}"
        )
    },
    {
        "id": "q-strc-12",
        "category": "structs",
        "subtopic": "2.8 Vetores de Structs",
        "level": "Básico",
        "title": "Acesso a membro de vetor de structs",
        "stem": (
            "Dado 'struct Banda { char nome[30]; int integrantes; } fav[5];' (Ex. 25–26 do PDF), "
            "como imprimir a quantidade de integrantes da terceira banda (índice 2)?"
        ),
        "code": "",
        "options": [
            "printf(\"%d\", fav.integrantes[2]);",
            "printf(\"%d\", fav[2]->integrantes);",
            "printf(\"%d\", fav[2].integrantes);",
            "printf(\"%d\", (*fav[2]).integrantes);",
            "printf(\"%d\", fav[3].integrantes);"
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: o índice vai no vetor 'fav[2]', não no campo 'integrantes'.",
            "Errado: fav[2] é uma struct Banda por valor, não um ponteiro; usa-se '.'.",
            "Correto: fav[2] seleciona o 3º elemento (índice 2) e '.integrantes' acessa o membro.",
            "Errado: fav[2] não é ponteiro, logo *fav[2] não compila.",
            "Errado: índice 3 é a quarta banda (0, 1, 2, 3)."
        ],
        "steps": [
            "Em C os índices iniciam em 0, logo a 3ª banda está em fav[2].",
            "fav[2] tem tipo struct Banda (valor), exigindo operador ponto '.'."
        ],
        "gabaritoResumo": "Em vetores de structs, indexe primeiro e use ponto: vetor[i].campo.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "struct Banda { char nome[30]; int integrantes; };\n"
            "void mostra_terceira(const struct Banda fav[5]) {\n"
            "    printf(\"%d\\n\", fav[2].integrantes);\n"
            "}"
        )
    },
    {
        "id": "q-strc-13",
        "category": "structs",
        "subtopic": "2.9 Operações sobre Vetores",
        "level": "Intermediário",
        "title": "Ordenação de vetor de structs por média",
        "stem": (
            "Para ordenar um vetor 'Aluno turma[MAX]' em ordem DECRESCENTE de média (Ex. 44 do PDF) "
            "usando Bubble Sort, qual condição e troca preservam a integridade dos registros?"
        ),
        "code": "",
        "options": [
            "Trocar apenas turma[j].media com turma[j+1].media quando turma[j].media < turma[j+1].media.",
            "Trocar a struct inteira usando 'Aluno tmp = turma[j]; turma[j] = turma[j+1]; turma[j+1] = tmp;' quando turma[j].media < turma[j+1].media.",
            "Comparar turma[j] < turma[j+1] diretamente e trocar os ponteiros.",
            "Trocar a struct inteira quando strcmp(turma[j].nome, turma[j+1].nome) > 0.",
            "Usar qsort sem função de comparação."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: trocar apenas a média desvincula a nota do nome/matrícula do aluno!",
            "Correto: para ordem decrescente, se o anterior for menor (<) que o próximo, trocamos toda a struct via tmp.",
            "Errado: C não define operador '<' entre structs.",
            "Errado: isso ordenaria por nome (alfabética crescente), não por média decrescente.",
            "Errado: qsort exige ponteiro para função comparadora."
        ],
        "steps": [
            "Ordem decrescente coloca maiores médias primeiro: troca se turma[j].media < turma[j+1].media.",
            "A troca deve mover todos os campos juntos (tmp = turma[j]; ...)."
        ],
        "gabaritoResumo": "Na ordenação de structs, compare o campo-chave mas troque a struct inteira.",
        "solutionCode": (
            "typedef struct { char nome[30]; float media; } Aluno;\n"
            "void ordena_desc(Aluno v[], int n) {\n"
            "    for (int i = 0; i < n - 1; i++)\n"
            "        for (int j = 0; j < n - 1 - i; j++)\n"
            "            if (v[j].media < v[j + 1].media) {\n"
            "                Aluno tmp = v[j]; v[j] = v[j + 1]; v[j + 1] = tmp;\n"
            "            }\n"
            "}"
        )
    },
    {
        "id": "q-strc-14",
        "category": "structs",
        "subtopic": "2.9 Operações sobre Vetores",
        "level": "Intermediário",
        "title": "Busca por título de livro em vetor de structs",
        "stem": (
            "No Ex. 13 do PDF, cada livro possui 'char titulo[31];'. Para verificar se 'acervo[i]' "
            "tem o título buscado em 'char busca[31]', qual condição é correta?"
        ),
        "code": "",
        "options": [
            "if (acervo[i].titulo == busca)",
            "if (strcmp(acervo[i].titulo, busca) == 0)",
            "if (strcmp(acervo[i].titulo, busca) == 1)",
            "if (strcpy(acervo[i].titulo, busca))",
            "if (acervo[i] == busca)"
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: compara os endereços dos dois arrays em memória, sempre dando falso.",
            "Correto: strcmp retorna 0 exatamente quando as duas strings têm conteúdo idêntico.",
            "Errado: retorno positivo indica que a primeira string é lexicograficamente maior, não igual.",
            "Errado: strcpy sobrescreve o título do livro com o texto buscado!",
            "Errado: tipos incompatíveis (struct Livro vs char *)."
        ],
        "steps": [
            "Strings em C são comparadas caractere a caractere por strcmp (ou strncmp).",
            "Igualdade exata corresponde ao retorno 0."
        ],
        "gabaritoResumo": "Sempre use strcmp(s1, s2) == 0 para igualdade de strings em structs.",
        "solutionCode": (
            "#include <string.h>\n"
            "typedef struct { char titulo[31]; int ano; } Livro;\n"
            "int acha_livro(const Livro v[], int n, const char *busca) {\n"
            "    for (int i = 0; i < n; i++)\n"
            "        if (strcmp(v[i].titulo, busca) == 0) return i;\n"
            "    return -1;\n"
            "}"
        )
    },
    {
        "id": "q-strc-15",
        "category": "structs",
        "subtopic": "2.10 Structs e Funções",
        "level": "Intermediário",
        "title": "Passagem por valor vs referência em C",
        "stem": (
            "Qual será a saída do programa abaixo?"
        ),
        "code": (
            "#include <stdio.h>\n"
            "typedef struct { int x, y; } Ponto;\n"
            "void f1(Ponto p)  { p.x += 10; }\n"
            "void f2(Ponto *p) { p->y += 10; }\n"
            "int main(void) {\n"
            "    Ponto pt = {1, 2};\n"
            "    f1(pt);\n"
            "    f2(&pt);\n"
            "    printf(\"%d %d\\n\", pt.x, pt.y);\n"
            "    return 0;\n"
            "}"
        ),
        "options": [
            "11 12",
            "1 2",
            "1 12",
            "11 2",
            "Erro de compilação: structs sempre decaem para ponteiros como arrays."
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: f1 recebeu uma cópia, logo pt.x não muda.",
            "Errado: f2 recebeu &pt e alterou pt.y.",
            "Correto: f1 altera só a cópia local (pt.x segue 1); f2 usa ponteiro e altera pt.y para 12.",
            "Errado: o efeito está invertido.",
            "Errado: structs NÃO decaem para ponteiros — são passadas por valor."
        ],
        "steps": [
            "f1(pt) recebe uma cópia da struct Ponto; p.x += 10 não afeta pt.x.",
            "f2(&pt) recebe o endereço de pt; p->y += 10 modifica pt.y de 2 para 12."
        ],
        "gabaritoResumo": "Structs vão por valor por padrão; use ponteiro (*) para modificar a struct original.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { int x, y; } Ponto;\n"
            "void f1(Ponto p) { p.x += 10; }\n"
            "void f2(Ponto *p) { p->y += 10; }\n"
            "int main(void) {\n"
            "    Ponto pt = {1, 2}; f1(pt); f2(&pt);\n"
            "    printf(\"%d %d\\n\", pt.x, pt.y);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-16",
        "category": "structs",
        "subtopic": "2.10 Structs e Funções",
        "level": "Intermediário",
        "title": "Retorno de struct em funções",
        "stem": (
            "No Ex. 54 do PDF, queremos escrever uma função 'soma' que recebe duas frações "
            "(FRACAO a, FRACAO b) e devolve a fração resultante. Qual assinatura e retorno estão corretos em C?"
        ),
        "code": (
            "typedef struct { int num, den; } FRACAO;"
        ),
        "options": [
            "FRACAO *soma(FRACAO a, FRACAO b) { FRACAO r = {0, 1}; return &r; }",
            "FRACAO soma(FRACAO a, FRACAO b) { FRACAO r = {a.num*b.den + b.num*a.den, a.den*b.den}; return r; }",
            "void soma(FRACAO a, FRACAO b) { a.num += b.num; }",
            "FRACAO soma(FRACAO a, FRACAO b) { return {a.num, b.den}; }",
            "Não é possível retornar struct em C; deve-se retornar void sempre."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: retorna o endereço de uma variável local 'r' que será destruída ao sair da função (dangling pointer!).",
            "Correto: retornar uma struct por valor copia seus campos para o chamador com total segurança.",
            "Errado: void não devolve nada e altera apenas a cópia local 'a'.",
            "Errado: 'return { ... };' sem cast composto '(FRACAO){...}' não é válido em C.",
            "Errado: C permite retornar structs por valor perfeitamente."
        ],
        "steps": [
            "Retornar ponteiro para variável local (&r) é erro grave (dangling pointer).",
            "Retornar FRACAO por valor devolve os dois inteiros empacotados de forma segura."
        ],
        "gabaritoResumo": "Funções em C podem retornar structs por valor; nunca retorne &variavel_local.",
        "solutionCode": (
            "typedef struct { int num, den; } FRACAO;\n"
            "FRACAO soma(FRACAO a, FRACAO b) {\n"
            "    FRACAO r = {a.num * b.den + b.num * a.den, a.den * b.den};\n"
            "    return r;\n"
            "}"
        )
    },
    {
        "id": "q-strc-17",
        "category": "structs",
        "subtopic": "2.11 Structs Aninhadas",
        "level": "Intermediário",
        "title": "Acesso misto (-> e .) em structs aninhadas",
        "stem": (
            "Considere as structs abaixo (baseadas no Ex. 15 e 40 do PDF). Dado 'Pessoa *pp = &p;', "
            "como acessar o ano de nascimento de 'p' através de 'pp'?"
        ),
        "code": (
            "typedef struct { int dia, mes, ano; } Data;\n"
            "typedef struct { char nome[30]; Data nasc; } Pessoa;"
        ),
        "options": [
            "pp->nasc->ano",
            "pp.nasc.ano",
            "pp->nasc.ano",
            "(*pp)->nasc.ano",
            "pp.nasc->ano"
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: nasc é uma struct Data embutida por valor, não um ponteiro; logo não aceita '->'.",
            "Errado: pp é ponteiro para Pessoa, exigindo '->' no primeiro nível.",
            "Correto: pp é ponteiro (->), e pp->nasc é struct Data por valor (.).",
            "Errado: *pp é Pessoa por valor, não ponteiro.",
            "Errado: inverte os operadores nos dois níveis."
        ],
        "steps": [
            "Nível 1: pp tem tipo 'Pessoa *' -> use '->' para chegar a nasc.",
            "Nível 2: pp->nasc tem tipo 'Data' (não ponteiro) -> use '.' para chegar a ano."
        ],
        "gabaritoResumo": "Seta '->' só onde há ponteiro; ponto '.' onde há struct por valor: pp->nasc.ano.",
        "solutionCode": (
            "typedef struct { int dia, mes, ano; } Data;\n"
            "typedef struct { char nome[30]; Data nasc; } Pessoa;\n"
            "int ano_nasc(const Pessoa *pp) {\n"
            "    return pp->nasc.ano;\n"
            "}"
        )
    },
    {
        "id": "q-strc-18",
        "category": "structs",
        "subtopic": "2.11 Structs Aninhadas",
        "level": "Básico",
        "title": "Ordem de declaração de structs aninhadas",
        "stem": (
            "Por que o código abaixo falha ao compilar?"
        ),
        "code": (
            "typedef struct {\n"
            "    Ponto supEsq;\n"
            "    Ponto infDir;\n"
            "} Retangulo;\n"
            "\n"
            "typedef struct { int x, y; } Ponto;"
        ),
        "options": [
            "Porque não é possível ter duas structs do mesmo tipo dentro de Retangulo.",
            "Porque Ponto foi usada dentro de Retangulo antes de ser declarada.",
            "Porque supEsq e infDir precisam ser ponteiros.",
            "Porque faltou #include <stdio.h>.",
            "Porque typedef não funciona com structs aninhadas."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: uma struct pode conter quantos membros de outro tipo struct desejar (Ex. 52 do PDF).",
            "Correto: o compilador C lê de cima para baixo e precisa conhecer o tamanho de Ponto ao definir Retangulo.",
            "Errado: membros por valor funcionam perfeitamente desde que Ponto seja definida antes.",
            "Errado: stdio.h não é necessário para declarar tipos sem I/O.",
            "Errado: typedef funciona normalmente para composição."
        ],
        "steps": [
            "O compilador processa o arquivo sequencialmente (top-down).",
            "Ao encontrar 'Ponto supEsq;' na linha 2, 'Ponto' ainda é um identificador desconhecido."
        ],
        "gabaritoResumo": "Structs internas devem ser declaradas antes da struct que as contém por valor.",
        "solutionCode": (
            "typedef struct { int x, y; } Ponto;\n"
            "typedef struct {\n"
            "    Ponto supEsq;\n"
            "    Ponto infDir;\n"
            "} Retangulo;"
        )
    },
    {
        "id": "q-strc-19",
        "category": "structs",
        "subtopic": "2.12 Structs com Vetores e Strings",
        "level": "Básico",
        "title": "Tamanho de buffer char para string de N letras",
        "stem": (
            "O Ex. 12 do PDF pede um campo 'marca (máximo 15 letras)' na struct Carro. "
            "Qual declaração em C evita estouro de buffer (buffer overflow) ao armazenar exatamente 15 letras?"
        ),
        "code": "",
        "options": [
            "char marca[14];",
            "char marca[15];",
            "char marca[16];",
            "char marca;",
            "int marca[15];"
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: caberiam no máximo 13 letras + '\\0'.",
            "Errado: 15 letras + '\\0' exigem 16 bytes; com 15 ocorreria escrita fora dos limites no '\\0'.",
            "Correto: 15 bytes para as letras + 1 byte obrigatório para o terminador nulo '\\0'.",
            "Errado: armazena apenas 1 caractere.",
            "Errado: vetor de int não é string C padrão."
        ],
        "steps": [
            "Toda string em C termina com o caractere nulo '\\0'.",
            "Para N caracteres úteis, o array precisa de pelo menos N + 1 bytes."
        ],
        "gabaritoResumo": "Para guardar até N caracteres em uma string C, declare char campo[N + 1].",
        "solutionCode": (
            "typedef struct {\n"
            "    char marca[16]; /* 15 letras + '\\0' */\n"
            "    int ano;\n"
            "    float preco;\n"
            "} Carro;"
        )
    },
    {
        "id": "q-strc-20",
        "category": "structs",
        "subtopic": "2.12 Structs com Vetores e Strings",
        "level": "Intermediário",
        "title": "Erro de atribuição direta em membro char[]",
        "stem": (
            "No código abaixo, qual linha provoca erro de compilação?"
        ),
        "code": (
            "#include <string.h>\n"
            "typedef struct { int mat; char curso[20]; } Aluno;\n"
            "int main(void) {\n"
            "    Aluno a;\n"
            "    a.mat = 10;\n"
            "    a.curso = \"ADS\";\n"
            "    return 0;\n"
            "}"
        ),
        "options": [
            "Linha 2: char curso[20] não pode estar junto de int mat.",
            "Linha 4: Aluno a não foi inicializado.",
            "Linha 5: a.mat não aceita o operador '='.",
            "Linha 6: a.curso é um array não modificável por '=', exigindo strcpy(a.curso, \"ADS\").",
            "Nenhuma linha: o código compila sem erros."
        ],
        "correct": 3,
        "optionExplanations": [
            "Errado: declaração perfeitamente válida.",
            "Errado: declarar sem inicializar é válido (apenas contém lixo até ser preenchido).",
            "Errado: tipos escalares como int aceitam '=' normalmente.",
            "Correto: em C não se atribui strings a arrays com '=' após a declaração; use strcpy/snprintf.",
            "Errado: 'assignment to expression with array type' é erro garantido."
        ],
        "steps": [
            "Identifique que a.curso tem tipo 'char [20]' (array).",
            "Arrays em C não são lvalues modificáveis; a cópia de conteúdo exige strcpy ou strncpy."
        ],
        "gabaritoResumo": "Nunca use '=' para copiar texto para dentro de char campo[]; use strcpy/snprintf.",
        "solutionCode": (
            "#include <string.h>\n"
            "typedef struct { int mat; char curso[20]; } Aluno;\n"
            "int main(void) {\n"
            "    Aluno a;\n"
            "    a.mat = 10;\n"
            "    strcpy(a.curso, \"ADS\");\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-21",
        "category": "structs",
        "subtopic": "2.13 Ponteiros Internos e Deep Free",
        "level": "Avançado",
        "title": "Ordem correta de liberação (Deep Free) em structs aninhadas no heap",
        "stem": (
            "No Ex. 20 do PDF, cada Diretor possui um vetor dinâmico 'Filme *filmes;' alocado após "
            "ler 'qtd'. Se o vetor 'Diretor *dirs' também foi alocado com malloc, qual a ordem "
            "correta para liberar toda a memória sem vazamentos nem use-after-free?"
        ),
        "code": (
            "typedef struct { char nome[20]; int ano; } Filme;\n"
            "typedef struct { char nome[21]; int qtd; Filme *filmes; } Diretor;"
        ),
        "options": [
            "free(dirs); seguido de for (i=0; i<n; i++) free(dirs[i].filmes);",
            "for (i=0; i<n; i++) free(dirs[i].filmes); seguido de free(dirs);",
            "Apenas free(dirs); já libera automaticamente dirs[i].filmes.",
            "free(dirs->filmes); sem laço for.",
            "Não é necessário liberar dirs[i].filmes porque Filme não tem ponteiros."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: após free(dirs), acessar dirs[i].filmes é use-after-free (memória já liberada).",
            "Correto: libera-se de dentro para fora — primeiro os vetores internos de cada diretor, depois o vetor dirs.",
            "Errado: C não possui coletor de lixo nem destrutores automáticos; free(dirs) vazaria todos os vetores filmes.",
            "Errado: liberaria apenas os filmes de dirs[0], vazando de dirs[1..n-1].",
            "Errado: todo bloco obtido com malloc exige seu próprio free."
        ],
        "steps": [
            "Se liberar 'dirs' primeiro, perdemos acesso seguro aos ponteiros 'dirs[i].filmes'.",
            "Logo, percorra 0..n-1 liberando dirs[i].filmes e só depois execute free(dirs)."
        ],
        "gabaritoResumo": "Deep free sempre ocorre de dentro para fora: filhos primeiro, estrutura pai por último.",
        "solutionCode": (
            "#include <stdlib.h>\n"
            "typedef struct { char nome[20]; int ano; } Filme;\n"
            "typedef struct { char nome[21]; int qtd; Filme *filmes; } Diretor;\n"
            "void libera_diretores(Diretor *dirs, int n) {\n"
            "    for (int i = 0; i < n; i++) free(dirs[i].filmes);\n"
            "    free(dirs);\n"
            "}"
        )
    },
    {
        "id": "q-strc-22",
        "category": "structs",
        "subtopic": "2.14 Alocação Dinâmica e Função cria",
        "level": "Intermediário",
        "title": "Alocação de struct única com malloc(sizeof(...))",
        "stem": (
            "Na implementação de 'struct produto* cria(int cod, const char *nome, int quant, float preco)' "
            "(Ex. 35 do PDF), qual linha aloca corretamente a memória no heap?"
        ),
        "code": "",
        "options": [
            "struct produto *p = malloc(sizeof(struct produto *));",
            "struct produto *p = malloc(sizeof(*p));",
            "struct produto p = malloc(sizeof(struct produto));",
            "struct produto *p = calloc(0, sizeof(struct produto));",
            "struct produto *p = &((struct produto){cod, \"\", quant, preco});"
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: sizeof(struct produto *) mede o tamanho de um ponteiro (8 bytes), insuficiente para a struct inteira!",
            "Correto: sizeof(*p) mede exatamente sizeof(struct produto) e acompanha mudanças futuras no tipo de p.",
            "Errado: tenta guardar o ponteiro retornado por malloc em uma struct por valor.",
            "Errado: calloc(0, ...) aloca 0 elementos.",
            "Errado: compound literal dentro da função cria tem duração automática e morre ao retornar."
        ],
        "steps": [
            "Precisamos alocar espaço para o objeto apontado (*p), não para o ponteiro.",
            "malloc(sizeof(*p)) é o idioma recomendado e à prova de erros."
        ],
        "gabaritoResumo": "Para alocar uma struct no heap, use malloc(sizeof(*p)) e verifique != NULL.",
        "solutionCode": (
            "#include <stdlib.h>\n"
            "#include <string.h>\n"
            "struct produto { int codigo; char nome[51]; int quantidade; float preco; };\n"
            "struct produto *cria(int cod, const char *nome, int quant, float preco) {\n"
            "    struct produto *p = malloc(sizeof(*p));\n"
            "    if (!p) return NULL;\n"
            "    p->codigo = cod; p->quantidade = quant; p->preco = preco;\n"
            "    strncpy(p->nome, nome, 50); p->nome[50] = '\\0';\n"
            "    return p;\n"
            "}"
        )
    },
    {
        "id": "q-strc-23",
        "category": "structs",
        "subtopic": "2.15 union",
        "level": "Intermediário",
        "title": "Tamanho em memória: struct vs union",
        "stem": (
            "Em uma arquitetura onde int tem 4 bytes, double tem 8 bytes e char[10] tem 10 bytes "
            "(alinhamento máximo 8), qual é a diferença conceitual entre declarar os 3 campos "
            "dentro de uma struct versus dentro de uma union?"
        ),
        "code": (
            "struct S { int a; double b; char c[10]; };\n"
            "union  U { int a; double b; char c[10]; };"
        ),
        "options": [
            "struct S e union U têm sempre exatamente o mesmo sizeof.",
            "union U tem tamanho pelo menos igual à soma 4 + 8 + 10 = 22 bytes.",
            "Na union U todos os membros iniciam no mesmo endereço, e seu tamanho é o do maior membro alinhado (16 bytes), enquanto struct S soma os campos com padding (32 bytes).",
            "Na union U é possível ler a, b e c simultaneamente sem que um sobrescreva o outro.",
            "struct S só pode armazenar um membro por vez."
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: struct separa os campos sequencialmente; union os sobrepõe.",
            "Errado: somar tamanhos ocorre na struct, não na union.",
            "Correto: union ocupa max(membros) arredondado ao alinhamento (10 alinhado a 8 -> 16 B); struct soma 4 + 4(pad) + 8 + 10 + 6(pad) = 32 B.",
            "Errado: escrever em um membro da union sobrescreve os bytes dos demais.",
            "Errado: struct armazena todos os membros simultaneamente."
        ],
        "steps": [
            "Em union U, o maior membro é char c[10] (10 bytes), arredondado para múltiplo do alinhamento 8 -> 16 bytes.",
            "Em struct S, int(4) + pad(4) + double(8) + char[10](10) + pad(6) = 32 bytes."
        ],
        "gabaritoResumo": "struct soma todos os campos (+ padding); union compartilha memória e mede o maior membro alinhado.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "struct S { int a; double b; char c[10]; };\n"
            "union  U { int a; double b; char c[10]; };\n"
            "int main(void) {\n"
            "    printf(\"struct=%zu union=%zu\\n\", sizeof(struct S), sizeof(union U));\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-24",
        "category": "structs",
        "subtopic": "2.15 union",
        "level": "Avançado",
        "title": "Tagged Union no cadastro de contratos (Ex. 34 do PDF)",
        "stem": (
            "No Ex. 34 do PDF, um plano de saúde tem Contrato Individual ou Coletivo armazenados "
            "em uma union. Por que devemos incluir um campo 'char tipo' ('I' ou 'C') na struct "
            "que envolve essa union?"
        ),
        "code": "",
        "options": [
            "Porque o compilador C proíbe declarar union sem um campo char.",
            "Porque a union em si não guarda qual dos seus membros foi gravado por último; sem a tag, ler o ramo errado interpreta bytes inválidos.",
            "Para dobrar o tamanho da union na memória.",
            "Para permitir que Contrato Individual e Coletivo sejam usados ao mesmo tempo.",
            "Para dispensar o uso de typedef."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: unions avulsas são permitidas, porém inseguras quando não sabemos o tipo ativo.",
            "Correto: a union não tem metadados em tempo de execução; a tag ('I'/'C') garante que o código leia o campo correto.",
            "Errado: a intenção é economizar RAM mantendo segurança.",
            "Errado: uma union continua armazenando apenas uma variante por vez.",
            "Errado: não tem relação com typedef."
        ],
        "steps": [
            "Como os membros de uma union ocupam os mesmos bytes, não há como saber qual variante está ativa olhando apenas para os dados.",
            "O padrão Tagged Union (struct com discriminador + union) resolve isso de forma segura."
        ],
        "gabaritoResumo": "Tagged union = struct { tag; union { ... }; } para saber qual membro da union é válido.",
        "solutionCode": (
            "typedef struct {\n"
            "    char tipo; /* 'I' ou 'C' */\n"
            "    union {\n"
            "        struct { int num; float renda; } ind;\n"
            "        struct { int num; int empMasc; } col;\n"
            "    } dados;\n"
            "} Contrato;"
        )
    },
    {
        "id": "q-strc-25",
        "category": "structs",
        "subtopic": "2.16 enum",
        "level": "Básico",
        "title": "Valores numéricos atribuídos pelo enum",
        "stem": (
            "Qual é o valor de cada constante no enum abaixo (baseado no Ex. 33 do PDF)?"
        ),
        "code": (
            "typedef enum {\n"
            "    NATACAO = 1,\n"
            "    HIDRO,\n"
            "    DANCA = 5,\n"
            "    KUNG_FU,\n"
            "    VIOLAO\n"
            "} Atividade;"
        ),
        "options": [
            "NATACAO=0, HIDRO=1, DANCA=5, KUNG_FU=6, VIOLAO=7",
            "NATACAO=1, HIDRO=2, DANCA=5, KUNG_FU=6, VIOLAO=7",
            "NATACAO=1, HIDRO=2, DANCA=3, KUNG_FU=4, VIOLAO=5",
            "NATACAO=1, HIDRO=3, DANCA=5, KUNG_FU=7, VIOLAO=9",
            "Erro de compilação: não é permitido pular números dentro de um enum."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: NATACAO foi explicitamente fixada em 1.",
            "Correto: cada item sem valor explícito assume o valor do anterior + 1 (1, 2, depois pula para 5, 6, 7).",
            "Errado: DANCA recebeu '= 5' explicitamente.",
            "Errado: o incremento padrão é +1, não +2.",
            "Errado: C permite atribuir valores explícitos em qualquer ponto do enum."
        ],
        "steps": [
            "NATACAO = 1 -> próximo sem valor (HIDRO) = 2.",
            "DANCA = 5 -> próximos (KUNG_FU, VIOLAO) = 6 e 7."
        ],
        "gabaritoResumo": "Em enum, cada constante sem valor explícito vale a anterior + 1.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef enum { NATACAO = 1, HIDRO, DANCA = 5, KUNG_FU, VIOLAO } Atividade;\n"
            "int main(void) {\n"
            "    printf(\"%d %d %d\\n\", HIDRO, KUNG_FU, VIOLAO); /* 2 6 7 */\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-26",
        "category": "structs",
        "subtopic": "2.16 enum",
        "level": "Intermediário",
        "title": "Impressão e uso de enum em structs",
        "stem": (
            "Um estudante definiu 'typedef enum { MANHA = 1, TARDE, NOITE } Turno;' e declarou "
            "'Turno t = TARDE;'. O que acontece ao executar 'printf(\"%s\", t);'?"
        ),
        "code": "",
        "options": [
            "Imprime \"TARDE\" automaticamente na tela.",
            "Imprime \"2\".",
            "Comportamento indefinido / provável crash (Segmentation Fault), pois %s espera char * e t é um inteiro (2).",
            "Imprime \"MANHA\".",
            "Erro de compilação: enum não pode ser passado para printf."
        ],
        "correct": 2,
        "optionExplanations": [
            "Errado: C não guarda os nomes dos identificadores enum em tempo de execução.",
            "Errado: para imprimir 2, seria necessário usar %d, não %s.",
            "Correto: %s tenta interpretar o inteiro 2 como um endereço de memória (0x2), causando falha de segmentação.",
            "Errado: não imprime o nome simbólico.",
            "Errado: compila (com warning), mas falha na execução."
        ],
        "steps": [
            "Em C, valores enum são constantes inteiras (TARDE == 2).",
            "Use %d para o número ou uma tabela de strings const char *nomes[] para imprimir o texto."
        ],
        "gabaritoResumo": "Enum em C é inteiro em runtime; nunca passe enum para %s no printf.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef enum { MANHA = 1, TARDE, NOITE } Turno;\n"
            "int main(void) {\n"
            "    const char *nomes[] = {\"\", \"Manha\", \"Tarde\", \"Noite\"};\n"
            "    Turno t = TARDE;\n"
            "    printf(\"%d (%s)\\n\", t, nomes[t]);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-27",
        "category": "structs",
        "subtopic": "2.17 Alinhamento, Padding e sizeof",
        "level": "Avançado",
        "title": "Cálculo de sizeof com padding de alinhamento",
        "stem": (
            "Em uma plataforma de 64 bits onde sizeof(char)=1 e sizeof(int)=4 (alinhamento de int = 4), "
            "qual é o valor esperado de sizeof(struct A) e sizeof(struct B)?"
        ),
        "code": (
            "struct A { char c1; int x; char c2; };\n"
            "struct B { int x; char c1; char c2; };"
        ),
        "options": [
            "sizeof(A) = 6 e sizeof(B) = 6",
            "sizeof(A) = 12 e sizeof(B) = 8",
            "sizeof(A) = 8 e sizeof(B) = 12",
            "sizeof(A) = 9 e sizeof(B) = 6",
            "sizeof(A) = 16 e sizeof(B) = 16"
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: 6 é a soma bruta sem considerar o alinhamento exigido pelo int.",
            "Correto: A tem c1(1) + 3 pad + x(4) + c2(1) + 3 pad = 12 B; B tem x(4) + c1(1) + c2(1) + 2 pad = 8 B.",
            "Errado: os valores estão invertidos.",
            "Errado: o tamanho total de uma struct deve ser múltiplo do maior alinhamento (4).",
            "Errado: nenhum campo exige alinhamento de 8 ou 16 bytes."
        ],
        "steps": [
            "Em A: offset 0 = c1; x precisa de múltiplo de 4 -> pula 1..3 (3 pad), x ocupa 4..7; c2 em 8; tamanho total múltiplo de 4 -> 12.",
            "Em B: x em 0..3; c1 em 4; c2 em 5; próximo múltiplo de 4 -> 8."
        ],
        "gabaritoResumo": "Ordenar membros do maior para o menor reduz padding: struct A = 12 B, struct B = 8 B.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "struct A { char c1; int x; char c2; };\n"
            "struct B { int x; char c1; char c2; };\n"
            "int main(void) {\n"
            "    printf(\"A=%zu B=%zu\\n\", sizeof(struct A), sizeof(struct B));\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-28",
        "category": "structs",
        "subtopic": "2.17 Bit Fields",
        "level": "Avançado",
        "title": "Restrições de campos de bits (bit fields)",
        "stem": (
            "Sobre campos de bits em C (como 'unsigned int flag : 1;'), assinale a alternativa CORRETA."
        ),
        "code": (
            "typedef struct {\n"
            "    unsigned int ativo : 1;\n"
            "    unsigned int nivel : 3;\n"
            "} Status;"
        ),
        "options": [
            "É possível obter o ponteiro de um bit field fazendo '&st.ativo'.",
            "O campo 'nivel : 3' consegue armazenar valores inteiros sem sinal de 0 até 7.",
            "É possível declarar um vetor de bit fields como 'unsigned int flags[4] : 1;'.",
            "sizeof(st.ativo) retorna 1 bit.",
            "Bit fields aumentam o tamanho da struct em comparação a usar dois ints comuns."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: endereço em C é por byte; aplicar '&' em bit field é proibido pelo compilador.",
            "Correto: com 3 bits sem sinal, o intervalo é 0 a (2^3 - 1) = 0..7.",
            "Errado: C proíbe arrays de bit fields.",
            "Errado: sizeof também não pode ser aplicado a um bit field.",
            "Errado: o objetivo é compactar múltiplos campos em menos bytes."
        ],
        "steps": [
            "3 bits sem sinal comportam 2^3 = 8 combinações (0 a 7).",
            "Operadores '&' e 'sizeof' são proibidos diretamente em membros bit field."
        ],
        "gabaritoResumo": "k bits sem sinal guardam 0..(2^k - 1); bit fields não aceitam '&', 'sizeof' nem vetores.",
        "solutionCode": (
            "#include <stdio.h>\n"
            "typedef struct { unsigned int ativo : 1; unsigned int nivel : 3; } Status;\n"
            "int main(void) {\n"
            "    Status st = {1, 7};\n"
            "    printf(\"sizeof=%zu ativo=%u nivel=%u\\n\", sizeof(st), st.ativo, st.nivel);\n"
            "    return 0;\n"
            "}"
        )
    },
    {
        "id": "q-strc-29",
        "category": "structs",
        "subtopic": "2.18 Estruturas Autorreferenciadas",
        "level": "Intermediário",
        "title": "Por que struct No contém 'struct No *prox' e não 'struct No prox'",
        "stem": (
            "Ao definir um nó de lista encadeada, por que 'struct No prox;' dentro de "
            "'struct No' gera erro de compilação, enquanto 'struct No *prox;' funciona?"
        ),
        "code": (
            "struct No {\n"
            "    int dado;\n"
            "    struct No *prox; /* valido */\n"
            "};"
        ),
        "options": [
            "Porque structs em C não podem conter outras structs de forma alguma.",
            "Porque conter a si mesma por valor implicaria recursão infinita de tamanho; já um ponteiro tem tamanho fixo conhecido.",
            "Porque a palavra prox é reservada em C.",
            "Porque structs autorreferenciadas só existem se usarem union.",
            "Porque 'struct No *prox' aloca automaticamente o próximo nó com malloc."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: structs podem conter outras structs já definidas anteriormente.",
            "Correto: para calcular sizeof(struct No), o compilador precisa de tamanho finito; todo ponteiro tem tamanho fixo (4 ou 8 bytes).",
            "Errado: prox é apenas um nome comum de campo.",
            "Errado: não precisa de union.",
            "Errado: ponteiros não alocam memória automaticamente; começam com lixo ou NULL."
        ],
        "steps": [
            "Se struct No contivesse struct No por valor, seu tamanho seria sizeof(int) + sizeof(struct No) = infinito.",
            "Com struct No *prox, o tamanho do ponteiro já é conhecido (ex.: 8 bytes em 64 bits)."
        ],
        "gabaritoResumo": "Estruturas autorreferenciadas usam ponteiro para si mesmas porque ponteiros têm tamanho fixo.",
        "solutionCode": (
            "#include <stddef.h>\n"
            "typedef struct No {\n"
            "    int dado;\n"
            "    struct No *prox;\n"
            "} No;\n"
            "int main(void) { No n = {42, NULL}; return n.dado; }"
        )
    },
    {
        "id": "q-strc-30",
        "category": "structs",
        "subtopic": "2.18 Erros Comuns em Structs",
        "level": "Básico",
        "title": "Comparação direta de structs com ==",
        "stem": (
            "Por que 'if (d1 == d2)' falha ao compilar quando d1 e d2 são variáveis do tipo 'Data'?"
        ),
        "code": (
            "typedef struct { int dia, mes, ano; } Data;\n"
            "int iguais(Data d1, Data d2) {\n"
            "    return (d1 == d2); /* ERRO! */\n"
            "}"
        ),
        "options": [
            "Porque Data precisa de typedef struct Data.",
            "Porque o operador '==' não é definido para structs em C; deve-se comparar campo a campo.",
            "Porque é obrigatório usar memcmp(&d1, &d2, sizeof(Data)) em todas as structs.",
            "Porque d1 e d2 deveriam ser declaradas como static.",
            "Porque structs só podem ser comparadas com strcmp."
        ],
        "correct": 1,
        "optionExplanations": [
            "Errado: o typedef está correto.",
            "Correto: C não define '==' nem '!=' para structs (inclusive por causa de bytes de padding com lixo); compare cada membro.",
            "Errado: memcmp é perigoso em structs com padding ou floats (-0.0 vs +0.0) porque o padding pode ter lixo diferente!",
            "Errado: static não muda operadores permitidos.",
            "Errado: strcmp serve apenas para strings (char *)."
        ],
        "steps": [
            "C só permite '=' (atribuição) entre structs, nunca '==' (comparação).",
            "Escreva uma função auxiliar que compara d1.dia == d2.dia && d1.mes == d2.mes && d1.ano == d2.ano."
        ],
        "gabaritoResumo": "C permite 'b = a' em structs, mas proíbe 'a == b': compare sempre campo a campo.",
        "solutionCode": (
            "typedef struct { int dia, mes, ano; } Data;\n"
            "int datas_iguais(Data d1, Data d2) {\n"
            "    return d1.dia == d2.dia && d1.mes == d2.mes && d1.ano == d2.ano;\n"
            "}"
        )
    }
]

CE_STRUCTS = [
    {
        "id": "ce-strc-1",
        "category": "structs",
        "subtopic": "2.2 Declaração e Variáveis",
        "statement": (
            "Em C padrão, a definição 'struct Aluno { int mat; float nota; };' aloca memória "
            "imediatamente para um registro na stack antes mesmo de qualquer variável ser declarada."
        ),
        "answer": False,
        "steps": [
            "A definição de uma struct cria apenas o molde (descrição do tipo) para o compilador.",
            "Memória só é reservada quando uma variável é declarada (ex.: struct Aluno a1;) ou alocada via malloc."
        ],
        "keyPoint": "Definição de struct não aloca memória; declaração de variável sim."
    },
    {
        "id": "ce-strc-2",
        "category": "structs",
        "subtopic": "2.4 Acesso: . vs ->",
        "statement": (
            "Se 'ps' é um ponteiro para 'struct Sensor', as expressões 'ps->referencia' e "
            "'(*ps).referencia' são exatamente equivalentes."
        ),
        "answer": True,
        "steps": [
            "O operador seta (->) foi criado justamente como açúcar sintático para desreferenciar o ponteiro e acessar o campo.",
            "Os parênteses em (*ps).referencia garantem que '*' execute antes de '.'."
        ],
        "keyPoint": "ptr->campo equivale a (*ptr).campo."
    },
    {
        "id": "ce-strc-3",
        "category": "structs",
        "subtopic": "2.5 Inicialização Designada",
        "statement": (
            "Na inicialização parcial 'Pessoa p = {.idade = 20};' em C99, os demais campos da "
            "struct que não foram citados ficam com lixo de memória indeterminado."
        ),
        "answer": False,
        "steps": [
            "Quando uma struct recebe qualquer inicializador entre chaves (posicional ou designado), todos os campos omitidos são automaticamente zerados (0 para números, NULL para ponteiros, '\\0' para chars).",
            "Lixo de memória só ocorre quando declaramos 'Pessoa p;' sem nenhum inicializador."
        ],
        "keyPoint": "Inicialização parcial com chaves zera todos os campos omitidos."
    },
    {
        "id": "ce-strc-4",
        "category": "structs",
        "subtopic": "2.7 Atribuição e Cópia Rasa",
        "statement": (
            "Ao executar 'b = a;' entre duas structs do mesmo tipo que possuem um campo "
            "'char *nome;' alocado dinamicamente, o compilador C cria automaticamente uma nova "
            "cópia da string no heap para 'b.nome'."
        ),
        "answer": False,
        "steps": [
            "O operador '=' em structs realiza uma cópia rasa byte a byte dos campos.",
            "Para um campo ponteiro, copia-se apenas o endereço de memória, fazendo a.nome e b.nome apontarem para o mesmo bloco no heap."
        ],
        "keyPoint": "b = a faz cópia rasa: ponteiros internos passam a apontar para o mesmo endereço."
    },
    {
        "id": "ce-strc-5",
        "category": "structs",
        "subtopic": "2.10 Structs e Funções",
        "statement": (
            "Diferentemente dos vetores em C, uma variável struct passada diretamente como argumento "
            "de função (ex.: altera(aluno1);) é recebida por valor (cópia), de modo que alterações "
            "nos campos do parâmetro não modificam a variável original."
        ),
        "answer": True,
        "steps": [
            "Vetores decaem para ponteiros ao serem passados para funções, mas structs não decaem.",
            "Para modificar a struct original dentro de uma função, é necessário passar seu endereço (&aluno1) para um parâmetro ponteiro (*)."
        ],
        "keyPoint": "Structs são passadas por valor por padrão em C."
    },
    {
        "id": "ce-strc-6",
        "category": "structs",
        "subtopic": "2.15 union",
        "statement": (
            "Em uma union, todos os membros começam no mesmo endereço de memória e o tamanho "
            "total (sizeof) corresponde ao tamanho do maior membro (respeitando o alinhamento), "
            "e não à soma dos tamanhos de todos os membros."
        ),
        "answer": True,
        "steps": [
            "Os campos de uma union compartilham o mesmo bloco de bytes.",
            "Por isso apenas um campo deve ser usado por vez, e sizeof(union) >= maior membro."
        ],
        "keyPoint": "Union sobrepõe seus campos na mesma região de memória."
    },
    {
        "id": "ce-strc-7",
        "category": "structs",
        "subtopic": "2.16 enum",
        "statement": (
            "Em 'enum Turno { MANHA = 1, TARDE, NOITE };', a constante NOITE assume "
            "automaticamente o valor inteiro 3."
        ),
        "answer": True,
        "steps": [
            "Como MANHA foi definida como 1, o compilador incrementa de 1 em 1 para os membros seguintes.",
            "Logo TARDE vale 2 e NOITE vale 3."
        ],
        "keyPoint": "Cada enumerador sem valor explícito vale o anterior + 1."
    },
    {
        "id": "ce-strc-8",
        "category": "structs",
        "subtopic": "2.17 Padding e sizeof",
        "statement": (
            "O valor retornado por sizeof(struct X) é sempre garantidamente igual à soma exata "
            "dos sizeof de cada membro individual da struct."
        ),
        "answer": False,
        "steps": [
            "Para atender às regras de alinhamento da CPU, o compilador pode inserir bytes de padding entre membros e ao final da struct.",
            "Por exemplo, struct { char c; int x; } tipicamente tem sizeof == 8 (e não 5)."
        ],
        "keyPoint": "Sempre use sizeof(MinhaStruct) em malloc/fread por causa do padding."
    },
    {
        "id": "ce-strc-9",
        "category": "structs",
        "subtopic": "2.18 Estruturas Autorreferenciadas",
        "statement": (
            "Uma struct pode conter um ponteiro para o próprio tipo (struct No *prox;), mas "
            "não pode conter uma instância de si mesma por valor (struct No prox;)."
        ),
        "answer": True,
        "steps": [
            "Um ponteiro possui tamanho fixo conhecido em tempo de compilação.",
            "Uma instância direta causaria definição recursiva de tamanho infinito."
        ],
        "keyPoint": "Autorreferência em C é sempre via ponteiro (struct No *)."
    },
    {
        "id": "ce-strc-10",
        "category": "structs",
        "subtopic": "2.18 Erros Comuns",
        "statement": (
            "Em C, embora 'b = a;' funcione para atribuir duas structs do mesmo tipo, a "
            "comparação 'if (a == b)' não é permitida diretamente pela linguagem."
        ),
        "answer": True,
        "steps": [
            "Atribuição direta ('=') copia todos os bytes da struct.",
            "Já '==' não é suportado para structs porque bytes de padding podem conter lixo distinto; deve-se comparar campo a campo."
        ],
        "keyPoint": "Struct aceita '=' para copiar, mas exige comparação campo a campo em vez de '=='."
    }
]

CLASSICAL_STRUCTS = [
    {
        "id": "cls-strc-1",
        "module": "Structs",
        "source": "Exercicios_Estruturas_Unioes_Enumeracoes.pdf — Ex. 6 e Ex. 21 (Cadastro de Alunos)",
        "title": "Cadastro de Turma: Maior P1, Maior/Menor Média e Aprovação",
        "problem": (
            "Crie uma estrutura representando os alunos do curso contendo matrícula (int), "
            "nome (até 40 caracteres), e notas das três provas (p1, p2, p3). Permita ao usuário "
            "cadastrar 5 alunos em um vetor de structs, encontre o aluno com maior nota na P1, "
            "o aluno com maior média geral, o aluno com menor média geral e informe para cada "
            "aluno se foi Aprovado ou Reprovado (critério: média >= 6.0)."
        ),
        "idea": (
            "1) Definir 'typedef struct { int mat; char nome[41]; float p1, p2, p3, media; } Aluno;' "
            "com 41 bytes no nome para comportar o '\\0'.\n"
            "2) Ler os dados limpando o buffer antes de fgets() e calculando a média logo após ler as 3 provas.\n"
            "3) Rastrear três índices (idxP1, idxMaior, idxMenor) iniciados em 0 em um único percurso de i = 1 até N-1.\n"
            "4) Exibir os destaques e a situação final (media >= 6.0f ? \"Aprovado\" : \"Reprovado\")."
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "#define N 5\n"
            "\n"
            "typedef struct {\n"
            "    int matricula;\n"
            "    char nome[41];\n"
            "    float p1, p2, p3;\n"
            "    float media;\n"
            "} Aluno;\n"
            "\n"
            "void limpa_buffer(void) {\n"
            "    int c;\n"
            "    while ((c = getchar()) != '\\n' && c != EOF) {}\n"
            "}\n"
            "\n"
            "void ler_turma(Aluno turma[], int n) {\n"
            "    for (int i = 0; i < n; i++) {\n"
            "        printf(\"--- Aluno %d ---\\n\", i + 1);\n"
            "        printf(\"Matricula: \");\n"
            "        scanf(\"%d\", &turma[i].matricula);\n"
            "        limpa_buffer();\n"
            "        printf(\"Nome: \");\n"
            "        if (fgets(turma[i].nome, sizeof(turma[i].nome), stdin) != NULL) {\n"
            "            turma[i].nome[strcspn(turma[i].nome, \"\\n\")] = '\\0';\n"
            "        }\n"
            "        printf(\"Notas P1, P2, P3: \");\n"
            "        scanf(\"%f %f %f\", &turma[i].p1, &turma[i].p2, &turma[i].p3);\n"
            "        turma[i].media = (turma[i].p1 + turma[i].p2 + turma[i].p3) / 3.0f;\n"
            "    }\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    Aluno turma[N];\n"
            "    ler_turma(turma, N);\n"
            "\n"
            "    int idxP1 = 0, idxMaior = 0, idxMenor = 0;\n"
            "    for (int i = 1; i < N; i++) {\n"
            "        if (turma[i].p1 > turma[idxP1].p1) idxP1 = i;\n"
            "        if (turma[i].media > turma[idxMaior].media) idxMaior = i;\n"
            "        if (turma[i].media < turma[idxMenor].media) idxMenor = i;\n"
            "    }\n"
            "\n"
            "    printf(\"\\nMaior P1: %s (%.1f)\\n\", turma[idxP1].nome, turma[idxP1].p1);\n"
            "    printf(\"Maior media: %s (%.2f)\\n\", turma[idxMaior].nome, turma[idxMaior].media);\n"
            "    printf(\"Menor media: %s (%.2f)\\n\", turma[idxMenor].nome, turma[idxMenor].media);\n"
            "\n"
            "    printf(\"\\nSituacao final:\\n\");\n"
            "    for (int i = 0; i < N; i++) {\n"
            "        const char *sit = (turma[i].media >= 6.0f) ? \"Aprovado\" : \"Reprovado\";\n"
            "        printf(\"[%d] %-20s | Media: %.2f | %s\\n\",\n"
            "               turma[i].matricula, turma[i].nome, turma[i].media, sit);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "trace": (
            "Teste de mesa (exemplo reduzido com 3 alunos):\n"
            "- turma[0]: mat=101, nome=\"Ana\",   P1=8.0, P2=7.0, P3=9.0 -> media = 8.00\n"
            "- turma[1]: mat=102, nome=\"Bruno\", P1=9.5, P2=4.0, P3=3.0 -> media = 5.50\n"
            "- turma[2]: mat=103, nome=\"Clara\", P1=9.0, P2=9.0, P3=9.0 -> media = 9.00\n"
            "Início: idxP1 = 0 (8.0), idxMaior = 0 (8.00), idxMenor = 0 (8.00).\n"
            "i = 1 (Bruno): P1 9.5 > 8.0 -> idxP1 = 1; media 5.50 < 8.00 -> idxMenor = 1.\n"
            "i = 2 (Clara): P1 9.0 <= 9.5 (mantém 1); media 9.00 > 8.00 -> idxMaior = 2.\n"
            "Saída: Maior P1 = Bruno (9.5); Maior média = Clara (9.00); Menor média = Bruno (5.50).\n"
            "Situação: Ana -> Aprovado; Bruno -> Reprovado (< 6.0); Clara -> Aprovado."
        )
    },
    {
        "id": "cls-strc-2",
        "module": "Structs",
        "source": "Exercicios_Estruturas_Unioes_Enumeracoes.pdf — Ex. 34 e Ex. 35 (Fábrica cria() + Tagged Union/Enum)",
        "title": "Estoque Dinâmico (struct produto* cria) com Categoria Enum e Tagged Union",
        "problem": (
            "Combine os padrões dos Exercícios 34 e 35 do PDF: defina uma estrutura 'produto' com "
            "código (int), nome (até 50 caracteres), quantidade (int), preço (float), uma enumeração "
            "para o tipo de fornecimento (NACIONAL ou IMPORTADO) e uma union discriminada que guarda "
            "o CNPJ nacional (quando NACIONAL) ou a taxa de importação em % (quando IMPORTADO). "
            "Implemente a função fábrica 'struct produto* cria(int cod, const char *nome, int quant, "
            "float preco, TipoForn tipo)' que aloca a struct no heap, inicializa os campos e retorna "
            "seu ponteiro, além da exibição via '->' e liberação segura com free()."
        ),
        "idea": (
            "1) Usar 'typedef enum { NACIONAL = 1, IMPORTADO } TipoForn;' como discriminador (tag) "
            "da union interna 'DadosOrigem'.\n"
            "2) Na função cria(...), chamar 'malloc(sizeof(*p))' e checar 'if (p == NULL) return NULL;'.\n"
            "3) Preencher os campos via operador seta '->', usando strncpy(..., 50) + '\\0' no nome.\n"
            "4) Na main, guardar os ponteiros em um vetor 'struct produto *est[2]', configurar o ramo "
            "correto da union conforme 'tipo', imprimir via 'est[i]->...' e chamar free() para cada item."
        ),
        "code": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n"
            "\n"
            "typedef enum { NACIONAL = 1, IMPORTADO } TipoForn;\n"
            "\n"
            "typedef union {\n"
            "    char cnpj[19];\n"
            "    float taxa_imp;\n"
            "} DadosOrigem;\n"
            "\n"
            "struct produto {\n"
            "    int codigo;\n"
            "    char nome[51];\n"
            "    int quantidade;\n"
            "    float preco;\n"
            "    TipoForn tipo;\n"
            "    DadosOrigem origem;\n"
            "};\n"
            "\n"
            "struct produto *cria(int cod, const char *nome, int quant, float preco, TipoForn tipo) {\n"
            "    struct produto *p = malloc(sizeof(*p));\n"
            "    if (p == NULL) return NULL;\n"
            "    p->codigo = cod;\n"
            "    strncpy(p->nome, nome, 50);\n"
            "    p->nome[50] = '\\0';\n"
            "    p->quantidade = quant;\n"
            "    p->preco = preco;\n"
            "    p->tipo = tipo;\n"
            "    if (tipo == NACIONAL) {\n"
            "        strcpy(p->origem.cnpj, \"00.000.000/0001-00\");\n"
            "    } else {\n"
            "        p->origem.taxa_imp = 0.0f;\n"
            "    }\n"
            "    return p;\n"
            "}\n"
            "\n"
            "void imprime_produto(const struct produto *p) {\n"
            "    if (!p) return;\n"
            "    printf(\"[#%d] %s | Qtd: %d | R$ %.2f | \",\n"
            "           p->codigo, p->nome, p->quantidade, p->preco);\n"
            "    if (p->tipo == NACIONAL) {\n"
            "        printf(\"Nacional (CNPJ: %s)\\n\", p->origem.cnpj);\n"
            "    } else {\n"
            "        printf(\"Importado (Taxa: %.1f%%)\\n\", p->origem.taxa_imp);\n"
            "    }\n"
            "}\n"
            "\n"
            "int main(void) {\n"
            "    struct produto *est[2];\n"
            "    est[0] = cria(10, \"Teclado ABNT2\", 15, 149.90f, NACIONAL);\n"
            "    est[1] = cria(20, \"Placa de Video\", 4, 2499.00f, IMPORTADO);\n"
            "\n"
            "    if (est[0]) strcpy(est[0]->origem.cnpj, \"12.345.678/0001-99\");\n"
            "    if (est[1]) est[1]->origem.taxa_imp = 18.5f;\n"
            "\n"
            "    for (int i = 0; i < 2; i++) {\n"
            "        imprime_produto(est[i]);\n"
            "        free(est[i]);\n"
            "        est[i] = NULL;\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "trace": (
            "Teste de mesa (Heap + Tagged Union):\n"
            "1) cria(10, \"Teclado ABNT2\", 15, 149.90, NACIONAL) aloca bloco 0xH100 no heap via malloc(sizeof(*p)).\n"
            "   Como p->tipo == NACIONAL (1), o ramo ativo da union é p->origem.cnpj.\n"
            "2) cria(20, \"Placa de Video\", 4, 2499.00, IMPORTADO) aloca bloco 0xH200 no heap.\n"
            "   Como p->tipo == IMPORTADO (2), o ramo ativo da union é p->origem.taxa_imp (0.0 -> 18.5%).\n"
            "3) imprime_produto() checa p->tipo antes de ler p->origem, evitando leitura do ramo errado.\n"
            "4) Saída esperada:\n"
            "   [#10] Teclado ABNT2 | Qtd: 15 | R$ 149.90 | Nacional (CNPJ: 12.345.678/0001-99)\n"
            "   [#20] Placa de Video | Qtd: 4 | R$ 2499.00 | Importado (Taxa: 18.5%)\n"
            "5) free(est[0]) e free(est[1]) liberam os dois blocos do heap e zeram os ponteiros."
        )
    }
]
