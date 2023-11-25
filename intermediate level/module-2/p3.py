# deserialize (read) the JSON data from the file



import json

file_path = ('B:\python learning\Intermediate-module2\output.json')

try:
    with open(file_path, 'r') as file:

        json_data = json.load(file)

        print(json_data)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON from the file '{file_path}': {e}")
except Exception as e:
    print(f"An error occurred: {e}")
