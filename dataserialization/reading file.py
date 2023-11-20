import json

with open ("data.json", "r")as json_file:
    loaddata= json.load(json_file)

print(loaddata)