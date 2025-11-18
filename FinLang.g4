grammar FinLang;

// ---------------------------
// PARSER
// ---------------------------

programa
    : (comando)* EOF
    ;

comando
    : declaracao
    | atribuicao
    | condicional
    | repeticao
    | entradaSaida
    | expr
    ;

declaracao
    : tipo ID ('=' expr)?
    ;

tipo
    : 'int'
    | 'real'
    | 'bool'
    | 'texto'
    ;

atribuicao
    : ID '=' expr
    ;

condicional
    : 'se' expr comando ('senao' comando)?
    ;

repeticao
    : 'repete' '(' ID '=' expr 'até' expr ')' comando
    ;

entradaSaida
    : 'escreva' '(' expr ')'
    | 'leia' '(' ID ')'
    ;

expr
    : expr op=('*' | '/' ) expr
    | expr op=('+' | '-') expr
    | '(' expr ')'
    | BOOL
    | NUM_INT
    | NUM_REAL
    | STRING
    | ID
    ;

// ---------------------------
// LEXER
// ---------------------------

ID : [a-zA-Z_][a-zA-Z0-9_]* ;

NUM_INT  : [0-9]+ ;
NUM_REAL : [0-9]+ '.' [0-9]+ ;

BOOL : 'verdadeiro' | 'falso' ;

STRING
    : '"' (~["\\] | '\\' . )* '"'
    ;

COMMENT : '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;

EMPTY : '[]' -> skip ;
