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
    def check_program(self, node: "Program"):
        """Entry point for checking a program AST."""
        return self.visit_program(node)
    
    def visit_program(self, node: "Program", o: Any = None):
        structSeen = {}

        # Built in functions readInt, readFloat, readString, printInt, printFloat, printString
        funcSeen = {
            "readInt": FuncDecl(IntType(), "readInt", [], BlockStmt([])),
            "readFloat": FuncDecl(FloatType(), "readFloat", [], BlockStmt([])),
            "readString": FuncDecl(StringType(), "readString", [], BlockStmt([])),
            "printInt": FuncDecl(VoidType(), "printInt", [Param(IntType(), "value")], BlockStmt([])),
            "printFloat": FuncDecl(VoidType(), "printFloat", [Param(FloatType(), "value")], BlockStmt([])),
            "printString": FuncDecl(VoidType(), "printString", [Param(StringType(), "value")], BlockStmt([]))}

        env = {"structs": structSeen, "functions": funcSeen, "vars": [{}]}
        for decl in node.decls:
            if isinstance(decl, StructDecl):
                if decl.name in structSeen:
                    raise Redeclared("Struct", decl.name)
                structSeen[decl.name] = decl
                self.visit(decl, env)
            elif isinstance(decl, FuncDecl):
                if decl.name in funcSeen:
                    raise Redeclared("Function", decl.name)
                funcSeen[decl.name] = decl
                self.visit(decl, env)
        
        

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        seen = {}
        structEnv = {**o, "current_struct": node} # Add current struct to environment for member type checks
        for member in node.members: 
            if member.name in seen:
                raise Redeclared("Member", member.name)
            seen[member.name] = member
            member_type = self.visit(member, structEnv)

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        if node.member_type is None:
            raise TypeCannotBeInferred(node)
        else:
            # Type cannot be struct being declared
            if isinstance(node.member_type, StructType):
                if node.member_type.struct_name == o["current_struct"].name:
                    raise TypeCannotBeInferred(node)
            return self.visit(node.member_type, o)

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        paramSeen = {}
        for param in node.params:
            if param.name in paramSeen:
                raise Redeclared("Parameter", param.name)
            paramSeen[param.name] = param
            self.visit(param, o)

        return_type = self.visit(node.return_type, o)
        new_dict = {**o, "params": paramSeen, "current_func": node} # Add parameters to the current scope for the function body
        self.visit(node.body, new_dict)

    def visit_param(self, node: "Param", o: Any = None):
        return self.visit(node.param_type, o)

    # Type system
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


    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        localVars = {}
        inner = {**o, "vars": o["vars"] + [localVars]} # Create new scope o["vars": {}, {}, ...]
        
        for stmt in node.statements:
            result = self.visit(stmt, inner) #Avoid int x = x + 1

            if isinstance(stmt, VarDecl):
                if stmt.name in o.get("params", {}):
                    raise Redeclared("Variable", stmt.name) #Local variable cannot have the same name as a parameter
                if stmt.name in localVars:
                    raise Redeclared("Variable", stmt.name)
                localVars[stmt.name] = stmt
                # Update type if inference occurred
                if result and isinstance(result, VarDecl) and result.var_type:
                    localVars[stmt.name].var_type = result.var_type

            if isinstance(stmt, AssignExpr):
                if result and isinstance(result, dict):
                    for var_name, var_type in result.items():
                        if var_name in localVars:
                            localVars[var_name].var_type = var_type

            if isinstance(stmt, ReturnStmt):
                # Get nearest function from the environment
                func_return_type = inner.get("current_func").return_type if inner.get("current_func") else None
                
                if stmt.expr:
                    return_type = self.visit(stmt.expr, inner)
                    print(f"Checking return statement: expected {func_return_type}, got {return_type}")
                    if return_type is None:
                        raise TypeCannotBeInferred(node)
                    if isinstance(func_return_type, VoidType):
                        raise TypeMismatchInStatement(stmt)
                    if isinstance(return_type, VoidType):
                        raise TypeMismatchInStatement(stmt)
                    if isinstance(func_return_type, FloatType) and isinstance(return_type, IntType):
                        continue  # Allow implicit int to float conversion
                    if isinstance(func_return_type, IntType) and isinstance(return_type, FloatType):
                        continue  # Allow implicit float to int conversion
                    if type(func_return_type) != type(return_type):
                        print(f"Type mismatch in return statement: expected {func_return_type}, got {return_type}")
                        raise TypeMismatchInStatement(stmt)
                else:
                    if not isinstance(func_return_type, VoidType):
                        raise TypeMismatchInStatement(stmt)


        
        # After all statements, check for untyped autos
        for var_name, var_decl in localVars.items():
            print(f"Checking variable '{var_name}' for type inference... Current type: {var_decl.var_type}")
            if not var_decl.var_type:  # Still untyped auto
                raise TypeCannotBeInferred(node)
                

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        memberTypeList = []
        if not node.var_type:
            # print(f"Inferring type for variable '{node.name}' from initializer...")
            if node.init_value:
                value_type = self.visit(node.init_value, o)
                if value_type is None:
                    raise TypeCannotBeInferred(node)
                print(f"Inferred type for variable '{node.name}': {value_type}")
                node.var_type = value_type
            return node
        else:
            var_type = self.visit(node.var_type, o)
            if isinstance(var_type, VoidType):
                raise TypeCannotBeInferred(node)
            
            if  type(var_type) == StructDecl:
                # var_type is struct decl
                for member in var_type.members:
                    memberTypeList.append(self.visit(member, o))

            if node.init_value:
                value_type = self.visit(node.init_value, o)
                if isinstance(value_type, VoidType):
                    raise TypeCannotBeInferred(node)
                
                if isinstance(node.init_value, StructLiteral):
                    if len(memberTypeList) != len(value_type):
                        print(f"Struct literal initializer has wrong number of members: expected {len(memberTypeList)}, got {len(value_type)}")
                        raise TypeMismatchInStatement(node)
                    for member_type, val_type in zip(memberTypeList, value_type):
                        if type(member_type) != type(val_type):
                            print(f"Type mismatch in struct literal initializer: expected {member_type}, got {val_type}")
                            raise TypeMismatchInStatement(node)
                else:
                    # For non-struct literals, check that declared type matches initializer type
                    if var_type and value_type and type(var_type) != type(value_type):
                        print(f"Type mismatch in variable declaration: declared type is {var_type}, initializer type is {value_type}")
                        raise TypeMismatchInStatement(node)
        return node


    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        condition_type = self.visit(node.condition, o)
        if not isinstance(condition_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        whileEnv = {**o, "in_loop": True} # Add flag to indicate we are inside a loop for break/continue checks
        condition_type = self.visit(node.condition, o)
        if not isinstance(condition_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.body, whileEnv)

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        loopVars = {}
        forEnv = {**o, "vars": o["vars"] + [loopVars], "in_loop": True} # Create new scope for loop variables
        if node.init:
            initial = self.visit(node.init, forEnv)
            if isinstance(initial, VarDecl):
                loopVars[initial.name] = initial # Add loop variable to the loop scope
        if node.condition:
            condition_type = self.visit(node.condition, forEnv)
            if not isinstance(condition_type, IntType):
                raise TypeMismatchInStatement(node)
        if node.update:
            self.visit(node.update, forEnv)
        self.visit(node.body, forEnv)


    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        switchEnv = {**o, "in_switch": True} # Add flag to indicate we are inside a switch for break/continue checks
        var_type = self.visit(node.expr, switchEnv)
        if not isinstance(var_type, IntType):
            raise TypeMismatchInStatement(node)
        for case in node.cases:
            self.visit(case, switchEnv)
        if node.default_case:
            self.visit(node.default_case, switchEnv)

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        var_type = self.visit(node.expr, o)
        if not isinstance(var_type, IntType):
            raise TypeMismatchInStatement(node)
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        for stmt in node.statements:
            self.visit(stmt, o)
        

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        # Check if we are inside a loop or switch statement
        if not o.get("in_loop", False) and not o.get("in_switch", False):
            raise MustInLoop(node)


    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        # Check if we are inside a loop or switch statement
        if not o.get("in_loop", False):
            raise MustInLoop(node)

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        if node.expr:
            var_type = self.visit(node.expr, o)
            if not var_type:
                raise TypeCannotBeInferred(node)
            return var_type
        return VoidType()
        
            


    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        try:
            self.visit(node.expr, o)
        except TypeMismatchInExpression as e:
            # If the expression is an AssignExpr, convert to statement error
            if isinstance(node.expr, AssignExpr):
                raise TypeMismatchInStatement(node.expr)
            raise

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        left_type = self.visit(node.left, o)
        right_type = self.visit(node.right, o)
        
        # Resolve identifiers to their variable types
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
        
        # Check for untyped autos
        if left_type is None and right_type is None:
            raise TypeCannotBeInferred(node)
        
        if left_type is None or right_type is None:
            # One side is untyped, infer from the other
            inferred_type = left_type or right_type
            if isinstance(inferred_type, VoidType):
                raise TypeMismatchInExpression(node)
            if isinstance(inferred_type, StringType):
                raise TypeCannotBeInferred(node) # Cannot infer auto from string type 
            
            # Update auto variable with inferred type
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
        
        # Compare types

        if node.operator in ['+', '-', '*', '/']:
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                if isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
                    return FloatType()
                return IntType()
            else:
                print(f"Type mismatch in binary operation: left is {left_type}, right is {right_type}")
                raise TypeMismatchInExpression(node)

        if node.operator == '%':
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            else:
                print(f"Type mismatch in binary operation: left is {left_type}, right is {right_type}")
                raise TypeMismatchInExpression(node)
            
        if node.operator in ['==', '!=', '<', '>', '<=', '>=']:
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                return IntType()  # Relational operators return int (0 or 1)
            raise TypeMismatchInExpression(node)

        if node.operator in ['&&', '||']:
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()  # Logical operators return int (0 or 1)
            raise TypeMismatchInExpression(node)
        
        
            


        elif type(left_type) != type(right_type):
            print(f"Type mismatch: left is {left_type}, right is {right_type}")
            raise TypeMismatchInExpression(node)
        
        return left_type



    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        node_type = self.visit(node.operand, o)
        if node.operator == '!':
            if isinstance(node_type, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)
        if node.operator in ['++', '--']:
            if (not (isinstance(node.operand, Identifier) or isinstance(node.operand, MemberAccess))):
                raise TypeMismatchInExpression(node)
            if isinstance(node_type, IntType):
                return node_type
            else:
                print(f"Type mismatch in prefix operation: operand is {node_type}")
                raise TypeMismatchInExpression(node)
            

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        node_type = self.visit(node.operand, o)
        if node.operator in ['++', '--']:
            if (not (isinstance(node.operand, Identifier) or isinstance(node.operand, MemberAccess))):
                raise TypeMismatchInExpression(node)
            if isinstance(node_type, IntType):
                return node_type
            else:
                print(f"Type mismatch in postfix operation: operand is {node_type}")
                raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
        
        left_node = self.visit(node.lhs, o)
        value = self.visit(node.rhs, o)
        if left_node is None and isinstance(node.lhs, Identifier):
            # Try to infer type from the right-hand side

            # if value is None, we cannot infer type
            if value is None:
                raise TypeCannotBeInferred(node)
            for scope in reversed(o["vars"]):
                if node.lhs.name in scope:
                    scope[node.lhs.name].var_type = value
                    return value  # Return the inferred type for the variable
        
        # If right-hand side is a struct literal, validate member types
        if isinstance(node.rhs, StructLiteral):
            if not isinstance(left_node, StructType):
                print(f"Type mismatch in assignment: left is {left_node}, expected struct type for struct literal")
                raise TypeMismatchInExpression(node)
            
            struct_name = left_node.struct_name
            if struct_name in o["structs"]:
                struct_decl = o["structs"][struct_name]
                memberTypeList = []
                for member in struct_decl.members:
                    memberTypeList.append(self.visit(member, o))
                
                if len(memberTypeList) != len(value):
                    print(f"Struct literal has wrong number of members: expected {len(memberTypeList)}, got {len(value)}")
                    raise TypeMismatchInExpression(node)
                
                for member_type, val_type in zip(memberTypeList, value):
                    if type(member_type) != type(val_type):
                        print(f"Type mismatch in struct literal: expected {member_type}, got {val_type}")
                        raise TypeMismatchInExpression(node)
        else:
            # For non-struct literals, check that left type matches right type
            print(f"Checking assignment: left is {left_node}, right is {value}")
            if left_node and value and type(left_node) != type(value):
                print(f"Type mismatch in assignment: left is {left_node}, right is {value}")
                raise TypeMismatchInExpression(node)
            
            # If left_node and value are struct types, check if they are the same struct
            if left_node and value and isinstance(left_node, StructType) and isinstance(value, StructType):
                if left_node.struct_name != value.struct_name:
                    print(f"Struct type mismatch in assignment: left is {left_node.struct_name}, right is {value.struct_name}")
                    raise TypeMismatchInExpression(node)
        
        return left_node # Return the type of the left-hand side for potential inference in the block statement


    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj_type = self.visit(node.obj, o)
        if not isinstance(obj_type, StructType):
            print(f"Type mismatch in member access: object is {obj_type}, expected struct type")
            raise TypeMismatchInExpression(node)
        struct_decl = self.visit(obj_type, o)
        for member in struct_decl.members:
            if member.name == node.member:
                return self.visit(member.member_type, o)
        raise TypeMismatchInExpression(node)
        


    def visit_func_call(self, node: "FuncCall", o: Any = None):
        if node.name not in o["functions"]:
            raise UndeclaredFunction(node.name)
        func_decl = o["functions"][node.name]

        if len(node.args) != len(func_decl.params): # Number of arguments does not match number of parameters
            raise TypeMismatchInExpression(node)

        for param, arg in zip(func_decl.params, node.args):
            param_type = self.visit(param.param_type, o)
            arg_type = self.visit(arg, o)
            
            if arg_type is None:
                if not param_type is None:
                    # Infer parameter type from argument
                    for scope in reversed(o["vars"]):
                        if isinstance(arg, Identifier) and arg.name in scope:
                            scope[arg.name].var_type = param_type # Infer type for auto parameter
                            break
                    continue
                else:
                    raise TypeCannotBeInferred(node)
            if type(param_type) != type(arg_type):
                print(f"Type mismatch in function call argument: expected {param_type}, got {arg_type}")
                raise TypeMismatchInExpression(node)

        return o["functions"][node.name].return_type

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

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return StringType()
