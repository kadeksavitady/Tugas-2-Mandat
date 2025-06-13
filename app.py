from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        words = text.lower().split()
        word_count = Counter(words)
        result = word_count.most_common(5)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
