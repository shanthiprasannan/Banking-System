"""Write a Python program that prompts the user to input a string and converts
it to an integer. Use try-except blocks to handle any exceptions that might occur"""

"""try:
    word = input("enter ")
    word=int(word)
    print(word)
except ValueError:
    print("please enter integer numbers")
Exercise 2
Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative."""

"""try:
    list1=[]
    value=int(input("enter the range of numbers you want to added to the list"))
    for i in range(value):
        num=int(input("enter the number to be added"))
        if num>=0:
            list1.append(num)
        else:
            raise Exception ("Only positive numbers are allowed")
    print("Elements in the list are : ",list1)
except ValueError:
    print("number should be integer")
except Exception as Error:
    print(Error)
    
    Exercise 3
Write a Python program that prompts the user to input a list of integers and computes 
the average of those integers. Use try-except blocks to handle any exceptions that might
occur.use the finally clause to print a message indicating that the program has finished running."""

"""
try:
    list1=[]
    value=int(input("enter the range of numbers you want to added to the list"))
    if value < 0:
        raise Exception("Only positive numbers are allowed")
    elif value < 0:
        raise ZeroDivisionError("Value must must be greater than zero")
    sum_of_elemesnt=0
    for i in range(value):
        num1 = int(input("enter the number to be added"))
        list1.append(num1)
        sum_of_elemesnt += num1
    print("Elements in the list are : ",list1)
    print(f"Averge of the elements in the {list1} is {sum_of_elemesnt/value}")
except ValueError:
    print("Number should be integer")
except Exception as Error:
    print(Error)
except ZeroDivisionError as error:
    print(error)
finally:
    print("End of the program")
    
    Exercise 4
Write a Python program that prompts the user to input a filename and writes
a string to that file. Use try-except blocks to handle any exceptions that might occur 
and print a welcome message if there is no exception occurred."""

try:
    file_name = input("enter your file name to read")
    with open(file_name,"r") as file1:
        print("welcome to the file ", file_name)
        print(file1.read())
except FileNotFoundError:
    print("File not found")

