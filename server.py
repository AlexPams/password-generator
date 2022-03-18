from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import passwordgenerator

app = Flask("app")


@app.route('/', )
def index():
    return render_template('index.html')


@app.route('/password', methods=['POST', 'GET'])
def password():
    if request.method == 'POST' and (request.form['password_length'] != ' ' and request.form['banned_symbols'] != ' '):
        return passwordgenerator.generate(int(request.form['password_length']), request.form['banned_symbols'])
    else:
        return "Error"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
