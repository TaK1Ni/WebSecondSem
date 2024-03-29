from flask import Flask, render_template, make_response, request

app = Flask(__name__)

application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/url')
def url():
    return render_template('url.html', title="Параметры URL", )

@app.route('/headers')
def headers():
    return render_template('headers.html', title="Заголовки")

@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html', title="Куки"))
    if 'user' in request.cookies:
        resp.delete_cookie('user')
    else:
        resp.set_cookie('user', 'admin')
    return resp

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    return render_template('forms.html', title="Параметры формы")

@app.route('/calc')
def calc():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    operator = request.args.get('operator')

    OPERATIONS = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    result = OPERATIONS.get(operator, lambda a, b: 0)(a, b)

    return render_template('calc.html', title="Калькулятор", result=result)

@app.route("/phoneNumber", methods=["POST", "GET"])
def phoneNumber():
    if request.method == 'POST':
        phone = request.form["phone"]

        if phone[0] not in ["+", "7", "8"]:
            error = "Недопустимый ввод. Неверный префикс."
            return render_template("phoneNumber.html", title="Проверка номера телефона", phone=error)

        phone_digits = [digit for digit in phone if digit.isdigit()]

        if len(phone_digits) not in [10, 11]:
            error = "Недопустимый ввод. Неверное количество цифр."
            return render_template("phoneNumber.html", title="Проверка номера телефона", phone=error)

        if len(phone_digits) == 10:
            phone_digits.insert(0, "8")

        return render_template("phoneNumber.html", title="Проверка номера телефона", phone="8-{1}{2}{3}-{4}{5}{6}-{7}{8}-{9}{10}".format(*phone_digits))
    else:
        return render_template("phoneNumber.html", title="Проверка номера телефона")