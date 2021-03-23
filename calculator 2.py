# DISCLAIMER: COPYRIGHT CODE OF SAMARTH TALAWAR...  

print("hello!!! Welcome to Calculator")
print("enter 'sum' for addtion")
print("enter 'dif' for subtraction")
print("enter 'pro' for multiplication")
print("enter 'div' for division")
codes = {"sum":f"{int(1)}", "dif":f"{int(2)}", "pro":f"{int(3)}", "div":f"{int(4)}"}

j = input("which arithmetic function do you want to run?      ")
i = int(codes[f"{j}"])
i1 = int(input("alright, enter your first number     "))
i2 = int(input("enter your second number     "))

def sum(x, y):
    return x+y
def dif(x,y):
    return x-y
def pro(x,y ):
    return x*y
def div(x, y):
    return x/y
if i < 2:
    print(f"the sum of {i1} and {i2} is {sum(i1, i2)}")
if 1<i<3:
    print(f"the difference between {i1} and {i2} is {dif(i1, i2)}")
if 2<i<4:
    print(f"the product of {i1} and {i2} is {pro(i1, i2)}")
if i>3:
    print(f"the division of {i1} and {i2} gives {div(i1, i2)}")
