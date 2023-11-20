# Write a Python code snippet that serializes a dictionary containing user data (e.g., name, age, email) into a JSON string. Include error handling for potential exceptions during serialization.


import json 
user_data = {
    "name": "shivam",
    "age" : 21,
    "email-id": "shivam2041515@gamil.com"
}



try:
    json_string=json.dumps(user_data)
    print("json_string",json_string)

    with open ("user_data.json","w") as json_file:
        json.dump(user_data,json_file)
except Exception as e:
    print("an unexpected error occurred",e)
    