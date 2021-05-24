import ply.yacc as yacc
from .lexer import tokens
from .mathml_elements import *


def _rule(docstring):
    def decorator(function):
        function.__doc__ = docstring
        return function

    return decorator


@_rule('expression : expression ENTITY expression')
def p_expression_entity(p):
    p[0] = mrow([p[1], special_char(p[2]), p[3]])


@_rule('expression : expression EQUALS expression')
def p_expression_equals(p):
    p[0] = mrow([p[1], operator('='), p[3]])


@_rule('expression : expression ADDSUB_OP term')
def p_expression_addsub_op(p):
    p[0] = mrow([p[1], operator(p[2]), p[3]])


@_rule('expression : term')
def p_expression_term(p):
    p[0] = p[1]


@_rule('term : term MULT_OP factor')
def p_term_multiply(p):
    p[0] = mrow([p[1], operator(p[2]), p[3]])


@_rule('term : term DIV_OP factor')
def p_expression_fraction(p):
    p[0] = fraction(p[1], p[3])


@_rule("term : factor")
def p_term_factor(p):
    p[0] = p[1]


@_rule("factor : ADDSUB_OP term")
def p_negative(p):
    p[0] = mrow([operator(p[1]), p[2]])


@_rule("factor : factor POWER factor")
def p_term_power(p):
    p[0] = superscript(p[1], p[3])


@_rule("factor : factor SUBSCRIPT factor")
def p_term_subscript(p):
    p[0] = subscript(p[1], p[3])


@_rule("factor : NUMBER")
def p_factor_num(p):
    p[0] = number(p[1])


@_rule("factor : SYMBOL")
def p_factor_symbol(p):
    p[0] = symbol(p[1])


@_rule("factor : MATHEMATICAL_ID OPEN_PAREN expression CLOSE_PAREN")
def p_factor_func(p):
    if p[1] == 'sqrt':
        p[0] = sqrt(p[3])
    else:
        p[0] = mrow([
            symbol(p[1]),
            operator('('),
            p[3],
            operator(')')
        ])


@_rule('factor : TEXT_FUNC')
def p_expression_textfunc(p):
    p[0] = text(p[1])


@_rule('factor : OPEN_PAREN expression CLOSE_PAREN')
def p_factor_parenthetical(p):
    p[0] = mrow([operator('('), p[2], operator(')')])


@_rule('factor : OPEN_INVIS_PAREN expression CLOSE_INVIS_PAREN')
def p_factor_invis_paren(p):
    p[0] = p[2]


parser = yacc.yacc()
