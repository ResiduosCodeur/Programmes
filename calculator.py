#DISLAIMER: Copyright code Samarth Talawar, All rights reserved

print("Welcome to the calculator!!")
print("enter 'sum' for addition      ")
print("enter 'dif' for subtraction    ")
print("enter 'pro' for multiplication ")
print("enter 'div' for division")
n = input("")
n1 = int(input("enter the first number         "))
n2 = int(input("enter the next one             "))
dictionary = {"pro":"3", "sum": "1", "dif":"2", "div":"4"}
i = int(dictionary[f"{n}"])


def sum(x, y):
	return x+y

def dif(x, y):
	return x-y

def pro(x, y):
	return x*y

def div(x, y):
	return x/y


if 0<i<2:
	print(f"sum of {n1} and {n2} is {sum(n1, n2)}")

if 1<i<3:
	print(f"difference between {n1} and {n2} is {dif(n1, n2)}")

if 2<i<4:
	print(f"product of {n1} and {n2} is {pro(n1, n2)}")

if 3<i<5:
	print(f"division of {n1} and {n2} gives {div(n1, n2)}")

