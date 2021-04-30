# mathml.py - converts a LaTTe Math AST into MathML Markup
from xml.etree.ElementTree import Element, tostring
from base.blockconverter import BlockConverter


class InvalidLaTTeMath(Exception):
    pass


def create_element(tag, text=None, attributes=None, children=()):
    """
    A one-liner to create an eTree element
    """
    if attributes is None:
        attributes = {}
    element = Element(tag, **attributes)
    element.text = text or ""

    for child in children:
        element.append(child)

    return element


def mrow(element):
    if element.tag == 'mrow':
        return element

    el = create_element('mrow')
    el.append(element)
    return el


class MathProcessor(BlockConverter):
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

        if mstyle is None:
            mstyle = {}

        self.tree = Element('math')
        self._current_el = [self.tree]

        if inline:
            self.tree.set('display', 'inline')
        else:
            self.tree.set('display', 'block')

        if mstyle:
            mstyle = Element('mstyle', **mstyle)
            self._add_el(mstyle)

        self.mrow_all = False

        self._current_el_needs = -1

        self.tree.set('xmlns', mathml_ns)

    def __str__(self):
        return tostring(self.tree)

    def _add_el(self, el):
        if self._current_el[-1].tag == self.MROW_GROUPS:
            el = mrow(el)
        if self._current_el_needs >= 0:
            if self._current_el_needs == 0:
                self._current_el.pop()
            self._current_el_needs -= 1
        self._current_el.append(el)

    def _set_append_el(self, el, consume):
        self.tree.append(el)
        self._current_el.append(el)
        self._current_el_needs = consume

    def _get_parent(self, child, tree=None):
        # because etree doesn't have a _get_parent element for some godshdang reason
        if not tree:
            tree = self.tree

        parent_map = {c: p for p in tree.iter() for c in p}
        return parent_map.get(child)

    def _add_number_el(self, number):
        """
        number: number to add

        Adds an <mn> element to the tree
        """
        self._add_el(create_element('mn', str(number)))

    def _add_text_to_current_el(self, text):
        """
        text: text to add

        Add text to the currently active element
        """
        current_text = self._current_el[-1].text
        if not current_text:
            self._current_el[-1].text = ""

        self._current_el[-1].text += text

    def _add_text_el(self, text=None):
        """
        text: text to add or None

        Adds a new <mtext> element to the tree
        """
        el = create_element('mtext')
        if text:
            el.text = text
        self._add_el(el)

    def _start_fraction(self):
        self._current_el.append(
            create_element('mfrac')
        )

    def _add_subscript(self, base, subscript):
        self._consume(2)
        self._add_el(mrow(
            create_element('msub', children=(
                mrow(base),
                mrow(subscript)
            ))
        ))

    def _add_superscript(self, base, superscript):
        self._consume(2)
        self._add_el(mrow(
            create_element('msup', children=(
                mrow(base),
                mrow(superscript)
            ))
        ))

    def _add_symbol(self, text):
        self._add_el(create_element('mo', '&{};'.format(text)))

    def addBody(self, body):
        """
        A filler method because parser isn't done
        """
        self._start_fraction()
        self._add_number_el(2)
        self._add_number_el(3)
