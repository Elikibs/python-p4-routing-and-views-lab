#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# running the app as a python script
if __name__ == '__main__':
    app.run(port=5555, debug=True)

# index base route and view
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'Get ready to explore more {parameter}')
    return f'Get ready to explore more {parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for i in range(parameter):
        result += str(i) + '<br>'
    return result

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation"
    return f'{num1} {operation} {num2} = {result}'
