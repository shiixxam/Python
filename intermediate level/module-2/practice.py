import requests
import json 

import requests

url = 'https://timesofindia.indiatimes.com/'


try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Request was successful")
        print(response.text)
    else:
        print(f"Error: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error making the request: {e}")




