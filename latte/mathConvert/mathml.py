# mathml.py - converts a LaTTe Math AST into MathML Markup
from abc import ABC
from xml.etree.ElementTree import Element, tostring
from base.block import Block
from mathConvert.mathml_elements import (
    create_element,
    number,
    symbol,
    operator,
    fraction,
    text,
    sqrt,
    superscript,
    special_char,
    subscript
)


class InvalidLaTTeMath(Exception):
    pass


class MathProcessor(Block, ABC):
    BLOCK_NAME = "math"

    def convertToHTML(self, args, body):
        ml = self._convertToMathML(body)
        if args.get('display', None):
            ml.set('display', 'inline')
        return ml

    @staticmethod
    def _convertToMathML(body, **args):
        ml = LaTTeMathML(**args)
        ml.addBody(body)
        return ml.tree


class LaTTeMathML:
    MATHML_NS = "http://www.w3.org/1998/Math/MathML"
    MROW_GROUPS = [
        'msup',
        'msub',
        'munderover',
        'munder',
        'mover',
        'mroot',
        'msqrt',
        'mfrac'
    ]

    def __init__(self, inline=True, mstyle=None, mathml_ns=MATHML_NS):

        self._parts = None
        if mstyle is None:
            mstyle = {}

        self.tree = Element('math')

        if inline:
            self.tree.set('display', 'inline')
        else:
            self.tree.set('display', 'block')

        if mstyle:
            mstyle = Element('mstyle', **mstyle)
            self._add_el(mstyle)

        self.tree.set('xmlns', mathml_ns)

    def __str__(self):
        return tostring(self.tree).decode()

    def _add_el(self, el):
        self.tree.append(el)

    def addBody(self, body):
        print(type(body))
        self.tree.append(body)
        print(self)
