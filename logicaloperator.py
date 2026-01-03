'''
temp = 24
is_raining = True

if temp > 30 or temp < 0 or is_raining :
    print("outdoor event is cancelled")
else:
    print("the weather is looking good the outdoor event will be held")


temp = 28
is_sunny = True

if temp <30 and is_sunny :
    print("its hot outside")
    print("its sunny")
elif temp <24 and temp >0 and is_sunny :
    print("its warm outside")
    print ("its sunny")

temp = 28
is_sunny = False

if temp <30 and not is_sunny :
    print("its hot ")
    print("its sunny")

'''