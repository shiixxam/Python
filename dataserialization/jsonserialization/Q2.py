# Develop a Python program that deserializes a JSON string representing a list of products (each with name, price, and quantity) into a Python list of dictionaries. Calculate the total cost of the products and display the result.


import json

json_data = '[{"name": "Laptop", "price": 1200, "quantity": 2}, {"name": "Phone", "price": 800, "quantity": 1}, {"name": "Tablet", "price": 500, "quantity": 3}]'

products = json.loads(json_data)

total_cost = 0
for product in products:
    total_cost += product['price'] * product['quantity']

print("Total cost:", total_cost)
