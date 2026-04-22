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
    def check_program(self, node: "Program"):
        """Entry point for checking a program AST."""
        return self.visit_program(node)
    
    def visit_program(self, node: "Program", o: Any = None):
        structSeen = {}

        funcSeen = {
            "readInt": FuncDecl(IntType(), "readInt", [], BlockStmt([])),
            "readFloat": FuncDecl(FloatType(), "readFloat", [], BlockStmt([])),
            "readString": FuncDecl(StringType(), "readString", [], BlockStmt([])),
            "printInt": FuncDecl(VoidType(), "printInt", [Param(IntType(), "value")], BlockStmt([])),
            "printFloat": FuncDecl(VoidType(), "printFloat", [Param(FloatType(), "value")], BlockStmt([])),
            "printString": FuncDecl(VoidType(), "printString", [Param(StringType(), "value")], BlockStmt([]))}

        env = {"structs": structSeen, "functions": funcSeen, "vars": [{}], "inferred_return_types": {}}
        for decl in node.decls:
            if isinstance(decl, StructDecl):
                if decl.name in structSeen:
                    raise Redeclared("Struct", decl.name)
                self.visit(decl, env)
                structSeen[decl.name] = decl
            elif isinstance(decl, FuncDecl):
                if decl.name in funcSeen:
                    raise Redeclared("Function", decl.name)
                funcSeen[decl.name] = decl
                self.visit(decl, env)
        
    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        seen = {}
        structEnv = {**o, "current_struct": node}
        for member in node.members: 
            if member.name in seen:
                raise Redeclared("Member", member.name)
            seen[member.name] = member
            member_type = self.visit(member, structEnv)

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        if node.member_type is None:
            raise TypeCannotBeInferred(node)
        else:
            return self.visit(node.member_type, o)

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        paramSeen = {}
        for param in node.params:
            if param.name in paramSeen:
                raise Redeclared("Parameter", param.name)
            paramSeen[param.name] = param
            self.visit(param, o)

        declared_return_type = None
        if node.return_type:
            declared_return_type = self.visit(node.return_type, o)
        
        if "inferred_return_types" not in o:
            o["inferred_return_types"] = {}
        
        inferred_container = [None]
        
        new_dict = {**o, "params": paramSeen, "current_func": node, "current_func_name": node.name, "declared_return_type": declared_return_type, "inferred_return_type_container": inferred_container}
        self.visit(node.body, new_dict)
        
        if declared_return_type is None and inferred_container[0] is not None:
            o["inferred_return_types"][node.name] = inferred_container[0]

    def visit_param(self, node: "Param", o: Any = None):
        return self.visit(node.param_type, o)

    def visit_int_type(self, node: "IntType", o: Any = None):
        return IntType()

    def visit_float_type(self, node: "FloatType", o: Any = None):
        return FloatType()

    def visit_string_type(self, node: "StringType", o: Any = None):
        return StringType()

    def visit_void_type(self, node: "VoidType", o: Any = None):
        return VoidType()

    def visit_struct_type(self, node: "StructType", o: Any = None):
        if node.struct_name not in o["structs"]:
            raise UndeclaredStruct(node.struct_name)
        return o["structs"][node.struct_name]

    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        localVars = {}
        inner = {**o, "vars": o["vars"] + [localVars]}
        
        for stmt in node.statements:
            result = self.visit(stmt, inner)

            if isinstance(stmt, VarDecl):
                if stmt.name in o.get("params", {}):
                    raise Redeclared("Variable", stmt.name)
                if stmt.name in localVars:
                    raise Redeclared("Variable", stmt.name)
                localVars[stmt.name] = stmt
                if result and isinstance(result, VarDecl) and result.var_type:
                    localVars[stmt.name].var_type = result.var_type

            if isinstance(stmt, AssignExpr):
                if result and isinstance(result, dict):
                    for var_name, var_type in result.items():
                        if var_name in localVars:
                            localVars[var_name].var_type = var_type

            if isinstance(stmt, ReturnStmt):
                self.visit(stmt, inner)

        for var_name, var_decl in localVars.items():
            if not var_decl.var_type:
                raise TypeCannotBeInferred(node)
                
    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        if not node.var_type:
            if node.init_value:
                if isinstance(node.init_value, StructLiteral):
                    self._validate_struct_literal(None, node.init_value.values, node.init_value, o)
                
                value_type = self.visit(node.init_value, o)
                if value_type is None:
                    raise TypeCannotBeInferred(node)
                node.var_type = value_type
            return node
        else:
            var_type = self.visit(node.var_type, o)
            if isinstance(var_type, VoidType):
                raise TypeCannotBeInferred(node)

            if node.init_value:
                value_type = self.visit(node.init_value, o)
                if isinstance(value_type, VoidType):
                    raise TypeCannotBeInferred(node)
                
                if isinstance(node.init_value, StructLiteral):
                    self._validate_struct_literal(var_type, node.init_value.values, node.init_value, o)
                else:
                    if value_type is None:
                        if isinstance(node.init_value, Identifier) and isinstance(var_type, (IntType, FloatType)):
                            for scope in reversed(o["vars"]):
                                if node.init_value.name in scope:
                                    var_obj = scope[node.init_value.name]
                                    if var_obj.var_type is None:
                                        var_obj.var_type = var_type
                                        break
                        else:
                            raise TypeMismatchInStatement(node)
                    elif var_type and type(var_type) != type(value_type):
                        raise TypeMismatchInStatement(node)
        return node

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        condition_type = self.visit(node.condition, o)
        if condition_type is None and isinstance(node.condition, Identifier):
            for scope in reversed(o["vars"]):
                if node.condition.name in scope:
                    scope[node.condition.name].var_type = IntType()
                    condition_type = IntType()
                    break
        if not isinstance(condition_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        whileEnv = {**o, "in_loop": True}
        condition_type = self.visit(node.condition, o)
        if condition_type is None and isinstance(node.condition, Identifier):
            for scope in reversed(o["vars"]):
                if node.condition.name in scope:
                    scope[node.condition.name].var_type = IntType()
                    condition_type = IntType()
                    break
        if not isinstance(condition_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.body, whileEnv)

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        loopVars = {}
        forEnv = {**o, "vars": o["vars"] + [loopVars], "in_loop": True}
        if node.init:
            initial = self.visit(node.init, forEnv)
            if isinstance(initial, VarDecl):
                loopVars[initial.name] = initial
        if node.condition:
            condition_type = self.visit(node.condition, forEnv)
            if not isinstance(condition_type, IntType):
                raise TypeMismatchInStatement(node)
        if node.update:
            self.visit(node.update, forEnv)
        self.visit(node.body, forEnv)

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        switchEnv = {**o, "in_switch": True}
        var_type = self.visit(node.expr, switchEnv)
        if var_type is None and isinstance(node.expr, Identifier):
            for scope in reversed(o["vars"]):
                if node.expr.name in scope:
                    scope[node.expr.name].var_type = IntType()
                    var_type = IntType()
                    break
        if not isinstance(var_type, IntType):
            raise TypeMismatchInStatement(node)
        
        caseVars = {}
        switchEnv = {**switchEnv, "vars": o["vars"] + [caseVars]}
        
        try:
            for case in node.cases:
                self.visit(case, switchEnv)
            if node.default_case:
                self.visit(node.default_case, switchEnv)
        except TypeMismatchInStatement as e:
            if isinstance(e.stmt, CaseStmt):
                raise TypeMismatchInStatement(node)
            raise
        except TypeCannotBeInferred as e:
            if isinstance(e.expr, (CaseStmt, DefaultStmt, VarDecl)):
                raise TypeCannotBeInferred(node)
            raise
        
        for var_name, var_decl in caseVars.items():
            if not var_decl.var_type:
                raise TypeCannotBeInferred(node)

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        var_type = self.visit(node.expr, o)
        
        if isinstance(node.expr, Identifier):
            raise TypeMismatchInStatement(node)
        
        if not isinstance(var_type, IntType):
            raise TypeMismatchInStatement(node)
        for stmt in node.statements:
            result = self.visit(stmt, o)
            if isinstance(stmt, VarDecl):
                caseVars = o["vars"][-1]
                if stmt.name in caseVars:
                    raise Redeclared("Variable", stmt.name)
                caseVars[stmt.name] = stmt
                if result and isinstance(result, VarDecl) and result.var_type:
                    caseVars[stmt.name].var_type = result.var_type

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        for stmt in node.statements:
            result = self.visit(stmt, o)
            if isinstance(stmt, VarDecl):
                caseVars = o["vars"][-1]
                if stmt.name in caseVars:
                    raise Redeclared("Variable", stmt.name)
                caseVars[stmt.name] = stmt
                if result and isinstance(result, VarDecl) and result.var_type:
                    caseVars[stmt.name].var_type = result.var_type
        
    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        if not o.get("in_loop", False) and not o.get("in_switch", False):
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        if not o.get("in_loop", False):
            raise MustInLoop(node)

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        declared_return_type = o.get("declared_return_type")
        inferred_container = o.get("inferred_return_type_container", [None])
        
        if node.expr:
            if isinstance(node.expr, StructLiteral):
                if declared_return_type is not None:
                    try:
                        self._validate_struct_literal(declared_return_type, node.expr.values, node.expr, o)
                    except TypeMismatchInExpression:
                        raise
                    var_type = declared_return_type
                elif inferred_container[0] is None:
                    raise TypeCannotBeInferred(node)
                else:
                    var_type = self.visit(node.expr, o)
            else:
                var_type = self.visit(node.expr, o)
            
            if not var_type:
                raise TypeCannotBeInferred(node)
            
            if declared_return_type is not None:
                if not isinstance(node.expr, StructLiteral) and type(var_type) != type(declared_return_type):
                    raise TypeMismatchInStatement(node)
            elif inferred_container[0] is None:
                if not isinstance(node.expr, StructLiteral):
                    inferred_container[0] = var_type
            else:
                if type(var_type) != type(inferred_container[0]):
                    raise TypeMismatchInStatement(node)
            
            return var_type
        else:
            if declared_return_type is not None:
                if not isinstance(declared_return_type, VoidType):
                    raise TypeMismatchInStatement(node)
            elif inferred_container[0] is None:
                inferred_container[0] = VoidType()
            else:
                if not isinstance(inferred_container[0], VoidType):
                    raise TypeMismatchInStatement(node)
            
            return VoidType()
        
    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        try:
            expr_result = self.visit(node.expr, o)
        except TypeMismatchInExpression as e:
            if isinstance(node.expr, AssignExpr) and e.expr == node.expr:
                if not isinstance(node.expr.rhs, AssignExpr) and not isinstance(node.expr.rhs, StructLiteral):
                    raise TypeMismatchInStatement(node)
            raise
        
        if isinstance(node.expr, AssignExpr) and isinstance(node.expr.lhs, Identifier) and isinstance(node.expr.rhs, StringLiteral):
            for scope in reversed(o["vars"]):
                if node.expr.lhs.name in scope:
                    var = scope[node.expr.lhs.name]
                    if isinstance(var.var_type, StringType):
                        raise TypeMismatchInStatement(node)
                    break

    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        left_type = self.visit(node.left, o)
        right_type = self.visit(node.right, o)
        
        if left_type is None and isinstance(node.left, Identifier):
            for scope in reversed(o["vars"]):
                if node.left.name in scope:
                    left_type = scope[node.left.name].var_type
                    break
        
        if right_type is None and isinstance(node.right, Identifier):
            for scope in reversed(o["vars"]):
                if node.right.name in scope:
                    right_type = scope[node.right.name].var_type
                    break
        
        if left_type is None and right_type is None:
            if node.operator in ['&&', '||', '%']:
                inferred_type = IntType()
                if isinstance(node.left, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.left.name in scope:
                            scope[node.left.name].var_type = inferred_type
                            break
                if isinstance(node.right, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.right.name in scope:
                            scope[node.right.name].var_type = inferred_type
                            break
                return inferred_type if node.operator == '%' else IntType()
            elif node.operator in ['+', '-', '*', '/']:
                if isinstance(node.left, IntLiteral) and isinstance(node.right, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.right.name in scope:
                            scope[node.right.name].var_type = IntType()
                            break
                    right_type = IntType()
                    left_type = IntType()
                elif isinstance(node.right, IntLiteral) and isinstance(node.left, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.left.name in scope:
                            scope[node.left.name].var_type = IntType()
                            break
                    left_type = IntType()
                    right_type = IntType()
                else:
                    raise TypeCannotBeInferred(node)
            else:
                raise TypeCannotBeInferred(node)
        
        if left_type is None or right_type is None:
            if node.operator in ['==', '!=', '<', '>', '<=', '>=']:
                raise TypeCannotBeInferred(node)
            elif node.operator in ['+', '-', '*', '/']:
                typed_operand_is_literal = False
                
                if left_type is not None and right_type is None:
                    typed_operand_is_literal = isinstance(node.left, (IntLiteral, FloatLiteral))
                elif right_type is not None and left_type is None:
                    typed_operand_is_literal = isinstance(node.right, (IntLiteral, FloatLiteral))
                
                if not typed_operand_is_literal:
                    raise TypeCannotBeInferred(node)
                
                inferred_type = left_type or right_type
                if isinstance(inferred_type, VoidType):
                    raise TypeMismatchInExpression(node)
                if isinstance(inferred_type, FloatType):
                    raise TypeCannotBeInferred(node)
                if isinstance(inferred_type, StringType):
                    raise TypeCannotBeInferred(node)
                
                if left_type is None and isinstance(node.left, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.left.name in scope:
                            scope[node.left.name].var_type = inferred_type
                            break
                
                if right_type is None and isinstance(node.right, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.right.name in scope:
                            scope[node.right.name].var_type = inferred_type
                            break
                
                left_type = left_type or inferred_type
                right_type = right_type or inferred_type
            elif node.operator in ['&&', '||']:
                inferred_type = left_type or right_type
                if isinstance(inferred_type, VoidType):
                    raise TypeMismatchInExpression(node)
                if left_type is None and isinstance(node.left, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.left.name in scope:
                            scope[node.left.name].var_type = inferred_type
                            break
                
                if right_type is None and isinstance(node.right, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.right.name in scope:
                            scope[node.right.name].var_type = inferred_type
                            break
                
                left_type = left_type or inferred_type
                right_type = right_type or inferred_type
            elif node.operator == '%':
                inferred_type = left_type or right_type
                if isinstance(inferred_type, VoidType):
                    raise TypeMismatchInExpression(node)
                if left_type is None and isinstance(node.left, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.left.name in scope:
                            scope[node.left.name].var_type = inferred_type
                            break
                
                if right_type is None and isinstance(node.right, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.right.name in scope:
                            scope[node.right.name].var_type = inferred_type
                            break
                
                left_type = left_type or inferred_type
                right_type = right_type or inferred_type
        
        if node.operator in ['+', '-', '*', '/']:
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                if isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
                    return FloatType()
                return IntType()
            else:
                raise TypeMismatchInExpression(node)

        if node.operator == '%':
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            else:
                raise TypeMismatchInExpression(node)
            
        if node.operator in ['==', '!=', '<', '>', '<=', '>=']:
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                return IntType()
            raise TypeMismatchInExpression(node)

        if node.operator in ['&&', '||']:
            if left_type is None or right_type is None:
                inferred_type = IntType()
                if left_type is None and isinstance(node.left, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.left.name in scope:
                            scope[node.left.name].var_type = inferred_type
                            break
                if right_type is None and isinstance(node.right, Identifier):
                    for scope in reversed(o["vars"]):
                        if node.right.name in scope:
                            scope[node.right.name].var_type = inferred_type
                            break
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)
        
        elif type(left_type) != type(right_type):
            raise TypeMismatchInExpression(node)
        
        return left_type

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        node_type = self.visit(node.operand, o)
        if node.operator == '!':
            if node_type is None and isinstance(node.operand, Identifier):
                for scope in reversed(o["vars"]):
                    if node.operand.name in scope:
                        scope[node.operand.name].var_type = IntType()
                        node_type = IntType()
                        break
            if isinstance(node_type, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)
        if node.operator in ['+', '-']:
            if node_type is None:
                raise TypeCannotBeInferred(node)
            if isinstance(node_type, (IntType, FloatType)):
                return node_type
            raise TypeMismatchInExpression(node)
        if node.operator in ['++', '--']:
            if (not (isinstance(node.operand, Identifier) or isinstance(node.operand, MemberAccess))):
                raise TypeMismatchInExpression(node)
            if node_type is None and isinstance(node.operand, Identifier):
                for scope in reversed(o["vars"]):
                    if node.operand.name in scope:
                        scope[node.operand.name].var_type = IntType()
                        node_type = IntType()
                        break
            if isinstance(node_type, IntType):
                return node_type
            else:
                raise TypeMismatchInExpression(node)
            
    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        node_type = self.visit(node.operand, o)
        if node.operator in ['++', '--']:
            if (not (isinstance(node.operand, Identifier) or isinstance(node.operand, MemberAccess))):
                raise TypeMismatchInExpression(node)
            if node_type is None and isinstance(node.operand, Identifier):
                for scope in reversed(o["vars"]):
                    if node.operand.name in scope:
                        scope[node.operand.name].var_type = IntType()
                        node_type = IntType()
                        break
            if isinstance(node_type, IntType):
                return node_type
            else:
                raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
        
        left_node = self.visit(node.lhs, o)
        value = self.visit(node.rhs, o)
        
        if left_node is None and isinstance(node.lhs, Identifier):
            if value is None:
                raise TypeCannotBeInferred(node)
            
            for scope in reversed(o["vars"]):
                if node.lhs.name in scope:
                    scope[node.lhs.name].var_type = value
                    return value
        
        if value is None and isinstance(node.rhs, Identifier) and left_node is not None:
            for scope in reversed(o["vars"]):
                if node.rhs.name in scope:
                    scope[node.rhs.name].var_type = left_node
                    value = left_node
                    break
        
        if isinstance(node.rhs, StructLiteral):
            if not isinstance(left_node, StructType):
                raise TypeMismatchInExpression(node.rhs)
            
            struct_name = left_node.struct_name
            if struct_name in o["structs"]:
                struct_decl = o["structs"][struct_name]
                self._validate_struct_literal(struct_decl, node.rhs.values, node.rhs, o)
        else:
            if left_node and value and type(left_node) != type(value):
                raise TypeMismatchInExpression(node)
            
            if left_node and value and isinstance(left_node, StructType) and isinstance(value, StructType):
                if left_node.struct_name != value.struct_name:
                    raise TypeMismatchInExpression(node)
        
        return left_node

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj_type = self.visit(node.obj, o)

        if not isinstance(obj_type, StructType):
            raise TypeMismatchInExpression(node)
        struct_decl = self.visit(obj_type, o)
        for member in struct_decl.members:
            if member.name == node.member:
                return self.visit(member.member_type, o)
        raise TypeMismatchInExpression(node)
        
    def _validate_struct_literal(self, expected_struct_decl: StructDecl, arg_values: List, arg_node: StructLiteral, o: Any) -> None:
        
        if expected_struct_decl is None:
            raise TypeCannotBeInferred(arg_node)
        
        memberTypeList = []
        for member in expected_struct_decl.members:
            set_current_struct = {**o, "current_struct": expected_struct_decl}
            memberTypeList.append(self.visit(member, set_current_struct))
        
        if len(memberTypeList) != len(arg_values):
            raise TypeMismatchInExpression(arg_node)
        
        for member_type, arg_value_node in zip(memberTypeList, arg_values):
            arg_type = self.visit(arg_value_node, o)
            
            if isinstance(member_type, StructDecl) and isinstance(arg_value_node, StructLiteral):
                self._validate_struct_literal(member_type, arg_value_node.values, arg_value_node, o)
            elif arg_type is None:
                if isinstance(member_type, VoidType):
                    raise TypeCannotBeInferred(arg_value_node)
                
                if isinstance(arg_value_node, Identifier):
                    for scope in reversed(o["vars"]):
                        if arg_value_node.name in scope:
                            scope[arg_value_node.name].var_type = member_type
                            break
            elif type(member_type) != type(arg_type):
                raise TypeMismatchInExpression(arg_node)

    def _are_same_struct_type(self, expected_type: Any, actual_type: Any) -> bool:
        
        if isinstance(expected_type, StructDecl) and isinstance(actual_type, StructType):
            return expected_type.name == actual_type.struct_name
        elif isinstance(expected_type, StructDecl) and isinstance(actual_type, StructDecl):
            return expected_type.name == actual_type.name
        return False

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        if node.name not in o["functions"]:
            raise UndeclaredFunction(node.name)
        func_decl = o["functions"][node.name]

        if len(node.args) != len(func_decl.params):
            raise TypeMismatchInExpression(node)

        for param, arg in zip(func_decl.params, node.args):
            param_type = self.visit(param.param_type, o)
            arg_type = self.visit(arg, o)
            
            if arg_type is None:
                if param_type is not None:
                    for scope in reversed(o["vars"]):
                        if isinstance(arg, Identifier) and arg.name in scope:
                            scope[arg.name].var_type = param_type
                            break
                    continue
                else:
                    raise TypeCannotBeInferred(node)
            
            if isinstance(arg, StructLiteral):
                if not isinstance(param_type, StructDecl):
                    raise TypeMismatchInExpression(arg)
                self._validate_struct_literal(param_type, arg.values, arg, o)
            
            else:
                if isinstance(param_type, StructDecl):
                    if not self._are_same_struct_type(param_type, arg_type):
                        raise TypeMismatchInExpression(node)
                else:
                    if type(param_type) != type(arg_type):
                        raise TypeMismatchInExpression(node)

        func_decl = o["functions"][node.name]
        return_type = func_decl.return_type
        
        if return_type is None:
            if node.name == o.get("current_func_name"):
                inferred_container = o.get("inferred_return_type_container", [None])
                if inferred_container[0] is not None:
                    return_type = inferred_container[0]
                else:
                    raise TypeCannotBeInferred(node)
            elif node.name in o.get("inferred_return_types", {}):
                return_type = o["inferred_return_types"][node.name]
            else:
                raise TypeCannotBeInferred(node)
        
        return return_type

    def visit_identifier(self, node: "Identifier", o: Any = None):
        for scope in reversed(o["vars"]):
            if node.name in scope:
                return scope[node.name].var_type
        if node.name in o.get("params", {}):
            return o["params"][node.name].param_type
        raise UndeclaredIdentifier(node.name)
        
    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        typeList = []
        for value in node.values:
            typeList.append(self.visit(value, o))
        return typeList

    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return StringType()
