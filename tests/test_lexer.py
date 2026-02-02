"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
from src.grammar.lexererr import ErrorToken


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
    expected = "IDENTIFIER,abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_002():
    """Test keywords recognition"""
    source = "func main if else while for let const"
    expected = "IDENTIFIER,func,IDENTIFIER,main,IF,if,ELSE,else,WHILE,while,FOR,for,IDENTIFIER,let,IDENTIFIER,const,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_003():
    """Test integer literals"""
    source = "42 0 -17 007"
    expected = "INT_T,42,INT_T,0,SUB,-,INT_T,17,INT_T,007,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_004():
    """Test float literals"""
    source = "3.14 -2.5 0.0 42. 5."
    expected = "FLOAT_T,3.14,SUB,-,FLOAT_T,2.5,FLOAT_T,0.0,FLOAT_T,42.,FLOAT_T,5.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_005():
    """Test boolean literals"""
    source = "true false"
    expected = "IDENTIFIER,true,IDENTIFIER,false,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_006():
    """Test valid string literals with escape sequences"""
    source = '"Hello World" "Line 1\\nLine 2" "Quote: \\"text\\""'
    expected = 'STRING_T,"Hello World",STRING_T,"Line 1\\nLine 2",STRING_T,"Quote: \\"text\\"",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_007():
    """Test string literals return content (ANTLR keeps quotes)"""
    source = '"Hello World"'
    expected = 'STRING_T,"Hello World",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_008():
    """Test empty string literal"""
    source = '""'
    expected = 'STRING_T,"",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_009():
    """Test operators and separators"""
    source = "+ - * / % == != < <= > >= && || ! = ( ) { } , ; :"
    expected = "ADD,+,SUB,-,MUL,*,DIV,/,MOD,%,EQ,==,NEQ,!=,LT,<,LEQ,<=,GT,>,GEQ,>=,AND,&&,OR,||,NOT,!,ASSIGN,=,LPAREN,(,RPAREN,),LBRACE,{,RBRACE,},COMMA,,,SEMI,;,COLON,:,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_010():
    """Test unsupported operators form individual tokens"""
    source = "-> >>"
    expected = "SUB,-,GT,>,GT,>,GT,>,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 2: COMMENTS
# =======================================================================

def test_011():
    """Test line comment"""
    source = """// This is a comment
                hello"""
    expected = "IDENTIFIER,hello,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_012():
    """Test block comment"""
    source = """/* This is a comment
        * hello
        */
        func foo() {}"""
    expected = "IDENTIFIER,func,IDENTIFIER,foo,LPAREN,(,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_013():
    """Test nested block comment (treated as content inside comment)"""
    source = """/* This is a comment
        hello
        /* xinchao
        bonjour
        */ */
        func foo() {}"""
    expected = "MUL,*,DIV,/,IDENTIFIER,func,IDENTIFIER,foo,LPAREN,(,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_014():
    """Test nested block comment sequence"""
    source = """/* This is a comment
        hello
        xinchao */
        bonjour */
        func foo() {}"""
    expected = "IDENTIFIER,bonjour,MUL,*,DIV,/,IDENTIFIER,func,IDENTIFIER,foo,LPAREN,(,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_015():
    """Test comment only"""
    source = '// abc //def'
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_016():
    """Test comment with function"""
    source = """// abc //def
            func main() {}
            """
    expected = "IDENTIFIER,func,IDENTIFIER,main,LPAREN,(,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_017():
    """Test incomplete block comment start"""
    source = "/* abc"
    expected = "DIV,/,MUL,*,IDENTIFIER,abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_018():
    """Test nested comments text"""
    source = "/* nested /* invalid */ */"
    expected = "MUL,*,DIV,/,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_019():
    """Test multiline comment"""
    source = """/* start still inside */ 42"""
    expected = "INT_T,42,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 3: COMPLEX CODE STRUCTURES
# =======================================================================

def test_020():
    """Test func main logic"""
    source = """func main() -> void { 
        if (x > 0) { 
            print("positive"); 
        }
    }"""
    expected = "IDENTIFIER,func,IDENTIFIER,main,LPAREN,(,RPAREN,),SUB,-,GT,>,VOID,void,LBRACE,{,IF,if,LPAREN,(,IDENTIFIER,x,GT,>,INT_T,0,RPAREN,),LBRACE,{,IDENTIFIER,print,LPAREN,(,STRING_T,\"positive\",RPAREN,),SEMI,;,RBRACE,},RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_021():
    """Test variable declarations"""
    source = """// Valid ASCII identifiers
        let myVariable = 42;
        let _internal = true;"""
    expected = "IDENTIFIER,let,IDENTIFIER,myVariable,ASSIGN,=,INT_T,42,SEMI,;,IDENTIFIER,let,IDENTIFIER,_internal,ASSIGN,=,IDENTIFIER,true,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_022():
    """Test pipeline operator (split into GT GT)"""
    source = "data >> filter(isValid);"
    expected = "IDENTIFIER,data,GT,>,GT,>,IDENTIFIER,filter,LPAREN,(,IDENTIFIER,isValid,RPAREN,),SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_023():
    """Test simple string assignment"""
    source = 'let msg = "Cafe";'
    expected = 'IDENTIFIER,let,IDENTIFIER,msg,ASSIGN,=,STRING_T,"Cafe",SEMI,;,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_024():
    """Test array-like assignment (Error on [)"""
    source = 'strArr = ["abc"];'
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "ErrorToken"
    assert exc_info.value.args[0] == "["

def test_025():
    """Test scope and shadowing"""
    source = """const GLOBAL_CONST: int = 42; 
        func example() {
            let x = 10;
        }"""
    expected = "IDENTIFIER,const,IDENTIFIER,GLOBAL_CONST,COLON,:,INT,int,ASSIGN,=,INT_T,42,SEMI,;,IDENTIFIER,func,IDENTIFIER,example,LPAREN,(,RPAREN,),LBRACE,{,IDENTIFIER,let,IDENTIFIER,x,ASSIGN,=,INT_T,10,SEMI,;,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_026():
    """Test comparison logic"""
    source = 'let str1 = ("abc" < "def");'
    expected = 'IDENTIFIER,let,IDENTIFIER,str1,ASSIGN,=,LPAREN,(,STRING_T,"abc",LT,<,STRING_T,"def",RPAREN,),SEMI,;,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_027():
    """Test modulus in identifier (Fail, splits token)"""
    source = 'let str%1 = 1;'
    expected = "IDENTIFIER,let,IDENTIFIER,str,MOD,%,INT_T,1,ASSIGN,=,INT_T,1,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_028():
    """Test function calls"""
    source = 'let sum = add(5, 3);'
    expected = "IDENTIFIER,let,IDENTIFIER,sum,ASSIGN,=,IDENTIFIER,add,LPAREN,(,INT_T,5,COMMA,,,INT_T,3,RPAREN,),SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_029():
    """Test windows path"""
    source = 'let path = "C:\\\\Users\\\\Admin";'
    expected = 'IDENTIFIER,let,IDENTIFIER,path,ASSIGN,=,STRING_T,"C:\\\\Users\\\\Admin",SEMI,;,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_030():
    """Test float literal without integer part"""
    source = 'let b = .5;'
    expected = "IDENTIFIER,let,IDENTIFIER,b,ASSIGN,=,FLOAT_T,.5,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_031():
    """Test integers with underscores (Splits)"""
    source = 'const result = 1_000_000;'
    expected = "IDENTIFIER,const,IDENTIFIER,result,ASSIGN,=,INT_T,1,IDENTIFIER,_000_000,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_032():
    """Test complex string escapes"""
    source = 'let s = "a\\nb\\tc\\"";'
    expected = 'IDENTIFIER,let,IDENTIFIER,s,ASSIGN,=,STRING_T,"a\\nb\\tc\\"",SEMI,;,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_033():
    """Test struct member access"""
    source = 'let a = point.x;'
    expected = "IDENTIFIER,let,IDENTIFIER,a,ASSIGN,=,IDENTIFIER,point,MEMBER,.,IDENTIFIER,x,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_034():
    """Test nested struct member access"""
    source = 'let value = obj.point.x;'
    expected = "IDENTIFIER,let,IDENTIFIER,value,ASSIGN,=,IDENTIFIER,obj,MEMBER,.,IDENTIFIER,point,MEMBER,.,IDENTIFIER,x,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_035():
    """Test dunder identifier"""
    source = 'let __init__ = "constructor";'
    expected = 'IDENTIFIER,let,IDENTIFIER,__init__,ASSIGN,=,STRING_T,"constructor",SEMI,;,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_036():
    """Test code with spaces and comments"""
    source = """let a = 1; // comment 
            let b = 2;"""
    expected = "IDENTIFIER,let,IDENTIFIER,a,ASSIGN,=,INT_T,1,SEMI,;,IDENTIFIER,let,IDENTIFIER,b,ASSIGN,=,INT_T,2,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_037():
    """Test if logic"""
    source = 'if (a <= b && b >= c) {}'
    expected = "IF,if,LPAREN,(,IDENTIFIER,a,LEQ,<=,IDENTIFIER,b,AND,&&,IDENTIFIER,b,GEQ,>=,IDENTIFIER,c,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_038():
    """Test scientific float in expression"""
    source = 'let x=func(42.)+log(1.0e-18);'
    expected = "IDENTIFIER,let,IDENTIFIER,x,ASSIGN,=,IDENTIFIER,func,LPAREN,(,FLOAT_T,42.,RPAREN,),ADD,+,IDENTIFIER,log,LPAREN,(,FLOAT_T,1.0e-18,RPAREN,),SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_039():
    """Test nested control flow"""
    source = """func main() -> void {
        while (true) {
            if (check()) {
                break;
            } else {
                continue;
            }
        }
    }"""
    expected = "IDENTIFIER,func,IDENTIFIER,main,LPAREN,(,RPAREN,),SUB,-,GT,>,VOID,void,LBRACE,{,WHILE,while,LPAREN,(,IDENTIFIER,true,RPAREN,),LBRACE,{,IF,if,LPAREN,(,IDENTIFIER,check,LPAREN,(,RPAREN,),RPAREN,),LBRACE,{,BREAK,break,SEMI,;,RBRACE,},ELSE,else,LBRACE,{,CONTINUE,continue,SEMI,;,RBRACE,},RBRACE,},RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 4: EDGE CASES & LITERALS
# =======================================================================

def test_040():
    """Test float scientific presentation"""
    source = "1.23e10 -4.56E-3 0.e0"
    expected = "FLOAT_T,1.23e10,SUB,-,FLOAT_T,4.56E-3,FLOAT_T,0.e0,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_041():
    """Test large float"""
    source = "3.14156 -73493.54343e-10"
    expected = "FLOAT_T,3.14156,SUB,-,FLOAT_T,73493.54343e-10,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_042():
    """Test float vs int"""
    source = "5 10.e-10"
    expected = "INT_T,5,FLOAT_T,10.e-10,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_043():
    """Test float boundary parsing"""
    source = "7-10 5.6e"
    expected = "INT_T,7,SUB,-,INT_T,10,FLOAT_T,5.6,IDENTIFIER,e,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_044():
    """Test scientific no dot"""
    source = "7E5"
    expected = "FLOAT_T,7E5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_045():
    """Test backslash string sequence as individual errors"""
    source = '\\\\\\'
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "ErrorToken"
    assert exc_info.value.args[0] == "\\"

def test_046():
    """Test identifier with underscore"""
    source = '712dbcD_i'
    expected = "INT_T,712,IDENTIFIER,dbcD_i,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_047():
    """Duplicate test of identifier with underscore"""
    source = '712dbcD_i'
    expected = "INT_T,712,IDENTIFIER,dbcD_i,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_048():
    """Test nested quotes in string"""
    source = "\"She said: \\\"Hello\\\\\\\"\""
    expected = 'STRING_T,"She said: \\\"Hello\\\\\\\"",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_049():
    """Test math no spaces"""
    source = "a+b*c-(d/e);"
    expected = "IDENTIFIER,a,ADD,+,IDENTIFIER,b,MUL,*,IDENTIFIER,c,SUB,-,LPAREN,(,IDENTIFIER,d,DIV,/,IDENTIFIER,e,RPAREN,),SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_050():
    """Test identifier with digits"""
    source = "_var123 another_456"
    expected = "IDENTIFIER,_var123,IDENTIFIER,another_456,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_051():
    """Test string with multiple escapes"""
    source = 'let name = "A\\"B\\nC\\tD";'
    expected = 'IDENTIFIER,let,IDENTIFIER,name,ASSIGN,=,STRING_T,"A\\"B\\nC\\tD",SEMI,;,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_052():
    """Test number followed by alpha"""
    source = '123abc'
    expected = "INT_T,123,IDENTIFIER,abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_053():
    """Test newlines in string token"""
    source = '"line1\\nline2\\nline3"'
    expected = 'STRING_T,"line1\\nline2\\nline3",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_054():
    """Test dots"""
    source = ".123 456."
    expected = "FLOAT_T,.123,FLOAT_T,456.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_055():
    """Test double dots"""
    source = '123.456.789'
    expected = "FLOAT_T,123.456,FLOAT_T,.789,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_056():
    """Test hex-like (not supported)"""
    source = '0x1F'
    expected = "INT_T,0,IDENTIFIER,x1F,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_057():
    """Test underscore numbers (not supported)"""
    source = '1_2_3_4'
    expected = "INT_T,1,IDENTIFIER,_2_3_4,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_058():
    """Test range operator-like"""
    source = '0..1'
    expected = "FLOAT_T,0.,FLOAT_T,.1,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_059():
    """Test escaped quote"""
    source = '"\\"escaped quote\\""'
    expected = 'STRING_T,"\\"escaped quote\\"",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_060():
    """Test backslashes string"""
    source = '"abc\\\\"'
    expected = 'STRING_T,"abc\\\\",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_061():
    """Test func name with digits"""
    source = 'func _main123() {}'
    expected = "IDENTIFIER,func,IDENTIFIER,_main123,LPAREN,(,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_062():
    """Test comparison no spaces"""
    source = 'main==true'
    expected = "IDENTIFIER,main,EQ,==,IDENTIFIER,true,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_063():
    """Test complex string"""
    source = 'let name1 = "Nguyen\\nVan\\tA";'
    expected = 'IDENTIFIER,let,IDENTIFIER,name1,ASSIGN,=,STRING_T,"Nguyen\\nVan\\tA",SEMI,;,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_064():
    """Test backslash text"""
    source = '"backslash: \\\\"'
    expected = 'STRING_T,"backslash: \\\\",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_065():
    """Test increment logic"""
    source = 'a+++b'
    expected = "IDENTIFIER,a,INC,++,ADD,+,IDENTIFIER,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_066():
    """Test func call no space"""
    source = 'let x=func(42)+log(1.0);'
    expected = "IDENTIFIER,let,IDENTIFIER,x,ASSIGN,=,IDENTIFIER,func,LPAREN,(,INT_T,42,RPAREN,),ADD,+,IDENTIFIER,log,LPAREN,(,FLOAT_T,1.0,RPAREN,),SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_067():
    """Test tab escape"""
    source = '"Tab\\tSpace"'
    expected = 'STRING_T,"Tab\\tSpace",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_068():
    """Test multiple escaped quotes"""
    source = '"Valid\\\\quote\\"in\\"string"'
    expected = 'STRING_T,"Valid\\\\quote\\"in\\"string",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_069():
    """Test scientific float"""
    source = 'let x = 1.e-10;'
    expected = "IDENTIFIER,let,IDENTIFIER,x,ASSIGN,=,FLOAT_T,1.e-10,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_070():
    """Test escapes"""
    source = '"abc\\n\\t\\r"'
    expected = 'STRING_T,"abc\\n\\t\\r",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_071():
    """Test concatenated text"""
    source = 'truefalse123'
    expected = "IDENTIFIER,truefalse123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_072():
    """Test leading zeros"""
    source = 'let v = 0000123;'
    expected = "IDENTIFIER,let,IDENTIFIER,v,ASSIGN,=,INT_T,0000123,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_073():
    """Test escaped quote end"""
    source = '"Escaped quote: \\" end"'
    expected = 'STRING_T,"Escaped quote: \\" end",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_074():
    """Test mixed escapes"""
    source = 'let s = "\\nNew\\tTab\\\\";'
    expected = 'IDENTIFIER,let,IDENTIFIER,s,ASSIGN,=,STRING_T,"\\nNew\\tTab\\\\",SEMI,;,EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 5: ERROR HANDLING (Token-based)
# =======================================================================

def test_075():
    """Test unclosed string literal results in ERROR token"""
    source = '"Hello World'
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "UncloseString"
    assert exc_info.value.args[0] == '"Hello World'
        

def test_076():
    """Test illegal escape sequence results in ERROR token"""
    source = '"Hello \\x World"'
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "IllegalEscape"
    assert exc_info.value.args[0] == '"Hello \\x World"'

def test_077():
    """Test invalid character (e.g., @) returns ERROR token"""
    source = "let x = 5; @ invalid"
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "ErrorToken"
    assert exc_info.value.args[0] == "@"

def test_078():
    """Test invalid character in middle of expression"""
    source = "120@abc"
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "ErrorToken"
    assert exc_info.value.args[0] == "@"

def test_079():
    """Test unsupported brackets return ERROR token instead of crashing"""
    source = 'let matrix: [int];'
    # Treating '[' as an unexpected character/error token
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "ErrorToken"
    assert exc_info.value.args[0] == "["

def test_080():
    """Test string literals with unescaped newline (returns ERROR)"""
    source = '"Line 1\nLine 2"'
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "UncloseString"
    assert exc_info.value.args[0] == '"Line 1\n'

def test_081():
    """Non-ASCII/Special symbols in identifier position"""
    source = 'let str$1 = "abc";'
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "ErrorToken"
    assert exc_info.value.args[0] == "$"

def test_082():
    """Test unicode escape (Not supported, returns ERROR)"""
    source = '"hello \\u1234"'
    with pytest.raises(Exception) as exc_info:
        Tokenizer(source).get_tokens_as_string()
    assert exc_info.type.__name__ == "IllegalEscape"
    assert exc_info.value.args[0] == '"hello \\u1234"'

def test_083():
    """Test illegal escape f (Formfeed)"""
    # \f is valid in TyC spec
    source = '"abc\\f"'
    expected = 'STRING_T,"abc\\f",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_084():
    """Test multiline comment"""
    source = """/* start still inside */ 42"""
    expected = "INT_T,42,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_085():
    source = 'let v = 0000123;'
    expected = "IDENTIFIER,let,IDENTIFIER,v,ASSIGN,=,INT_T,0000123,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_086():
    source = '"Escaped quote: \\" end"'
    expected = "STRING_T,\"Escaped quote: \\\" end\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_087():
    source = 'let s = "\\nNew\\tTab\\\\";'
    expected = "IDENTIFIER,let,IDENTIFIER,s,ASSIGN,=,STRING_T,\"\\nNew\\tTab\\\\\",SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_088():
    source = """int add(int a, int b) {
        return a + b;
    }
    
    float multiply(float a, float b) {
        return a * b;
    }"""
    expected = "INT,int,IDENTIFIER,add,LPAREN,(,INT,int,IDENTIFIER,a,COMMA,,,INT,int,IDENTIFIER,b,RPAREN,),LBRACE,{,RETURN,return,IDENTIFIER,a,ADD,+,IDENTIFIER,b,SEMI,;,RBRACE,},FLOAT,float,IDENTIFIER,multiply,LPAREN,(,FLOAT,float,IDENTIFIER,a,COMMA,,,FLOAT,float,IDENTIFIER,b,RPAREN,),LBRACE,{,RETURN,return,IDENTIFIER,a,MUL,*,IDENTIFIER,b,SEMI,;,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


# =======================================================================
# SECTION 6: COMPREHENSIVE KEYWORD AND OPERATOR TESTS (089-100)
# =======================================================================

def test_089():
    """Test all keywords: auto, break, case, continue, default, else, float, for, if, int, return, string, struct, switch, void, while"""
    source = "auto break case continue default else float for if int return string struct switch void while"
    expected = "AUTO,auto,BREAK,break,CASE,case,CONTINUE,continue,DEFAULT,default,ELSE,else,FLOAT,float,FOR,for,IF,if,INT,int,RETURN,return,STRING,string,STRUCT,struct,SWITCH,switch,VOID,void,WHILE,while,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_090():
    """Test member access operator with chained access"""
    source = "person.name person.age rect.point.x"
    expected = "IDENTIFIER,person,MEMBER,.,IDENTIFIER,name,IDENTIFIER,person,MEMBER,.,IDENTIFIER,age,IDENTIFIER,rect,MEMBER,.,IDENTIFIER,point,MEMBER,.,IDENTIFIER,x,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_091():
    """Test increment and decrement operators"""
    source = "x++ ++x y-- --y a+++b"
    expected = "IDENTIFIER,x,INC,++,INC,++,IDENTIFIER,x,IDENTIFIER,y,DEC,--,DEC,--,IDENTIFIER,y,IDENTIFIER,a,INC,++,ADD,+,IDENTIFIER,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_092():
    """Test string with all supported escape sequences"""
    source = '"\\b\\f\\r\\n\\t\\"\\\\test"'
    expected = 'STRING_T,"\\b\\f\\r\\n\\t\\"\\\\test",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_093():
    """Test struct declaration tokens"""
    source = "struct Point { int x; int y; };"
    expected = "STRUCT,struct,IDENTIFIER,Point,LBRACE,{,INT,int,IDENTIFIER,x,SEMI,;,INT,int,IDENTIFIER,y,SEMI,;,RBRACE,},SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_094():
    """Test switch-case statement tokens"""
    source = "switch (x) { case 1: break; default: break; }"
    expected = "SWITCH,switch,LPAREN,(,IDENTIFIER,x,RPAREN,),LBRACE,{,CASE,case,INT_T,1,COLON,:,BREAK,break,SEMI,;,DEFAULT,default,COLON,:,BREAK,break,SEMI,;,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_095():
    """Test for loop with all components"""
    source = "for (auto i = 0; i < 10; ++i) { }"
    expected = "FOR,for,LPAREN,(,AUTO,auto,IDENTIFIER,i,ASSIGN,=,INT_T,0,SEMI,;,IDENTIFIER,i,LT,<,INT_T,10,SEMI,;,INC,++,IDENTIFIER,i,RPAREN,),LBRACE,{,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_096():
    """Test float with scientific notation variants"""
    source = "1e5 2E-10 3.14e+5 .5e2 7E5"
    expected = "FLOAT_T,1e5,FLOAT_T,2E-10,FLOAT_T,3.14e+5,FLOAT_T,.5e2,FLOAT_T,7E5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_097():
    """Test logical operators with operands"""
    source = "a && b || c !d"
    expected = "IDENTIFIER,a,AND,&&,IDENTIFIER,b,OR,||,IDENTIFIER,c,NOT,!,IDENTIFIER,d,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_098():
    """Test all relational operators"""
    source = "a == b a != b a < b a <= b a > b a >= b"
    expected = "IDENTIFIER,a,EQ,==,IDENTIFIER,b,IDENTIFIER,a,NEQ,!=,IDENTIFIER,b,IDENTIFIER,a,LT,<,IDENTIFIER,b,IDENTIFIER,a,LEQ,<=,IDENTIFIER,b,IDENTIFIER,a,GT,>,IDENTIFIER,b,IDENTIFIER,a,GEQ,>=,IDENTIFIER,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_099():
    """Test string with backslash and escape at end"""
    source = '"path\\\\to\\\\file"'
    expected = 'STRING_T,"path\\\\to\\\\file",EOF'
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_100():
    """Test complex expression with mixed operators and types"""
    source = "int result = (a + b) * (c - d) / e % f;"
    expected = "INT,int,IDENTIFIER,result,ASSIGN,=,LPAREN,(,IDENTIFIER,a,ADD,+,IDENTIFIER,b,RPAREN,),MUL,*,LPAREN,(,IDENTIFIER,c,SUB,-,IDENTIFIER,d,RPAREN,),DIV,/,IDENTIFIER,e,MOD,%,IDENTIFIER,f,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected
