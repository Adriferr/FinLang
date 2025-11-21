grammar FinLang;

// ---------------------------
// PARSER
// ---------------------------

programa
    : (comando)* EOF
    ;

// comandos: observação — expressões/atribuições/IO simples terminam em ';'
comando
    : declaracao
    | atribuicao ';'
    | incremento ';'
    | entradaSaida ';'
    | condicional
    | repeticao
    | bloco
    ;

bloco
    : '{' comando* '}'
    ;

declaracao
    : tipo ID ('=' expr)? ';'
    ;

tipo
    : INT
    | REAL
    | BOOL_T
    | TEXTO
    ;

atribuicao
    : ID '=' expr
    ;

condicional
    : SE '(' expr ')' comando (SENAO comando)?
    ;

// inicialização pode ser declaracao OU atribuicao (ou vazio),
// condicao pode ser uma expr (ou vazia), incremento pode ser atribuicao OU incremento (ou vazio)
repeticao
    : REPETE '(' (declaracao | atribuicao)? ';' expr? ';' (atribuicao | incremento)? ')' comando
    ;

entradaSaida
    : ESCREVA '(' expr ')'
    | LEIA '(' ID ')'
    ;

// incrementos como comandos (pre e post)
incremento
    : INCREMENTO ID
    | DECREMENTO ID
    | ID INCREMENTO
    | ID DECREMENTO
    ;

// ---------------------------
// Expressões com precedência
// ---------------------------

expr
    : exprLogico
    ;

exprLogico
    : exprRelacional ( (AND | OR) exprRelacional )*
    ;

exprRelacional
    : exprAritmetica ( (MENOR | MAIOR | MENOR_IGUAL | MAIOR_IGUAL | IGUAL | DIF) exprAritmetica )*
    ;

exprAritmetica
    : termo ( (MAIS | MENOS) termo )*
    ;

termo
    : fator ( (MULT | DIV) fator )*
    ;

fator
    : '(' expr ')'
    | BOOL
    | NUM_REAL
    | NUM_INT
    | STRING
    | ID
    ;

// ---------------------------
// LEXER
// ---------------------------

// palavras-reservadas
INT     : 'inteiro';
REAL    : 'real';
BOOL_T  : 'bool';
TEXTO   : 'texto';

SE      : 'se';
SENAO   : 'senao';

REPETE  : 'repete';

ESCREVA : 'escreva';
LEIA    : 'leia';

// operadores compostos e símbolos 
INCREMENTO : '++' ;
DECREMENTO : '--' ;

// operadores aritméticos
MAIS : '+' ;
MENOS   : '-' ;
MULT     : '*' ;
DIV     : '/' ;

// operadores relacionais
MENOR_IGUAL : '<=' ;
MAIOR_IGUAL : '>=' ;
IGUAL       : '==' ;
DIF         : '!=' ;
MENOR       : '<' ;
MAIOR       : '>' ;

// operadores lógicos opcionais
AND : 'e' ;   // ou '&&'
OR  : 'ou' ;  // ou '||'

// literais e identificadores
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

NUM_INT  : [0-9]+ ;
NUM_REAL : [0-9]+ '.' [0-9]+ ;

// booleanos literais
BOOL : 'verdadeiro' | 'falso' ;

// strings
STRING
    : '"' (~["\\] | '\\' . )* '"'
    ;

// comentários e espaços
COMMENT : '//' ~[\r\n]* -> skip ;
WS : [ \t\r\n]+ -> skip ;
