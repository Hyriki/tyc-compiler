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
    """Test TypeMismatchInStatement when assigning float to int variable"""
    source = """
void main() {
    int x = 10;
    int y = 3.14;
    int z = x + y;
}
"""
    expected = "TypeMismatchInStatement(VarDecl(IntType(), y = FloatLiteral(3.14)))"
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
    source = """
struct Point {
    int x;
    int y;
};
struct Point {
    int z;
};
"""
    assert Checker(source).check_from_source() == "Redeclared(Struct, Point)"

def test_007():
    source = """
int add(int x, int y) {
    return x + y;
}
int add(int a, int b) {
    return a + b;
}
"""
    assert Checker(source).check_from_source() == "Redeclared(Function, add)"

def test_008():
    source = """
void main() {
    int count = 10;
    int count = 20;  // Redeclared(Variable, count)
}
"""
    assert Checker(source).check_from_source() == "Redeclared(Variable, count)"

def test_009():
    source = """
int calculate(int x, float y, int x) {  // Redeclared(Parameter, x)
    return x + y;
}
"""
    assert Checker(source).check_from_source() == "Redeclared(Parameter, x)"

def test_010():
    source = """
void example() {
    int value = 100;  // Function variable
    
    {
        int value = 200;  // Valid: shadows function variable
        {
            int value = 300;  // Valid: shadows block variable
        }
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_011():
    source = """
void test() {
    int x = 10;
    {
        int y = 20;  // Valid: different variable name
    }
    int y = 30;  // Valid: y in outer scope doesn't conflict with y in inner scope (different block)
}

"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_012():
    source = """
void example() {
    int result = undeclaredVar + 10;  // UndeclaredIdentifier(undeclaredVar)
}
"""
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(undeclaredVar)"


def test_013():
    source = """
void test() {
    int x = y + 5;  // UndeclaredIdentifier(y) - y used before declaration
    int y = 10;
}
"""
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(y)"


def test_014():
    source = """
void method1() {
    int localVar = 42;
}

void method2() {
    int value = localVar + 1;  // UndeclaredIdentifier(localVar) - different function scope
}
"""
    assert Checker(source).check_from_source() == "UndeclaredIdentifier(localVar)"


def test_015():
    source = """
void valid() {
    int x = 10;
    int y = x + 5;  // Valid: x is declared before use
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_016():
    source = """
int calculate(int x, int y) {
    int result = x + y;  // Valid: parameters x and y are visible
    return result;
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_017():
    source = """
void nested() {
    int outer = 10;
    {
        int inner = outer + 5;  // Valid: outer is in enclosing scope
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_018():
    source = """
void main() {
    int result = calculate(5, 3);  // UndeclaredFunction(calculate)
}
"""
    assert Checker(source).check_from_source() == "UndeclaredFunction(calculate)"

def test_019():
    source = """
void test() {
    int value = add(10, 20);  // UndeclaredFunction(add) - if add is declared later
}

int add(int x, int y) {
    return x + y;
}
"""
    assert Checker(source).check_from_source() == "UndeclaredFunction(add)"

def test_020():
    source = """
int multiply(int x, int y) {
    return x * y;
}

void main() {
    int result = multiply(5, 3);  // Valid: multiply is declared before
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_021():
    source = """
void example() {
    int x = readInt();        // Valid: built-in function
    printInt(x);              // Valid: built-in function
    float y = readFloat();    // Valid: built-in function
    string s = readString();  // Valid: built-in function
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_022():
    source = """
void main() {
    Point p;  // UndeclaredStruct(Point)
}

struct Point {
    int x;
    int y;
};
"""
    assert Checker(source).check_from_source() == "UndeclaredStruct(Point)"

def test_023():
    source = """
void test() {
    Person person;  // UndeclaredStruct(Person) - if Person is declared later
}

struct Person {
    string name;
    int age;
};
"""
    assert Checker(source).check_from_source() == "UndeclaredStruct(Person)"

def test_024():
    source = """
struct Address {
    string street;
    City city;  // UndeclaredStruct(City) - if City is declared later
};

struct City {
    string name;
};
"""
    assert Checker(source).check_from_source() == "UndeclaredStruct(City)"

def test_025():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    Point p1;  // Valid: Point is declared before
    Point p2 = {10, 20};  // Valid: Point is declared before
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_026():
    source = """
struct Point {
    int x;
    int y;
};

struct Address {
    string street;
    Point location;  // Valid: Point is declared before
};
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_027():
    source = """
void loopError() {
    break;     // Error: MustInLoop(break)
}
"""
    assert Checker(source).check_from_source() == "MustInLoop(BreakStmt())"

def test_028():
    source = """
void loopError() {
    continue;  // Error: MustInLoop(continue)
}
"""
    assert Checker(source).check_from_source() == "MustInLoop(ContinueStmt())"

def test_029():
    source = """
void switchError() {
    int x = 1;
    switch (x) {
        case 1:
            break;
            continue;
    }
}
"""
    assert Checker(source).check_from_source() == "MustInLoop(ContinueStmt())"

def test_030():
    source = """
void switchError() {
    for (int i = 0; i < 5; ++i) {            
        break;
        continue;
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_031():
    source = """
void arithmeticError() {
    int x = 5;
    string text = "hello";
    
    int sum = x + text;     // Error: TypeMismatchInExpression at binary operation
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(BinaryOp(Identifier(x), +, Identifier(text)))"

def test_032():
    source = """
void arithmeticError() {
    int x = 5;
    string text = "hello";
    
    float result = x * text; // Error: TypeMismatchInExpression at binary operation
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(BinaryOp(Identifier(x), *, Identifier(text)))"


def test_033():
    source = """
void modulusError() {
    float f = 3.14;
    int x = 10 % 2;
    
    int result = f % x;      // Error: TypeMismatchInExpression at binary operation (float % int)
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(BinaryOp(Identifier(f), %, Identifier(x)))"


def test_034():
    source = """
void modulusError() {
    float f = 3.14;
    int x = 10;
    
    int result2 = x % f;     // Error: TypeMismatchInExpression at binary operation (int % float)
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(BinaryOp(Identifier(x), %, Identifier(f)))"

def test_035():
    source = """
void relationalError() {
    int x = 10 == 1;
    string text = "hello";
    
    int equal = text == x;   // Error: TypeMismatchInExpression at binary operation
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(BinaryOp(Identifier(text), ==, Identifier(x)))"

def test_036():
    source = """
void relationalError() {
    int x = 10 > 2;
    string text = "hello";
    
    int result = x < text;   // Error: TypeMismatchInExpression at binary operation
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(BinaryOp(Identifier(x), <, Identifier(text)))"


def test_037():
    source = """
void logicalError() {
    float f = 3.14;
    int x = 10 && 20;
    
    int result = f && x;     // Error: TypeMismatchInExpression at binary operation
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(BinaryOp(Identifier(f), &&, Identifier(x)))"


def test_038():
    source = """
void logicalError() {
    float f = 3.14;
    int x = !10;
    
    int not = !f;            // Error: TypeMismatchInExpression at unary operation
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(PrefixOp(!Identifier(f)))"

def test_039():
    source = """
void incrementError() {
    float f = 3.14;
    ++f;                     // Error: TypeMismatchInExpression at unary operation
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(PrefixOp(++Identifier(f)))"

def test_040():
    source = """
void incrementError() {
    float f = 3.14;
    f++;                     // Error: TypeMismatchInExpression at postfix operation
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(PostfixOp(Identifier(f)++))"


def test_041():
    source = """
void incrementOperandError() {
    int x = 5;
    ++ x;
    x ++;
    ++5;                     // Error: TypeMismatchInExpression at unary operation (cannot increment literal)
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(PrefixOp(++IntLiteral(5)))"


def test_042():
    source = """
void incrementOperandError() {
    int x = 5;
    --(x + 1);               // Error: TypeMismatchInExpression at unary operation (cannot increment expression)
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(PrefixOp(--BinaryOp(Identifier(x), +, IntLiteral(1))))"

def test_043():
    source = """
void incrementOperandError() {
    int x = 5;
    (x + 2)++;               // Error: TypeMismatchInExpression at postfix operation (cannot increment expression
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(PostfixOp(BinaryOp(Identifier(x), +, IntLiteral(2))++))"


def test_044():
    source = """
struct Point {
    int x;
    int y;
};

void memberAccessError() {
    int x = 10;
    int value = x.member;    // Error: TypeMismatchInExpression at member access
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(MemberAccess(Identifier(x).member))"

def test_045():
    source = """
struct Point {
    int x;
    int y;
};

void memberAccessError() {
    Point p = {10, 20};
    int t = p.x + p.y;
    int invalid = p.z;       // Error: TypeMismatchInExpression at member access (z doesn't exist)
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(MemberAccess(Identifier(p).z))"

def test_046():
    source = """
void process(int x) { }

void callError() {
    string text = "123";
    process(text);   // sai kiểu: string -> int
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(FuncCall(process, [Identifier(text)]))"

def test_047():
    source = """
int add(int x, int y) {
    return x + y;
}

void callArgumentError() {
    int result = add(10);   // thiếu 1 tham số
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(FuncCall(add, [IntLiteral(10)]))"

def test_048():
    source = """
int add(int x, int y) {
    return x + y;
}

void callArgumentError() {
    int result = add(10, 20, 30);   // dư tham số
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(FuncCall(add, [IntLiteral(10), IntLiteral(20), IntLiteral(30)]))"

def test_049():
    source = """
void assignmentExpressionError() {
    int x = 10;
    string text = "hello";
    float f = 3.14;
    
    int result = (x = text) + 5;     // Error: TypeMismatchInExpression at assignment expression (int = string)
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(AssignExpr(Identifier(x) = Identifier(text)))"

def test_050():
    source = """
void conditionalError() {
    float x = 5.0;
    if (x) {
        printInt(1);
    }
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(IfStmt(if Identifier(x) then BlockStmt([ExprStmt(FuncCall(printInt, [IntLiteral(1)]))])))"

def test_051():
    source = """
void conditionalError() {
    string message = "hello";
    if (message) {
        printString(message);
    }
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(IfStmt(if Identifier(message) then BlockStmt([ExprStmt(FuncCall(printString, [Identifier(message)]))])))"

def test_052():
    source = """
void whileError() {
    float f = 1.5;
    while (f) {
        printFloat(f);
    }
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(WhileStmt(while Identifier(f) do BlockStmt([ExprStmt(FuncCall(printFloat, [Identifier(f)]))])))"

def test_053():
    source = """
void whileError() {
    int x = 10;
    string text = "hello";
    
    x = text;
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(x) = Identifier(text))))"

def test_054():
    source = """
void foo() {
    int i = 0;
    for (i=1; "s"; i++) {}
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(1))); StringLiteral('s'); PostfixOp(Identifier(i)++) do BlockStmt([])))"

def test_055():
    source = """
void switchError() {
    float f = 3.14;
    switch (f) {  // Error: TypeMismatchInStatement at switch statement
        case 1: break;
    }
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(SwitchStmt(switch Identifier(f) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])]))"

def test_056():
    source = """
int getValue() {
    return "invalid";  // Error: TypeMismatchInStatement at return statement
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(ReturnStmt(return StringLiteral('invalid')))"


def test_057():
    source = """
int returnVoidError() {
    return;  // Error: TypeMismatchInStatement at return statement (non-void function must return value)
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(ReturnStmt(return))"


def test_058():
    source = """
int foo() {
    auto a;
    a = 10;
    a = 2;
    a = 1.2;
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(a) = FloatLiteral(1.2))))"


def test_059():
    source = """
int foo() {
    auto a;
    auto b;
    a = b;
}
"""
    expected = "TypeCannotBeInferred(AssignExpr(Identifier(a) = Identifier(b)))"
    assert Checker(source).check_from_source() == expected


def test_060():
    source = """
int foo() {
    auto a;
    auto b;
    {{{
        b && a;
    }}}
    b = 2;
    a = 2.2;
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(a) = FloatLiteral(2.2))))"


def test_061():
    source = """
foo() {
   return 1;
}
int foo1() {
   int a;
   a = foo();
   float b;
   b = foo();
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(b) = FuncCall(foo, []))))"

def test_064():
    source = """
    struct Point {
        int Point;
        int y;
    };
    void main(Point a) {}
    """
    assert Checker(source).check_from_source() == "Static checking passed"


def test_069():
    source = """
void main() {
    int a; int b;
    if (1) int a = b;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_074():
    source = """
struct Point {
    int x;
    int y;
};
Point foo() {
    return {1};
}
"""
    expected = "TypeMismatchInExpression(StructLiteral({IntLiteral(1)}))"
    assert Checker(source).check_from_source() == expected


def test_077():
    source = """
    void main() {
        int a;
        for(;;) int a;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_081():
    source = """
    void main() {
        for(int a;;) int a;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_086():
    source = """
void main() {
    int a;
    switch (1) {
        case 1:
            int a;
            int b;
            float b;
    }
}
"""
    expected = "Redeclared(Variable, b)"
    assert Checker(source).check_from_source() == expected


def test_088():
    source = """
    void main() {
        int a;
        switch (1) {
            case 1:
                int a;
                int b;
            case 2:
                int c = a;
                {int a;}
            default:
                int d = b;
                string b;
        }
    }
    """
    assert Checker(source).check_from_source() == "Redeclared(Variable, b)"

def test_092():
    source = """
    struct A { A a; };
    """
    assert Checker(source).check_from_source() == "UndeclaredStruct(A)"


def test_099():
    source = """
A main (){}
struct A {};
"""
    expected = "UndeclaredStruct(A)"
    assert Checker(source).check_from_source() == expected


def test_101():
    source = """
struct Point {
    int x;
    int y;
};
struct Rect {
    Point a;
    Point b;
};
void main() {
    Rect r = {{1, 2}, {3, 4}};
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_102():
    source = """
struct Point {
    int x;
    int y;
};
struct Rect {
    Point a;
    Point b;
};
void main() {
    Rect r = {{1}, {3, 4}};
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(StructLiteral({IntLiteral(1)}))"

def test_103():
    source = """
struct Point { int x; int y; };
void main() {
    auto a;
    auto b;
    int c = a + b;
}
"""
    assert Checker(source).check_from_source() == "TypeCannotBeInferred(BinaryOp(Identifier(a), +, Identifier(b)))"

def test_104():
    source = """
void main() {
    auto s = {1, 2};
}
"""
    expected = "TypeCannotBeInferred(StructLiteral({IntLiteral(1), IntLiteral(2)}))"
    assert Checker(source).check_from_source() == expected


def test_105():
    source = """
void main() {
    int x = 1;
    switch (1) {
        case x:
            break;
    }
}
"""
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(SwitchStmt(switch IntLiteral(1) cases [CaseStmt(case Identifier(x): [BreakStmt()])]))"

def test_106():
    source = """
foo() {
    return {1, 2};
}
void main() {}
"""
    assert Checker(source).check_from_source() == "TypeCannotBeInferred(ReturnStmt(return StructLiteral({IntLiteral(1), IntLiteral(2)})))"

def test_107():
    source = """
foo() {
    return;
}
void main() {}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_108():
    source = """
struct Point {
    int x;
    int y;
};
Point foo() {
    return {10, 20};
}
void main() {}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_109():
    source = """
void main() {
    int x = 5;
    auto y;
    x = y;
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_111():
    source = """
void main() {
    auto x;
    int y = (x = 5) + 3;
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_112():
    source = """
void main() {
    int x = 5;
    auto y;
    int z = (x = y) + 3;
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"

def test_113():
    source = """
struct Point {
    int x;
    int y;
};
void consume(Point p) {
}
void main() {
    consume({10, 20});
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_115():
    source = """
void main(int A, int B) {
    A = B;
    {
    int A;
    A = C;
    }
}
"""
    expected = "Redeclared(Variable, A)"
    assert Checker(source).check_from_source() == expected

def test_129():
    source = """
    void main() {
        int a;
    
        1.2 % (1.2 + 2.1);
    }
    """
    assert Checker(source).check_from_source() == "TypeMismatchInExpression(BinaryOp(FloatLiteral(1.2), %, BinaryOp(FloatLiteral(1.2), +, FloatLiteral(2.1))))"


def test_145():
    source = """
void main(){
    switch(1 || 2){case 1.0: }
}
"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch BinaryOp(IntLiteral(1), ||, IntLiteral(2)) cases [CaseStmt(case FloatLiteral(1.0): [])]))"
    assert Checker(source).check_from_source() == expected


def test_153():
    source = """
void main(){
    for (string s; ; ) {}
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_154():
    source = """
void main(){
    float b;
    for (b=1.0; ; ) {}
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_156():
    source = """
void main(){
    string b;
    for (; ; b = "S") {}
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_196():
    source = """
void main() {
    int x;
    x = x = x = 3.14;
}
"""
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(x) = FloatLiteral(3.14)))"
    assert Checker(source).check_from_source() == expected


def test_220():
    source = """
void main() {
    auto a;
    auto b;
    int c = a + b;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(a), +, Identifier(b)))"
    assert Checker(source).check_from_source() == expected


def test_227():
    source = """
void main() {
    auto b;
    int c = b > 2;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(b), >, IntLiteral(2)))"
    assert Checker(source).check_from_source() == expected

def test_229():
    source = """
    void main() {
        auto a;
        auto b;
        auto d = a % b;
        float e = d;
    }
    """
    assert Checker(source).check_from_source() == "TypeMismatchInStatement(VarDecl(FloatType(), e = Identifier(d)))"


def test_234():
    source = """
void main() {
    auto a;
    ++ a;
    float b = a;
}
"""
    expected = "TypeMismatchInStatement(VarDecl(FloatType(), b = Identifier(a)))"
    assert Checker(source).check_from_source() == expected

def test_237():
    source = """
    void main() {
        auto a;
        + a;
        float b = a;
    }
    """
    assert Checker(source).check_from_source() == "TypeCannotBeInferred(PrefixOp(+Identifier(a)))"


def test_240():
    source = """
void main() {
    auto a; auto b;
    a = 1;
    a + b;
}
"""
    assert Checker(source).check_from_source() == "TypeCannotBeInferred(BinaryOp(Identifier(a), +, Identifier(b)))"


def test_244():
    source = """
void foo(int a){}
void main() {
    auto a;
    foo(a);
    float b = a;
}
"""
    expected = "TypeMismatchInStatement(VarDecl(FloatType(), b = Identifier(a)))"
    assert Checker(source).check_from_source() == expected


def test_248():
    source = """
void main() {
    auto a;
    if (a) {}
    float b = a;
}
"""
    expected = "TypeMismatchInStatement(VarDecl(FloatType(), b = Identifier(a)))"
    assert Checker(source).check_from_source() == expected


def test_249():
    source = """
void main() {
    auto a;
    while (a) {}
    float b = a;
}
"""
    expected = "TypeMismatchInStatement(VarDecl(FloatType(), b = Identifier(a)))"
    assert Checker(source).check_from_source() == expected


def test_254():
    source = """
void main() {
    for (auto a;;) {float b = a;}

}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_255():
    source = """
void main() {
    auto a;
    switch (a){}
    float b = a;
}
"""
    expected = "TypeMismatchInStatement(VarDecl(FloatType(), b = Identifier(a)))"
    assert Checker(source).check_from_source() == expected


def test_260():
    source = """
func() { auto a; return a;}
void main() {
    auto a = func();
    float b = a;
}
"""
    expected = "TypeCannotBeInferred(ReturnStmt(return Identifier(a)))"
    assert Checker(source).check_from_source() == expected


def test_265():
    source = """
void unused_auto() {
    auto x;
}
"""
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, x)]))"
    assert Checker(source).check_from_source() == expected


def test_269():
    source = """
void unused_auto() {
    switch (1) {
        case 1:
            auto c;
    }
}
"""
    expected = "TypeCannotBeInferred(SwitchStmt(switch IntLiteral(1) cases [CaseStmt(case IntLiteral(1): [VarDecl(auto, c)])]))"
    assert Checker(source).check_from_source() == expected


def test_271():
    source = """
void main() {
    auto b;
    int c = 1.0 + b;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(FloatLiteral(1.0), +, Identifier(b)))"
    assert Checker(source).check_from_source() == expected


def test_290():
    source = """
void main() {
    auto b;
    float a = b;
    b = 1.0;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_294():
    source = """
void foo() {
    int x = 1;
    switch (x) {
        case - 1:
        case 1 + 2:
        case - 2:
        case 1 || 2 * 3 / 4 + 2:

    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_295():
    source = """
void foo() {
    int x = 1;
    switch (x) {
        case x:
    }
}
"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch Identifier(x) cases [CaseStmt(case Identifier(x): [])]))"
    assert Checker(source).check_from_source() == expected


def test_298():
    source = """
void foo() {
    switch (1) {
        case x:
    }
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected


def test_307():
    source = """
foo() {
    int a = foo();
    return 1;
}
"""
    expected = "TypeCannotBeInferred(FuncCall(foo, []))"
    assert Checker(source).check_from_source() == expected


def test_313():
    source = """
struct A {};
struct B {};
void foo() {
    A a;
    B b = a;
}
"""
    expected = "TypeMismatchInStatement(VarDecl(StructType(B), b = Identifier(a)))"
    assert Checker(source).check_from_source() == expected


def test_315():
    source = """
struct Point {
    int x;
    int y;
};

void foo() {
    auto a;
    auto b;
    Point p = {a , b};
    a = b = 1;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_324():
    source = """
void main(){
    1 + {1, 2};
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(1), +, StructLiteral({IntLiteral(1), IntLiteral(2)})))"
    assert Checker(source).check_from_source() == expected

def test_328():
    source = """
main(){
    return 1;
    return main();
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"
