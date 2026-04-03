"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator

def test_001():
    source = "void main() {}"
    expected = "Program([FuncDecl(VoidType(), main, [], [])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_002():
    source = ""
    expected = "Program([])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_003():
    source = "int main() { return 0; }"
    expected = "Program([FuncDecl(IntType(), main, [], [ReturnStmt(return IntLiteral(0))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_004():
    source = "int main(point a, point b) { return a.x + b.y; }"
    expected = "Program([FuncDecl(IntType(), main, [Param(StructType(point), a), Param(StructType(point), b)], [ReturnStmt(return BinaryOp(MemberAccess(Identifier(a).x), +, MemberAccess(Identifier(b).y)))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_005():
    source = "int a = 10;"
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_006():
    source = "struct Point { int x; int y; };"
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_007():
    source = "struct Node {};"
    expected = "Program([StructDecl(Node, [])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_008():
    source = "int add(int a, int b) {} void main() { add(1, 2); }"
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(add, [IntLiteral(1), IntLiteral(2)]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_009():
    source = "string print(string text) {} void main() { print(\"Hello, World!\"); }"
    expected = "Program([FuncDecl(StringType(), print, [Param(StringType(), text)], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(print, [StringLiteral('Hello, World!')]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_010():
    source = "float add(float a, float b) {} void main() { add(1.0, 2.0); }"
    expected = "Program([FuncDecl(FloatType(), add, [Param(FloatType(), a), Param(FloatType(), b)], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(add, [FloatLiteral(1.0), FloatLiteral(2.0)]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_011():
    source = "void setPoint(Point x) {} void main() {Point x = {1, 2}; setPoint(x); }"
    expected = "Program([FuncDecl(VoidType(), setPoint, [Param(StructType(Point), x)], []), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), x = StructLiteral({IntLiteral(1), IntLiteral(2)})), ExprStmt(FuncCall(setPoint, [Identifier(x)]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_012():
    source = "void setPoint(Point x) {} void main() {Point x = {}; setPoint(x); }"
    expected = "Program([FuncDecl(VoidType(), setPoint, [Param(StructType(Point), x)], []), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), x = StructLiteral({})), ExprStmt(FuncCall(setPoint, [Identifier(x)]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_013():
    source = "int add(int a, int b) {} void main() { add(); }"
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(add, []))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_014():
    source = " main() { int x = 5; }"
    expected = "Program([FuncDecl(auto, main, [], [VarDecl(IntType(), x = IntLiteral(5))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_015():
    source = "void main() { if (true) { int x = 5; } else { int y = 10; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(true) then BlockStmt([VarDecl(IntType(), x = IntLiteral(5))]), else BlockStmt([VarDecl(IntType(), y = IntLiteral(10))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_016():
    source = "void main() { if (true) { int x = 5; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(true) then BlockStmt([VarDecl(IntType(), x = IntLiteral(5))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_017():
    source = "void main() { if (a = 123) { print(abc); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if AssignExpr(Identifier(a) = IntLiteral(123)) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(abc)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_018():
    source = "void main() { if (a == 123 && b == 456) { print(abc); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if AssignExpr(Identifier(a) = BinaryOp(IntLiteral(123), &&, AssignExpr(Identifier(b) = IntLiteral(456)))) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(abc)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_019():
    source = "void main() { if (a == 123 && b == 456) { print(abc); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(BinaryOp(Identifier(a), ==, IntLiteral(123)), &&, BinaryOp(Identifier(b), ==, IntLiteral(456))) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(abc)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_020():
    source = "void main() { if (a == 123 || b == 456) { print(abc); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(BinaryOp(Identifier(a), ==, IntLiteral(123)), ||, BinaryOp(Identifier(b), ==, IntLiteral(456))) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(abc)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_021():
    source = "void main() { if (a >= 123 || b < 456) { print(abc); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(BinaryOp(Identifier(a), >=, IntLiteral(123)), ||, BinaryOp(Identifier(b), <, IntLiteral(456))) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(abc)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_022():
    source = "void main() { if (a >= 123 || b < 456) { string str = \"Hello World\"; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(BinaryOp(Identifier(a), >=, IntLiteral(123)), ||, BinaryOp(Identifier(b), <, IntLiteral(456))) then BlockStmt([VarDecl(StringType(), str = StringLiteral('Hello World'))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_023():
    source = "void main() {Name x; if (a >= 123 || b < 456) { string str = \"Hello World\"; x = {str};} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Name), x), IfStmt(if BinaryOp(BinaryOp(Identifier(a), >=, IntLiteral(123)), ||, BinaryOp(Identifier(b), <, IntLiteral(456))) then BlockStmt([VarDecl(StringType(), str = StringLiteral('Hello World')), ExprStmt(AssignExpr(Identifier(x) = StructLiteral({Identifier(str)})))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_024():
    source = "void main() {int i = 0; while (i < 10) { print(i); i = i + 1; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)])), ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_025():
    source = "void main() {for (int i = 0; i < 10; i = i + 1) { print(i); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_026():
    source = "void main() {for (int i = 0; i < 10; i++) { print(i); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_027():
    source = "void main() {for (int i = 0; i < 10; i = 5 + a) { print(i); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(IntLiteral(5), +, Identifier(a))) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_028():
    source = "void main() {for (int i = 0; i < 10; ++i) { print(i); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(++Identifier(i)) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_029():
    source = "void main() {for (int i = 0; i < 10; getVar().i++) { print(i); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(MemberAccess(FuncCall(getVar, []).i)++) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_030():
    source = "void main() {for (int i; i < 10; getVar().i = a) { print(i); a = a + 1;} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(MemberAccess(FuncCall(getVar, []).i) = Identifier(a)) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)])), ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_031():
    source = "void main() {for (int i = 0; i < 5; i++) { if (i == 5) continue; else a = i;}}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(5)); PostfixOp(Identifier(i)++) do BlockStmt([IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(5)) then ContinueStmt(), else ExprStmt(AssignExpr(Identifier(a) = Identifier(i))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_032():
    source = "void main() {for (int i = 0; i < 5; i++) { if (i == 5) continue; else if (i == a) break; else a = a - 5;}}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(5)); PostfixOp(Identifier(i)++) do BlockStmt([IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(5)) then ContinueStmt(), else IfStmt(if BinaryOp(Identifier(i), ==, Identifier(a)) then BreakStmt(), else ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), -, IntLiteral(5))))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_033():
    source = "int evaluate(int a){} void main() { int a; switch (evaluate(a)) {case 1: print(\"One\"); break; case 2: print(\"Two\"); break; default: print(\"Other\");}}"
    expected = "Program([FuncDecl(IntType(), evaluate, [Param(IntType(), a)], []), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), SwitchStmt(switch FuncCall(evaluate, [Identifier(a)]) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')])), BreakStmt()]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Two')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_034():
    source = "int evaluate(int a){} void main() { int a; switch (evaluate(a)) {case 1: print(\"One\"); break; case 2: print(\"Two\"); break;}}"
    expected = "Program([FuncDecl(IntType(), evaluate, [Param(IntType(), a)], []), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), SwitchStmt(switch FuncCall(evaluate, [Identifier(a)]) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')])), BreakStmt()]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Two')])), BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_035():
    source = "int evaluate(int a){} void main() { int a; switch (evaluate(a)) {case 1: print(\"One\"); break; default: print(a); case 3: print(\"Two\"); break;}}"
    expected = "AST Generation Error"
    assert expected in str(ASTGenerator(source).generate())
    assert True

def test_036():
    source = "int evaluate(int a){} void main() { int a; switch (evaluate(a)) {case 1: print(\"One\"); continue; case 2: print(\"Two\"); default: print(\"Other\");}}"
    expected = "Program([FuncDecl(IntType(), evaluate, [Param(IntType(), a)], []), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), SwitchStmt(switch FuncCall(evaluate, [Identifier(a)]) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')])), ContinueStmt()]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Two')]))])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_037():
    source = "int evaluate(int a){} void main() { int a; switch (evaluate(a)) {case -2: print(\"One\");}}"
    expected = "Program([FuncDecl(IntType(), evaluate, [Param(IntType(), a)], []), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), SwitchStmt(switch FuncCall(evaluate, [Identifier(a)]) cases [CaseStmt(case PrefixOp(-IntLiteral(2)): [ExprStmt(FuncCall(print, [StringLiteral('One')]))])])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_038():
    source = "int evaluate(int a){} void main() { int a; switch (evaluate(a)) {case (-1+6): print(\"One\");}}"
    expected = "Program([FuncDecl(IntType(), evaluate, [Param(IntType(), a)], []), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), SwitchStmt(switch FuncCall(evaluate, [Identifier(a)]) cases [CaseStmt(case BinaryOp(PrefixOp(-IntLiteral(1)), +, IntLiteral(6)): [ExprStmt(FuncCall(print, [StringLiteral('One')]))])])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_039():
    source = "int evaluate(int a){} void main() { int a; switch (evaluate(a)) {case (-1+6): if (a==3) getA().x; else {setA(3); print(A);}}}"
    expected = "Program([FuncDecl(IntType(), evaluate, [Param(IntType(), a)], []), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), SwitchStmt(switch FuncCall(evaluate, [Identifier(a)]) cases [CaseStmt(case BinaryOp(PrefixOp(-IntLiteral(1)), +, IntLiteral(6)): [IfStmt(if BinaryOp(Identifier(a), ==, IntLiteral(3)) then ExprStmt(MemberAccess(FuncCall(getA, []).x)), else BlockStmt([ExprStmt(FuncCall(setA, [IntLiteral(3)])), ExprStmt(FuncCall(print, [Identifier(A)]))]))])])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_040():
    source = "void main() { if (x) if (y) a; else b; else c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(x) then IfStmt(if Identifier(y) then ExprStmt(Identifier(a)), else ExprStmt(Identifier(b))), else ExprStmt(Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_041():
    source = "void main() { if (x) if (y) a; else b;}"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(x) then IfStmt(if Identifier(y) then ExprStmt(Identifier(a)), else ExprStmt(Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 42-46: Expressions - Member Access
# ============================================================================
def test_042():
    source = "void main() { a.b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(MemberAccess(Identifier(a).b))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_043():
    source = "void main() { a.b.c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(MemberAccess(MemberAccess(Identifier(a).b).c))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_044():
    source = "void main() { a.b++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(MemberAccess(Identifier(a).b)++))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_045():
    source = "void main() { f().x; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(MemberAccess(FuncCall(f, []).x))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_046():
    source = "void main() { a.b = c.d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = MemberAccess(Identifier(c).d)))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 47-48: Expressions - Function Calls
# ============================================================================
def test_047():
    source = "void main() { f(g(x), y); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [FuncCall(g, [Identifier(x)]), Identifier(y)]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_048():
    source = "void main() { f({1, 2}); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, [StructLiteral({IntLiteral(1), IntLiteral(2)})]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 49-50: Expressions - Full Precedence
# ============================================================================
def test_049():
    source = "void main() { a + b * c == d && e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c))), ==, Identifier(d)), &&, Identifier(e)))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_050():
    source = "void main() { !a.b + -c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(PrefixOp(!MemberAccess(Identifier(a).b)), +, PrefixOp(-Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 51-52: Statements - If (Dangling Else & Chain)
# ============================================================================
def test_051():
    source = "void main() { if (a) b; else if (c) d; else e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then ExprStmt(Identifier(b)), else IfStmt(if Identifier(c) then ExprStmt(Identifier(d)), else ExprStmt(Identifier(e))))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_052():
    source = "void main() { if (a) { if (b) c; } else d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then BlockStmt([IfStmt(if Identifier(b) then ExprStmt(Identifier(c)))]), else ExprStmt(Identifier(d)))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 53: Statements - Nested Whiles
# ============================================================================
def test_053():
    source = "void main() { while (a) while (b) c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do WhileStmt(while Identifier(b) do ExprStmt(Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 54-62: Statements - For Edge Cases
# ============================================================================
def test_054():
    source = "void main() { for(;;) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_055():
    source = "void main() { for(i=0;;) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); None; None do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_056():
    source = "void main() { for(auto i=0; i<10; i++) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(auto, i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_057():
    source = "void main() { for(; i<10;) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_058():
    source = "void main() { for(;; i++) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; PostfixOp(Identifier(i)++) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_059():
    source = "void main() { for(int i=10; i>0; --i) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(10)); BinaryOp(Identifier(i), >, IntLiteral(0)); PrefixOp(--Identifier(i)) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_060():
    source = "void main() { for(int i=10; i>0; i--) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(10)); BinaryOp(Identifier(i), >, IntLiteral(0)); PostfixOp(Identifier(i)--) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_061():
    source = "void main() { for(;;) while(1) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do WhileStmt(while IntLiteral(1) do BlockStmt([])))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_062():
    source = "void main() { for(int i=0; ; i++) if (i==5) break; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; PostfixOp(Identifier(i)++) do IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(5)) then BreakStmt()))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 63-69: Statements - Switch Edge Cases
# ============================================================================
def test_063():
    source = "void main() { switch(a) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_064():
    source = "void main() { switch(a) { case 1: case 2: break; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [CaseStmt(case IntLiteral(1): []), CaseStmt(case IntLiteral(2): [BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_065():
    source = "void main() { switch(a) { default: print(1); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [], default DefaultStmt(default: [ExprStmt(FuncCall(print, [IntLiteral(1)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_066():
    # Error: Case sau Default (Trái với rule caseBlock* defaultBlock?)
    source = "void main() { switch(a) { default: break; case 2: break; } }"
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_067():
    source = "void main() { switch(a) { default: } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [], default DefaultStmt(default: []))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_068():
    source = "void main() { switch(1+2) { case 3: } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch BinaryOp(IntLiteral(1), +, IntLiteral(2)) cases [CaseStmt(case IntLiteral(3): [])])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_069():
    source = "void main() { switch(a) { case 1+a: } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(a) cases [CaseStmt(case BinaryOp(IntLiteral(1), +, Identifier(a)): [])])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 70-71: Break, Continue, Return
# ============================================================================
def test_070():
    source = "void main() { break; continue; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [BreakStmt(), ContinueStmt()])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_071():
    source = "void main() { return; return x; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ReturnStmt(return), ReturnStmt(return Identifier(x))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 72-73: Blocks
# ============================================================================
def test_072():
    source = "void main() { {{{}}} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [BlockStmt([BlockStmt([BlockStmt([])])])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_073():
    source = "void main() { {a;} {b;} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [BlockStmt([ExprStmt(Identifier(a))]), BlockStmt([ExprStmt(Identifier(b))])])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 74-75: Expression Statements
# ============================================================================
def test_074():
    source = "void main() { f(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(f, []))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_075():
    source = "void main() { i++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(i)++))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 76-80: Parser Errors (Strictly Reject)
# ============================================================================
def test_076():
    source = "void main() { ; }" # Lỗi: empty statement không có trong rule
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_077():
    source = "void main() { int arr[10]; }" # Lỗi: không hỗ trợ array
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_078():
    source = "void main() { int a, b; }" # Lỗi: khai báo nhiều biến 1 dòng
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_079():
    source = "void main() { void a; }" # Lỗi: void không được làm kiểu biến
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_080():
    source = "void main() { struct Point { int x; }; }" # Lỗi: local struct decl
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

# ============================================================================
# 81-89: Tricky / Edge Cases
# ============================================================================
def test_081():
    source = "void main() { switch(x){ default: default: } }" # Lỗi: multiple default
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_082():
    source = "void main() { for(;; {} }" # Lỗi: thiếu ngoặc đóng )
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_083():
    source = "void main() { a < b = c; }" # Lỗi: Relational on LHS of assignment
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_084():
    source = "void main() { if ((a) {} }" # Lỗi: unmatched parentheses
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_085():
    source = "void main() { {1, 2} = a; }" # Lỗi: struct literal on LHS of assign
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_086():
    source = "void main() { for (int i = ; i < 10; i++) {} }" # Lỗi: invalid init
    assert "AST Generation Error" in str(ASTGenerator(source).generate())
    assert True

def test_087():
    source = "void main() { a = b = c = 0; }" # Chained assignment
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = IntLiteral(0)))))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_088():
    source = "void main() { ++a++; }" # Prefix và postfix: ++(a++)
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++PostfixOp(Identifier(a)++)))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_089():
    source = "void main() { return {1, 2}; }" # Return struct literal
    expected = "Program([FuncDecl(VoidType(), main, [], [ReturnStmt(return StructLiteral({IntLiteral(1), IntLiteral(2)}))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

# ============================================================================
# 90-100: Complex programs & Integration
# ============================================================================
def test_090():
    source = "void main() { if (!a && b || c == d) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(BinaryOp(PrefixOp(!Identifier(a)), &&, Identifier(b)), ||, BinaryOp(Identifier(c), ==, Identifier(d))) then BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_091():
    source = "void main() { return f(x); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ReturnStmt(return FuncCall(f, [Identifier(x)]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_092():
    source = "void main() { print(\"String \\n Escape\"); }"
    expected = r"Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(print, [StringLiteral('String \\n Escape')]))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_093():
    source = "struct A { B b; };" # Struct chứa type là struct khác
    expected = "Program([StructDecl(A, [MemberDecl(StructType(B), b)])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_094():
    source = "void main() { auto x = 5; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, x = IntLiteral(5))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_095():
    source = "void main() { string s = \"a\" + \"b\"; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StringType(), s = BinaryOp(StringLiteral('a'), +, StringLiteral('b')))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_096():
    source = "void main() { float x = -3.14; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(FloatType(), x = PrefixOp(-FloatLiteral(3.14)))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_097():
    source = "void f() { return; }"
    expected = "Program([FuncDecl(VoidType(), f, [], [ReturnStmt(return)])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_098():
    source = "void main() { continue; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ContinueStmt()])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_099():
    source = "void main() { Point p = {1, {2, 3}}; }" # Nested struct literal
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), StructLiteral({IntLiteral(2), IntLiteral(3)})}))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True

def test_100():
    source = "struct P { int x; }; int main() { P p = {1}; return p.x; }" # Full program tích hợp
    expected = "Program([StructDecl(P, [MemberDecl(IntType(), x)]), FuncDecl(IntType(), main, [], [VarDecl(StructType(P), p = StructLiteral({IntLiteral(1)})), ReturnStmt(return MemberAccess(Identifier(p).x))])])"
    assert str(ASTGenerator(source).generate()) == expected
    assert True
