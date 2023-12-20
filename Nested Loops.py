"""Exercise 1
Write a program to print the following pattern:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="\t")

    print("\n")

    Exercise 2
Write a program to print the following pattern:
1
2 3
4 5 6
7 8 9 10 """
x=1
for i in range(1,5):
    for j in range(i,0,-1):
        print(x,end="\t")
        x+=1

    print("\n")
