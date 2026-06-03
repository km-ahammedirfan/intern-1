a = int(input("enter the first number:"))
b = int(input("enter the second number:"))

print("\tMENU \n ------------")

def addition(a,b):
    result = a+b
    print("sum is :",result)

def substraction(a,b):
    result = a-b
    print("difference is :",result)


def multiplication(a,b):
    result = a*b
    print("product is :",result)

def division(a,b):
    result = a/b
    print("dividend is :",result)


print("1.addition \n 2.substraction \n 3.multiplication \n 4.division")
ch= int(input("enter the choice:"))
if ch==1:
    addition(a,b)

elif ch==2:
    substraction(a,b)

elif ch==3:
    multiplication(a,b)

elif ch==4:
    division(a,b)

else:
    print("invalid choice")