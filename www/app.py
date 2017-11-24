from flask import Flask, request, render_template, abort, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('signin.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('manage.html', username=username)
    else:
        return render_template('signin.html', message='Bad username or password', username=username)


@app.route('/signup', methods=['GET', 'POST'])
def signup_form():
    return render_template('signup.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
