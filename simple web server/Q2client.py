import requests 
import json 



url = 'http://localhost:5000/data'

response =requests.get('http://localhost:5000/data')

if response.status_code == 200:
    data = json.loads(response.text)
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"city: {data['city']}")
else:
    print(f"failed to got data,status code :{response.status_code}")