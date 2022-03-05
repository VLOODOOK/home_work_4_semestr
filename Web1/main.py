from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def homepage():
    return render_template('homepage.html', title='Домашняя страница')


@app.route('/distribution')
def distribution():
    astronauts = ['Риддли Скотт', 'Бла Бла', 'Тук Тук', 'Боб А', 'А Боб', 'Тик Так']
    return render_template('distribution.html', astronauts=astronauts, len=len(astronauts))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
