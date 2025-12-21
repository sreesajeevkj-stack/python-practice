'''
age =  int(input("Enter the age :"))

if age>=18:
    print("You are eligible ")
else :
    print("you are not eligible")

response = str(input("Would you like food (Y/N) :"))
if response == "Y":
    print("YOU CAN HAVE WHAT EVER FOOD YOU LIKE!!!")
elif response == "N":
    print("NOW YOU CAN HAVE SOME DRINKS OR SOME STARTERS")
else :
    print("WRITE SOME SUGGESTIONS TO ADD IN MENU")

ONLINE = True
if ONLINE:
    print("THE USER IS ONLINE")
else:
    print("THE USER IS OFFLINE")
'''