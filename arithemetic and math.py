"""
car =4

car=car+1
car+=1   (add)
car=car-1
car-=1    (sub)
car=car*1
car*=1   (mul)
car=car/1
car/=1   (div)
car =car**1
car**=1  (power)

x=1.34
y=4
z=5


result = round(x)   (used in round of the number)
result = min(x,y,z) (used to find the minimum value amoung the number)
result =max(x,y,z)  (used to find the m,aximum value amoung the number)
result = abs(x)     (used in finding the absolute value if the integer is negative it will turn it into positive)
result = pow(4,3)   (used in assigning the value for power)

print(result)
"""
'''
#MATH
#import math #(helps in importiong the math variables and values)

#x=9

#print(math.pi) [value of pi]
#print(math.e)  [value of exponent]
#result = math.sqrt(x) [square root value]
#result =math.ceil(x)  [used in round off to higher value]
#result =math.floor(x)  [used in round off to lower value]


#print(result)

#import math

#radius = float(input("Enter the radius of the circle: "))

#circumference = 2*math.pi*radius
#print(f"The circumference is : {circumference}")



import math

radius = float(input ("Enter the radius of the circle:"))

area = math.pi * pow(radius,2)
print(f"the area of the circle is :{round(area)}")


import math
a = float(input("Enter the number a:"))
b = float (input("Enter the number b:"))

c = math.sqrt(pow(a,2)+pow(b,2))
print (f"The hypotheneuse of the triangle SIDE A AND B {c}")

'''
