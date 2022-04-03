import json

from flask import Flask, render_template
from random import randint


app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def homepage():
    return render_template('homepage.html', title='Домашняя страница')


@app.route('/member')
def member():
    with open('templates/member.json', 'r', encoding='utf') as f:
        data = json.loads(f.read())
        data = data['member'][randint(0, 3)]
    return render_template('member.html', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
