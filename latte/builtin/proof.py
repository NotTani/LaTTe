from base.block import Block

class ProofBlock(Block):
    symbols = {
        'for all': '',
        'and': '',
        'implies': '',
        ('xor', 'exclusive or'): '',
        'alpha': 'alpha',
        'beta': 'beta',
        'gamma': 'gamma'
    }
    def html(self, body: str, embedded=False, **args):
