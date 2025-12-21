operator = input("Enter the symbol for operation +,-,*,/ :")
num1 = float(input("ENTER THE FIRST NUMBER FOR OPERATION:"))
num2 = float(input("ENTER THE SECOND NUMBER FOR OPERATION:"))
if operator == '+' :
    result = num1+num2
    print(result)
elif operator == '-':
    result = num1-num2
    print(result)
elif operator == '*':
    result = num1*num2
    print(result)
elif operator == '/':
    result = num1/num2
    print(result)