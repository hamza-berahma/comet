grammar Rapcode;

// --- Parser Rules ---

program: statement* EOF;

statement:
      assignment SEMI?        # AssignStmt
    | output SEMI?            # OutputStmt
    | ifStatement SEMI?       # IfStmt
    | loop SEMI?              # LoopStmt
    | breakStatement SEMI?    # BreakStmt
    ;

assignment: IDENTIFIER ASSIGN expr;
output: OUTPUT expr;
breakStatement: BREAK;

ifStatement:
    IF NOT? expr THEN
        statement*
    (ELSE
        statement*)?
    ENDIF;

loop: LOOP statement* ENDLOOP;

// Expressions, ordered by precedence (lowest to highest)
expr:
      expr op=(EQ | NEQ) expr              # EqualityExpr
    | expr op=(LT | LTE | GT | GTE) expr   # RelationalExpr
    | expr op=(ADD | SUB) expr             # AddSubExpr
    | expr op=(MUL | DIV | MOD) expr       # MulDivExpr
    | SUB expr                             # UnaryMinusExpr  // <-- NEW: Handles negative numbers
    | atom                                 # AtomExpr
    | '(' expr ')'                         # ParenExpr
    ;

atom:
      IDENTIFIER              # IdAtom
    | STRING                  # StringAtom
    | NUMBER                  # NumberAtom
    | boolean                 # BooleanAtom
    | inputCall               # InputCallAtom
    ;

boolean: TRUE | FALSE;
inputCall: INPUT '(' expr ')';

// --- Lexer Rules (No changes here) ---

// Keywords
IF: 'IF';
THEN: 'THEN';
ELSE: 'ELSE';
ENDIF: 'ENDIF';
LOOP: 'LOOP';
ENDLOOP: 'ENDLOOP';
BREAK: 'BREAK';
OUTPUT: 'OUTPUT';
INPUT: 'INPUT';
NOT: 'NOT';
TRUE: 'TRUE';
FALSE: 'FALSE';

// Operators
ASSIGN: ':=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '=';
NEQ: '!=';
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';

// Atoms
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' ( ~["\\] | '\\' . )*? '"';
COMMENT: '//' .*? '\r'? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;
SEMI: ';';

