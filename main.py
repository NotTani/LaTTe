from flask import Flask
from latte.extension import LaTTe
from markdown import markdown

with open('input.latte') as f:
    md = f.read()

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
            </div>
        </body>
    </html>
    """


app.run()
