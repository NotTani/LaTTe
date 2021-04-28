from .mathConvert.mathml import LaTTeMathML
from markdown.inlinepatterns import InlineProcessor


class MathInlineProcessor(InlineProcessor):
    PATTERN = r"{{(?P<inner>..*)}}"

    def handleMatch(self, m, data):
        lml = LaTTeMathML(inline=True)
        lml.addBody(m.group('inner'))
        return lml.tree, m.start(0), m.end(0)
