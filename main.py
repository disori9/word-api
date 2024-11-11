from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
word_df = pd.read_csv('data/dictionary.csv')
# The reason why I put word_df outside the function scope is because we do not need to change the df each time a url
# is called, since all the words is in one csv file. That is the main difference with the weather-api that I just built.
# While it would still work if I put it inside api, it will create unnecessary issues that may overwhelm the system,
# whereas in weather-api, the data file
# We need to access is dynamic, meaning each station's data file is different from one another, thus we need to put
# it inside the function call to dynamically change the df based on the station inputted by the user

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def api(word):
    word_definition = word_df.loc[word_df['word'] == word]['definition'].squeeze()
    word_dict = {"definition": word_definition,
            "word": word}
    return word_dict


if __name__ == "__main__":
    app.run(debug=True)