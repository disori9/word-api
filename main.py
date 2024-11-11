from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def api(word):
    word_df = pd.read_csv('data/dictionary.csv')
    word_definition = word_df.loc[word_df['word'] == word]['definition'].squeeze()
    word_dict = {"definition": word_definition,
            "word": word}
    return word_dict


if __name__ == "__main__":
    app.run(debug=True)