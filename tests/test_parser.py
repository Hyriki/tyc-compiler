"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


def assert_parse_success(source: str):
    assert Parser(source).parse() == "success"


def assert_parse_error(source: str):
    result = Parser(source).parse()
    assert result.startswith("Error on line")


# =======================================================================
# SECTION 1: VALID PROGRAMS (001-060)
# =======================================================================


def test_001():
    """Empty program"""
    source = ""
    assert_parse_success(source)


def test_002():
    """Program with only main function"""
    source = "void main() {}"
    assert_parse_success(source)


def test_003():
    """Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert_parse_success(source)


def test_004():
    """Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert_parse_success(source)


def test_005():
    """Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert_parse_success(source)


def test_006():
    """If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert_parse_success(source)


def test_007():
    """While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert_parse_success(source)


def test_008():
    """For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert_parse_success(source)


def test_009():
    """Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert_parse_success(source)


def test_010():
    """Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert_parse_success(source)


def test_011():
    """If-else statement"""
    source = "void main() { if (1) return; else return; }"
    assert_parse_success(source)


def test_012():
    """While loop"""
    source = "void main() { while (1) { break; } }"
    assert_parse_success(source)


def test_013():
    """For loop with varDecl init"""
    source = "void main() { for (auto i = 0; i < 10; ++i) { } }"
    assert_parse_success(source)


def test_014():
    """For loop with expr init"""
    source = "void main() { for (i = 0; i < 10; i = i + 1) { } }"
    assert_parse_success(source)


def test_015():
    """For loop with empty condition and update"""
    source = "void main() { for (;;){ break; } }"
    assert_parse_success(source)


def test_016():
    """For loop with empty init and update"""
    source = "void main() { for (; i < 10; ) { i = i + 1; } }"
    assert_parse_success(source)


def test_017():
    """Switch with cases and default"""
    source = "void main() { switch (x) { case 1: break; default: break; } }"
    assert_parse_success(source)


def test_018():
    """Empty switch"""
    source = "void main() { switch (x) { } }"
    assert_parse_success(source)


def test_019():
    """Return expression"""
    source = "int main() { return 1; }"
    assert_parse_success(source)


def test_020():
    """Return in void function"""
    source = "void main() { return; }"
    assert_parse_success(source)


def test_021():
    """Break and continue in loop"""
    source = "void main() { while (1) { if (1) break; else continue; } }"
    assert_parse_success(source)


def test_022():
    """Function call as statement"""
    source = "void main() { printInt(1); }"
    assert_parse_success(source)


def test_023():
    """Assignment chain"""
    source = "void main() { int a; int b; int c; a = b = c = 1; }"
    assert_parse_success(source)


def test_024():
    """Member access assignment"""
    source = "struct Point { int x; }; void main() { Point p; p.x = 1; }"
    assert_parse_success(source)


def test_025():
    """Struct literal initialization"""
    source = "struct Point { int x; int y; }; void main() { Point p = {1, 2}; }"
    assert_parse_success(source)


def test_026():
    """Nested struct literal initialization"""
    source = "struct Point2 { int x; int y; }; struct Point3 { Point2 p; int z; }; void main() { Point3 p = {{1, 2}, 3}; }"
    assert_parse_success(source)


def test_027():
    """Prefix and postfix operators"""
    source = "int main() { int x; x = 1; x++; ++x; --x; x--; return x; }"
    assert_parse_success(source)


def test_028():
    """Logical operators"""
    source = "int main() { int a; int b; a = (b && 1) || !b; return a; }"
    assert_parse_success(source)


def test_029():
    """Relational and equality operators"""
    source = "int main() { int a; int b; a = (b == 1) || (b != 2) || (b < 3) || (b >= 4); return a; }"
    assert_parse_success(source)


def test_030():
    """Parenthesized expression"""
    source = "int main() { int x; x = (1 + 2) * (3 + 4); return x; }"
    assert_parse_success(source)


def test_031():
    """Function call in expression"""
    source = "int add(int a, int b) { return a + b; } int main() { int x; x = add(1, 2); return x; }"
    assert_parse_success(source)


def test_032():
    """Shadowing in nested blocks"""
    source = "int main() { int x = 1; { int x = 2; } return x; }"
    assert_parse_success(source)


def test_033():
    """Variable declared with struct type"""
    source = "struct S { int x; }; void main() { S s; }"
    assert_parse_success(source)


def test_034():
    """Member access in expression"""
    source = "struct S { int x; }; int main() { S s; s.x = 3; return s.x; }"
    assert_parse_success(source)


def test_035():
    """String literal in varDecl"""
    source = "void main() { string s = \"hello\"; }"
    assert_parse_success(source)


def test_036():
    """Float literal in varDecl"""
    source = "void main() { float f = 3.14; }"
    assert_parse_success(source)


def test_037():
    """Assignment of float expression"""
    source = "void main() { float f; f = 1.0 + 2.5; }"
    assert_parse_success(source)


def test_038():
    """Switch with fallthrough"""
    source = "void main() { switch (x) { case 1: x = 2; case 2: x = 3; } }"
    assert_parse_success(source)


def test_039():
    """Switch default in middle"""
    source = "void main() { switch (x) { default: x = 0; case 1: x = 1; } }"
    assert_parse_success(source)


def test_040():
    """If without braces"""
    source = "void main() { if (1) return; }"
    assert_parse_success(source)


def test_041():
    """Empty struct literal usage"""
    # This ensures {} is parsed as struct literal, not a block, in assignment
    source = "struct P { int x; }; void main() { P p = {}; }"
    assert_parse_success(source)


def test_042():
    """For without braces"""
    source = "void main() { for (auto i = 0; i < 3; ++i) return; }"
    assert_parse_success(source)


def test_043():
    """Function with struct parameter"""
    source = "struct S { int x; }; int f(S s) { return s.x; }"
    assert_parse_success(source)


def test_044():
    """Function call with struct literal argument"""
    source = "struct S { int x; }; int f(S s) { return s.x; } int main() { return f({1}); }"
    assert_parse_success(source)


def test_045():
    """Unary plus and minus"""
    source = "int main() { int x; x = -1 + +2; return x; }"
    assert_parse_success(source)


def test_046():
    """Chained member access"""
    source = "struct P { int x; }; struct Q { P p; }; int main() { Q q; q.p.x = 1; return q.p.x; }"
    assert_parse_success(source)


def test_047():
    """Call with no arguments"""
    source = "int f() { return 1; } int main() { return f(); }"
    assert_parse_success(source)


def test_048():
    """Auto variable from function call"""
    source = "int f() { return 1; } void main() { auto x = f(); }"
    assert_parse_success(source)


def test_049():
    """Multiple declarations interleaving"""
    source = "struct A { int x; }; void foo() {} struct B { float y; }; void bar() {}"
    assert_parse_success(source)


def test_050():
    """Multiple statements in block"""
    source = "void main() { int a = 1; int b = 2; a = a + b; b = a - b; }"
    assert_parse_success(source)


def test_051():
    """Return with parenthesized expression"""
    source = "int main() { return (1 + 2) * 3; }"
    assert_parse_success(source)


def test_052():
    """Assignment to member access"""
    source = "struct S { int x; }; void main() { S s; s.x = s.x + 1; }"
    assert_parse_success(source)


def test_053():
    """Nested if-else"""
    source = "void main() { if (1) if (0) return; else return; }"
    assert_parse_success(source)


def test_054():
    """Unary not with relational"""
    source = "int main() { int x; x = !(1 < 2); return x; }"
    assert_parse_success(source)


def test_055():
    """Precedence with multiplication"""
    source = "int main() { int x; x = 1 + 2 * 3; return x; }"
    assert_parse_success(source)


def test_056():
    """Function call with member access arg"""
    source = "struct S { int x; }; void f(int a) { return; } void main() { S s; f(s.x); }"
    assert_parse_success(source)


def test_057():
    """Switch case with unary minus"""
    source = "void main() { switch (x) { case -1: break; } }"
    assert_parse_success(source)


def test_058():
    """Switch case with constant expression"""
    # Spec allows cases to be constant expressions (e.g. 1+2)
    source = "void main() { switch (x) { case 1 + 2: break; } }"
    assert_parse_success(source)


def test_059():
    """While with inner switch"""
    source = "void main() { while (1) { switch (x) { case 1: break; } } }"
    assert_parse_success(source)


def test_060():
    """Member access from function call result"""
    source = "struct S { int x; }; S make() { S s; return s; } int main() { return make().x; }"
    assert_parse_success(source)


# =======================================================================
# SECTION 2: INVALID PROGRAMS (061-100)
# =======================================================================


def test_061():
    """Extra closing brace"""
    source = "void main() {} }"
    assert_parse_error(source)


def test_062():
    """Struct missing semicolon"""
    source = "struct S { int x; } void main() {}"
    assert_parse_error(source)


def test_063():
    """Struct member missing semicolon"""
    source = "struct S { int x } ; void main() {}"
    assert_parse_error(source)


def test_064():
    """Function missing body"""
    source = "int f(int a, int b);"
    assert_parse_error(source)


def test_065():
    """Function missing RPAREN"""
    source = "int f(int a, int b { return a; }"
    assert_parse_error(source)


def test_066():
    """Function missing LPAREN"""
    source = "int f int a) { return a; }"
    assert_parse_error(source)


def test_067():
    """Parameter missing type"""
    source = "int f(a) { return a; }"
    assert_parse_error(source)


def test_068():
    """Parameter missing identifier"""
    source = "int f(int) { return 1; }"
    assert_parse_error(source)


def test_069():
    """Variable declaration missing identifier"""
    source = "void main() { int = 1; }"
    assert_parse_error(source)


def test_070():
    """Variable declaration missing semicolon"""
    source = "void main() { int x = 1 }"
    assert_parse_error(source)


def test_071():
    """Auto declaration missing semicolon"""
    source = "void main() { auto x = 1 }"
    assert_parse_error(source)


def test_072():
    """Return missing semicolon"""
    source = "int main() { return 1 }"
    assert_parse_error(source)


def test_073():
    """Break missing semicolon"""
    source = "void main() { while (1) { break } }"
    assert_parse_error(source)


def test_074():
    """Stray semicolon (Empty statement not allowed)"""
    # Spec: ';' by itself does not constitute a valid statement
    source = "void main() { ; }"
    assert_parse_error(source)


def test_075():
    """If missing parentheses"""
    source = "void main() { if 1 { return; } }"
    assert_parse_error(source)


def test_076():
    """If missing statement"""
    source = "void main() { if (1) }"
    assert_parse_error(source)


def test_077():
    """While missing parentheses"""
    source = "void main() { while 1 { } }"
    assert_parse_error(source)


def test_078():
    """For missing semicolon"""
    source = "void main() { for (i = 0 i < 10; i = i + 1) { } }"
    assert_parse_error(source)


def test_079():
    """For missing RPAREN"""
    source = "void main() { for (i = 0; i < 10; i = i + 1 { } }"
    assert_parse_error(source)


def test_080():
    """Switch missing brace"""
    source = "void main() { switch (x) case 1: break; }"
    assert_parse_error(source)


def test_081():
    """Case missing colon"""
    source = "void main() { switch (x) { case 1 break; } }"
    assert_parse_error(source)


def test_082():
    """Default missing colon"""
    source = "void main() { switch (x) { default break; } }"
    assert_parse_error(source)


def test_083():
    """Switch missing closing brace"""
    source = "void main() { switch (x) { case 1: break; "
    assert_parse_error(source)


def test_084():
    """Block missing closing brace"""
    source = "void main() { if (1) { return; }"
    assert_parse_error(source)


def test_085():
    """Assignment missing rhs"""
    source = "void main() { int x; x = ; }"
    assert_parse_error(source)


def test_086():
    """Expression statement missing semicolon"""
    source = "void main() { x = 1 }"
    assert_parse_error(source)


def test_087():
    """Struct missing identifier"""
    source = "struct { int x; }; void main() {}"
    assert_parse_error(source)


def test_088():
    """Void not allowed as parameter type"""
    source = "int f(void x) { return x; }"
    assert_parse_error(source)


def test_089():
    """Void not allowed in variable declaration"""
    source = "void main() { void x; }"
    assert_parse_error(source)


def test_090():
    """For missing second semicolon"""
    source = "void main() { for (int i = 0; i < 10) { } }"
    assert_parse_error(source)


def test_091():
    """Case missing expression"""
    source = "void main() { switch (x) { case : break; } }"
    assert_parse_error(source)


def test_092():
    """Else without statement"""
    source = "void main() { if (1) return; else }"
    assert_parse_error(source)


def test_093():
    """Nested struct definition - Not allowed in TyC"""
    source = "struct A { struct B { int x; } b; };"
    assert_parse_error(source)


def test_094():
    source = "void main() { string s = \"Line1\nLine2\"; }"
    
    # Manually parse to check the specific Lexer error message
    result = Parser(source).parse()
    
    # The test passes if it catches the lexical error OR a parsing error
    assert result.startswith("Unclosed String") or result.startswith("Error on line"), \
        f"Expected 'Unclosed String' or 'Error on line', but got: {result}"


def test_095():
    """Missing expression in switch condition"""
    source = "void main() { switch () { case 1: break; } }"
    assert_parse_error(source)


def test_096():
    """Auto type in function parameter"""
    # Spec: Parameters cannot use auto for type inference
    source = "void f(auto x) { return; }"
    assert_parse_error(source)


def test_097():
    """Malformed default label (default followed by expr)"""
    # Spec: default must be followed immediately by colon, not an expression
    source = "void main() { switch (x) { default 1: break; } }"
    assert_parse_error(source)


def test_098():
    # Spec: Illegal escape is any backslash followed by unsupported char
    source = r'void main() { string s = "Bad \q"; }'
    
    # Manually parse to check the specific Lexer error message
    result = Parser(source).parse()
    
    # The test passes if it catches the lexical error OR a parsing error
    assert result.startswith("Illegal Escape") or result.startswith("Error on line"), \
        f"Expected 'Illegal Escape' or 'Error on line', but got: {result}"


def test_099():
    """Statement outside of any function"""
    source = "x = 5; void main() {}"
    assert_parse_error(source)


def test_100():
    """Function declaration inside another function"""
    source = "void main() { void sub() {} }"
    assert_parse_error(source)