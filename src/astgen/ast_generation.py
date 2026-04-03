"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""
    def visitProgram(self, ctx:TyCParser.ProgramContext):
        decl_list = [self.visit(decl) for decl in ctx.declaration()]
        return Program(decl_list)
    
    def visitDeclaration(self, ctx:TyCParser.DeclarationContext):
        if ctx.structDecl():
            return self.visit(ctx.structDecl())
        else:
            return self.visit(ctx.functionDecl())

    def visitIntType(self, ctx:TyCParser.IntTypeContext):
        return IntType()
    
    def visitFloatType(self, ctx:TyCParser.FloatTypeContext):
        return FloatType()
    
    def visitStringType(self, ctx:TyCParser.StringTypeContext):
        return StringType()
    
    def visitIdentifierType(self, ctx:TyCParser.IdentifierTypeContext):
        return StructType(ctx.IDENTIFIER().getText())
    
    def visitIntLiteral(self, ctx:TyCParser.IntLiteralContext):
        value = int(ctx.INT_T().getText())
        return IntLiteral(value)
    
    def visitFloatLiteral(self, ctx:TyCParser.FloatLiteralContext):
        value = float(ctx.FLOAT_T().getText())
        return FloatLiteral(value)
    
    def visitStringLiteral(self, ctx:TyCParser.StringLiteralContext):
        value = ctx.STRING_T().getText()
        return StringLiteral(value)
    
    def visitStructLiteralExpr(self, ctx:TyCParser.StructLiteralExprContext):
        struct_literal = ctx.structLiteral()
        return self.visit(struct_literal)
    
    def visitArgList(self, ctx:TyCParser.ArgListContext):
        expr_list = [self.visit(expr) for expr in ctx.expr()]
        return expr_list
    
    def visitStructDecl(self, ctx:TyCParser.StructDeclContext):
        name = ctx.IDENTIFIER().getText()
        member_list = [self.visit(member) for member in ctx.structMember()]
        return StructDecl(name, member_list)
    
    def visitStructMember(self, ctx:TyCParser.StructMemberContext):
        name = ctx.IDENTIFIER().getText()
        memberType = self.visit(ctx.type_())
        return MemberDecl(memberType, name)
    
    def visitStructLiteral(self, ctx:TyCParser.StructLiteralContext):
        expr_list = [self.visit(expr) for expr in ctx.expr()]
        return StructLiteral(expr_list)
    
    def visitFunctionDecl(self, ctx:TyCParser.FunctionDeclContext):
        return_type = self.visit(ctx.returnType()) if ctx.returnType() else None
        name = ctx.IDENTIFIER().getText()
        param_list = self.visit(ctx.paramList()) if ctx.paramList() else []
        body = self.visit(ctx.blockStm())
        return FuncDecl(return_type, name, param_list, body)
    
    def visitReturnType(self, ctx:TyCParser.ReturnTypeContext):
        if ctx.type_():
            return self.visit(ctx.type_())
        else:
            return VoidType()
    
    def visitParamList(self, ctx:TyCParser.ParamListContext):
        param_list = [self.visit(param) for param in ctx.param()]
        return param_list
    
    def visitParam(self, ctx:TyCParser.ParamContext):
        param_type = self.visit(ctx.type_())
        name = ctx.IDENTIFIER().getText()
        return Param(param_type, name)
    
    def visitBlockStm(self, ctx:TyCParser.BlockStmContext):
        stmt_list = [self.visit(stmt) for stmt in ctx.statement()]
        return BlockStmt(stmt_list)
    
    def visitVarDeclStmt(self, ctx:TyCParser.VarDeclStmtContext):
        return self.visit(ctx.varDecl())
    
    def visitBlockStmt(self, ctx:TyCParser.BlockStmtContext):
        blockStmt = ctx.blockStm()
        return self.visit(blockStmt)
    
    def visitIfStmt(self, ctx:TyCParser.IfStmtContext):
        condition = self.visit(ctx.expr())
        if_stmt = self.visit(ctx.statement(0))
        else_stmt = self.visit(ctx.statement(1)) if ctx.ELSE() else None
        return IfStmt(condition, if_stmt, else_stmt)
    
    def visitWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.statement())
        return WhileStmt(condition, body)
    
    def visitForStmt(self, ctx:TyCParser.ForStmtContext):
        init = self.visit(ctx.forInit())
        condition = self.visit(ctx.expr()) if ctx.expr() else None
        update = self.visit(ctx.updater()) if ctx.updater() else None
        body = self.visit(ctx.statement())
        return ForStmt(init, condition, update, body)
    
    def visitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        expr = self.visit(ctx.expr())
        cases = []
        default_case = None
        for case in ctx.caseBlock():
            cases.append(self.visit(case))
        if ctx.defaultBlock():
            default_case = self.visit(ctx.defaultBlock())
        return SwitchStmt(expr, cases, default_case)
    
    # Visit a parse tree produced by TyCParser#ReturnStmt.
    def visitReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        else:
            return ReturnStmt(None)


    # Visit a parse tree produced by TyCParser#BreakStmt.
    def visitBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        return BreakStmt()


    # Visit a parse tree produced by TyCParser#ContinueStmt.
    def visitContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by TyCParser#ExprStmt.
    def visitExprStmt(self, ctx:TyCParser.ExprStmtContext):
        return ExprStmt(self.visit(ctx.expr()))


    # Visit a parse tree produced by TyCParser#varDecl.
    def visitVarDecl(self, ctx:TyCParser.VarDeclContext):
        name = ctx.IDENTIFIER().getText()
        var_type = self.visit(ctx.type_()) if ctx.type_() else None
        init_value = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(var_type, name, init_value)

    def visitForInit(self, ctx:TyCParser.ForInitContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.assignExprHelper():
            assign_expr = self.visit(ctx.assignExprHelper())
            return ExprStmt(assign_expr)
        else:
            return None
    
    def visitCaseBlock(self, ctx:TyCParser.CaseBlockContext):
        expr = self.visit(ctx.expr())
        stmt_list = [self.visit(stmt) for stmt in ctx.statement()]
        return CaseStmt(expr, stmt_list)

    def visitDefaultBlock(self, ctx:TyCParser.DefaultBlockContext):
        stmt_list = [self.visit(stmt) for stmt in ctx.statement()]
        return DefaultStmt(stmt_list)
    
    # Visit a parse tree produced by TyCParser#assignExprHelper.
    def visitAssignExprHelper(self, ctx:TyCParser.AssignExprHelperContext):
        lhs = self.visit(ctx.assignLhs())
        rhs = self.visit(ctx.expr())
        return AssignExpr(lhs, rhs)

    # Visit a parse tree produced by TyCParser#updater.
    def visitUpdater(self, ctx:TyCParser.UpdaterContext):
        if ctx.assignExprHelper():
            return self.visit(ctx.assignExprHelper())
        else:
            return self.visit(ctx.incDecHelper())

    # Visit a parse tree produced by TyCParser#incDecHelper.
    def visitIncDecHelper(self, ctx:TyCParser.IncDecHelperContext):
        operand = self.visit(ctx.assignLhs())
        op = ctx.INC().getText() if ctx.INC() else ctx.DEC().getText()
        if ctx.getChild(0).getText() in ["++", "--"]:
            return PrefixOp(op, operand)
        else:
            return PostfixOp(op, operand)
        
    # Visit a parse tree produced by TyCParser#expr.
    def visitExpr(self, ctx:TyCParser.ExprContext):
        return self.visit(ctx.assignExpr())


    # Visit a parse tree produced by TyCParser#AssignOp.
    def visitAssignOp(self, ctx:TyCParser.AssignOpContext):
        lhs = self.visit(ctx.assignLhs())
        rhs = self.visit(ctx.assignExpr())
        return AssignExpr(lhs, rhs)


    # Visit a parse tree produced by TyCParser#AssignPass.
    def visitAssignPass(self, ctx:TyCParser.AssignPassContext):
        return self.visit(ctx.logicalOrExpr())


    # Visit a parse tree produced by TyCParser#AssignId.
    def visitAssignId(self, ctx:TyCParser.AssignIdContext):
        return Identifier(ctx.IDENTIFIER().getText())


    # Visit a parse tree produced by TyCParser#AssignMember.
    def visitAssignMember(self, ctx:TyCParser.AssignMemberContext):
        obj = self.visit(ctx.postfixExpr())
        member = ctx.IDENTIFIER().getText()
        return MemberAccess(obj, member)


    # Visit a parse tree produced by TyCParser#OrOp.
    def visitOrOp(self, ctx:TyCParser.OrOpContext):
        lhs = self.visit(ctx.logicalOrExpr())
        rhs = self.visit(ctx.logicalAndExpr())
        op = ctx.OR().getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#OrPass.
    def visitOrPass(self, ctx:TyCParser.OrPassContext):
        return self.visit(ctx.logicalAndExpr())


    # Visit a parse tree produced by TyCParser#AndPass.
    def visitAndPass(self, ctx:TyCParser.AndPassContext):
        return self.visit(ctx.equalityExpr())


    # Visit a parse tree produced by TyCParser#AndOp.
    def visitAndOp(self, ctx:TyCParser.AndOpContext):
        lhs = self.visit(ctx.logicalAndExpr())
        rhs = self.visit(ctx.equalityExpr())
        op = ctx.AND().getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#EqPass.
    def visitEqPass(self, ctx:TyCParser.EqPassContext):
        return self.visit(ctx.relationalExpr())


    # Visit a parse tree produced by TyCParser#EqOp.
    def visitEqOp(self, ctx:TyCParser.EqOpContext):
        lhs = self.visit(ctx.equalityExpr())
        rhs = self.visit(ctx.relationalExpr())
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#RelOp.
    def visitRelOp(self, ctx:TyCParser.RelOpContext):
        lhs = self.visit(ctx.relationalExpr())
        rhs = self.visit(ctx.additiveExpr())
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#RelPass.
    def visitRelPass(self, ctx:TyCParser.RelPassContext):
        return self.visit(ctx.additiveExpr())


    # Visit a parse tree produced by TyCParser#AddOp.
    def visitAddOp(self, ctx:TyCParser.AddOpContext):
        lhs = self.visit(ctx.additiveExpr())
        rhs = self.visit(ctx.multiplicativeExpr())
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#AddPass.
    def visitAddPass(self, ctx:TyCParser.AddPassContext):
        return self.visit(ctx.multiplicativeExpr())


    # Visit a parse tree produced by TyCParser#MulOp.
    def visitMulOp(self, ctx:TyCParser.MulOpContext):
        lhs = self.visit(ctx.multiplicativeExpr())
        rhs = self.visit(ctx.unaryExpr())
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#MulPass.
    def visitMulPass(self, ctx:TyCParser.MulPassContext):
        return self.visit(ctx.unaryExpr())


    # Visit a parse tree produced by TyCParser#UnaryOp.
    def visitUnaryOp(self, ctx:TyCParser.UnaryOpContext):
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.unaryExpr())
        return PrefixOp(op, operand)


    # Visit a parse tree produced by TyCParser#PrefixOp.
    def visitPrefixOp(self, ctx:TyCParser.PrefixOpContext):
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.unaryExpr())
        return PrefixOp(op, operand)


    # Visit a parse tree produced by TyCParser#UnaryPass.
    def visitUnaryPass(self, ctx:TyCParser.UnaryPassContext):
        return self.visit(ctx.postfixExpr())


    # Visit a parse tree produced by TyCParser#PostfixOp.
    def visitPostfixOp(self, ctx:TyCParser.PostfixOpContext):
        operand = self.visit(ctx.postfixExpr())
        op = ctx.getChild(1).getText()
        return PostfixOp(op, operand)


    # Visit a parse tree produced by TyCParser#PostfixPass.
    def visitPostfixPass(self, ctx:TyCParser.PostfixPassContext):
        return self.visit(ctx.primaryExpr())


    # Visit a parse tree produced by TyCParser#MemberAccessOp.
    def visitMemberAccessOp(self, ctx:TyCParser.MemberAccessOpContext):
        obj = self.visit(ctx.postfixExpr())
        member = ctx.IDENTIFIER().getText()
        return MemberAccess(obj, member)


    # Visit a parse tree produced by TyCParser#ParenOp.
    def visitParenOp(self, ctx:TyCParser.ParenOpContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by TyCParser#LiteralOp.
    def visitLiteralOp(self, ctx:TyCParser.LiteralOpContext):
        return self.visit(ctx.literal())


    # Visit a parse tree produced by TyCParser#FuncCallOp.
    def visitFuncCallOp(self, ctx:TyCParser.FuncCallOpContext):
        name = ctx.IDENTIFIER().getText()
        arg_list = self.visit(ctx.argList()) if ctx.argList() else []
        return FuncCall(name, arg_list)


    # Visit a parse tree produced by TyCParser#IdOp.
    def visitIdOp(self, ctx:TyCParser.IdOpContext):
        return Identifier(ctx.IDENTIFIER().getText())