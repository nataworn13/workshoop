x = "Awesome"


def myFunc():
    global x
    # print (x = Awesome)
    print("Python is " + x)
    # print (x = Fantastic)
    x = "Fantastic"


myFunc()
print("Python is " + x)