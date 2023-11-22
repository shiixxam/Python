import requests
import json



url = 'https://www.sscoe.edu.in/'

try:
    response = requests.get(url)
    response.raise_for_status   # if we use this we don't ned to use that if response.status_code == 200: then print response.raise_for_status is like exception handling 
    if response.status_code == 200:
        print("Request was successful!")

        # Writing the content to a JSON file
        with open("output.json", "w") as json_file:
            json_file.write(response.text)

        print("Content saved as JSON in 'output.json'")
    else:
        print(f"Unexpected status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error making the request: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")