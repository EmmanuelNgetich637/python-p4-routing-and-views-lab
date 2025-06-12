#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f"{param}"

@app.route('/count/<int:param>')
def count(param):
    return '\n'.join([str(i) for i in range(param)]) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation in ['add', '+']:
        result = num1 + num2
    elif operation in ['subtract', 'sub', '-']:
        result = num1 - num2
    elif operation in ['multiply', 'mult', '*']:
        result = num1 * num2
    elif operation in ['divide', 'div', '/']:
        result = num1 / num2
    elif operation in ['modulo', 'mod', '%']:
        result = num1 % num2
    else:
        return 'Invalid operation'

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
