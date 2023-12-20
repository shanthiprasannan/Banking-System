set1=set()
print(set1)
print(type(set1))
for i in range(1,12,2):
    set1.add(i)
print(set1)
set1.add(10)
print(set1)
set1.update([55,77])
print(set1)

set1.remove(55)

print(set1)

set2={1,2,3}
set3={3,4,5,6}
set3=set2.union(set3)
print(set3)
set3=set1.intersection(set3)
print(set3)
fset=frozenset(set1)

print(fset)


''''#tupple
t1=()
print(type(t1))
t1=(1)
print(type(t1))
t1=(1,)
print(type(t1))
t1=tuple()
print(t1)
t1=(1,2,3)
print(t1)
print(t1[2])
t3=(14,15,16)
t4=(15,88,99)
t5=t3,t4
print(t5)
t6=t3+t4
print(t6)'''

t1=(1,2,3)

a,b,c=t1
print(a)
print(b)
print(c)
l1=list(t1)
l1.append(25)
t2=tuple(l1)
print(t2)
