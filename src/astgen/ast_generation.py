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
    
    def visitFunctionCall(self, ctx:TyCParser.FunctionCallContext):
        arg_list = self.visit(ctx.argList())
        name = ctx.IDENTIFIER().getText()
        return FuncCall(name, arg_list)
    
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
        return_type = self.visit(ctx.returnType())
        name = ctx.IDENTIFIER().getText()
        param_list = self.visit(ctx.paramList())
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
        blockStmt = ctx.blockStmt()
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
        condition = self.visit(ctx.cond) if ctx.cond else None
        update = self.visit(ctx.update) if ctx.update else None
        body = self.visit(ctx.statement())
        return ForStmt(init, condition, update, body)
    
    def visitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        expr = self.visit(ctx.expr())
        cases = []
        default_case = None
        for case in ctx.caseBlock():
            if case.DEFAULT():
                default_case = self.visit(case)
            else:
                cases.append(self.visit(case))
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
        elif ctx.expr():
            return self.visit(ctx.expr())
        else:
            return None
    
    def visitCaseBlock(self, ctx:TyCParser.CaseBlockContext):
        if ctx.DEFAULT():
            statements = [self.visit(stmt) for stmt in ctx.statement()]
            return DefaultStmt(statements)
        else:
            case_expr = self.visit(ctx.expr())
            statements = [self.visit(stmt) for stmt in ctx.statement()]
            return CaseStmt(case_expr, statements)

    # Visit a parse tree produced by TyCParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:TyCParser.RelationalExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(left, op, right)


    # Visit a parse tree produced by TyCParser#AssignmentExpr.
    def visitAssignmentExpr(self, ctx:TyCParser.AssignmentExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        return AssignExpr(lhs, rhs)


    # Visit a parse tree produced by TyCParser#UnaryExpr.
    def visitUnaryExpr(self, ctx:TyCParser.UnaryExprContext):
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.expr())
        return PrefixOp(op, operand)


    # Visit a parse tree produced by TyCParser#LogicalAndExpr.
    def visitLogicalAndExpr(self, ctx:TyCParser.LogicalAndExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#PrefixExpr.
    def visitPrefixExpr(self, ctx:TyCParser.PrefixExprContext):
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.expr())
        return PrefixOp(op, operand)


    # Visit a parse tree produced by TyCParser#PostfixExpr.
    def visitPostfixExpr(self, ctx:TyCParser.PostfixExprContext):
        op = ctx.getChild(1).getText()
        operand = self.visit(ctx.expr())
        return PostfixOp(op, operand)


    # Visit a parse tree produced by TyCParser#MultiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:TyCParser.MultiplicativeExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#LogicalOrExpr.
    def visitLogicalOrExpr(self, ctx:TyCParser.LogicalOrExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:TyCParser.FunctionCallExprContext):
        return self.visit(ctx.functionCall())


    # Visit a parse tree produced by TyCParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:TyCParser.EqualityExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#AdditiveExpr.
    def visitAdditiveExpr(self, ctx:TyCParser.AdditiveExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(lhs, op, rhs)


    # Visit a parse tree produced by TyCParser#IdentifierExpr.
    def visitIdentifierExpr(self, ctx:TyCParser.IdentifierExprContext):
        return Identifier(ctx.IDENTIFIER().getText())


    # Visit a parse tree produced by TyCParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:TyCParser.LiteralExprContext):
        return self.visit(ctx.literal())
        


    # Visit a parse tree produced by TyCParser#ParenExpr.
    def visitParenExpr(self, ctx:TyCParser.ParenExprContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by TyCParser#MemberAccessExpr.
    def visitMemberAccessExpr(self, ctx:TyCParser.MemberAccessExprContext):
        member = ctx.IDENTIFIER().getText()
        obj = self.visit(ctx.expr())
        return MemberAccess(obj, member)


    pass
