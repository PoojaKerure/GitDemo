# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print("Name is:",name)
#
#
# mc=MyClass()
# mc.myfun()
# mc.display("Pooja")

# Instance and Static method...

# class MyClass:
#     def m1(self):
#         print("Instance Method")
#     @staticmethod
#     def m2():
#         print("Static Method")
#
# mc=MyClass()
# mc.m1()
# MyClass.m2()

# Declaring static parameters

# class MyClass:
#     def m1(self):
#         print("Instance Method")
#     @staticmethod
#     def m2(self):
#         print(self)
#
# mc=MyClass()
# mc.m1()
# MyClass.m2(10)

# Declaring variables inside the class..

# class MyClass():
#     a,b=100,200
#
#     def add(self):
#         print(self.a+self.b)
#
#     def mul(self):
#         print(self.a*self.b)
#
# mc=MyClass()
# mc.add()
# mc.mul()

# local variable,class variable,global variable
#
# i,j=15,25    #Global Variables
#
# class  MyClass:
#     a,b=10,20    #Class variable
#
#     def add(self,x,y):   #local variable
#         print(x+y)       #accesing local variables
#         print(self.a+self.b)   #accessing class variables
#         print(i+j)
#
# mc=MyClass()
# mc.add(30,40)

# a,b=15,25
#
# class MyClass:
#     a,b=10,20
#
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b'])
#
# mc=MyClass()
# mc.add(100,200)

# creating multiple object for single class...

# class MyClass:
#     def display(self):
#         print("Good Morning")
#
# obj1=MyClass()
# obj1.display()
#
# obj2=MyClass()
# obj2.display()

# named object and nameless object..
#
# class MyClass:
#     def display(self):
#         print("Good Morning")
#
# obj1=MyClass() #Named Object
# obj1.display()
#
# MyClass().display()  #Nameless object


# How to check  memory location..

# class MyClass:
#     def m1(self):
#         pass
#
# c1=MyClass()
# c2=MyClass()
# c3=c1
#
# print(id(c1))
# print(id(c2))
# print(id(c3))
#
# print(c1 is c2)
# print(c1 is c3)
#
# print(c1 is not c2)
# print(c1 is not c3)

# constructor

# class MyClass:
#     def m1(self):
#         print("Good morning")
#
#     def __int__(self):
#         print("this is a constructor")
#
# c=MyClass();
# c.m1()


# class MyClass:
#     def values(self,val1,val2):
#         print(val1)
#         print(val2)
#         self.val1=val1
#         self.val2=val2
#
#     def  add(self):
#         print(self.val1 + self.val2)
#
#
# mc=MyClass()
# mc.values(10,20)
# mc.add()

# class MyClass():
#     def m1(self):
#         print("this is m1 method")
#         self.m2(100)
#
#     def m2(self,a):
#         print("this is m2 method",a)
#
# mc=MyClass()
# mc.m1()

# class MyClass:
#     name="patil"
#     def __init__(self, name):
#         print(name)
#         print(self.name)
#
# c = MyClass("pooja")

# class  Emp():
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def display(self):
#         print("EmpId:{} EName:{}  Sal:{}".format(self.eid,self.ename,self.sal))
#         print("EmpId:%d Ename:%s Esal:%g" % (self.eid,self.ename,self.sal))
#
#
# c=Emp(101,'pooja',25000)
# c.display()

#__str__:executes automatically when you print reference variable
# class MyClass():
#     def __str__(self):
#         return "Welcome"
#
# c=MyClass()
# print(c)

# class  Emp():
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def __str__(self):
#         return ("EmpId:{} EName:{}  Sal:{}".format(self.eid,self.ename,self.sal))
#
#
#
# c=Emp(101,'pooja',25000)
# print(c)


#__del__ :-
#
# class MyClass:
#     def __del__(self):
#         print("Destroyed")
#
# f1=MyClass()
# f2=MyClass()
#
# del f1


# class Student:
#     name="Pooja"

# s1=Student()
# print(s1.name)

# class Car:
#     color="blue"
#     brand="mercedece"
# s1=Car()
# print(s1.color)
# print(s1.brand)

# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
#         print("adding new student in database..")
#
# s1=Student("karan")
# print(s1.name)

# class Student:
#     name="Karan"
#
# s1=Student()
# print(s1.name)


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student in database")     #constructors
#
# s1=Student("Karan",90)
# print(s1.name,s1.marks)
# s2=Student("Arjun",87)
# print(s2.name,s2.marks)


# class Student:
#     def hello(self):
#         print("hello")     #default value
#
# s1=Student()
# s1.hello()


# class Student:
#     @staticmethod
#     def hello():
#         print("hello")     #static method
#
# s1=Student()
# s1.hello()

# class Student:
#     name="Pooja"
#
# s1=Student()
# print(s1.name)

# class Car:
#     color="blue"
#     brand="mercedece"
#
# car1=Car()
# print(car1.color)
# print(car1.brand)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new students in database")
#     def hello(self):
#         print("hello",self.name)
#     def get_marks(self):
#         return self.marks
#
# s1=Student("pooja",97)
# s1.hello()
# print(s1.get_marks())
# print(s1.name,s1.marks)

# s2=Student("Arjun",87)
# print(s2.name,s2.marks)


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your avg score is:",sum/3)
#
# s1=Student("pooja",[97,98,99])
# s1.get_avg()


# class Student:
#     @staticmethod
#     def hello():
#         print("hello")
#
# s1=Student()
# s1.hello()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("Hello my name is " + self.name)
#     # def __str__(self):
#     #     return f"{self.name}({self.age})"
#
# s1=Person("Pooja",25)
# s1.age=40
# # del s1.age
# s1.myfunc()
# print(s1.name,s1.age)
# print(s1)

# class Person:
#     def __init__(self,firstname,lastname):
#         self.fname=firstname
#         self.lname=lastname
#     def printname(self):
#         print(self.fname,self.lname)
#
#     def Student(Person):
#         def __init__(self,firstname,lastname):
#             Person.__init__(self,firstname,lastname)
#
# s1=Person("Pooja","Kerure")
# s1.printname()

# i,j=15,25
# class MyClass:
#     a,b=10,20
#     def add(self,x,y):
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
#
# s1=MyClass()
# s1.add(40,60)

a,b=15,25
class MyClass:
    a,b=10,20
    def add(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])

s1=MyClass()
s1.add(100,200)






















































































