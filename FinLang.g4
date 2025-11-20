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
    | bloco
    | expr
    ;

bloco
    : '{' (comando)* '}'
    ;

declaracao
    : tipo ID ('=' expr)?
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

repeticao
    : REPETE '(' ID '=' expr ATE expr ')' comando
    ;

entradaSaida
    : ESCREVA '(' expr ')'
    | LEIA '(' ID ')'
    ;

expr
    : expr op=('*' | '/' ) expr                     # ExprMult
    | expr op=('+' | '-') expr                      # ExprAdd
    | expr op=('==' | '!=' | '<' | '>' | '<=' | '>=') expr  # ExprRel
    | expr op=('&&' | '||') expr                    # ExprLogic
    | '!' expr                                      # ExprNot
    | '(' expr ')'                                  # ExprParen
    | BOOL                                          # ExprBool
    | NUM_INT                                       # ExprInt
    | NUM_REAL                                      # ExprReal
    | STRING                                        # ExprString
    | ID                                            # ExprId
    ;


// ---------------------------
// LEXER
// ---------------------------

// PALAVRAS-RESERVADAS (devem vir antes de ID)
INT     : 'int';
REAL    : 'real';
BOOL_T  : 'bool';
TEXTO   : 'texto';

SE      : 'se';
SENAO   : 'senao';

REPETE  : 'repete';
ATE     : 'até';

ESCREVA : 'escreva';
LEIA    : 'leia';

// Tokens gerais
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

NUM_INT  : [0-9]+ ;
NUM_REAL : [0-9]+ '.' [0-9]+ ;

BOOL : 'verdadeiro' | 'falso' ;

STRING
    : '"' (~["\\] | '\\' . )* '"'
    ;

COMMENT : '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;
