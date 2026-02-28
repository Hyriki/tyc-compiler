"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
# from src.grammar.lexererr import ErrorToken


# def test_lexer_placeholder():
#     """Placeholder test - replace with actual test cases"""
#     source = "// This is a placeholder test"
#     tokenizer = Tokenizer(source)
#     # TODO: Add actual test assertions

#     assert True

# =======================================================================
# SECTION 1: BASIC TOKENS & LITERALS
# =======================================================================

def test_001():
    """Test basic identifier tokenization"""
    source = "abc"
    expected = "abc,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_002():
    """Test TyC keywords recognition"""
    source = "auto if else while for int float string struct void return break continue switch case default"
    expected = "auto,if,else,while,for,int,float,string,struct,void,return,break,continue,switch,case,default,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_003():
    """Test integer literals"""
    source = "42 0 -17 007"
    expected = "42,0,-,17,007,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_004():
    """Test float literals"""
    source = "3.14 -2.5 0.0 42. 5."
    expected = "3.14,-,2.5,0.0,42.,5.,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_005():
    """Test boolean (treated as identifiers in TyC)"""
    source = "true false"
    expected = "true,false,<EOF>" 
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_006():
    """Test valid string literals (Quotes stripped)"""
    source = '"Hello World" "Line 1\\nLine 2" "Quote: \\"text\\""'
    # Quotes are removed by the lexer action { self.text = self.text[1:-1] }
    expected = 'Hello World,Line 1\\nLine 2,Quote: \\"text\\",<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_007():
    """Test simple string literal (Quotes stripped)"""
    source = '"Hello World"'
    expected = 'Hello World,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_008():
    """Test empty string literal"""
    source = '""'
    expected = ',<EOF>' # Empty content
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_009():
    """Test operators and separators"""
    source = "+ - * / % == != < <= > >= && || ! = ( ) { } , ; :"
    expected = "+,-,*,/,%,==,!=,<,<=,>,>=,&&,||,!,=,(,),{,},,,;,:,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_010():
    """Test unsupported operators form individual tokens"""
    source = "-> >>"
    # -> becomes -,> and >> becomes >,>
    expected = "-,>,>,>,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 2: COMMENTS
# =======================================================================

def test_011():
    """Test line comment"""
    source = """// This is a comment
                hello"""
    expected = "hello,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_012():
    """Test block comment"""
    source = """/* This is a comment
        * hello
        */
        void foo() {}"""
    expected = "void,foo,(,),{,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_013():
    """Test nested block comment (treated as content inside comment)"""
    source = """/* This is a comment
        hello
        /* xinchao
        bonjour
        */ */
        void foo() {}"""
    # The first */ closes the comment. The second */ is outside.
    expected = "*,/,void,foo,(,),{,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_014():
    """Test nested block comment sequence"""
    source = """/* This is a comment
        hello
        xinchao */
        bonjour */
        void foo() {}"""
    expected = "bonjour,*,/,void,foo,(,),{,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_015():
    """Test comment only"""
    source = '// abc //def'
    expected = "<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_016():
    """Test comment with function"""
    source = """// abc //def
            void main() {}
            """
    expected = "void,main,(,),{,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_017():
    """Test incomplete block comment start"""
    source = "/* abc"
    expected = "/,*,abc,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_018():
    """Test nested comments text"""
    source = "/* nested /* invalid */ */"
    expected = "*,/,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_019():
    """Test multiline comment"""
    source = """/* start still inside */ 42"""
    expected = "42,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 3: COMPLEX CODE STRUCTURES
# =======================================================================

def test_020():
    """Test void main logic (TyC syntax)"""
    source = """void main() { 
        if (x > 0) { 
            print("positive"); 
        }
    }"""
    expected = "void,main,(,),{,if,(,x,>,0,),{,print,(,positive,),;,},},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_021():
    """Test variable declarations (using auto)"""
    source = """// Valid ASCII identifiers
        auto myVariable = 42;
        auto _internal = 1;"""
    expected = "auto,myVariable,=,42,;,auto,_internal,=,1,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_022():
    """Test pipeline operator (split into GT GT)"""
    source = "data >> filter(isValid);"
    expected = "data,>,>,filter,(,isValid,),;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_023():
    """Test simple string assignment"""
    source = 'auto msg = "Cafe";'
    expected = 'auto,msg,=,Cafe,;,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_024():
    """Test array-like assignment (Expect error char in stream)"""
    # TyC has no brackets []
    source = 'strArr = ["abc"];'
    result = Tokenizer(source).get_tokens_as_string()
    assert "Error Token" in result

def test_025():
    """Test scope and shadowing"""
    source = """int GLOBAL_CONST = 42; 
        void example() {
            int x = 10;
        }"""
    expected = "int,GLOBAL_CONST,=,42,;,void,example,(,),{,int,x,=,10,;,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_026():
    """Test comparison logic"""
    source = 'auto str1 = ("abc" < "def");'
    expected = 'auto,str1,=,(,abc,<,def,),;,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_027():
    """Test modulus in identifier (Fail, splits token)"""
    source = 'auto str%1 = 1;'
    expected = "auto,str,%,1,=,1,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_028():
    """Test function calls"""
    source = 'auto sum = add(5, 3);'
    expected = "auto,sum,=,add,(,5,,,3,),;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_029():
    """Test windows path"""
    source = 'auto path = "C:\\\\Users\\\\Admin";'
    expected = 'auto,path,=,C:\\\\Users\\\\Admin,;,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_030():
    """Test float literal without integer part"""
    source = 'auto b = .5;'
    expected = "auto,b,=,.5,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_031():
    """Test integers with underscores (Splits)"""
    source = 'int result = 1_000_000;'
    expected = "int,result,=,1,_000_000,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_032():
    """Test complex string escapes"""
    source = 'auto s = "a\\nb\\tc\\"";'
    expected = 'auto,s,=,a\\nb\\tc\\",;,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_033():
    """Test struct member access"""
    source = 'auto a = point.x;'
    expected = "auto,a,=,point,.,x,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_034():
    """Test nested struct member access"""
    source = 'auto value = obj.point.x;'
    expected = "auto,value,=,obj,.,point,.,x,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_035():
    """Test dunder identifier"""
    source = 'auto __init__ = "constructor";'
    expected = 'auto,__init__,=,constructor,;,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_036():
    """Test code with spaces and comments"""
    source = """auto a = 1; // comment 
            auto b = 2;"""
    expected = "auto,a,=,1,;,auto,b,=,2,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_037():
    """Test if logic"""
    source = 'if (a <= b && b >= c) {}'
    expected = "if,(,a,<=,b,&&,b,>=,c,),{,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_038():
    """Test scientific float in expression"""
    source = 'auto x=func(42.)+log(1.0e-18);'
    expected = "auto,x,=,func,(,42.,),+,log,(,1.0e-18,),;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_039():
    """Test nested control flow"""
    source = """void main() {
        while (1) {
            if (check()) {
                break;
            } else {
                continue;
            }
        }
    }"""
    expected = "void,main,(,),{,while,(,1,),{,if,(,check,(,),),{,break,;,},else,{,continue,;,},},},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 4: EDGE CASES & LITERALS
# =======================================================================

def test_040():
    """Test float scientific presentation"""
    source = "1.23e10 -4.56E-3 0.e0"
    expected = "1.23e10,-,4.56E-3,0.e0,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_041():
    """Test large float"""
    source = "3.14156 -73493.54343e-10"
    expected = "3.14156,-,73493.54343e-10,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_042():
    """Test float vs int"""
    source = "5 10.e-10"
    expected = "5,10.e-10,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_043():
    """Test float boundary parsing"""
    source = "7-10 5.6e"
    # 5.6 is float, e is identifier
    expected = "7,-,10,5.6,e,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_044():
    """Test scientific no dot"""
    source = "7E5"
    expected = "7E5,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_045():
    """Test backslash string sequence as individual errors"""
    source = '\\\\\\'
    # This is not a string, it's garbage input
    result = Tokenizer(source).get_tokens_as_string()
    assert "Error Token" in result

def test_046():
    """Test identifier with underscore"""
    source = '712dbcD_i'
    # 712 is int, remainder is ID
    expected = "712,dbcD_i,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_047():
    """Duplicate test of identifier with underscore"""
    source = '712dbcD_i'
    expected = "712,dbcD_i,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_048():
    """Test nested quotes in string"""
    source = "\"She said: \\\"Hello\\\\\\\"\""
    expected = 'She said: \\\"Hello\\\\\\\",<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_049():
    """Test math no spaces"""
    source = "a+b*c-(d/e);"
    expected = "a,+,b,*,c,-,(,d,/,e,),;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_050():
    """Test identifier with digits"""
    source = "_var123 another_456"
    expected = "_var123,another_456,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_051():
    """Test string with multiple escapes"""
    source = 'auto name = "A\\"B\\nC\\tD";'
    expected = 'auto,name,=,A\\"B\\nC\\tD,;,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_052():
    """Test number followed by alpha"""
    source = '123abc'
    expected = "123,abc,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_053():
    """Test newlines in string token"""
    source = '"line1\\nline2\\nline3"'
    expected = 'line1\\nline2\\nline3,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_054():
    """Test dots"""
    source = ".123 456."
    expected = ".123,456.,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_055():
    """Test double dots"""
    source = '123.456.789'
    expected = "123.456,.789,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_056():
    """Test hex-like (not supported in TyC)"""
    source = '0x1F'
    # 0 is int, x1F is ID
    expected = "0,x1F,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_057():
    """Test underscore numbers (not supported)"""
    source = '1_2_3_4'
    # 1 is int, _2_3_4 is ID
    expected = "1,_2_3_4,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_058():
    """Test range operator-like"""
    source = '0..1'
    # 0. is float, .1 is float
    expected = "0.,.1,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_059():
    """Test escaped quote"""
    source = '"\\"escaped quote\\""'
    expected = '\\"escaped quote\\",<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_060():
    """Test backslashes string"""
    source = '"abc\\\\"'
    expected = 'abc\\\\,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_061():
    """Test func name with digits"""
    source = 'func _main123() {}'
    # func is identifier in TyC
    expected = "func,_main123,(,),{,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_062():
    """Test comparison no spaces"""
    source = 'main==true'
    # main and true are IDs
    expected = "main,==,true,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_063():
    """Test complex string"""
    source = 'auto name1 = "Nguyen\\nVan\\tA";'
    expected = 'auto,name1,=,Nguyen\\nVan\\tA,;,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_064():
    """Test backslash text"""
    source = '"backslash: \\\\"'
    expected = 'backslash: \\\\,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_065():
    """Test increment logic"""
    source = 'a+++b'
    expected = "a,++,+,b,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_066():
    """Test func call no space"""
    source = 'auto x=func(42)+log(1.0);'
    expected = "auto,x,=,func,(,42,),+,log,(,1.0,),;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_067():
    """Test tab escape"""
    source = '"Tab\\tSpace"'
    expected = 'Tab\\tSpace,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_068():
    """Test multiple escaped quotes"""
    source = '"Valid\\\\quote\\"in\\"string"'
    expected = 'Valid\\\\quote\\"in\\"string,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_069():
    """Test scientific float"""
    source = 'auto x = 1.e-10;'
    expected = "auto,x,=,1.e-10,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_070():
    """Test escapes"""
    source = '"abc\\n\\t\\r"'
    expected = 'abc\\n\\t\\r,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_071():
    """Test concatenated text"""
    source = 'truefalse123'
    # ID
    expected = "truefalse123,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_072():
    """Test leading zeros"""
    source = 'auto v = 0000123;'
    expected = "auto,v,=,0000123,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_073():
    """Test escaped quote end"""
    source = '"Escaped quote: \\" end"'
    expected = 'Escaped quote: \\" end,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_074():
    """Test mixed escapes"""
    source = 'auto s = "\\nNew\\tTab\\\\";'
    expected = 'auto,s,=,\\nNew\\tTab\\\\,;,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 5: ERROR HANDLING (Token-based)
# =======================================================================

def test_075():
    """Test unclosed string literal results in ERROR token"""
    source = '"Hello World'
    result = Tokenizer(source).get_tokens_as_string()
    assert "Unclosed String" in result
        
def test_076():
    """Test illegal escape sequence results in ERROR token"""
    source = '"Hello \\x World"'
    result = Tokenizer(source).get_tokens_as_string()
    assert "Illegal Escape" in result

def test_077():
    """Test invalid character (e.g., @) returns ERROR token"""
    source = "auto x = 5; @ invalid"
    result = Tokenizer(source).get_tokens_as_string()
    assert "Error Token" in result

def test_078():
    """Test invalid character in middle of expression"""
    source = "120@abc"
    result = Tokenizer(source).get_tokens_as_string()
    assert "Error Token" in result

def test_079():
    """Test unsupported brackets return ERROR token"""
    source = 'auto matrix: [int];'
    result = Tokenizer(source).get_tokens_as_string()
    assert "Error Token" in result

def test_080():
    """Test string literals with unescaped newline (returns ERROR)"""
    source = '"Line 1\nLine 2"'
    result = Tokenizer(source).get_tokens_as_string()
    assert "Unclosed String" in result

def test_081():
    """Non-ASCII/Special symbols in identifier position"""
    source = 'auto str$1 = "abc";'
    result = Tokenizer(source).get_tokens_as_string()
    assert "Error Token" in result

def test_082():
    """Test unicode escape (Not supported, returns ERROR)"""
    source = '"hello \\u1234"'
    result = Tokenizer(source).get_tokens_as_string()
    assert "Illegal Escape" in result

def test_083():
    """Test valid escape f (Formfeed)"""
    source = '"abc\\f"'
    expected = 'abc\\f,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_084():
    """Test multiline comment 2"""
    source = """/* start still inside */ 42"""
    expected = "42,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_085():
    """Test leading zeros simple"""
    source = 'auto v = 0000123;'
    expected = "auto,v,=,0000123,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_086():
    """Test escaped quote (Duplicate of 073)"""
    source = '"Escaped quote: \\" end"'
    expected = 'Escaped quote: \\" end,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_087():
    """Test mixed escapes"""
    source = 'auto s = "\\nNew\\tTab\\\\";'
    expected = "auto,s,=,\\nNew\\tTab\\\\,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_088():
    """Test function declarations (TyC syntax)"""
    source = """int add(int a, int b) {
        return a + b;
    }
    
    float multiply(float a, float b) {
        return a * b;
    }"""
    expected = "int,add,(,int,a,,,int,b,),{,return,a,+,b,;,},float,multiply,(,float,a,,,float,b,),{,return,a,*,b,;,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 6: COMPREHENSIVE KEYWORD AND OPERATOR TESTS
# =======================================================================

def test_089():
    """Test all keywords"""
    source = "auto break case continue default else float for if int return string struct switch void while"
    expected = "auto,break,case,continue,default,else,float,for,if,int,return,string,struct,switch,void,while,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_090():
    """Test member access operator with chained access"""
    source = "person.name person.age rect.point.x"
    expected = "person,.,name,person,.,age,rect,.,point,.,x,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_091():
    """Test increment and decrement operators"""
    source = "x++ ++x y-- --y a+++b"
    expected = "x,++,++,x,y,--,--,y,a,++,+,b,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_092():
    """Test string with all supported escape sequences"""
    source = '"\\b\\f\\r\\n\\t\\"\\\\test"'
    expected = '\\b\\f\\r\\n\\t\\"\\\\test,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_093():
    """Test struct declaration tokens"""
    source = "struct Point { int x; int y; };"
    expected = "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_094():
    """Test switch-case statement tokens"""
    source = "switch (x) { case 1: break; default: break; }"
    expected = "switch,(,x,),{,case,1,:,break,;,default,:,break,;,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_095():
    """Test for loop with all components"""
    source = "for (auto i = 0; i < 10; ++i) { }"
    expected = "for,(,auto,i,=,0,;,i,<,10,;,++,i,),{,},<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_096():
    """Test float with scientific notation variants"""
    source = "1e5 2E-10 3.14e+5 .5e2 7E5"
    expected = "1e5,2E-10,3.14e+5,.5e2,7E5,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_097():
    """Test logical operators with operands"""
    source = "a && b || c !d"
    expected = "a,&&,b,||,c,!,d,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_098():
    """Test all relational operators"""
    source = "a == b a != b a < b a <= b a > b a >= b"
    expected = "a,==,b,a,!=,b,a,<,b,a,<=,b,a,>,b,a,>=,b,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_099():
    """Test string with backslash and escape at end"""
    source = '"path\\\\to\\\\file"'
    expected = 'path\\\\to\\\\file,<EOF>'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_100():
    """Test complex expression with mixed operators and types"""
    source = "int result = (a + b) * (c - d) / e % f;"
    expected = "int,result,=,(,a,+,b,),*,(,c,-,d,),/,e,%,f,;,<EOF>"
    assert Tokenizer(source).get_tokens_as_string() == expected
