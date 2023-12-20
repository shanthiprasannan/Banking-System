"""list1=[22,33,44,55,66,11]
n=int(input("enter a number"))
for i in list1:
    if i==n:
        print("number is in the list")

list1=[22,33,44,55,66,11]
print(list1[1:4])
list1.append(100)
print(list1)
list1.insert(3,99)
print(list1)
list1.extend([66,77])
print(list1)
list2=[1,2,3]
list3=list1+list2
print(list3)
list3.remove(66)
print(list3)
del list3[5]
print(list3)
list3.pop(2)
print(list3)
#list3.pop(2,3)
print(list3)
items={"india":"delhi","england":"london"}
print(items)
print(type(items))
dict1=dict((["k1","v1"],["k2","v2"]))
print(dict1)

dict2={
    "h":"helium",
    "o2":"oxygen",
    "li":"lithium"

}
print(dict2)
#insertion
dict2["h"]="hydrogen"
print(dict2)
del dict2["h"]
print(dict2)"""

dict1=dict()
print(dict1)
#n=int(input("please enter the number of students"))

for i in range(1,4):

    name=input("enetr student name")
    m1=int(input("enter cs marks"))
    m2=int(input("enter eng marks"))
    m3=int(input("enter maths marks"))
    dict1[name]={"cs":m1,"eng":m2,"maths":m3}
    i+=1
print(dict1)

sname=input("enter student name to check:\t")
sub=input("enter subject name:\t")
if sname not in dict1:
    print("student not found")
else:
    print("marks of the",sub,"is",dict1[name][sub])
