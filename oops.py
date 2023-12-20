"""
Exercise 1:
Build a program to manage a university's course catalog. You want to define a base class Course that has the following properties:
course_code: a string representing the course code (e.g., "CS101")
course_name: a string representing the course name (e.g., "Introduction to Computer Science")
credit_hours: an integer representing the credit hours for the course (e.g., 3)
You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
CoreCourse should have an additional property required_for_major which is a boolean representing whether the course is required for a particular major.
ElectiveCourse should have an additional property elective_type which is a string representing the type of elective (e.g., "general", "technical", "liberal arts").wshddhshYUDYDCDHCDUDGCVHCGCV CVG  CVC  CC  BC"""

"""class Course:
    def __init__(self,course_code,course_name,credit_hours):
        self.course_code=course_code
        self.course_name=course_name
        self.credit_hours=credit_hours


class Corecourse(Course):
    def __init__(self,course_code,course_name,credit_hours,required_for_major):
        super().__init__(course_code,course_name,credit_hours)
        self.required_for_major = required_for_major

class Elective_course(Course):
    def __init__(self,course_code,course_name,credit_hours,elective_type):
        super().__init__(course_code,course_name,credit_hours)
        self.elective_type= elective_type

core=Corecourse('CS101','Computer Science',3,True)
E1=Elective_course('IT101','Information Technology',2,'Technical')
E2=Elective_course('Gk101','General Knowledge',2,'General')
E3=Elective_course('AR101','Sculptures',2,'Liberal Arts')

print("Core course code:",core.course_code,"\nCore course name : ", core.course_name,"\nCredit Hors : ",core.credit_hours,
      "\nRequired for Major : ",core.required_for_major)
print(30*"*")
print("Elective course code : ",E1.course_code,"\nElective Corse name : ",E1.course_name,"\nCredit hours for elective",E1.credit_hours,
      "\nElective type : ",E1.elective_type)
print(30*"*")
print("Elective course code : ",E2.course_code,"\nElective Corse name : ",E2.course_name,"\nCredit hours for elective",E2.credit_hours,
      "\nElective type : ",E2.elective_type)
print(30*"*")
print("Elective course code : ",E3.course_code,"\nElective Corse name : ",E3.course_name,"\nCredit hours for elective",E3.credit_hours,
      "\nElective type : ",E3.elective_type)
print(30*"*")

Exercise 2:
Create a base class Shape with methods area() and perimeter() and a subclass Rectangle that
inherits from Shape and implements its own version of the area() and perimeter() methods.
"""

"""class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self):
        l=int(input("enter the length: "))
        b=int(input("enter the length: "))
        self.l=l
        self.b=b
    def area(self):
        print(f"area of the rectangle is {self.l * self.b}.")
    def perimeter(self):
        print(f"Perimeter of the rectangle is {2*(self.b + self.l)}. ")
s1=Rectangle()
s1.area()
s1.perimeter()"""

"""Exercise 3:
Create a base class Vehicle with properties make, model, and year and a method 
description() that returns a string with information about the vehicle. Create two
subclasses Car and Motorcycle that inherit from Vehicle and implement their own version of the description() method."""

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def description(self):
        print(self.make,self.model,self.year)
class Car(Vehicle):
    def __init__(self,type,make,model,year):
        super().__init__(make,model,year)
        self.type=type
    def description(self):
        return f"{self.make} {self.model} {self.year}, {self.type}"
class Motorcycle(Vehicle):
    def __init__(self,make,model,year,type):
        super().__init__(make,model,year)
        self.type=type
    def description(self):
        return f"{self.make} {self.model} {self.year}, {self.type}"
v1=Vehicle("Tata","Santro",2013)
c1=Car("Racing car","Roadster",2020,"Lamborghini")
m1=Motorcycle("harley Davidson","Sportster",2020,"sport")
v1.description()
print(c1.description())
print(m1.description())
