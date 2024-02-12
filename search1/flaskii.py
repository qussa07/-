from flask import Flask, request, render_template
from flask import url_for
from pprint import pprint

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def home(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<flag>')
def abc(flag):
    nng = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
           'инженер по терраформированию', 'климатолог',
           'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
           'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
           'штурман', 'пилот дронов']
    return render_template('proof.html', prof=flag, proflist=nng)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    anketa = {'title': 'Firsov',
              'surname': 'Mask',
              'name': 'Ilon',
              'education': 'higher',
              'profession': 'billionaire',
              'sex': 'man',
              'motivation': 'Mars',
              'ready': 'yes'
              }
    return render_template('auto_answer.html', **anketa)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
