# mathml.py - converts a LaTTe Math AST into MathML Markup
import xml.etree.ElementTree as eTree
from base.blockconverter import BlockConverter


class InvalidLaTTeMath(Exception):
    pass


def create_element(tag, text=None, attributes=None, children=()):
    """
    A one-liner to create an eTree element
    """
    if attributes is None:
        attributes = {}
    element = eTree.Element(tag, **attributes)
    element.text = text or ""

    for child in children:
        element.append(child)

    return element


class MathProcessor(BlockConverter):
    def convertToHTML(self, args, body):
        ml = self._convertToMathML(body)
        if args.get('display', None):
            ml.set('display', 'inline')
        return ml

    @staticmethod
    def _convertToMathML(body, **args):
        ml = AsciiMathML(**args)
        ml.addBody(body)
        return ml.tree


class AsciiMathML:
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

    def __init__(self, mstyle=None, mathml_ns=MATHML_NS):

        if mstyle is None: mstyle = {}

        self.tree = eTree.Element('math')
        self._current_el = self.tree

        mstyle = eTree.Element('mstyle', **mstyle)
        self.tree.append(mstyle)

        self.tree.set('xmlns', mathml_ns)

    def __str__(self):
        return str(self.tree)

    def _add_el(self, el):
        self._current_el.append(el)

    def _get_parent(self, child, tree=None):
        # because etree doesn't have a _get_parent element
        if not tree:
            tree = self.tree

        parent_map = {c: p for p in tree.iter() for c in p}
        return parent_map.get(child)

    def _add_number_el(self, number):
        """
        number: number to add

        Adds an <mn> element to the tree
        """
        if number < 0:
            self._add_negative_number(number)
        else:
            self._add_el(create_element('mn', str(number)))

    def _add_negative_number(self, number):
        """
        number: negative number to add

        Adds a negative number to the tree
        """
        if self._current_el.tag in self.MROW_GROUPS:
            # ** because class is a reserved word
            el = create_element('mrow', **{'class': 'neg-num'})
            append_el =



    def _add_text_to_current_el(self, text):
        """
        text: text to add

        Add text to the currently active element
        """
        current_text = self._current_el.text
        if not current_text:
            self._current_el.text = ""

        self._current_el.text += text

    def _add_text_el(self, text=None):
        """
        text: text to add or None

        Adds a new <mtext> element to the
        """
        el = create_element('mtext')
        if text:
            el.text = text
        self._add_el(el)
