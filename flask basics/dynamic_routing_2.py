from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/Home')
def index():
    return "Hi"


@app.route('/Details')
def about():
    return "Bye"


@app.route('/Connect_us')
def contact():
    return "Tata"


# DBUGGING


@app.route('/Users/<address>')
def mobile(address):
    x = "welcome {}"
    y = x.format(address[50])
    return y


if __name__ == '__main__':
    app.run(debug = True)