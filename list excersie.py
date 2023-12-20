#exercise 1

"""list1=[1,2,3,4,5]
print(list1)

Exercise 2
Insert 3 new values to the list and print the updated list."""

#list1=[1,2,3,4,5]
#print(list1)
"""list1.extend(["sam", "ann",6,7,8])
print(list1)"""

"""Exercise 3
Access the third element in the list and print the element."""

#print(list1[2])

"""Exercise 4
Create a new list of 3 random strings and concatenate the two lists into a third list.
"""

"""list1=[1,2,3,4,5]
print(list1)"""
"""list2=["one","two","three"]
print(list2)
list3=list1+list2
print(list3)"""

"""Exercise 5
Try to use a for loop to print each element in the list.
"""
"""list1=[1,2,3,4,5]
print(list1)"""
"""for i in list1:
    print(i)
    
    Exercise 6
Create a list and print all the even numbers in that list"""
"""list1=list(range(2,25))                    """
"""print(list1)                               """
"""list2=[]                                   """
"""for i in list1:                            """
"""    if i%2==0:                             """
"""        list2.append(i)                    """
"""    else:                                  """
"""        continue                           """
"""print("list of even numbers is \n",list2)  """

"""Exercise 1
Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively."""



"""Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'."""

"""dict1={"name":"john","age":25,"address":"New York"}
print(dict1)
dict1["phone"]=1234567890
print(dict1)"""

#Q3. Remove the key 'address' from the dictionary created in Q1.

"""del dict1["address"]
print(dict1)"""
#Q4.  Print the value of the key 'age' from the dictionary created in Q1.
"""dict1={"name":"john","age":25,"address":"New York"}
print("age is :",dict1["age"])"""

#Q5. Check if the key 'phone' exists in the dictionary created in Q1.

"""dict1={"name":"john","age":25,"address":"New York"}
if "phone" in dict1:
    print("the key \"phone\" exists in the dictionay")
else:
    print("key word doesnot exist in the dictionary")"""

#Q1.Create a set with values 1, 2, 3, 4, and 5.

"""set1={1,2,3,4,5}
print(set1)"""

#Q2. Add the value 6 to the set created in Q1.

"""set1.add(6)
print(set1)"""
#Q3. Remove the value 3 from the set created in Q1.
"""set1={1,2,3,4,5}
print(set1)
set1.remove(3)
print(set1)"""

#Q4. Print the length of the set created in Q1.
"""set1={1,2,3,4,5}
print(len(set1))"""

#Q5. Create a new set by union of the set created in Q1 with another set {6, 7, 8}.


"""set1={1,2,3,4,5}
set2={6,7,8}
set3=set1.union(set2)
print(set3)"""

#Q1. Create a tuple with values 1, 2, 3, and 4

"""tuple1=(1,2,3,4)
print(tuple1)

Q2. Print the length of the tuple created in Q1."""

"""tuple1=(1,2,3,4)
print(len(tuple1))"""

#Q3. Create a new tuple by concatenating the tuple from Q1 with another tuple (5, 6).

"""tuple1=(1,2,3,4)
tuple2=(5,6)
tuple3=tuple1+tuple2
print(tuple3)"""

#Q4. Print the first two values of the tuple created in Q3.

"""tuple3=(1, 2, 3, 4, 5, 6)
print(tuple3[0:2])
Q5. Check if the value 4 exists in the tuple created in Q1."""

"""tuple1=(1,2,3,4)
if 4 in tuple1:
    print("the number exits")
else:
    print("the number dosnot exits")"""


#Write a program that asks the user to enter his/her name and then partly encrypt and display it.

"""name=input("name is:")
ename=name[0]+(len(name)-2)* "*" +name[-1]
print(ename)

Exercises 2
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2  """

"""list1=["ana","sana","maam","anna"]
list2=[i for i in list1 if i[0]==i[-1]]
print("strings in the list which has same first and last characters is :",list2)"""

#Write a Python program to multiply all the items in a list
"""list1=[12,14,45,67,78]
print("list is :",list1)
result=1
for i in list1:
    result*=i
print("product of the items in the list is :",result)

Exercise 4
Create dictionary from a list where the keys are the elements of the list and value of the dictionary is result after dividing the element by 3
"""

"""list1=list(range(5,100,5))
print("the list is :",list1)
dict1={i:round(i/3,2) for i in list1}
print("the dictionary is :",dict1)

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















