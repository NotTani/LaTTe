from .mathConvert.mathml import LaTTeMathML
from .mathConvert.lexer import tokenize
from .mathConvert.parser import parser
from markdown.inlinepatterns import InlineProcessor


class MathInlineProcessor(InlineProcessor):
    PATTERN = r"{{(?P<inner>..*)}}"

    def handleMatch(self, m, data):
        lml = LaTTeMathML(inline=False)
        lml.addBody(parser.parse(m.group('inner')))
        return lml.tree, m.start(0), m.end(0)
