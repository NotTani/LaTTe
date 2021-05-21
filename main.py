from flask import Flask
from latte.extension import LaTTe
from markdown import markdown

md = """
# This DOES render correctly
; This shouldn't render at all
*right*? {{sqrt(11)}}
"""

out = markdown(
    md,
    extensions=[LaTTe()]
)

app = Flask(__name__)


@app.route('/')
def index():
    return f"""
    <html>
        <head>
            <link rel="stylesheet" href="https://jgthms.com/wysiwyg.css/docs.css">
        </head>
        <body>
            <div class="wysiwyg">
                {out}
                <script type="text/javascript" id="MathJax-script" async
                    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
                </script>
            </div>
        </body>
    </html>
    """


app.run()
