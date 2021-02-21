from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index2():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def index3():
    text_list = ['Человечество вырастает из детства.',
                 'Человечеству мала одна планета.',
                 'Мы сделаем обитаемыми безжизненные пока планеты.',
                 'И начнем с Марса!',
                 'Присоединяйся!']
    txt = ''
    for i in text_list:
        txt += f'<p>{i}</p>'
    return txt


@app.route('/image_mars')
def index4():
    return f'''
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.jpg')}" 
               alt="здесь должна была быть картинка, но не нашлась">
<p>Вот она какая, красная планета.</p>'''


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                    Человечество вырастает из детства.</br>
                    </div>
                    <div class="alert alert-warning" role="alert">
                    Человечеству мала одна планета.</br>
                    </div>
                    <div class="alert alert-success" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты.</br>
                    </div>
                    <div class="alert alert-dark" role="alert">
                    И начнем с Марса!</br>
                    </div>
                    <div class="alert alert-danger" role="alert">
                    Присоединяйся!</br>
                    </div>
                  </body>
                </html>'''


@app.route('/choice/<planet_name>')
def planet(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение - {planet_name}!</h1>
                    <div class="alert alert-danger" role="alert">
                    <h2>Эта планета близка к Земле;</br></h2>
                    </div>
                    <div class="alert alert-primary" role="alert">
                    <h2>На ней много необходимых ресурсов;</h2></br>
                    </div>
                    <div class="alert alert-warning" role="alert">
                    <h2>На ней есть вода и атмосфера;</h2></br>
                    </div>
                    <div class="alert alert-success" role="alert">
                    <h2>На ней есть небольшое магнитное поле;</h2></br>
                    </div>
                    <div class="alert alert-dark" role="alert">
                    <h2>Наконец, она просто красива!</h2></br>
                    </div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                    <h2>Ваш рейтинг после {level} этапа отбора</br></h2>
                    </div>
                    <h2>составляет {rating}!</h2>
                    <div class="alert alert-warning" role="alert">
                    <h2>Желаем удачи!</h2></br>
                    </div>
                  </body>
                </html>'''


@app.route('/selection', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                 'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
                 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
                 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
        prof_form = ''
        for i in profs:
            prof_form += f'''<div class="form-check">
                <input class="form-check-input" type="checkBox" name="prof" id="{i}" value="{i}">
                <label class="form-check-label" for="{i}">
                  {i}
                </label>
                </div>'''
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                          <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                          <h1><p align="center">Анкета претендента</p></h1>
                            <h2><p align="center">на участие в миссии</p></h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input name="surname" type="text" class="form-control" placeholder="Введите фамилию"/>
                                    <input name="name" type="text" class="form-control" placeholder="Введите имя"/>
                                    </br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </br>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select>
                                          <option>Дошкольное</option>
                                          <option>Начальное общее</option>
                                          <option>Основное общее</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="classSelect">Какие у вас есть профессии?</label>
                                        {prof_form}
                                    </div>
                                    </br>
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
                                    </br>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    </br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['prof'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
