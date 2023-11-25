# 5.	Mixed Arguments: Define a function with a mix of positional and keyword arguments and call it



def fun(name,age,company="xresearch"):# company name is defalut mixed value. 
    return f"My name is {name},i am {age} years's old and I work in {company}."
    
x=fun(name="shivam",age=22)
print(x)

y=fun("kiran",2222222222222222222)
print(y)



