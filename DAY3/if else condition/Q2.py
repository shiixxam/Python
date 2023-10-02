# 5.	Temperature Classifier: Request a temperature value from the user. Classify it as "hot" if it's above 30°C, "moderate" if between 20°C and 30°C, and "cold" if below 20°C using if-else statements. Print the classification

temperature=float(input("enter the Temprature"))
if temperature > 30:
    print("Temperture is hot")
elif temperature >=20:
    print("Temperature is moderate")
else:
    print("temperature is cold")
