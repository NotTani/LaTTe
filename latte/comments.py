from markdown.preprocessors import Preprocessor
import re


class CommentPreprocessor(Preprocessor):
    """ Ignores comment lines """
    def run(self, lines):
        nl = []
        for line in lines:
            if not re.search('^;', line):
                nl.append(line)
        return nl
