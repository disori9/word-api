from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def api(word):
    word = word
    word_definition = ""
    word_dict = {"definition": word.upper(),
            "word": word}
    return word_dict


if __name__ == "__main__":
    app.run(debug=True)