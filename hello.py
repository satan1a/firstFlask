from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/usr/<name>')
def user(name):
    return "<h1>Hello,{0}!</h1>".format(name)
    # return '<h1>Hello, %s!</h1>' % name


@app.route('/test/bad')
def bad():
    return "Bad Request", 400


# @app.route('/test/redirect')
# def redirect():
#     return redirect("http://www.thereroad.com"), 302
# TODO


if __name__ == '__main__':
    app.run(debug=True)
