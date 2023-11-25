#  10. Table Formatting: Format data into a table with columns and rows.




from tabulate import tabulate
data=[
    ["name","age","city"],
    ["alpha",22,"newyork"],
    ['bita',22,"london"],
    ["gama",22,"govandi"]
]

table= tabulate(data,headers="firstrow",tablefmt="grid")

print(table)