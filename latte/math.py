import xml.etree.ElementTree as ETree
from markdown.inlinepatterns import InlineProcessor


class MathInlineProcessor(InlineProcessor):
    PATTERN = r"{{(..*)}}"

    def handleMatch(self, m, data):
        el = ETree.Element('div')
        el.text = f'Math: {m.group(1)}'
        return el, m.start(0), m.end(0)
