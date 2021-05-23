from flask import Flask, render_template, request, Markup
from latte.mathConvert.mathml import LaTTeMathML

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tryit', methods=['GET', 'POST'])
def try_it():
    if request.method == "GET":
        return render_template("tryit_form.html")
    elif request.method == "POST":
        try:
            out = str(LaTTeMathML.from_string(request.form['latteinput']))
        except Exception as e:
            return f"An error occured: {e}", 500

        return render_template('output.html', out=Markup(out))

    return "Guess who found the secret message! No, wait, it's you. I was talking about you. You found the secret " \
           "message. You don't need to guess."


if __name__ == "__main__":
    app.run()
