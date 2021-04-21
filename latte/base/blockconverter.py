# Block Converter Processor
import abc


class BlockConverter(abc.ABC):
    BLOCK_NAME = None

    def convertEmbeddedHTML(self, parameters, body):
