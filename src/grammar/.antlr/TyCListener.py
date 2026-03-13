# Generated from /Users/hyriki/Documents/GitHub/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete listener for a parse tree produced by TyCParser.
class TyCListener(ParseTreeListener):

    # Enter a parse tree produced by TyCParser#program.
    def enterProgram(self, ctx:TyCParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyCParser#program.
    def exitProgram(self, ctx:TyCParser.ProgramContext):
        pass


    # Enter a parse tree produced by TyCParser#declaration.
    def enterDeclaration(self, ctx:TyCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by TyCParser#declaration.
    def exitDeclaration(self, ctx:TyCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by TyCParser#IntType.
    def enterIntType(self, ctx:TyCParser.IntTypeContext):
        pass

    # Exit a parse tree produced by TyCParser#IntType.
    def exitIntType(self, ctx:TyCParser.IntTypeContext):
        pass


    # Enter a parse tree produced by TyCParser#FloatType.
    def enterFloatType(self, ctx:TyCParser.FloatTypeContext):
        pass

    # Exit a parse tree produced by TyCParser#FloatType.
    def exitFloatType(self, ctx:TyCParser.FloatTypeContext):
        pass


    # Enter a parse tree produced by TyCParser#StringType.
    def enterStringType(self, ctx:TyCParser.StringTypeContext):
        pass

    # Exit a parse tree produced by TyCParser#StringType.
    def exitStringType(self, ctx:TyCParser.StringTypeContext):
        pass


    # Enter a parse tree produced by TyCParser#IdentifierType.
    def enterIdentifierType(self, ctx:TyCParser.IdentifierTypeContext):
        pass

    # Exit a parse tree produced by TyCParser#IdentifierType.
    def exitIdentifierType(self, ctx:TyCParser.IdentifierTypeContext):
        pass


    # Enter a parse tree produced by TyCParser#IntLiteral.
    def enterIntLiteral(self, ctx:TyCParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by TyCParser#IntLiteral.
    def exitIntLiteral(self, ctx:TyCParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by TyCParser#FloatLiteral.
    def enterFloatLiteral(self, ctx:TyCParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by TyCParser#FloatLiteral.
    def exitFloatLiteral(self, ctx:TyCParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by TyCParser#StringLiteral.
    def enterStringLiteral(self, ctx:TyCParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by TyCParser#StringLiteral.
    def exitStringLiteral(self, ctx:TyCParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by TyCParser#StructLiteralExpr.
    def enterStructLiteralExpr(self, ctx:TyCParser.StructLiteralExprContext):
        pass

    # Exit a parse tree produced by TyCParser#StructLiteralExpr.
    def exitStructLiteralExpr(self, ctx:TyCParser.StructLiteralExprContext):
        pass


    # Enter a parse tree produced by TyCParser#functionCall.
    def enterFunctionCall(self, ctx:TyCParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by TyCParser#functionCall.
    def exitFunctionCall(self, ctx:TyCParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by TyCParser#argList.
    def enterArgList(self, ctx:TyCParser.ArgListContext):
        pass

    # Exit a parse tree produced by TyCParser#argList.
    def exitArgList(self, ctx:TyCParser.ArgListContext):
        pass


    # Enter a parse tree produced by TyCParser#structDecl.
    def enterStructDecl(self, ctx:TyCParser.StructDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#structDecl.
    def exitStructDecl(self, ctx:TyCParser.StructDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#structMember.
    def enterStructMember(self, ctx:TyCParser.StructMemberContext):
        pass

    # Exit a parse tree produced by TyCParser#structMember.
    def exitStructMember(self, ctx:TyCParser.StructMemberContext):
        pass


    # Enter a parse tree produced by TyCParser#structLiteral.
    def enterStructLiteral(self, ctx:TyCParser.StructLiteralContext):
        pass

    # Exit a parse tree produced by TyCParser#structLiteral.
    def exitStructLiteral(self, ctx:TyCParser.StructLiteralContext):
        pass


    # Enter a parse tree produced by TyCParser#functionDecl.
    def enterFunctionDecl(self, ctx:TyCParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#functionDecl.
    def exitFunctionDecl(self, ctx:TyCParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#returnType.
    def enterReturnType(self, ctx:TyCParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by TyCParser#returnType.
    def exitReturnType(self, ctx:TyCParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by TyCParser#paramList.
    def enterParamList(self, ctx:TyCParser.ParamListContext):
        pass

    # Exit a parse tree produced by TyCParser#paramList.
    def exitParamList(self, ctx:TyCParser.ParamListContext):
        pass


    # Enter a parse tree produced by TyCParser#param.
    def enterParam(self, ctx:TyCParser.ParamContext):
        pass

    # Exit a parse tree produced by TyCParser#param.
    def exitParam(self, ctx:TyCParser.ParamContext):
        pass


    # Enter a parse tree produced by TyCParser#blockStm.
    def enterBlockStm(self, ctx:TyCParser.BlockStmContext):
        pass

    # Exit a parse tree produced by TyCParser#blockStm.
    def exitBlockStm(self, ctx:TyCParser.BlockStmContext):
        pass


    # Enter a parse tree produced by TyCParser#VarDeclStmt.
    def enterVarDeclStmt(self, ctx:TyCParser.VarDeclStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#VarDeclStmt.
    def exitVarDeclStmt(self, ctx:TyCParser.VarDeclStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#BlockStmt.
    def enterBlockStmt(self, ctx:TyCParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#BlockStmt.
    def exitBlockStmt(self, ctx:TyCParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#IfStmt.
    def enterIfStmt(self, ctx:TyCParser.IfStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#IfStmt.
    def exitIfStmt(self, ctx:TyCParser.IfStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#WhileStmt.
    def enterWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#WhileStmt.
    def exitWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#ForStmt.
    def enterForStmt(self, ctx:TyCParser.ForStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#ForStmt.
    def exitForStmt(self, ctx:TyCParser.ForStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#SwitchStmt.
    def enterSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#SwitchStmt.
    def exitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#ReturnStmt.
    def enterReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#ReturnStmt.
    def exitReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#BreakStmt.
    def enterBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#BreakStmt.
    def exitBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#ContinueStmt.
    def enterContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#ContinueStmt.
    def exitContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#ExprStmt.
    def enterExprStmt(self, ctx:TyCParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#ExprStmt.
    def exitExprStmt(self, ctx:TyCParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#varDecl.
    def enterVarDecl(self, ctx:TyCParser.VarDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#varDecl.
    def exitVarDecl(self, ctx:TyCParser.VarDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#forInit.
    def enterForInit(self, ctx:TyCParser.ForInitContext):
        pass

    # Exit a parse tree produced by TyCParser#forInit.
    def exitForInit(self, ctx:TyCParser.ForInitContext):
        pass


    # Enter a parse tree produced by TyCParser#caseBlock.
    def enterCaseBlock(self, ctx:TyCParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by TyCParser#caseBlock.
    def exitCaseBlock(self, ctx:TyCParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by TyCParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:TyCParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by TyCParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:TyCParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by TyCParser#AssignmentExpr.
    def enterAssignmentExpr(self, ctx:TyCParser.AssignmentExprContext):
        pass

    # Exit a parse tree produced by TyCParser#AssignmentExpr.
    def exitAssignmentExpr(self, ctx:TyCParser.AssignmentExprContext):
        pass


    # Enter a parse tree produced by TyCParser#UnaryExpr.
    def enterUnaryExpr(self, ctx:TyCParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by TyCParser#UnaryExpr.
    def exitUnaryExpr(self, ctx:TyCParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by TyCParser#LogicalAndExpr.
    def enterLogicalAndExpr(self, ctx:TyCParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by TyCParser#LogicalAndExpr.
    def exitLogicalAndExpr(self, ctx:TyCParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by TyCParser#PrefixExpr.
    def enterPrefixExpr(self, ctx:TyCParser.PrefixExprContext):
        pass

    # Exit a parse tree produced by TyCParser#PrefixExpr.
    def exitPrefixExpr(self, ctx:TyCParser.PrefixExprContext):
        pass


    # Enter a parse tree produced by TyCParser#PostfixExpr.
    def enterPostfixExpr(self, ctx:TyCParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by TyCParser#PostfixExpr.
    def exitPostfixExpr(self, ctx:TyCParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by TyCParser#MultiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:TyCParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by TyCParser#MultiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:TyCParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by TyCParser#LogicalOrExpr.
    def enterLogicalOrExpr(self, ctx:TyCParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by TyCParser#LogicalOrExpr.
    def exitLogicalOrExpr(self, ctx:TyCParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by TyCParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:TyCParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by TyCParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:TyCParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by TyCParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:TyCParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by TyCParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:TyCParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by TyCParser#AdditiveExpr.
    def enterAdditiveExpr(self, ctx:TyCParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by TyCParser#AdditiveExpr.
    def exitAdditiveExpr(self, ctx:TyCParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by TyCParser#IdentifierExpr.
    def enterIdentifierExpr(self, ctx:TyCParser.IdentifierExprContext):
        pass

    # Exit a parse tree produced by TyCParser#IdentifierExpr.
    def exitIdentifierExpr(self, ctx:TyCParser.IdentifierExprContext):
        pass


    # Enter a parse tree produced by TyCParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:TyCParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by TyCParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:TyCParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by TyCParser#ParenExpr.
    def enterParenExpr(self, ctx:TyCParser.ParenExprContext):
        pass

    # Exit a parse tree produced by TyCParser#ParenExpr.
    def exitParenExpr(self, ctx:TyCParser.ParenExprContext):
        pass


    # Enter a parse tree produced by TyCParser#MemberAccessExpr.
    def enterMemberAccessExpr(self, ctx:TyCParser.MemberAccessExprContext):
        pass

    # Exit a parse tree produced by TyCParser#MemberAccessExpr.
    def exitMemberAccessExpr(self, ctx:TyCParser.MemberAccessExprContext):
        pass



del TyCParser