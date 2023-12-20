n=int(input("To know the ticket price, please enter your age"))
if n>=0 and n<16:
    print("your ticket price is 3")
elif n>=16 and n<60:
    print("your ticket price is 6")
elif n>=60:
    print("your ticket price is 2")
