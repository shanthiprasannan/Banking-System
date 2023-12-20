"""Exercise 1
Write a program to print all the even numbers within the given range.

n=int(input("enter the range"))
for i in range(2,n):
    a=i%2
    if a==0:
        print(i,end="\t")


Exercise 2
Find the factorial of a given number using loops(note the number is received from the user)

n=int(input("enter the number"))
fac=1
if n>=1:
    for i in range(1,n+1):
        fac*=i

    print("factorial of the number",n,"is",fac)
else:
    print("please enter a integer number")






Exercise 3
Reverse a number using while loop

n=int(input("enter the number"))
y=0
while n>0:
    x=n%10
    y=y*10+x
    n=n//10

print("revere of the number is {}".format(y))



Exercise 4
Finding the multiples of a number using loop

n=int(input("enter the number"))
r=int(input("enter the range"))
print("the multiples are :")
for i in  range(1,r+1):
    x=i%n
    if x==0:
        print(i,end="\t")





Exercise 5
Check how many times a given number can be divided by 4 before it is less than or equal to 12

n=int(input("enter the number to be checked"))
x=n
i=0
while n>12:
    n=n/4
    i+=1

print("number of times",x,"is divisible by 4 is  :",i)




Exercise 6
Write a program to print the inputted value as it is and break the loop if the value is 'done'.
Example run of the program
:hello there
hello there
:finished
finished
:done
Done

string=input("enter the input value")
for i in range(5):
    print(i,end="\t")
    if string=="done":
        break

        Exercise 7
Write a while loop that continues to run until the user inputs a number greater than 100

n=int(input("enter the number"))
i=5
while i>0:
    if n>100:
        break
    else:
        print(n)


        Exercise 8
Write a program that prints the numbers from 1 to 10. But for multiples of three print
"Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which 
are multiples of both three and five print "FizzBuzz" """

for i in range(1,11):
    if i%3==0 and i%5==0:
        print("FizzBuzz",end="\t")

    elif i%3==0:
       print("Fizz",end="\t")
    elif i%5==0:
        print("Buzz",end="\t")
    else:
        print(i,end="\t")




