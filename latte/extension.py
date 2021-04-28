from .comments import CommentPreprocessor
from .math import MathInlineProcessor

from markdown import Markdown
from markdown.extensions import Extension


class LaTTe(Extension):
    def __init__(self, lblocks=None):
        super().__init__()

        self.latteBlocks = lblocks

        if self.latteBlocks is None:
            self.latteBlocks = []

    def registerLBlock(self, lblock):
        self.latteBlocks.append(lblock)

    def extendMarkdown(self, md: Markdown) -> None:
        md.preprocessors.register(
            CommentPreprocessor(),
            name="Comment Preprocessor",
            priority=0
        )
        md.inlinePatterns.register(
            MathInlineProcessor(MathInlineProcessor.PATTERN),
            name="Math Inline Processor",
            priority=1
        )
