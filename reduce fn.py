import functools

n=[1,2,3,4,5]
def add(x,y):
    return (x+y)

print(functools.reduce(add,n))
print(functools.reduce(lambda x,y:x+y,n))


print(functools.reduce(lambda x,y:x*y,n))
print(functools.reduce(lambda x,y: x if x>y else y,n))
