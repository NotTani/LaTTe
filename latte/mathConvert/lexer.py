import ply.lex as lex
from ply.lex import TOKEN

tokens = (
    "NUMBER",
    "ENTITY",

    "MATHEMATICAL_ID",
    "CONTROL_ID",
    "GENERIC_ID",
    "OPEN_PAREN",
    "CLOSE_PAREN",

    "PLUS",
    "MINUS",
    "DIV",
    "MULTI"
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
    return t


@TOKEN(r'(?P<n>:?[a-zA-Z]+)')
def t_GENERIC_ID(t):
    n = t.lexer.lexmatch.group('n')
    if n.startswith(':'):
        t.type = "CONTROL_ID"
        n = n[1:]
    else:
        t.type = "GENERIC_ID"
    t.value = n
    return t


@TOKEN(r'\ +')
def t_SPACE(_):
    pass


@TOKEN(r'(?P<o>\+\-\/\*)')
def t_OP(t):
    op = t.lexer.lexmatch.group('o')
    if op == '+':
        t.type = "PLUS"
    elif op == '-':
        t.type = "MINUS"
    elif op == '/':
        t.type = "DIV"
    elif op == '*':
        t.type = 'MULTI'

    return t


@TOKEN(r'[' +
       ''.join([r'\\' + tok for tok, _ in parens.keys()]) +
       ''.join([r'\\' + tok for _, tok in parens.values()]) + r']')
def t_PAREN(t):
    pass


t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'

lexer = lex.lex()