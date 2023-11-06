# Implement a Flask route that serves JSON data when accessed via a GET request. Write a Python client program that uses the requests module to fetch this JSON data. Parse the JSON response and extract specific information.




from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/data',methods =['get'])
def  get_data():
    data = {'name': 'shivam', 'age': 21, 'city': 'titwala'}
    {'name':'harsh','age':21 ,'city':'vithalwadi'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)