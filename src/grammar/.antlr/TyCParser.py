# Generated from e:/Study Files/Github/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,274,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,3,1,49,8,1,1,2,1,2,1,2,1,2,3,2,
        55,8,2,1,3,1,3,1,3,1,3,3,3,61,8,3,1,4,1,4,1,4,3,4,66,8,4,1,4,1,4,
        1,5,1,5,1,5,5,5,73,8,5,10,5,12,5,76,9,5,1,6,1,6,1,6,1,6,5,6,82,8,
        6,10,6,12,6,85,9,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,
        8,98,8,8,10,8,12,8,101,9,8,3,8,103,8,8,1,8,1,8,1,9,3,9,108,8,9,1,
        9,1,9,1,9,3,9,113,8,9,1,9,1,9,1,9,1,10,1,10,3,10,120,8,10,1,11,1,
        11,1,11,5,11,125,8,11,10,11,12,11,128,9,11,1,12,1,12,1,12,1,13,1,
        13,5,13,135,8,13,10,13,12,13,138,9,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,3,14,151,8,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,3,14,163,8,14,1,14,1,14,3,14,167,8,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,178,8,14,10,14,
        12,14,181,9,14,1,14,1,14,1,14,1,14,3,14,187,8,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,3,14,197,8,14,1,15,1,15,3,15,201,8,15,1,
        15,1,15,1,15,3,15,206,8,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,
        16,215,8,16,1,17,1,17,1,17,3,17,220,8,17,1,17,1,17,5,17,224,8,17,
        10,17,12,17,227,9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,3,18,241,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,5,18,269,8,18,10,18,12,18,272,9,18,
        1,18,0,1,36,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,0,6,1,0,41,42,2,0,27,28,40,40,1,0,29,31,1,0,27,28,1,0,34,37,1,
        0,32,33,306,0,41,1,0,0,0,2,48,1,0,0,0,4,54,1,0,0,0,6,60,1,0,0,0,
        8,62,1,0,0,0,10,69,1,0,0,0,12,77,1,0,0,0,14,89,1,0,0,0,16,93,1,0,
        0,0,18,107,1,0,0,0,20,119,1,0,0,0,22,121,1,0,0,0,24,129,1,0,0,0,
        26,132,1,0,0,0,28,196,1,0,0,0,30,200,1,0,0,0,32,214,1,0,0,0,34,219,
        1,0,0,0,36,240,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,
        41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,
        0,0,1,45,1,1,0,0,0,46,49,3,12,6,0,47,49,3,18,9,0,48,46,1,0,0,0,48,
        47,1,0,0,0,49,3,1,0,0,0,50,55,5,4,0,0,51,55,5,5,0,0,52,55,5,6,0,
        0,53,55,5,47,0,0,54,50,1,0,0,0,54,51,1,0,0,0,54,52,1,0,0,0,54,53,
        1,0,0,0,55,5,1,0,0,0,56,61,5,45,0,0,57,61,5,46,0,0,58,61,5,48,0,
        0,59,61,3,16,8,0,60,56,1,0,0,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,
        1,0,0,0,61,7,1,0,0,0,62,63,5,47,0,0,63,65,5,20,0,0,64,66,3,10,5,
        0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,5,21,0,0,68,9,
        1,0,0,0,69,74,3,36,18,0,70,71,5,25,0,0,71,73,3,36,18,0,72,70,1,0,
        0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,11,1,0,0,0,76,74,
        1,0,0,0,77,78,5,8,0,0,78,79,5,47,0,0,79,83,5,22,0,0,80,82,3,14,7,
        0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,
        1,0,0,0,85,83,1,0,0,0,86,87,5,23,0,0,87,88,5,24,0,0,88,13,1,0,0,
        0,89,90,3,4,2,0,90,91,5,47,0,0,91,92,5,24,0,0,92,15,1,0,0,0,93,102,
        5,22,0,0,94,99,3,36,18,0,95,96,5,25,0,0,96,98,3,36,18,0,97,95,1,
        0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,103,1,0,0,
        0,101,99,1,0,0,0,102,94,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,
        104,105,5,23,0,0,105,17,1,0,0,0,106,108,3,20,10,0,107,106,1,0,0,
        0,107,108,1,0,0,0,108,109,1,0,0,0,109,110,5,47,0,0,110,112,5,20,
        0,0,111,113,3,22,11,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,
        0,0,0,114,115,5,21,0,0,115,116,3,26,13,0,116,19,1,0,0,0,117,120,
        3,4,2,0,118,120,5,7,0,0,119,117,1,0,0,0,119,118,1,0,0,0,120,21,1,
        0,0,0,121,126,3,24,12,0,122,123,5,25,0,0,123,125,3,24,12,0,124,122,
        1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,23,1,
        0,0,0,128,126,1,0,0,0,129,130,3,4,2,0,130,131,5,47,0,0,131,25,1,
        0,0,0,132,136,5,22,0,0,133,135,3,28,14,0,134,133,1,0,0,0,135,138,
        1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,136,
        1,0,0,0,139,140,5,23,0,0,140,27,1,0,0,0,141,197,3,30,15,0,142,197,
        3,26,13,0,143,144,5,13,0,0,144,145,5,20,0,0,145,146,3,36,18,0,146,
        147,5,21,0,0,147,150,3,28,14,0,148,149,5,14,0,0,149,151,3,28,14,
        0,150,148,1,0,0,0,150,151,1,0,0,0,151,197,1,0,0,0,152,153,5,19,0,
        0,153,154,5,20,0,0,154,155,3,36,18,0,155,156,5,21,0,0,156,157,3,
        28,14,0,157,197,1,0,0,0,158,159,5,18,0,0,159,160,5,20,0,0,160,162,
        3,32,16,0,161,163,3,36,18,0,162,161,1,0,0,0,162,163,1,0,0,0,163,
        164,1,0,0,0,164,166,5,24,0,0,165,167,3,36,18,0,166,165,1,0,0,0,166,
        167,1,0,0,0,167,168,1,0,0,0,168,169,5,21,0,0,169,170,3,28,14,0,170,
        197,1,0,0,0,171,172,5,16,0,0,172,173,5,20,0,0,173,174,3,36,18,0,
        174,175,5,21,0,0,175,179,5,22,0,0,176,178,3,34,17,0,177,176,1,0,
        0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,182,1,0,
        0,0,181,179,1,0,0,0,182,183,5,23,0,0,183,197,1,0,0,0,184,186,5,12,
        0,0,185,187,3,36,18,0,186,185,1,0,0,0,186,187,1,0,0,0,187,188,1,
        0,0,0,188,197,5,24,0,0,189,190,5,10,0,0,190,197,5,24,0,0,191,192,
        5,11,0,0,192,197,5,24,0,0,193,194,3,36,18,0,194,195,5,24,0,0,195,
        197,1,0,0,0,196,141,1,0,0,0,196,142,1,0,0,0,196,143,1,0,0,0,196,
        152,1,0,0,0,196,158,1,0,0,0,196,171,1,0,0,0,196,184,1,0,0,0,196,
        189,1,0,0,0,196,191,1,0,0,0,196,193,1,0,0,0,197,29,1,0,0,0,198,201,
        3,4,2,0,199,201,5,9,0,0,200,198,1,0,0,0,200,199,1,0,0,0,201,202,
        1,0,0,0,202,205,5,47,0,0,203,204,5,44,0,0,204,206,3,36,18,0,205,
        203,1,0,0,0,205,206,1,0,0,0,206,207,1,0,0,0,207,208,5,24,0,0,208,
        31,1,0,0,0,209,215,3,30,15,0,210,211,3,36,18,0,211,212,5,24,0,0,
        212,215,1,0,0,0,213,215,5,24,0,0,214,209,1,0,0,0,214,210,1,0,0,0,
        214,213,1,0,0,0,215,33,1,0,0,0,216,217,5,15,0,0,217,220,3,36,18,
        0,218,220,5,17,0,0,219,216,1,0,0,0,219,218,1,0,0,0,220,221,1,0,0,
        0,221,225,5,26,0,0,222,224,3,28,14,0,223,222,1,0,0,0,224,227,1,0,
        0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,35,1,0,0,0,227,225,1,0,0,
        0,228,229,6,18,-1,0,229,241,5,47,0,0,230,241,3,6,3,0,231,241,3,8,
        4,0,232,233,5,20,0,0,233,234,3,36,18,0,234,235,5,21,0,0,235,241,
        1,0,0,0,236,237,7,0,0,0,237,241,3,36,18,9,238,239,7,1,0,0,239,241,
        3,36,18,8,240,228,1,0,0,0,240,230,1,0,0,0,240,231,1,0,0,0,240,232,
        1,0,0,0,240,236,1,0,0,0,240,238,1,0,0,0,241,270,1,0,0,0,242,243,
        10,7,0,0,243,244,7,2,0,0,244,269,3,36,18,8,245,246,10,6,0,0,246,
        247,7,3,0,0,247,269,3,36,18,7,248,249,10,5,0,0,249,250,7,4,0,0,250,
        269,3,36,18,6,251,252,10,4,0,0,252,253,7,5,0,0,253,269,3,36,18,5,
        254,255,10,3,0,0,255,256,5,39,0,0,256,269,3,36,18,4,257,258,10,2,
        0,0,258,259,5,38,0,0,259,269,3,36,18,3,260,261,10,1,0,0,261,262,
        5,44,0,0,262,269,3,36,18,1,263,264,10,11,0,0,264,265,5,43,0,0,265,
        269,5,47,0,0,266,267,10,10,0,0,267,269,7,0,0,0,268,242,1,0,0,0,268,
        245,1,0,0,0,268,248,1,0,0,0,268,251,1,0,0,0,268,254,1,0,0,0,268,
        257,1,0,0,0,268,260,1,0,0,0,268,263,1,0,0,0,268,266,1,0,0,0,269,
        272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,37,1,0,0,0,272,270,
        1,0,0,0,28,41,48,54,60,65,74,83,99,102,107,112,119,126,136,150,162,
        166,179,186,196,200,205,214,219,225,240,268,270
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'int'", "'float'", "'string'", "'void'", "'struct'", 
                     "'auto'", "'break'", "'continue'", "'return'", "'if'", 
                     "'else'", "'case'", "'switch'", "'default'", "'for'", 
                     "'while'", "'('", "')'", "'{'", "'}'", "';'", "','", 
                     "':'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
                     "'++'", "'--'", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "INT", "FLOAT", "STRING", "VOID", "STRUCT", "AUTO", 
                      "BREAK", "CONTINUE", "RETURN", "IF", "ELSE", "CASE", 
                      "SWITCH", "DEFAULT", "FOR", "WHILE", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "SEMI", "COMMA", "COLON", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "GT", 
                      "LEQ", "GEQ", "OR", "AND", "NOT", "INC", "DEC", "MEMBER", 
                      "ASSIGN", "INT_T", "FLOAT_T", "IDENTIFIER", "STRING_T", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_type = 2
    RULE_literal = 3
    RULE_functionCall = 4
    RULE_argList = 5
    RULE_structDecl = 6
    RULE_structMember = 7
    RULE_structLiteral = 8
    RULE_functionDecl = 9
    RULE_returnType = 10
    RULE_paramList = 11
    RULE_param = 12
    RULE_blockStm = 13
    RULE_statement = 14
    RULE_varDecl = 15
    RULE_forInit = 16
    RULE_caseBlock = 17
    RULE_expr = 18

    ruleNames =  [ "program", "declaration", "type", "literal", "functionCall", 
                   "argList", "structDecl", "structMember", "structLiteral", 
                   "functionDecl", "returnType", "paramList", "param", "blockStm", 
                   "statement", "varDecl", "forInit", "caseBlock", "expr" ]

    EOF = Token.EOF
    WS=1
    LINE_COMMENT=2
    BLOCK_COMMENT=3
    INT=4
    FLOAT=5
    STRING=6
    VOID=7
    STRUCT=8
    AUTO=9
    BREAK=10
    CONTINUE=11
    RETURN=12
    IF=13
    ELSE=14
    CASE=15
    SWITCH=16
    DEFAULT=17
    FOR=18
    WHILE=19
    LPAREN=20
    RPAREN=21
    LBRACE=22
    RBRACE=23
    SEMI=24
    COMMA=25
    COLON=26
    ADD=27
    SUB=28
    MUL=29
    DIV=30
    MOD=31
    EQ=32
    NEQ=33
    LT=34
    GT=35
    LEQ=36
    GEQ=37
    OR=38
    AND=39
    NOT=40
    INC=41
    DEC=42
    MEMBER=43
    ASSIGN=44
    INT_T=45
    FLOAT_T=46
    IDENTIFIER=47
    STRING_T=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(TyCParser.DeclarationContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355824) != 0):
                self.state = 38
                self.declaration()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structDecl(self):
            return self.getTypedRuleContext(TyCParser.StructDeclContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(TyCParser.FunctionDeclContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_declaration




    def declaration(self):

        localctx = TyCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.structDecl()
                pass
            elif token in [4, 5, 6, 7, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.functionDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)


    class IdentifierTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)


    class IntTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TyCParser.INT, 0)


    class FloatTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)



    def type_(self):

        localctx = TyCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = TyCParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(TyCParser.INT)
                pass
            elif token in [5]:
                localctx = TyCParser.FloatTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(TyCParser.FLOAT)
                pass
            elif token in [6]:
                localctx = TyCParser.StringTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(TyCParser.STRING)
                pass
            elif token in [47]:
                localctx = TyCParser.IdentifierTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.match(TyCParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_T(self):
            return self.getToken(TyCParser.STRING_T, 0)


    class FloatLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_T(self):
            return self.getToken(TyCParser.FLOAT_T, 0)


    class IntLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_T(self):
            return self.getToken(TyCParser.INT_T, 0)


    class StructLiteralExprContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def structLiteral(self):
            return self.getTypedRuleContext(TyCParser.StructLiteralContext,0)




    def literal(self):

        localctx = TyCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                localctx = TyCParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(TyCParser.INT_T)
                pass
            elif token in [46]:
                localctx = TyCParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(TyCParser.FLOAT_T)
                pass
            elif token in [48]:
                localctx = TyCParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.match(TyCParser.STRING_T)
                pass
            elif token in [22]:
                localctx = TyCParser.StructLiteralExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.structLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(TyCParser.ArgListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_functionCall




    def functionCall(self):

        localctx = TyCParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(TyCParser.IDENTIFIER)
            self.state = 63
            self.match(TyCParser.LPAREN)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 535462570622976) != 0):
                self.state = 64
                self.argList()


            self.state = 67
            self.match(TyCParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_argList




    def argList(self):

        localctx = TyCParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.expr(0)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 70
                self.match(TyCParser.COMMA)
                self.state = 71
                self.expr(0)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructMemberContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_structDecl




    def structDecl(self):

        localctx = TyCParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(TyCParser.STRUCT)
            self.state = 78
            self.match(TyCParser.IDENTIFIER)
            self.state = 79
            self.match(TyCParser.LBRACE)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355440) != 0):
                self.state = 80
                self.structMember()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(TyCParser.RBRACE)
            self.state = 87
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structMember




    def structMember(self):

        localctx = TyCParser.StructMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.type_()
            self.state = 90
            self.match(TyCParser.IDENTIFIER)
            self.state = 91
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_structLiteral




    def structLiteral(self):

        localctx = TyCParser.StructLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(TyCParser.LBRACE)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 535462570622976) != 0):
                self.state = 94
                self.expr(0)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 95
                    self.match(TyCParser.COMMA)
                    self.state = 96
                    self.expr(0)
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 104
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def blockStm(self):
            return self.getTypedRuleContext(TyCParser.BlockStmContext,0)


        def returnType(self):
            return self.getTypedRuleContext(TyCParser.ReturnTypeContext,0)


        def paramList(self):
            return self.getTypedRuleContext(TyCParser.ParamListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_functionDecl




    def functionDecl(self):

        localctx = TyCParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 106
                self.returnType()


            self.state = 109
            self.match(TyCParser.IDENTIFIER)
            self.state = 110
            self.match(TyCParser.LPAREN)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355440) != 0):
                self.state = 111
                self.paramList()


            self.state = 114
            self.match(TyCParser.RPAREN)
            self.state = 115
            self.blockStm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_returnType




    def returnType(self):

        localctx = TyCParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnType)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.type_()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(TyCParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ParamContext)
            else:
                return self.getTypedRuleContext(TyCParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_paramList




    def paramList(self):

        localctx = TyCParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.param()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 122
                self.match(TyCParser.COMMA)
                self.state = 123
                self.param()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_param




    def param(self):

        localctx = TyCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.type_()
            self.state = 130
            self.match(TyCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_blockStm




    def blockStm(self):

        localctx = TyCParser.BlockStmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_blockStm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(TyCParser.LBRACE)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 535462571490928) != 0):
                self.state = 133
                self.statement()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ContinueStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)
        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)


    class SwitchStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)
        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)
        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)
        def caseBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.CaseBlockContext)
            else:
                return self.getTypedRuleContext(TyCParser.CaseBlockContext,i)



    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(TyCParser.IF, 0)
        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)


    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)
        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)



    class VarDeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDecl(self):
            return self.getTypedRuleContext(TyCParser.VarDeclContext,0)



    class BreakStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)
        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)


    class BlockStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def blockStm(self):
            return self.getTypedRuleContext(TyCParser.BlockStmContext,0)



    class ForStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)
        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)
        def forInit(self):
            return self.getTypedRuleContext(TyCParser.ForInitContext,0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)
        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)



    class ReturnStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)




    def statement(self):

        localctx = TyCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = TyCParser.VarDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.varDecl()
                pass

            elif la_ == 2:
                localctx = TyCParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.blockStm()
                pass

            elif la_ == 3:
                localctx = TyCParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(TyCParser.IF)
                self.state = 144
                self.match(TyCParser.LPAREN)
                self.state = 145
                self.expr(0)
                self.state = 146
                self.match(TyCParser.RPAREN)
                self.state = 147
                self.statement()
                self.state = 150
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 148
                    self.match(TyCParser.ELSE)
                    self.state = 149
                    self.statement()


                pass

            elif la_ == 4:
                localctx = TyCParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.match(TyCParser.WHILE)
                self.state = 153
                self.match(TyCParser.LPAREN)
                self.state = 154
                self.expr(0)
                self.state = 155
                self.match(TyCParser.RPAREN)
                self.state = 156
                self.statement()
                pass

            elif la_ == 5:
                localctx = TyCParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(TyCParser.FOR)
                self.state = 159
                self.match(TyCParser.LPAREN)
                self.state = 160
                self.forInit()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 535462570622976) != 0):
                    self.state = 161
                    self.expr(0)


                self.state = 164
                self.match(TyCParser.SEMI)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 535462570622976) != 0):
                    self.state = 165
                    self.expr(0)


                self.state = 168
                self.match(TyCParser.RPAREN)
                self.state = 169
                self.statement()
                pass

            elif la_ == 6:
                localctx = TyCParser.SwitchStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 171
                self.match(TyCParser.SWITCH)
                self.state = 172
                self.match(TyCParser.LPAREN)
                self.state = 173
                self.expr(0)
                self.state = 174
                self.match(TyCParser.RPAREN)
                self.state = 175
                self.match(TyCParser.LBRACE)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==17:
                    self.state = 176
                    self.caseBlock()
                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 182
                self.match(TyCParser.RBRACE)
                pass

            elif la_ == 7:
                localctx = TyCParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.match(TyCParser.RETURN)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 535462570622976) != 0):
                    self.state = 185
                    self.expr(0)


                self.state = 188
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 8:
                localctx = TyCParser.BreakStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 189
                self.match(TyCParser.BREAK)
                self.state = 190
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 9:
                localctx = TyCParser.ContinueStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 191
                self.match(TyCParser.CONTINUE)
                self.state = 192
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 10:
                localctx = TyCParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 193
                self.expr(0)
                self.state = 194
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_varDecl




    def varDecl(self):

        localctx = TyCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 47]:
                self.state = 198
                self.type_()
                pass
            elif token in [9]:
                self.state = 199
                self.match(TyCParser.AUTO)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 202
            self.match(TyCParser.IDENTIFIER)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 203
                self.match(TyCParser.ASSIGN)
                self.state = 204
                self.expr(0)


            self.state = 207
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(TyCParser.VarDeclContext,0)


        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_forInit




    def forInit(self):

        localctx = TyCParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forInit)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.expr(0)
                self.state = 211
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_caseBlock




    def caseBlock(self):

        localctx = TyCParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 216
                self.match(TyCParser.CASE)
                self.state = 217
                self.expr(0)
                pass
            elif token in [17]:
                self.state = 218
                self.match(TyCParser.DEFAULT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 221
            self.match(TyCParser.COLON)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 535462571490928) != 0):
                self.state = 222
                self.statement()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def LT(self):
            return self.getToken(TyCParser.LT, 0)
        def GT(self):
            return self.getToken(TyCParser.GT, 0)
        def LEQ(self):
            return self.getToken(TyCParser.LEQ, 0)
        def GEQ(self):
            return self.getToken(TyCParser.GEQ, 0)


    class AssignmentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)


    class UnaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def NOT(self):
            return self.getToken(TyCParser.NOT, 0)
        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)
        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)


    class LogicalAndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def AND(self):
            return self.getToken(TyCParser.AND, 0)


    class PrefixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def INC(self):
            return self.getToken(TyCParser.INC, 0)
        def DEC(self):
            return self.getToken(TyCParser.DEC, 0)


    class PostfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def INC(self):
            return self.getToken(TyCParser.INC, 0)
        def DEC(self):
            return self.getToken(TyCParser.DEC, 0)


    class MultiplicativeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def MUL(self):
            return self.getToken(TyCParser.MUL, 0)
        def DIV(self):
            return self.getToken(TyCParser.DIV, 0)
        def MOD(self):
            return self.getToken(TyCParser.MOD, 0)


    class LogicalOrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def OR(self):
            return self.getToken(TyCParser.OR, 0)


    class FunctionCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(TyCParser.FunctionCallContext,0)



    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def EQ(self):
            return self.getToken(TyCParser.EQ, 0)
        def NEQ(self):
            return self.getToken(TyCParser.NEQ, 0)


    class AdditiveExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)
        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)


    class IdentifierExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)


    class LiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(TyCParser.LiteralContext,0)



    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)


    class MemberAccessExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def MEMBER(self):
            return self.getToken(TyCParser.MEMBER, 0)
        def IDENTIFIER(self):
            return self.getToken(TyCParser.IDENTIFIER, 0)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = TyCParser.IdentifierExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 229
                self.match(TyCParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = TyCParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 230
                self.literal()
                pass

            elif la_ == 3:
                localctx = TyCParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 231
                self.functionCall()
                pass

            elif la_ == 4:
                localctx = TyCParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 232
                self.match(TyCParser.LPAREN)
                self.state = 233
                self.expr(0)
                self.state = 234
                self.match(TyCParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = TyCParser.PrefixExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 236
                _la = self._input.LA(1)
                if not(_la==41 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 237
                self.expr(9)
                pass

            elif la_ == 6:
                localctx = TyCParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 238
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1099914280960) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 239
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 268
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.MultiplicativeExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 242
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 243
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 244
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.AdditiveExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 245
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 246
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 247
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.RelationalExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 249
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 257698037760) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = TyCParser.EqualityExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 252
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 253
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = TyCParser.LogicalAndExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 254
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 255
                        self.match(TyCParser.AND)
                        self.state = 256
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = TyCParser.LogicalOrExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 257
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 258
                        self.match(TyCParser.OR)
                        self.state = 259
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = TyCParser.AssignmentExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 260
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 261
                        self.match(TyCParser.ASSIGN)
                        self.state = 262
                        self.expr(1)
                        pass

                    elif la_ == 8:
                        localctx = TyCParser.MemberAccessExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 263
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 264
                        self.match(TyCParser.MEMBER)
                        self.state = 265
                        self.match(TyCParser.IDENTIFIER)
                        pass

                    elif la_ == 9:
                        localctx = TyCParser.PostfixExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 266
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 267
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==42):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 10)
         




