# Question 1: Create a Flask web application with a route that displays a simple HTML page. Include a route for handling form submissions via POST requests. Demonstrate the interaction between the client and server for both routes.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('formlogin.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Hello {name}, your email is {email}!"

if __name__ == '__main__':
    app.run(debug=True)
