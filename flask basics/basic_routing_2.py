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


if __name__ == '__main__':
    app.run(debug = True)