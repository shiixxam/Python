# 8.	List Processing: Write a function that processes a list and returns a modified version of the list.


def list1(input_list):
    modified_list = [ x ** 2 for x in input_list]
    return modified_list

my_list=[1,2,3,4,5]
result=list1(my_list)
print(result)