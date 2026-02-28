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

functionCall: IDENTIFIER LPAREN argList? RPAREN;
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
	| FOR LPAREN forInit expr? SEMI expr? RPAREN statement	# ForStmt
	| SWITCH LPAREN expr RPAREN LBRACE caseBlock* RBRACE	# SwitchStmt
	| RETURN expr? SEMI										# ReturnStmt
	| BREAK SEMI											# BreakStmt
	| CONTINUE SEMI											# ContinueStmt
	| expr SEMI												# ExprStmt;

// Helpers
varDecl: (type | AUTO) IDENTIFIER (ASSIGN expr)? SEMI;
forInit: varDecl | expr SEMI | SEMI;
caseBlock: (CASE expr | DEFAULT) COLON statement*;

// 7. Expressions
expr:
	// --- Priority 0: Atoms ---
	IDENTIFIER				# IdentifierExpr
	| literal				# LiteralExpr
	| functionCall			# FunctionCallExpr
	| LPAREN expr RPAREN	# ParenExpr

	// --- Priority 1: Member Access (.) [Left Associative] ---
	| expr MEMBER IDENTIFIER # MemberAccessExpr

	// --- Priority 2: Postfix (++ --) [Left Associative] ---
	| expr (INC | DEC) # PostfixExpr

	// --- Priority 3: Prefix (++ --) [Right Associative] ---
	| <assoc = right> (INC | DEC) expr # PrefixExpr

	// --- Priority 4: Unary (! - +) [Right Associative] ---
	| <assoc = right> (NOT | SUB | ADD) expr # UnaryExpr

	// --- Priority 5: Multiplicative (* / %) [Left Associative] ---
	| expr (MUL | DIV | MOD) expr # MultiplicativeExpr

	// --- Priority 6: Additive (+ -) [Left Associative] ---
	| expr (ADD | SUB) expr # AdditiveExpr

	// --- Priority 7: Relational (< <= > >=) [Left Associative] ---
	| expr (LT | GT | LEQ | GEQ) expr # RelationalExpr

	// --- Priority 8: Equality (== !=) [Left Associative] ---
	| expr (EQ | NEQ) expr # EqualityExpr

	// --- Priority 9: Logical AND (&&) [Left Associative] ---
	| expr AND expr # LogicalAndExpr

	// --- Priority 10: Logical OR (||) [Left Associative] ---
	| expr OR expr # LogicalOrExpr

	// --- Priority 11: Assignment (=) [Right Associative] ---
	| <assoc = right> expr ASSIGN expr # AssignmentExpr;

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