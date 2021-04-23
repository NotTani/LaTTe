# Block Converter Processor
import abc

class BlockConverter:
    BLOCK_NAME = None

    BLOCK_LEVEL = True
    INLINE = True

    def __init__(self, body, embedded=False, **args):
        self.body = body
        self.embedded = embedded
        self.args = args

    def __str__(self):
        return f"<{self.__class__.__name__} {self.args}>"

    def convertHTML(self, body, embedded=False, **args):
        raise NotImplementedError(
            f"Block {self.__class__.__name__} doesn't have a convertHTML method"
        )
