#  Write a Python code snippet using the requests module to send a GET request to a public API (e.g., JSONPlaceholder) and display the response content. Explain the structure of the response object.

# import requests

# r = requests.get("https://timesofindia.indiatimes.com/?from=mdr")

# print(r.text)
# print(r.status_code)


import requests
import json

url = "https://timesofindia.indiatimes.com/?from=mdr"

r = requests.get(url)

if r.status_code == 200:
    # Assuming you want to save the content of the response as JSON
    data = {
        "url": url,
        "content": r.text
    }
    
    # Specify the filename for your JSON file
    json_filename = "times_of_india_data.json"
    
    # Save the data to the JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)
    
    print(f"Data saved to {json_filename}")
else:
    print(f"Failed to retrieve data. Status code: {r.status_code}")

