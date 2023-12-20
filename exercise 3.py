"""Topic : functions and its types of arguments
Exercises 1:
Write a function to implement calculator
Sample run:
Press 1 for addition
Press 2 for subtraction
Press 3 for Multiplication
Press 4 for Division
Enter your option: 1
Enter your first number:  23
Enter your second number: 10
Addition of 23 and 10 is : 33"""

"""def calc (num1,num2,opp):
    if opp == 1:
        #print("done")
        return "sum of the numbers " + str(num1) +" and "+ str(num2) + " is "+ str(num1+num2)
    elif opp == 2:
        return "Different between "+ str(max(num1,num2)) +" and " + str(min(num1,num2)) +" is " + str(max(num1,num2)-min(num1,num2))
    elif opp == 3:
        return "product of "+ str(num1) +" and " +str(num2)+" is "+ str(num1*num2)
    elif opp == 4:
        return "Dividing "+str(num1)+" and "+str(num2) +" we get "+ str(round(num1/num2,2))
    else:
        print("Please enter a valid number for the operation")

print("Note:\n1 for Addition\n2 for Subtraction\n3 for multiplication\n4 for Division\n")
num1=float(input("Enter the first number\n "))
num2=float(input("Enter the second number\n "))
opp=int(input("Enter the number for opearation \n"))
print(calc(num1,num2,opp))"""


"""def fun(num1, num2=10, num3="None"):
    if num3== "None":
        print(f"sum of {num1} and {num2} is {num1+num2}.")
    else:
        print(f"product of the numbers {num1},{num2} and {num3} is {num1*num2*num3}")

fun(2)
fun(10,num2=11)
fun( num1=100,num2=200, num3=300)"""

"""def sum1(*num1):
    j=0
    for i in num1:
        if i%2==0:
            j+=i
        else:
            continue
    return "sum of even numbers in " + str(num1) +" is " + str(j)

print(sum1(1,2,3,4,5))
print(sum1(22,23,3,25))"""

"""def pro (*num1,num2=1):
    x=1
    for i in num1:
        x*=i
    x*=num2
    print(f"product of {num2} and each element in {num1} is {x}")

pro(1,2,3,4,5,num2=22)
pro(-1,-2,-3,num2=2)"""

"""def string5(*str1):
    list1=[]
    list2=[]
    for i in str1:
        list1.append(i)
        if len(i)>=5:
            list2.append(i)
    print("list of strings is ", list1)
    print("list of strings with length equal to or greater than 5 is",list2)

string5("anu","shanthi", "greater", "world", "string", "manu")"""

"""def fn(*str1):
    name=""
    list1=[]
    list2=[]
    vowel=['a','e','i','o','u']
    for i in str1:
        i=i.lower()
        list1.append(i)
        for j in i:
            if j not in vowel:
                name+=j
        list2.append(name)
        name=""
    print("list of the string is ",list1)
    print("list of the wors without vowels is ", list2)

fn("anu","shanthi", "greater", "world", "string", "manu")"""


"""def sum1(x):
    if len(x)==1:
        return x[0]
    else:
        return x[0]+sum1(x[1:])
print("sum of the elements in the list is ",[10,20,30], "is ", sum1([10,20,30]))"""

"""num=int(input("enter a number: "))
print("checking if the number is even or odd")
print((lambda x:x%2==0)(num))"""


"""num1=int(input("enter the number to be added with 15"))
num2=int(input("enter the number to be multiplied"))
num3=int(input("enter the second number to be multiplied"))
print(f"sum of {num1} and 15 is : ",(lambda x:x+15)(num1))
print(f"product of {num2} and {num3} is : ", (lambda x,y:x*y)(num2,num3))"""

"""e=input("enter the mathematical expression")
print("The solution for given mathematical expression is ",eval(e))"""

# print(" The expression \' 5>2 and 3<4\' is", eval("5>2 and 3<4"))

"""print(eval("[x*2 for x in range(5)]"))"""

"""def con(word):
    vowel=["a","e","i","o","u"]
    word=word.lower()
    if word in vowel:
        return True
    else:
        return False


print(list(filter(con,["a","d","3","i"])))"""

"""def pnum(list1):
    for i in range(2,list1):
        if list1%i==0:
            return False
    return True
print(list(filter(pnum,[7,12,3,4,56,34,37])))"""

"""def str5(words):
    if len(words)>5:
        return True
print(list(filter(str5,["anu","walking","sleeping","run","running"])))"""

#print(list(map(lambda x:x.upper(),["anu","walking","sleeping","run","running"])))



"""import supportclass as sc
a=sc.person1["age"]
print(a)"""

"""import sys
print("hello world")
#sys.exit()
print("bye")
print(sys.platform)
for path in sys.path:
    print(path)"""

from time import time

"""def star(fun):
    def wrapper():
        t1=time()
        fun()
        t2=time()
        print("The function execution time is\t",t1-t2)
    return wrapper

@star
def time_exe():
    print("Hi, Welcome to python world")
    a=15
    b=12
    c=a+b
    print("sum of two numbers is",c)

time_exe()
    """

def dec(fun):
    def wrapper(country):
        result=fun(country)
        return result.upper()
    return wrapper
@dec
def city(country):
    return "Residing at Ernakulam "+ country

print(city("India"))






