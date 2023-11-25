# 3.	Arbitrary Arguments: Define a function that accepts an arbitrary number of arguments and prints them.


def argument(*args):
    for arg in args:
        print(arg)
argument(1,2,3,True,"hellllllllllllllloooo")
