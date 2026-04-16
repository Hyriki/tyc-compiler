"""
Test cases for TyC Static Semantic Checker

This module contains test cases for the static semantic checker.
100 test cases covering all error types and comprehensive scenarios.
"""

from tests.utils import Checker
from src.utils.nodes import (
    Program,
    FuncDecl,
    BlockStmt,
    VarDecl,
    AssignExpr,
    ExprStmt,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    Identifier,
    BinaryOp,
    MemberAccess,
    FuncCall,
    StructDecl,
    MemberDecl,
    Param,
    ReturnStmt,
)


# ============================================================================
# Valid Programs (test_001 - test_010)
# ============================================================================


def test_001():
    """Test a valid program that should pass all checks"""
    source = """
void main() {
    int x = 5;
    int y = x + 1;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_002():
    """Test valid program with auto type inference"""
    source = """
void main() {
    auto x = 10;
    auto y = 3.14;
    auto z = x + y;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_003():
    """Test valid program with functions"""
    source = """
int add(int x, int y) {
    return x + y;
}
void main() {
    int sum = add(5, 3);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_004():
    """Test valid program with struct"""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_005():
    """Test valid program with nested blocks"""
    source = """
void main() {
    int x = 10;
    {
        int y = 20;
        int z = x + y;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_006():
    source = """ void valid1() {
    auto x = 10;         // Valid: type inferred as int from literal
    auto y = 3.14;       // Valid: type inferred as float from literal
    auto msg = "hello";  // Valid: type inferred as string from literal
} """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_007():
    source = """ void valid2() {
    auto a;
    a = 10;        // Valid: type inferred as int from assignment (first usage)

    auto b;
    b = 3.14;      // Valid: type inferred as float from assignment (first usage)
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_008():
    source = """
    void unusedAuto(){
    auto x; //
}

 """
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, x)]))"
    assert Checker(source).check_from_source() == expected

def test_009():
    source = """ void valid2() {
    auto a;
    a = 10;        // Valid: type inferred as int from assignment (first usage)

    auto b = a;      // Valid: type inferred as int from assignment (first usage)
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_010():
    source = """void func() {
    auto x;
    return x;
      // TypeCannotBeInferred(ReturnStmt(return Identifier(x)))
}
"""
    expected = "TypeCannotBeInferred(ReturnStmt(return Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_011():
    source = """void func() {
    auto x;
    auto y;
    return x + y;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_012():
    source = """

void valid3() {
    auto x;
    x = readInt();
    auto y;
    int temp = 10;
    y = temp + 5;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_013():
    source = """
    void valid4() {
    auto value;
    auto result = value + 5;  // Valid: value inferred as int (other operand is IntLiteral 5)
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_014():
    source = """
void circular() {
    auto a;
    auto b;
    a = b;  // TypeCannotBeInferred(AssignExpr(Identifier(a) = Identifier(b)))
    // (A following `b = a` would be the same class of problem; it is not reported in the same run after the error above.)
}"""
    expected = "TypeCannotBeInferred(AssignExpr(Identifier(a) = Identifier(b)))"
    assert Checker(source).check_from_source() == expected

def test_015():
    source = """
    void compare_autos() {
    auto x;
    auto y;
    int result = x < y;  // TypeCannotBeInferred(BinaryOp(Identifier(x), <, Identifier(y)))
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), <, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_016():
    source = """
    void valid6() {
        auto x;
        printInt(x);  // Valid: type inferred as int from printInt(int) parameter type
        //TODO will the x become int or still auto?
    }  """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_017():
    source = """
    void valid5() {
    int a = 10;
    float b = 3.14;
    auto sum = a + b;  // Valid: type inferred as float from expression
}   """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_018():
    source = """
    void whileError() {
    float f = 1.5;
    while (f) {  // Error: TypeMismatchInStatement at while statement
        printFloat(f);
    }
}"""
    expected = "TypeMismatchInStatement(WhileStmt(while Identifier(f) do BlockStmt([ExprStmt(FuncCall(printFloat, [Identifier(f)]))])))"
    assert Checker(source).check_from_source() == expected

def test_019():
    source = """
    void whileError() {
    int f = 1;
    while (f) {  // Error: TypeMismatchInStatement at while statement
        printInt(f);
        auto x;
        x = f;  // Valid: type inferred as int from assignment
    }
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_020():
    source = """
    void ifError() {
    float f = 1.5;
    if (f) {  // Error: TypeMismatchInStatement at if statement
        printFloat(f);
    }
}"""
    expected = "TypeMismatchInStatement(IfStmt(if Identifier(f) then BlockStmt([ExprStmt(FuncCall(printFloat, [Identifier(f)]))])))"
    assert Checker(source).check_from_source() == expected

def test_021():
    source = """
    void forError() {
    float f = 1.5;
    for (int i = 0; f; i = i + 1) {  // Error: TypeMismatchInStatement at for statement
        printFloat(f);
    }
}"""
    expected = "TypeMismatchInStatement(ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); Identifier(f); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(FuncCall(printFloat, [Identifier(f)]))])))"
    assert Checker(source).check_from_source() == expected

def test_022():
    source = """
    void assignmentError() {
    int x = 10;
    string text = "hello";
    float f = 3.14;
    
    x = text;    // Error: TypeMismatchInStatement at assignment
    text = x;    // Error: TypeMismatchInStatement at assignment
    f = x;       // Error: TypeMismatchInStatement at assignment (no int to float coercion in assignment)
}"""
    expected = "TypeMismatchInStatement(AssignExpr(Identifier(x) = Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_023():
    source = """
    // Error: Struct assignment type mismatch
    struct Point {
        int x;
        int y;
    };

    struct Person {
        string name;
        int age;
    };

    void structError() {
        Point p;
        Person person;
        p = person;  // Error: TypeMismatchInStatement at assignment
    }"""
    expected = "TypeMismatchInStatement(AssignExpr(Identifier(p) = Identifier(person)))"
    assert Checker(source).check_from_source() == expected

def test_024():
    source = """
    // Error: Switch expression type mismatch
void switchError() {
    float f = 3.14;
    switch (f) {  // Error: TypeMismatchInStatement at switch statement
        case 1: break;
    }
}"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch Identifier(f) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])]))"
    assert Checker(source).check_from_source() == expected

def test_025():
    source = """
    // Error: Switch expression type mismatch
void switchError() {
    int f = 1;
    switch (f) {  // Error: TypeMismatchInStatement at switch statement
        case 1.5: break;
    }
}"""
    expected = "TypeMismatchInStatement(CaseStmt(case FloatLiteral(1.5): [BreakStmt()]))"
    assert Checker(source).check_from_source() == expected

def test_026():
    source = """
    void returnStmt(){
        return;
    }
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_027():
    source = """
    int getValue() {
    return "invalid";  // Error: TypeMismatchInStatement at return statement
}"""
    expected = "TypeMismatchInStatement(ReturnStmt(return StringLiteral('invalid')))"
    assert Checker(source).check_from_source() == expected

def test_028():
    source = """
    string getText() {
    return 42;  // Error: TypeMismatchInStatement at return statement
}"""
    expected = "TypeMismatchInStatement(ReturnStmt(return IntLiteral(42)))"
    assert Checker(source).check_from_source() == expected

def test_029():
    source = """
    void returnError() {
    return 10;  // Error: TypeMismatchInStatement at return statement (void function cannot return value)
}"""
    expected = "TypeMismatchInStatement(ReturnStmt(return IntLiteral(10)))"
    assert Checker(source).check_from_source() == expected

def test_030():
    source = """
    int returnVoidError() {
    return;  // Error: TypeMismatchInStatement at return statement (non-void function must return value)
}"""
    expected = "TypeMismatchInStatement(ReturnStmt(return))"
    assert Checker(source).check_from_source() == expected

def test_031():
    source = """
    void returnError() {
        
    }
    int returnVoidError() {
    return returnError();  // Error: TypeMismatchInStatement at return statement (non-void function must return value)
}"""
    expected = "TypeMismatchInStatement(ReturnStmt(return FuncCall(returnError, [])))"
    assert Checker(source).check_from_source() == expected

def test_032():
    source = """
    // Valid: Proper type matching
struct Point {
    int x;
    int y;
};
void valid() {
    int x = 10;
    int y = 20;
    if (x < y) {  // Valid: condition is int
        x = y;    // Valid: both sides are int
    }
    
    Point p1 = {10, 20};
    Point p2 = {30, 40};
    p1 = p2;      // Valid: both sides are Point
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_033():
    source = """
    // Valid: Assignment expression in expression context
    struct Point {
        int x;
        int y;
    };
void assignmentExpressionValid() {
    auto x;
    int y = (x = 5) + 7;  // Valid: assignment expression returns value of x (after assignment)
    // y = 12, x = 5
    
    int a;
    int b;
    int c;
    a = b = c = 10;  // Valid: right-associative chained assignment
    // All a, b, c are 10
    
    
    Point p;
    int result = (p.x = 5) + 3;  // Valid: member access assignment expression
    // result = 8, p.x = 5
}"""
    # expected = "TypeMismatchInStatement(AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = IntLiteral(10))))"
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_034():
    source = """
    void expressionError(){
    string x;
    string y;
    int a = x + y;  // Error: TypeMismatchInExpression at binary operation (no string + string)
    }"""
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), +, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_035():
    source = """
    // Error: Arithmetic operation type mismatch
void arithmeticError() {
    int x = 5;
    string text = "hello";
    
    int sum = x + text;     // Error: TypeMismatchInExpression at binary operation
    float result = x * text; // Error: TypeMismatchInExpression at binary operation
}"""
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), +, Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_036():
    source = """
    // Error: Modulus with non-int operands
void modulusError() {
    float f = 3.14;
    int x = 10;
    
    //int result = f % x;       Error: TypeMismatchInExpression at binary operation (float % int)
    int result2 = x % f;     // Error: TypeMismatchInExpression at binary operation (int % float)
}"""
    # expected = "TypeMismatchInExpression(BinaryOp(Identifier(f), %, Identifier(x)))"
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), %, Identifier(f)))"
    assert Checker(source).check_from_source() == expected

def test_037():
    source = """
    // Error: Relational operation type mismatch
void relationalError() {
    int x = 10;
    string text = "hello";
    
    int result = x < text;   // Error: TypeMismatchInExpression at binary operation
    int equal = text == x;   // Error: TypeMismatchInExpression at binary operation
}"""
    # expected = "TypeMismatchInExpression(BinaryOp(Identifier(text), ==, Identifier(x)))"
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), <, Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_038():
    source = """
    // Error: Logical operation type mismatch
void logicalError() {
    float f = 3.14;
    int x = 10;
    
    //int result = f && x;     // Error: TypeMismatchInExpression at binary operation
    int not = !f;            // Error: TypeMismatchInExpression at unary operation
}"""
    # expected = "TypeMismatchInExpression(BinaryOp(Identifier(f), &&, Identifier(x)))"
    expected = "TypeMismatchInExpression(PrefixOp(!Identifier(f)))"
    assert Checker(source).check_from_source() == expected

def test_039():
    source = """
    // Error: Increment/decrement on non-int
void incrementError() {
    float f = 3.14;
    //++f;                     // Error: TypeMismatchInExpression at unary operation
    f++;                     // Error: TypeMismatchInExpression at postfix operation
}"""
    # expected = "TypeMismatchInExpression(PrefixOp(++Identifier(f)))"
    expected = "TypeMismatchInExpression(PostfixOp(Identifier(f)++))"
    assert Checker(source).check_from_source() == expected

def test_040():
    source = """
    // Error: Increment/decrement on literal or expression
void incrementOperandError() {
    int x = 5;
    ++5;                     // Error: TypeMismatchInExpression at unary operation (cannot increment literal)
    --(x + 1);               // Error: TypeMismatchInExpression at unary operation (cannot increment expression)
    (x + 2)++;               // Error: TypeMismatchInExpression at postfix operation (cannot increment expression)
}"""
    expected = "TypeMismatchInExpression(PrefixOp(++IntLiteral(5)))"
    assert Checker(source).check_from_source() == expected

def test_041():
    source = """
    // Error: Increment/decrement on literal or expression
void incrementOperandError() {
    int x = 5;
    //++5;                     // Error: TypeMismatchInExpression at unary operation (cannot increment literal)
    --(x + 1);               // Error: TypeMismatchInExpression at unary operation (cannot increment expression)
    (x + 2)++;               // Error: TypeMismatchInExpression at postfix operation (cannot increment expression)
}"""
    expected = "TypeMismatchInExpression(PrefixOp(--BinaryOp(Identifier(x), +, IntLiteral(1))))"
    assert Checker(source).check_from_source() == expected

def test_042():
    source = """
    // Error: Increment/decrement on literal or expression
void incrementOperandError() {
    int x = 5;
    //++5;                     // Error: TypeMismatchInExpression at unary operation (cannot increment literal)
    //--(x + 1);               // Error: TypeMismatchInExpression at unary operation (cannot increment expression)
    (x + 2)++;               // Error: TypeMismatchInExpression at postfix operation (cannot increment expression)
}"""
    expected = "TypeMismatchInExpression(PostfixOp(BinaryOp(Identifier(x), +, IntLiteral(2))++))"
    assert Checker(source).check_from_source() == expected

def test_043():
    source = """
    // Error: Member access on non-struct
struct Point {
        int x;
        int y;
    };
void memberAccessError() {
    int x = 10;
    int value = x.x;    // Error: TypeMismatchInExpression at member access
    
    
    
    Point p = {10, 20};
    int invalid = p.x;       // Error: TypeMismatchInExpression at member access (z doesn't exist)
}"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(x).x))"
    assert Checker(source).check_from_source() == expected

def test_044():
    source = """
    // Error: Member access on non-struct
    struct Point {
        int x;
        int y;
    };
void memberAccessError() {
    int x = 10;
    //int value = x.member;    // Error: TypeMismatchInExpression at member access
    
    
    Point p = {10, 20};
    int invalid = p.z;       // Error: TypeMismatchInExpression at member access (z doesn't exist)
}"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(p).z))"
    assert Checker(source).check_from_source() == expected

def test_045():
    source = """
    // Error: Function call argument type mismatch
void process(int x) { }

void callError() {
    string text = "123";
    process(text);           // Error: TypeMismatchInExpression at function call
}

int add(int x, int y) {
    return x + y;
}"""
    expected = "TypeMismatchInExpression(FuncCall(process, [Identifier(text)]))"
    assert Checker(source).check_from_source() == expected

def test_046():
    source = """
    int add (int x, int y) {
    return x + y;
}
    void callArgumentError() {
    int result = add(10);    // Error: TypeMismatchInExpression at function call (wrong number of arguments)
    int result2 = add(10, 20, 30);  // Error: TypeMismatchInExpression at function call (wrong number of arguments)
}"""
    expected = "TypeMismatchInExpression(FuncCall(add, [IntLiteral(10)]))"
    assert Checker(source).check_from_source() == expected

def test_047():
    source = """
       int add (int x, int y) {
    return x + y;
}
    void callArgumentError() {
    //int result = add(10);    // Error: TypeMismatchInExpression at function call (wrong number of arguments)
    int result2 = add(10, 20, 30);  // Error: TypeMismatchInExpression at function call (wrong number of arguments)
}"""
    expected = "TypeMismatchInExpression(FuncCall(add, [IntLiteral(10), IntLiteral(20), IntLiteral(30)]))"
    assert Checker(source).check_from_source() == expected

def test_048():
    source = """
    // Error: Assignment expression type mismatch
void assignmentExpressionError() {
    int x = 10;
    string text = "hello";
    float f = 3.14;
    
    int result = (x = text) + 5;     // Error: TypeMismatchInExpression at assignment expression (int = string)
    int value = (x = f) + 3;         // Error: TypeMismatchInExpression at assignment expression (int = float)
}"""
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_049():
    source = """
    // Error: Assignment expression type mismatch
void assignmentExpressionError() {
    int x = 10;
    string text = "hello";
    float f = 3.14;
    
    //int result = (x = text) + 5;     // Error: TypeMismatchInExpression at assignment expression (int = string)
    int value = (x = f) + 3;         // Error: TypeMismatchInExpression at assignment expression (int = float)
}"""
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = Identifier(f)))"
    assert Checker(source).check_from_source() == expected

def test_050():
    source = """
    // Valid: Proper expression types
struct Point {
    int x;
    int y;
};
void valid() {
    int x = 10;
    int y = 20;
    int sum = x + y;         // Valid: both int
    int compare = x < y;     // Valid: relational returns int
    int logic = x && y;      // Valid: logical returns int
    ++x;                     // Valid: increment on int
    
    
    
    Point p = {10, 20};
    int x_coord = p.x;       // Valid: member access
    
    // Valid: Assignment expression in expression context
    int a;
    int b = (a = 5) + 7;      // Valid: assignment expression returns value of a (5), b = 12
    
    // Valid: Chained assignment expression
    int c;
    int d;
    int e;
    c = d = e = 10;          // Valid: right-associative, all variables are 10
    
    // Valid: Member access assignment expression
    int result = (p.x = 15) + 5;  // Valid: assignment expression returns value of p.x (15), result = 20
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_051():
    source = """
    // Error: Break/continue outside loop
void loopError() {
    break;     // Error: MustInLoop(break)
    continue;  // Error: MustInLoop(continue)
}"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_052():
    source = """
    // Error: Break/continue outside loop
void loopError() {
    //break;     // Error: MustInLoop(break)
    continue;  // Error: MustInLoop(continue)
}"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_053():
    source = """
    // Error: Break/continue in if without loop
void conditionalError() {
    if (1) {
        break;     // Error: MustInLoop(break)
        continue;  // Error: MustInLoop(continue)
    }
}"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_054():
    source = """
    // Error: Break/continue in if without loop
void conditionalError() {
    if (1) {
        //break;     // Error: MustInLoop(break)
        continue;  // Error: MustInLoop(continue)
    }
}"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_055():
    source = """
    // Error: Continue in switch (continue not allowed in switch)
void switchError() {
    int x = 1;
    switch (x) {
        case 1:
            continue;  // Error: MustInLoop(continue) - continue not allowed in switch
            break;
    }
}"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_056():
    source = """
    // Error: Break/continue in function called from loop
void helperMethod() {
    //break;     // Error: MustInLoop(break) - different function scope
    continue;  // Error: MustInLoop(continue)
}

void loopWithCall() {
    for (auto i = 0; i < 10; ++i) {
        helperMethod();  // Method call doesn't transfer loop context
    }
}
"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_057():
    source = """
    // Error: Break/continue in function called from loop
void helperMethod() {
    break;     // Error: MustInLoop(break) - different function scope
    continue;  // Error: MustInLoop(continue)
}

void loopWithCall() {
    for (auto i = 0; i < 10; ++i) {
        helperMethod();  // Method call doesn't transfer loop context
    }
}"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_058():
    source = """
    // Valid: Break/continue in loops
void validLoops() {
    for (auto i = 0; i < 10; ++i) {
        if (i == 5) {
            break;     // Valid: in for loop
        }
        if (i % 2 == 0) {
            continue;  // Valid: in for loop
        }
        printInt(i);
    }
    
    auto j = 0;
    while (j < 10) {
        if (j == 3) {
            continue;  // Valid: in while loop
        }
        if (j == 8) {
            break;     // Valid: in while loop
        }
        printInt(j);
        ++j;
    }
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_059():
    source = """
    // Valid: Break in switch
void validSwitch() {
    int day = 2;
    switch (day) {
        case 1:
            printInt(1);
            break;     // Valid: break in switch
        case 2:
        case 3:
            printInt(2);
            break;     // Valid: break in switch
        default:
            printInt(0);
    }
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_060():
    source = """
    // Valid: Nested loops
void nestedLoops() {
    for (auto i = 0; i < 5; ++i) {
        for (auto j = 0; j < 5; ++j) {
            if (i == j) {
                continue;  // Valid: affects inner loop
            }
            if (j > 3) {
                break;     // Valid: breaks inner loop
            }
        }
    }
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_061():
    source = """
    // Error: `auto x` is still unknown when typing `x + "hello"` (same message if only `x` is declared)
void string_mix() {
    auto x;
    auto y;  // unused here; failure is reported on the next line’s initializer
    auto result = x + "hello";  // TypeCannotBeInferred(BinaryOp(Identifier(x), +, StringLiteral('hello')))
}"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected

def test_062():
    source = """
    struct Point {
    int x;
    int y;
};
struct Point {  // Redeclared(Struct, Point)
    int z;
};"""
    expected = "Redeclared(Struct, Point)"
    assert Checker(source).check_from_source() == expected

def test_063():
    source = """
    // Error: Redeclared Function in global scope
int add(int x, int y) {
    return x + y;
}
int add(int a, int b) {  // Redeclared(Function, add) - no function overloading
    return a + b;
}"""
    expected = "Redeclared(Function, add)"
    assert Checker(source).check_from_source() == expected

def test_064():
    source = """
    // Valid: same identifier for a struct type and a function (separate global namespaces)
struct foo {
    int x;
    int y;
};
int foo(int x, int y) {  // Not Redeclared: struct foo and function foo are distinct
    return x + y;
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_065():
    source = """
    // Error: Redeclared Variable in same block
void main() {
    int count = 10;
    int count = 20;  // Redeclared(Variable, count)
}"""
    expected = "Redeclared(Variable, count)"
    assert Checker(source).check_from_source() == expected

def test_066():
    source = """
    // Error: Redeclared Parameter
int calculate(int x, float y, int x) {  // Redeclared(Parameter, x)
    return x + y;
}"""
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected

def test_067():
    source = """
    // Error: Local variable reuses parameter name (same function; not allowed even in nested blocks)
void func(int x) {
    int x = 10;  // Redeclared(Variable, x)
}"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_068():
    source = """
    // Error: Duplicate struct member names in the same struct
struct Point {
    int x;
    int x;  // Redeclared(Member, x)
};"""
    expected = "Redeclared(Member, x)"
    assert Checker(source).check_from_source() == expected

def test_069():
    source = """
    // Valid: Shadowing in different scopes
void example() {
    int value = 100;  // Function variable
    
    {
        int value = 200;  // Valid: shadows function variable
        {
            int value = 300;  // Valid: shadows block variable
        }
    }
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_070():
    source = """
    // Valid: Different scopes (no shadowing conflict)
void test() {
    int x = 10;
    {
        int y = 20;  // Valid: different variable name
    }
    int y = 30;  // Valid: y in outer scope doesn't conflict with y in inner scope (different block)
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_071():
    source = """
    // Error: Undeclared Variable
void example() {
    int result = undeclaredVar + 10;  // UndeclaredIdentifier(undeclaredVar)
}"""
    expected = "UndeclaredIdentifier(undeclaredVar)"
    assert Checker(source).check_from_source() == expected

def test_072():
    source = """
    // Error: Using variable before declaration in same scope
void test() {
    int x = y + 5;  // UndeclaredIdentifier(y) - y used before declaration
    int y = 10;
}"""
    expected = "UndeclaredIdentifier(y)"
    assert Checker(source).check_from_source() == expected

def test_073():
    source = """
    // Error: Out of scope access
void method1() {
    int localVar = 42;
}

void method2() {
    int value = localVar + 1;  // UndeclaredIdentifier(localVar) - different function scope
}"""
    expected = "UndeclaredIdentifier(localVar)"
    assert Checker(source).check_from_source() == expected

def test_074():
    source = """
    // Valid: Proper declaration order
void valid() {
    int x = 10;
    int y = x + 5;  // Valid: x is declared before use
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_075():
    source = """
    // Valid: Parameter visible throughout function
int calculate(int x, int y) {
    int result = x + y;  // Valid: parameters x and y are visible
    return result;
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_076():
    source = """
    // Valid: Variable in enclosing scope
void nested() {
    int outer = 10;
    {
        int inner = outer + 5;  // Valid: outer is in enclosing scope
    }
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_077():
    source = """
    // Error: Undeclared Function
void main() {
    int result = calculate(5, 3);  // UndeclaredFunction(calculate)
}"""
    expected = "UndeclaredFunction(calculate)"
    assert Checker(source).check_from_source() == expected

def test_078():
    source = """
    // Error: Function called before declaration (if declaration comes later)
void test() {
    int value = add(10, 20);  // UndeclaredFunction(add) - if add is declared later
}
int add(int x, int y) {
    return x + y;
}"""
    expected = "UndeclaredFunction(add)"
    assert Checker(source).check_from_source() == expected

def test_079():
    source = """
    // Valid: Function declared before use
int multiply(int x, int y) {
    return x * y;
}

void main() {
    int result = multiply(5, 3);  // Valid: multiply is declared before
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_080():
    source = """
    // Valid: Built-in functions

void example() {
    int x = readInt();        // Valid: built-in function
    printInt(x);              // Valid: built-in function
    float y = readFloat();    // Valid: built-in function
    string s = readString();  // Valid: built-in function
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_081():
    source = """
   // Error: Undeclared Struct
void main() {
    Point p;  // UndeclaredStruct(Point)
}

struct Point {
    int x;
    int y;
};
"""
    expected = "UndeclaredStruct(Point)"
    assert Checker(source).check_from_source() == expected

def test_082():
    source = """
    // Error: Using struct type before declaration
void test() {
    Person person;  // UndeclaredStruct(Person) - if Person is declared later
}

struct Person {
    string name;
    int age;
};"""
    expected = "UndeclaredStruct(Person)"
    assert Checker(source).check_from_source() == expected

def test_083():
    source = """
    // Error: Struct member using undeclared struct type
struct Address {
    string street;
    City city;  // UndeclaredStruct(City) - if City is declared later
};

struct City {
    string name;
};"""
    expected = "UndeclaredStruct(City)"
    assert Checker(source).check_from_source() == expected

def test_084():
    source = """
    // Valid: Struct declared before use
struct Point {
    int x;
    int y;
};

void main() {
    Point p1;  // Valid: Point is declared before
    Point p2 = {10, 20};  // Valid: Point is declared before
    p1 = {"1", 2};  // Valid: type mismatch in struct member initialization is not checked here (but would be caught in type checking phase)
}"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_085():
    source = """
    // Valid: Struct member using previously declared struct
struct Point {
    int x;
    int y;
};

struct Address {
    string street;
    Point location;  // Valid: Point is declared before
};"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected
