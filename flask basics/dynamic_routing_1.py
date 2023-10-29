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


# DYNAMIC ROUTING


@app.route('/Users/<name>')
def users(name):
    x = "welcome {}"
    y = x.format(name)
    return y


if __name__ == '__main__':
    app.run(debug = True)