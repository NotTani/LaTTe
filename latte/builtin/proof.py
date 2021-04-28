from base.blockconverter import BlockConverter

class ProofBlock(BlockConverter):
    symbols = {
        'for all': '',
        'and': '',
        'implies': '',
        ('xor', 'exclusive or'): '',
        'alpha': 'alpha',
        'beta': 'beta',
        'gamma': 'gamma'
    }
    def convertHTML(self, body: str, embedded=False, **args):
