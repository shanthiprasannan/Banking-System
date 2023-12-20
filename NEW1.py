"""file1=open("sample1","r")
print(file1)
#print(file1.read())
#print(file1.read(7))
#print(file1.readline())
print(file1.readlines())"""

class rectangle:
    def area(self,l,b):
      area=l*b
      return area
    def peri(self,l,b):
        peri=2*(l+b)
        return peri

c1=rectangle()
print ("area is ",c1.area(2,3))
print ("perimeter is ",c1.peri(2,3))


