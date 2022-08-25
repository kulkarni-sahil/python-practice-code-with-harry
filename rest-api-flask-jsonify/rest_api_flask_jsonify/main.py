from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum_check = 0
    order = len(str(n))
    copy_of_n = n

    digit_raised_to_order = []

    response = {
        'Number': n,
        'Armstrong': None,
        'DigitRaisedToOrder': digit_raised_to_order
    }

    while n > 0:
        digit = n % 10
        digit_order = digit ** order
        sum_check += digit_order
        digit_raised_to_order.append(digit_order)
        n = n // 10

    if copy_of_n == sum_check:
        response['Armstrong'] = True
    else:
        response['Armstrong'] = False

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

