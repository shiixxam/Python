# 4.	Multiple Custom Exceptions: Define and raise multiple custom exceptions in your code, handling them separately.

class valuetohigh(Exception):
    pass
class valuetolow(Exception):
    pass

def limit(temperature):
    try:    
        if temperature<0:
            raise valuetolow("temperature is very low :")
        elif temperature >50:
            raise valuetolow("temperature is to high :")
        else:
            print("temprature limit set to ",temperature,"°C")

    except valuetolow as e1:
        print("Custom Exception - ValueTooLowError:", e1)
    except valuetohigh as e2:
        print("Custom Exception - ValueTooHighError:", e2)

try:
    temperture_limit=int(input("enter the tempeurate :"))
except ValueError:
    print("invalid input .please enter the valid inetegr")
else:
    limit(temperture_limit)
