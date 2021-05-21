import ply.lex as lex
from ply.lex import TOKEN
from mathConvert.mathml import InvalidLaTTeMath

MATHEMATICAL_FUNCTIONS = [
    'sin',
    'cos',
    'ceil',
    'floor',
    'abs',
    'sqrt'
]

tokens = (
    "MATHEMATICAL_ID",
    "NUMBER",
    "EQUALS",
    "POWER",
    "SUBSCRIPT",
    "ENTITY",

    "ADDSUB_OP",
    "DIV_OP",
    "MULT_OP",
    "SYMBOL",
    "CONTROL_ID",
    "OPEN_PAREN",
    "CLOSE_PAREN",
)

parens = {
    '{': '}',
    '[': ']',
    '(': ')'
}


@TOKEN(r'(-)?\d+(\.\d+)?')
def t_NUMBER(t):
    return t


@TOKEN(r'&(?P<entity_name>.+);')
def t_ENTITY(t):
    t.value = t.lexer.lexmatch.group('entity_name')
    if t.value == "+" or "-":
        t.type = "OP_ADDSUB"
    elif t.value == "*":
        t.type = "OP_MULT"
    elif t.value == "/":
        t.type = "OP_DIV"
    return t


t_MATHEMATICAL_ID = '(sin)|(cos)|(ceil)|(floor)|(abs)'
t_SYMBOL = r'(?P<n>[a-zA-Z])'
t_POWER = r'\^'
t_SUBSCRIPT = r'_'
t_CONTROL_ID = '(?P<n>:[a-zA-Z]+)'


@TOKEN(r'\ +')
def t_SPACE(_):
    pass


@TOKEN(r'(?P<o>[\+\-\/\*])')
def t_OP(t):
    t.value = t.lexer.lexmatch.group('o')
    if t.value == '+' or t.value == '-':
        t.type = "ADDSUB_OP"
    elif t.value == '*':
        t.type = "MULT_OP"
    elif t.value == '/':
        t.type = "DIV_OP"
    return t


t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_EQUALS = r'='


# def t_error(error):
#     raise InvalidLaTTeMath(error)


lexer = lex.lex()


def tokenize(inp):
    lexer.input(inp)
    toks = []
    while True:
        token = lexer.token()
        if not token:
            break
        toks.append(token)

    return toks