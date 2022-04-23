from flask import Flask, render_template, request
import os


app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def homepage():
    return render_template('homepage.html', title='Домашняя страница')


@app.route('/distribution')
def distribution():
    astronauts = ['Риддли Скотт', 'Бла Бла', 'Тук Тук', 'Боб А', 'А Боб', 'Тик Так']
    return render_template('distribution.html', astronauts=astronauts, len=len(astronauts))


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        dirname = r'Web5\static\img'
        files = os.listdir(dirname)
        return render_template('carousel.html', title='carousel', files=files)
    elif request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(r'Web5\static\img', f.filename))
        return "Файл отправлен, зайдите вновь на страницу"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
