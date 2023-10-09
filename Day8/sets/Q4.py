# 4. Set Difference: Find and print the items that are in the fruits set but not in the vegetables set.


fruits = {"apple", "banana", "orange", "grape", "kiwi","carrot"}

vegetables = {"carrot", "tomato", "cucumber","orange"}


difference=vegetables.difference(fruits)
difference1=fruits.difference(vegetables)

print("Items in vegetable but not in fruits:", difference)


print("Items in vegetables but not in fruits:", difference1)
