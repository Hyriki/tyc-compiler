grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit()
        value = result.text[1:] 
        if value and value[-1] in ('\n', '\r'):
            value = value[:-1]  
        raise UncloseString(value)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text[1:]) 
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text) 
    else:
        return super().emit()
}

options{
	language = Python3;
}

// TODO: Define grammar rules here

//================= Parser Rules =================//
program: declaration* EOF;
declaration: structDecl | functionDecl;
// | varDecl ;

// 2. Types
type:
	INT				# IntType
	| FLOAT			# FloatType
	| STRING		# StringType
	| IDENTIFIER	# IdentifierType;

// 3. Literals
literal:
	INT_T			# IntLiteral
	| FLOAT_T		# FloatLiteral
	| STRING_T		# StringLiteral
	| structLiteral	# StructLiteralExpr;

argList: expr (COMMA expr)*;

// 4. Struct Declaration
structDecl: STRUCT IDENTIFIER LBRACE structMember* RBRACE SEMI;
structMember: type IDENTIFIER SEMI;
structLiteral: LBRACE (expr (COMMA expr)*)? RBRACE;

// 5. Function Declaration
functionDecl: (returnType)? IDENTIFIER LPAREN paramList? RPAREN blockStm;
returnType: type | VOID;

paramList: param (COMMA param)*;
param: type IDENTIFIER;

// 6. Statements
blockStm: LBRACE statement* RBRACE;

statement:
	varDecl													# VarDeclStmt
	| blockStm												# BlockStmt
	| IF LPAREN expr RPAREN statement (ELSE statement)?		# IfStmt
	| WHILE LPAREN expr RPAREN statement					# WhileStmt
	| FOR LPAREN forInit expr? SEMI updater? RPAREN statement	# ForStmt
	| SWITCH LPAREN expr RPAREN LBRACE caseBlock* defaultBlock? RBRACE	# SwitchStmt
	| RETURN expr? SEMI										# ReturnStmt
	| BREAK SEMI											# BreakStmt
	| CONTINUE SEMI											# ContinueStmt
	| expr SEMI												# ExprStmt;

// Helpers
varDecl: (type | AUTO) IDENTIFIER (ASSIGN expr)? SEMI;
forInit: varDecl | assignExprHelper SEMI| SEMI;
caseBlock: CASE expr COLON statement*;
defaultBlock: DEFAULT COLON statement*;
assignExprHelper: assignLhs ASSIGN expr;
updater: assignExprHelper | incDecHelper;
incDecHelper:
    assignLhs (INC | DEC)
    | (INC | DEC) assignLhs;


// 7. Expressions
expr: assignExpr;

assignExpr: assignLhs ASSIGN assignExpr # AssignOp
          | logicalOrExpr # AssignPass;

assignLhs: IDENTIFIER # AssignId
         | postfixExpr MEMBER IDENTIFIER # AssignMember;

logicalOrExpr: logicalOrExpr OR logicalAndExpr # OrOp
             | logicalAndExpr # OrPass;

logicalAndExpr: logicalAndExpr AND equalityExpr # AndOp
              | equalityExpr # AndPass;

equalityExpr: equalityExpr (EQ | NEQ) relationalExpr # EqOp
            | relationalExpr # EqPass;

relationalExpr: relationalExpr (LT | GT | LEQ | GEQ) additiveExpr # RelOp
              | additiveExpr # RelPass;

additiveExpr: additiveExpr (ADD | SUB) multiplicativeExpr # AddOp
            | multiplicativeExpr # AddPass;

multiplicativeExpr: multiplicativeExpr (MUL | DIV | MOD) unaryExpr # MulOp
                  | unaryExpr # MulPass;

unaryExpr: (ADD | SUB | NOT) unaryExpr # UnaryOp
         | (INC | DEC) unaryExpr # PrefixOp
         | postfixExpr # UnaryPass;

postfixExpr: postfixExpr (INC | DEC) # PostfixOp
           | postfixExpr MEMBER IDENTIFIER # MemberAccessOp
           | primaryExpr # PostfixPass;

primaryExpr: LPAREN expr RPAREN # ParenOp
           | literal # LiteralOp
           | IDENTIFIER LPAREN argList? RPAREN # FuncCallOp
           | IDENTIFIER # IdOp;

//================= Lexer Rules =================//
WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs

// Comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// Keywords (Strictly from Spec)
INT: 'int';
FLOAT: 'float';
STRING: 'string';
VOID: 'void';
STRUCT: 'struct';
AUTO: 'auto';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
CASE: 'case';
SWITCH: 'switch';
DEFAULT: 'default';
FOR: 'for';
WHILE: 'while';

// SEPARATORS
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
COMMA: ',';
COLON: ':';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';
OR: '||';
AND: '&&';
NOT: '!';
INC: '++';
DEC: '--';
MEMBER: '.';
ASSIGN: '=';

// Literals
INT_T: [0-9]+;

//FIXME: Add support for hexadecimal, octal, binary if needed Float spec: 0.0, 3.14, 1.23e4,
// 5.67E-2, 1., .5 .e4 1.e4
fragment EXPONENT: [eE] [+-]? [0-9]+;
FLOAT_T:
	[0-9]+ '.' [0-9]* EXPONENT?
	| '.' [0-9]+ EXPONENT?
	| [0-9]+ EXPONENT;

// Identifiers
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Valid String
STRING_T: '"' STRING_CONTENT* '"' { self.text = self.text[1:-1] };

// Error Handling (Order matters)
ILLEGAL_ESCAPE: '"' STRING_CONTENT* '\\' ~[bfrnt\\"\r\n];
UNCLOSE_STRING: '"' STRING_CONTENT* ([\r\n] | EOF);

// Fragments
fragment STRING_CONTENT: ESC_SEQ | [\u0000-\u0009\u000B\u000C\u000E-\u0021\u0023-\u005B\u005D-\u00FF];
fragment ESC_SEQ: '\\' [bfrnt\\"];
ERROR_CHAR: .;