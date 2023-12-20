"""Exercise 5
Write a Python program to receive 3 numbers from the user and print the greatest among them."""

num1=int(input("enter the first number\n"))
num2=int(input("enetr the second number\n"))
num3=int(input("enter the third number \n"))
if num1>num2 and num1>num3:
    print("greatest number is ", num1)
elif num2>num1 and num2>num3:
    print("greatest number is ", num2)
elif num3>num1 and num3>num2:
    print("greatest number is ", num3)

