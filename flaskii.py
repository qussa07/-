from flask import Flask, request, render_template
from flask import url_for
from pprint import pprint

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def home(title):
    return render_template('base.html', title=title)


@app.route('/promotion')
def promotion():
    return 'Человечество вырастает из детства.</br>' \
           ' Человечеству мала одна планета.</br>' \
           'Мы сделаем обитаемыми безжизненные пока планеты.</br>' \
           'И начнем с Марса!Присоединяйся!' \
           '<title> Привет, Марс!</title>'


@app.route('/image_mars')
def image():
    return f''' <h1> Жди нас, Марс!</h1>
    <img src="https://images.techinsider.ru/upload/img_cache/982/982fe0d83f1e1f1884869767148de802_ce_1500x1000x62x0.jpg" 
           alt="здесь должна была быть картинка, но не нашлась"> 
           <p> Вот она красная планета!</p>
           <title> Привет, Марс!</title>'''


@app.route('/promotion_image')
def promotion2():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="static/css/style.css">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title> Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="https://images.techinsider.ru/upload/img_cache/982/982fe0d83f1e1f1884869767148de802_ce_1500x1000x62x0.jpg" 
                    alt="здесь должна была быть картинка, но не нашлась"> 
                    <div class="alert alert-primary" role="alert">
                    Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                     Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-info" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-light" role="alert">
                    И начнем с Марса!
                    </div>
                    <div class="alert alert-dark" role="alert">
                    Присоединяйся!
                    </div>  
                    
                  </body>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        checkbox = ''
        prof = [
            ['инженер-исследователь', 'inzhener-issledovatel'], ['пилот', 'pilot'], ['строитель', 'stroitel'],
            ['экзобиолог', 'ekzobiolog'], ['врач', 'vrach'],
            ['инженер по терраформированию', 'inzhener po terraformirovaniyu'],
            ['климатолог', 'klimatolog'], ['специалист по радиационной защите', 'specialist po radiacionnoj zashchite'],
            ['астрогеолог', 'astrogeolog'], ['гляциолог', 'glyaciolog'],
            ['инженер жизнеобеспечения', 'inzhener zhizneobespecheniya'],
            ['метеоролог', 'meteorolog'], ['оператор марсохода', 'operator marsohoda'],
            ['киберинженер', 'kiberinzhener'],
            ['штурман', 'shturman'], ['пилот дронов', 'pilot dronov']
        ]
        for i in prof:
            checkbox += f'''<div class="form-group form-check"> 
                                        <input type="checkbox" class="form-check-input" id="{i[1]}" name="accept">
                                        <label class="form-check-label" for="acceptRules">{i[0]}</label>
                                    </div>'''
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета прендента</h1>
                            <h2> на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <form class="name" method="post">
                                        <input type="email" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <form class="surname" method="post">
                                        <input type="email" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        </br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    
                                    <div class="form-group">
                                        <label for="classSelect">Какое у васи образование ?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии ?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    {checkbox}
                                    </br>
                                    <div class="form-group form-check"> 
                                        
                                        <input type="checkbox" class="form-check-input" id="accept" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли вы остаться на
                                         марсе?
                                        </label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        pprint(dict(request.form))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
