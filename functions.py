"""

def add():
    n1=10
    n2=10
    print(n1+n2)
add()


"""
"""def add(a,b):
    print(a+b)

a=int(input("enter the nummber\n"))
b=int(input("enter the nummber\n"))
add(a,b)"""

'''def add():
    n1=10
    n2=10
    sum=n1+n2
    return sum
result=add()
print(result)'''

def fact(x):
    if x==0:
        return 1
    else:
        return (x*fact(x-1))

print(fact(5))

