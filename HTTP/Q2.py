#  Develop a Python program that utilizes the requests module to simulate form submissions. Send a POST request to a sample form endpoint, including form data. Validate the success of the submission by examining the response status code.



import requests

form_url = "https://google.com/submit-form"

form_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "This is a test message for the form submission."
}

response = requests.post(form_url, data=form_data)

if response.status_code == 200:
    print("Form submission was successful.")
else:
    print(f"Form submission failed. Status code: {response.status_code}")

