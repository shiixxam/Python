# 10.	Print Even Indices: Use the range() function to iterate over a list and print elements at even indices.



my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for index in range(0, len(my_list), 2):
    print(my_list[index])




days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
for x in range(0, len(days), 2):
    print(days[x])
