'''s1='hello hai'
l1=list(s1)
l1[0]='l'
print(l1)
s2=str(l1)
print(s2)
s3=" ".join(l1)
print(s3)
s4=" ".join(reversed(s3))
print(s4)'''
#set

"""l1=[1,2,3,4,5,6,7]
s1=[i*i for i in l1]
print(s1)"""

#set comprehension
"""
l1={1,2,3,4,5,6,7}
s1={i*i for i in l1}
print(s1)"""

#dictionary comprehension
"""l1=[1,2,3,4,5,6,7]
d1={x:x**2 for x in l1}
print(d1)"""

s1=[1,2,3,4]
b1=[1,4,9,12]
z=zip(s1,b1)
for i in z:
    print(i)
