from latte.core import Parser
from latte.extend import InlineBlock


class XkcdBlock(InlineBlock):
    name = "xkcd"
    re = r"%xkcd (.*)%"

    def html(self) -> str:
        return f"""
        <img src="https://xkcd.com/comics/{self.match.group(0)}.png">
        """


parser = Parser()
parser.register_block(XkcdBlock)

with open("README.md") as f:
    html = parser.parse(
        f.readlines(),
        embedded=True
    )
