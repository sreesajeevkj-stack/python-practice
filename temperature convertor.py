unit = input("Enter the temperature wheather in celcius [C]or fahrenhiet [F] :")
temperature = float(input("Enter the temperature:"))

if unit == "C" :
    temperature = round((temperature * 9)/5 + 32 ,2)
    unit = "farenhiet"
    print(f"The converted temperature is {temperature} {unit}")
elif unit == "F" :
    temperature = round((temperature -32)* 5/9 ,2)
    unit = "celcius"
    print(f"The converted temperature is {temperature} {unit}")
else:
    print(f"The Entered {unit} of temperature is invalid")
