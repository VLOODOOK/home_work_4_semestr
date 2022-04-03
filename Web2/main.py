from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def homepage():
    return render_template('homepage.html', title='Домашняя страница')


@app.route('/table/<string:gender>/<int:number>')
def table(gender, number):
    if gender == 'male' and number >= 25:
        return render_template("table.html",
                               color='blue',
                               image=url_for('static', filename='gramozeka.jpg'),
                               title='table')
    if gender == 'male' and number < 25:
        return render_template("table.html",
                               color='orange',
                               image=url_for('static', filename='popugai.jpg'),
                               title='table')
    if gender == 'female' and number >= 25:
        return render_template("table.html",
                               color='red',
                               image=url_for('static', filename='gramozeka.jpg'),
                               title='table')
    if gender == 'female' and number < 25:
        return render_template("table.html",
                               color='pink',
                               image=url_for('static', filename='popugai.jpg'),
                               title='table')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
