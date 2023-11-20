import json

data = {
    'name':'shivam',
    "age": 30,
    "is_student": False,
    "hobbies": ["reading", "programming"]
}


json_data=json.dumps(data)
# print(json_data)


obj= json.loads(json_data)
print(obj)

# with open ("data.json" , "w")as json_file:
#     json.dump(data,json_file)


