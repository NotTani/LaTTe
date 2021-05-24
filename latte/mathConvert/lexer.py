import ply.lex as lex
from ply.lex import TOKEN

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
    "SYMBOL",
    "NUMBER",
    "EQUALS",
    "POWER",
    "SUBSCRIPT",
    "ENTITY",

    "ADDSUB_OP",
    "DIV_OP",
    "MULT_OP",
    "CONTROL_ID",
    "OPEN_PAREN",
    "CLOSE_PAREN",
    "OPEN_INVIS_PAREN",
    "CLOSE_INVIS_PAREN"
)

parens = {
    '{': '}',
    '[': ']',
    '(': ')'
}


@TOKEN(r'(-)?\d+(\.\d+)?')
def t_NUMBER(t):
    return t


@TOKEN(r'\&(?P<entity_name>.+);')
def t_ENTITY(t):
    t.value = t.lexer.lexmatch.group('entity_name')
    return t


t_MATHEMATICAL_ID = r'sin|cos|ceil|floor|abs|sqrt'
t_SYMBOL = r'[a-zA-Z]'
t_POWER = r'\^'
t_SUBSCRIPT = r'_'
t_CONTROL_ID = '(?P<n>:[a-zA-Z]+)'


@TOKEN(r'\ +')
def t_SPACE(_):
    pass


@TOKEN(r'(?P<o>[\+\-\/\*#])')
def t_OP(t):
    t.value = t.lexer.lexmatch.group('o')
    if t.value == '+' or t.value == '-':
        t.type = "ADDSUB_OP"
    elif t.value in ('#', '*'):
        if t.value == '#':
            t.value = ''
        t.type = "MULT_OP"
    elif t.value == '/':
        t.type = "DIV_OP"
    return t


t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_OPEN_INVIS_PAREN = r'@g\{'
t_CLOSE_INVIS_PAREN = r'\}'
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
