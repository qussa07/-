from flask import Flask, request, render_template, redirect
from flask import url_for
from pprint import pprint

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('пароль астронавта', validators=[DataRequired()])
    id_kap = StringField('id капитана', validators=[DataRequired()])
    password_kap = PasswordField('пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')



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

@app.route('/armor', methods=['GET', 'POST'])
def armor():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('armor.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return render_template('success.html')




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
