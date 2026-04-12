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
int readInt() {
    return 0;
}
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
    void printInt(int x) {
    }
    void valid6() {
        auto x;
        printInt(x);  // Valid: type inferred as int from printInt(int) parameter type
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
    void printInt(float x) {
        auto a = x;
    }
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
        return;
    }
    int returnVoidError() {
    return returnError();  // Error: TypeMismatchInStatement at return statement (non-void function must return value)
}"""
    expected = "TypeMismatchInStatement(ReturnStmt(return FuncCall(returnError, [])))"
    assert Checker(source).check_from_source() == expected

def test_032():
    source = """
    // Valid: Proper type matching
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