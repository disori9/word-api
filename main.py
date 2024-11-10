from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<word>')
def definition(word):
    word = word
    word_definition = ""
    return {"definition": word_definition,
            "word": word}
if __name__ == "__main__":
    app.run(debug=True)