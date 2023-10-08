# 7.	Tuple Immutability: Attempt to change the name of a month in the tuple. Observe and explain the error that occurs.


x=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
x[2]='Mar'
print(x)


# """ERROR!
# Traceback (most recent call last):
#   File "<string>", line 4, in <module>
# TypeError: 'tuple' object does not support item assignment
# > """