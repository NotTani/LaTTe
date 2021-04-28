from flask import Flask
from latte.extension import LaTTe
from markdown import markdown

md = """
# This should render correctly
; This shouldn't render at all
*right*? {{math}}
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
            <!-- <link rel="stylesheet" href="https://jgthms.com/wysiwyg.css/docs.css"> -->
        </head>
        <body>
            {out}
            <math>
                <mstyle>
                    <mrow>
                      <mi>a</mi> <mo>&InvisibleTimes;</mo> <msup><mi>x</mi><mn>2</mn></msup>
                      <mo>+</mo><mi>b</mi><mo>&InvisibleTimes;</mo><mi>x</mi>
                      <mo>+</mo><mi>c</mi>
                    </mrow> 
                </mstyle>
            </math>
            <script type="text/javascript" id="MathJax-script" async
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
            </script>
        </body>
    </html>
    """


app.run()
