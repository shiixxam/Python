from flask import Flask , url_for,redirect

app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to xresearch"


@app.route('/employee')
def employee():
    return "sir promotion kab milega"


@app.route('/boss')
def boss():
    return "hello employee kaam kro promotion jldi milega"

@app.route('/user/<name>')
def user(name):
    if name == 'employee':
        return redirect(url_for('employee'))
    if name == 'boss':
        return redirect(url_for('boss'))


app.run(debug=True)