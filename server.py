from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import flash
from flask import get_flashed_messages
import passwordgenerator

app = Flask("app")
app.config['SECRET_KEY'] = "xOPd3OP4CHv)|^.UwEl2+GBSNglj~"


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST' and (request.form['password_length'] != ' ' and request.form['banned_symbols'] != ' '):
        flash(passwordgenerator.generate(int(request.form['password_length']), request.form['banned_symbols']))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
