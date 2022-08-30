from flask import (
    Flask,
    request,
)

from calculator import Calculator

app = Flask(__name__)


@app.route('/api/add', methods=['POST'])
def add():
    return operation('add')


@app.route('/api/subtract', methods=['POST'])
def subtract():
    return operation('subtract')


@app.route('/api/multiply', methods=['POST'])
def multiply():
    return operation('multiply')


@app.route('/api/divide', methods=['POST'])
def divide():
    return operation('divide')

@app.route('/api/square', methods=['POST'])
def square():
    return request.json.get('x') ** 2

@app.route('/api/cube', methods=['POST'])
def square():
    return request.json.get('x') ** 3


def operation(method):
    factors = []
    factors.append(float(request.json.get('x')))
    factors.append(float(request.json.get('y')))
    obj = Calculator()
    result = getattr(obj, method)(*factors)

    return str(result)


app.run(host='0.0.0.0', port=8080)
