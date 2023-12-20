def task(n):
    return n+n
n=[2,23,14,20]
res=map(task,n)
print(list(res))

print(list(map(lambda n:n+n,[10,20,2,3])))
print(list(map(lambda n:n**2,[2,4,6])))

