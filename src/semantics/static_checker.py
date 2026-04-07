"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""

from functools import reduce
from platform import node
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]
from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)


class StaticChecker(ASTVisitor):
    def visit_program(self, node: "Program", o: Any = None):
        structSeen = {}
        funcSeen = {}
        for decl in node.decls:
            if isinstance(decl, StructDecl):
                if decl.name in structSeen:
                    raise Redeclared("Struct", decl.name)
                structSeen[decl.name] = decl
            elif isinstance(decl, FuncDecl):
                if decl.name in funcSeen:
                    raise Redeclared("Function", decl.name)
                funcSeen[decl.name] = decl
        dictToPass = {"structs": structSeen, "functions": funcSeen, "vars": [{}]}
        for decl in node.decls:
            self.visit(decl, dictToPass)
        

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        seen = {}
        for member in node.members:
            if member.name in seen:
                raise Redeclared("Variable", member.name)
            seen[member.name] = member
            self.visit(member, o)

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        pass

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        paramSeen = {}
        for param in node.params:
            if param.name in paramSeen:
                raise Redeclared("Parameter", param.name)
            paramSeen[param.name] = param
            self.visit(param, o)

        self.visit(node.return_type, o)
        new_dict = {**o, "vars": o["vars"] + [paramSeen]}
        self.visit(node.body, new_dict)

    def visit_param(self, node: "Param", o: Any = None):
        pass

    # Type system
    def visit_int_type(self, node: "IntType", o: Any = None):
        pass

    def visit_float_type(self, node: "FloatType", o: Any = None):
        pass

    def visit_string_type(self, node: "StringType", o: Any = None):
        pass

    def visit_void_type(self, node: "VoidType", o: Any = None):
        pass

    def visit_struct_type(self, node: "StructType", o: Any = None):
        pass

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        localVars = {}
        new_dict = {**o, "vars": o["vars"] + [localVars]}
        for stmt in node.statements:
            self.visit(stmt, new_dict) #Avoid int x = x + 1
            if isinstance(stmt, VarDecl):
                if stmt.name in localVars:
                    raise Redeclared("Variable", stmt.name)
                localVars[stmt.name] = stmt

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        if node.init_value:
            self.visit(node.init_value, o)


    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        self.visit(node.condition, o)
        self.visit(node.then_body, o)
        if node.else_body:
            self.visit(node.else_body, o)

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        self.visit(node.condition, o)
        self.visit(node.body, o)

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        if node.init:
            self.visit(node.init, o)
        if node.condition:
            self.visit(node.condition, o)
        if node.update:
            self.visit(node.update, o)
        self.visit(node.body, o)


    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        pass

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        pass

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        pass

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        pass

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        pass

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        if node.expr:
            self.visit(node.expr, o)


    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        self.visit(node.expr, o)

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        self.visit(node.left, o)
        self.visit(node.right, o)


    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        self.visit(node.operand, o)

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        self.visit(node.operand, o)

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        self.visit(node.left, o)
        self.visit(node.right, o)


    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        pass

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        pass

    def visit_identifier(self, node: "Identifier", o: Any = None):
        for scope in reversed(o["vars"]):
            if node.name in scope:
                break
        else:
            raise UndeclaredIdentifier(node.name)


    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        pass

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        pass

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        pass

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        pass
