# s=set()
# print(type(s))
#
# d={}
# print(type(d))


# name="Arun"
# age=25
# price=35.7
# a=True
# b=3+1j
#
# print(type(a))
# print(type(b))
# print(name)
# print(age)
# print(price)

# print("My name is:",name)
# print("My age is: ",age)

# a,b=5,2
# c=a/b
# print(c)   #5/2=2.5
#
# a,b=5,2
# c=a//b
# print(c)   #5//2=2.5~2
#
#
# a,b=5,2
# c=a%b
# print(c) #5%2=remainder is 1 , in modulo n/d=++=+,+ -=-,--=+,- +=+

# name=input("name: ")
# print(name)
# print(type(name))

# age=int(input("age: "))
# print(age)
# print(type(age))

# price=float(input("price: "))
# print(price)
# print(type(price))

# a=5
# if a<10:
#     print("True")
# elif a>10:
#     print("True")
# else:
#     print("False")

# age=25
# if age>=18:
#     print("eligible for voting")
# elif age<=18:
#     print("under age")
# else:
#     print("not eligible for voting ")

# light=input("light: ")
# if light=="red":
#     print("stop")
# elif light=="green":
#     print("go")
# elif light=="yellow":
#     print("look")
#
# else:
#     print("light is broken")


# marks=int(input("marks: "))
# if marks>=90:
#     print("A")
# elif marks>=70 and marks <90:
#     print("B")
# elif marks>=45 and marks <70:
#     print("C")
# else:
#     print("fail")


#single line if/ternery operator

# food=input("food: ")
# eat="yes" if food=="cake" else "no"
# print(eat)

#Arithmatic operators

# a=4
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

#relational/comparision operator

# a=50
# b=20
# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)


#Assignment operator
# num=10
# num=num+10
# num+=10
# num-=10
# num*=10
# num**=10
# print(num)

#logical operator
# a=5
# b=2
# print(a>b and a==b)
# print(a>b or b<a)
# print(not(a>b))

#type conversion
# a=2
# b=4.25
# sum=a+b
# print(sum)

#type casting
# a,b=1,"2"
# c=int(b)
# print(c)

# sentence ="python is a good programming language"
# word=sentence.split()
# count=sentence.count("o")
# find=sentence.find("i")
# print(sentence)
# print(word)
# print(count)
# print(find)


# Words = ["hello", 1, 3, "world", 4.56, 3]
#
# count_word=Words.count(3)
# index_word=Words.index("world")
# reverse_word=Words.reverse()
# pop_word=Words.pop()
#
# print(Words)
# print(count_word)
# print(index_word)
# print(reverse_word)
# print(pop_word)


# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# # sum=num1+num2
# print(num1+num2)

# side=float(input("Enter side of square:"))
# area=side*side
# print(area)

# a=float(input("Enter float1 value:"))
# b=float(input("Enter float2 value:"))
#
# print("average=",(a+b)/2)

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
#
# print(a>=b)

# str1="pooja"
# print(len(str1))
#
# print(str1[0])    # indexing
# print(str1[1])
# print(str1[1:3])   #slicing
# print(str1[:5])
# print(str1[:2])
# print(str1[-1])   #negative slicing
# print(str1[-4])

# str1="apna college"
#str1="apna college in"
# print(str1.endswith("ge"))
# print(str1.count("l"))
# print(str1.capitalize())
# print(str1.replace("in","is"))
# print(str1.format())
# print(str1.find("n"))


# str="i am studing python from apna college"
# print(str)
# print(str.swapcase())
# print(str.upper())
# print(str.startswith("I"))
# print(str.split())

# str=input("Enter your name:")
# len=len(str)
# print(len)


# marks=int(input("Enter student marks:"))
# if marks>=90:
#     print("A")
# elif marks>=80 and marks<90:
#     print("B")
# elif marks>=70 and marks<80:
#     print("C")
# else:
#     print("D")


#nested if

# age=90
#
# if age>=18:
#     if age>=80:
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot  drive")

# num=5
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
#
# if a>b and a>c:
#     print("first number is gretest",a)
# elif b>c:
#     print("sencond number is largest",b)
# else:
#     print("third number is largest")

# marks=[85,65,45,80,70,35,90,85,40]
# print(marks)
# print(len(marks))
# print(marks[0])
# print(marks[6])
# marks[1]=60
# print(marks)
# print(marks[0:7])
# print(marks[0:])
# print(marks[-3:-1])
# print(type(marks))

# student=["pooja",75,"arun",80,"sharu",20,10,10,30]
# student.insert(2,"joo")
# student.pop()
# student.reverse()
# student.append("harshi")
# student.append(90)
# print(student.count(10))
# student.sort()
# student.remove(30)
# # print(student)
# print(student)
# print(len(student))
# print(student[0])

#print("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

# import datetime
#
# # Get the current date and time
# now = datetime.datetime.now()
#
# # Create a datetime object representing the current date and time
#
# # Display a message indicating what is being printed
# print("Current date and time : ")
#
# # Print the current date and time in a specific format
# print(now.strftime("%Y-%m-%d %H:%M:%S"))


# from math import pi
#
# # Prompt the user to input the radius of the circle
# r = float(input("Input the radius of the circle : "))
#
# # Calculate the area of the circle using the formula: area = π * r^2
# area = pi * r ** 2
#
# # Display the result, including the radius and calculated area
# print("The area of the circle with radius " + str(r) + " is: " + str(area))

#
# # Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
# values = input("Input some comma-separated numbers: ")
#
# # Split the 'values' string into a list using commas as separators and store it in the 'list' variable
# list = values.split(",")
#
# # Convert the 'list' into a tuple and store it in the 'tuple' variable
# tuple = tuple(list)
#
# # Print the list
# print('List : ', list)
#
# # Print the tuple
# print('Tuple : ', tuple)


# color_list = ["Red","Green","White" ,"Black"]
# print(color_list)
# print(color_list[0])
# print(color_list[3])

# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)

# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)
#
# calculate(5, 6)


# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]
#
# print(listOne == listTwo)
# print(listOne is listTwo)

# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)


# for i in range(10, 15, 1):
#   print( i, end=', ')

# salary = 8000
# def printSalary():
#     salary = 12000
#     print("Salary:", salary)
#
# printSalary()
# print("Salary:", salary)

# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )

# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)

# var= "James Bond"
# print(var[2::-1])

# for x in range(0.5, 5.5, 0.5):
#   print(x)

# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# tup=(2,1,3,1)
# print(tup)
# print(tup[0])

# tup=(1,)
# print(tup)
# print(type(tup))


# movies=[]
# mov1=input("Enter 1st movie:")
# mov2=input("Enter 2nd movie:")
# mov3=input("Enter 3rd movie:")
#
# movies.append("DJ")
# movies.append("Salar")
# movies.append("KGF")
#
# print(movies)


# list1=[1,2,1]
#
# copy_list1=list1.copy()
# copy_list1.reverse()
#
# if (copy_list1==list1):
#     print("palidrome")
# else:
#     print("not palidrome")

# str1="i am learning python"
# print(str1.count("a"))
# print(str1.index("n"))
# print(str1.split())
# print(len(str1))

# list1=[1,2,4,3,5,6,7,3,2]
# # list1.reverse()
# # list1.sort()
# print(list1.count(3))
# print(list1[0])
# print(list1[1:4])
# print(list1)
# print(type(list1))
# print(list1.pop())


# grade=("C","D","A","A","B","A")
# print(grade.count("A"))

# grade=["C","D","A","A","B","A"]
# grade.sort()
# print(grade)


# dict1={"name":"pooja","age":25,"gender":"Female","marks":95}
# dict1["name"]="arun"
# print(dict1)
# print(dict1["name"])
# print(dict1["age"])
# print(dict1["gender"])
# print(dict1["marks"])

# dict={}
# dict["name"]="pooja"
# dict["age"]=25
# print(type(dict))
# print(dict)

#nested dictionary
# student={
#     "name":"Pooja",
#     "Score":{
#         "che":98,
#         "phy":97,
#         "math":95
#     }
# }

# print(student)
# print(student["Score"]["che"])
# print(student.keys())
# print(student.values())
# print(list(student.items()))
# print(student.get("name"))
# print(student.update({"city":"Delhi"}))
# print(student)


# set1={1,2,3}
# set2={2,3,4}
#
# print(set1.union(set2))
# print(set1.intersection(set2))


# dict={"table":["a piece of furniture","list of facts and figures"],"cat":"a small  animal"}
# print(dict)

# str="pooja"
# print(type(str))

# list1=[1]
# print(list1)
# print(type(list1))
#
# tup=(1,)
# print(tup)
# print(type(tup))

# dict={"a":1,"b":2}
# print(dict)
# print(type(dict))
#
# s=set()
# s1=["banana","apple","mango"]
# # s.add(1)
# # s.add(2)
# # s.add(2)
# # s.add(3)
# s.update(s1)  #adding multiple values
# print(s)
# print(type(s))

# fruits = set()
# fruits.add(['apple', 'banana'])
# print(fruits)  #gives error


# s="apna college"
# print(s)
# print(s.count("e"))
# print(s.split())
# print(s[0])
# print(s[1:4])
# print(s.find("l"))
# print(s.format())
# print(type(s))

# list1=["pooja",2,4,3,5,6,7,"arun"]
# list2=[10,20,30,40]
# print(list1[0])
# print(list1[1:3])
# # list1.reverse()
# # list1.pop()
# list1.extend(list2)
# print(len(list1))


# tup=(1,2,3,4,5,6,3,2,1)
# print(tup.index(5))
# print(tup.count(3))
# print(len(tup))

# s1={1,2,3,10,4,5,6,1,2}
# s2={"a","b","c","d"}
#
# print(len(s1))
# print(s1)
# print(type(s1))
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)


# x=lambda a:a+10
# print(x(5))

# x=lambda a,b:a*b
# print(x(2,3))
#
# x=lambda a,b,c:a+b+c
# print(x(5,7,8))


# A=1,2,3,4
# a,b,c,d=A
# print(type(A))


# count=1
# while count<=5:
#     print("hello",count)
#     count+=1
#
# print("end loop")

# i=5
# while i>=1:
#     print(i)
#     i-=1
#
# print("loop ended")

# i=1
# while i<=100:
#     print(i)
#     i+=1
#
# print("loop ended")

# i=100
# while i>=1:
#     print(i)
#     i-=1
#
# print("loop ended")

# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
# print("loop ended")

# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1
# print("loop ended")

# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("Found idx",i)
#     i+=1
# print("loop ended")


# i=1
# while i<=5:
#     print(i)
#     if (i==3):
#         break
#     i+=1
# print("loop ended")

# i=0
# while i<=5:
#     if (i==3):
#         i += 1
#         continue
#     print(i)
#     i+=1
# print("loop ended")


# i=0
# while i<=5:
#     if (i%2==0):
#         i += 1
#         continue
#     print(i)
#     i+=1
# print("loop ended")

# i=0
# while i<=5:
#     if (i%2!=0):
#         i += 1
#         continue
#     print(i)
#     i+=1
# print("loop ended")

# for i in range(10):
#     print(i)


# nums=[1,2,3,4,5]
#
# for val in nums:
#     print(val)


# nums=[1,4,9,16,25,36,49,64,81,100]
#
# for i in nums:
#     print(i)

# nums=(1,4,9,16,25,36,49,64,81,100,25)
# x=25
# idx=0
# for i in nums:
#     if (i==x):
#         print("found indx of",idx)
#     idx+=1


# for i in range(1,10):
#     print(i)

# for i in range(2,101,2):
#     print(i)

# for i in range(1,101,2):
#     print(i)


# for i in range(1,101):
#     print(i)


# for i in range(100,0,-1):
#     print(i)

# n=int(input("Enter the number:"))
# for i in range(1,11):
#     print(n*i)


# for i in range(5):
#     pass
# print("some useful work")

# n=5
# sum=0
#
# for i in range(1,n+1):
#     sum+=i
#
# print("total sum is",sum)

# n=7
# sum=0
# i=1
# while i<=n:
#     sum += i
#     i+=1
# print("total sum is",sum)

# n=3
# fact=1
#
# for i in range(1,n+1):
#     fact*=i
#
# print("total sum is",fact)


# i=1
# while i<=5:
#     print(i)
#     i+=1
#
# print("Loop End")

# i=1
# while i<=100:
#     print(i)
#     i+=1
# print("loop ended")

# i=100
# while i>=1:
#     print(i)
#     i-=1
# print("loop end")


# n=int(input("Enter the number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
#
# print("loop end")


# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1
# print("loop end")

# nums=[1,4,9,16,25,36,49,64,81,100]
# x=36
# i=0
# while i<len(nums):
#     if (nums[i]==x):
#         print("found x",i)
#     i+=1
#
# print("loop end")

# i=0
# while i<=10:
#     if (i%2==0):
#         print(i)
#     i+=1
#
# print("loop end")

# i=0
# while i<=10:
#     if (i%2!=0):
#         print(i)
#     i+=1
# print("end loop")

# i=0
# while i<=10:
#     print(i)
#     if (i==3):
#         break
#     i+=1
# print("end loop")


# i=0
# while i<=10:
#     if (i==3): # 3 value is going to be skip
#         i+=1
#         continue
#     print(i)
#     i+=1
#
#
# print("loop end")

# for i  in range(10):
#     print(i)

# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# for i  in range(1,10,2):
#     print(i)

# for i  in range(10,0,-2):
#     print(i)

# n=int(input("Enter the number:"))
# for i in range(1,11):
#     print(n*i)

# n=[1,4,9,16,25,36,49,64,81,100]
# for i in n:
#     print(i)

# n=(1,4,9,16,25,36,49,64,81,100,25)
# x=25
# idx=0
# for i in n:
#     if (i==x):
#         print("found idx of",idx)
#     idx+=1

# n=4
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("total fact is",fact)

# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
#
# cal_sum(4,2)

# def cal_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
#
# cal_avg(80,90,70)

# names=["thore","spiderman","shaktiman","ironman","superman"]
# cities=["Delhi","Pune","Hyderabad","Bengaluru","Chennai"]

# def  fun_len(list):
#     print(len(list))
#
# fun_len(names)
#
# def fun_list(list):
#     for items in list:
#         print(items,end=" ")
#
# fun_list(cities)
# fun_list(names)


# def cal_fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(fact)
#
# cal_fact(5)

# def convertor(usd_val):
#     inr_val=usd_val*83
#     print(usd_val,"USD=",inr_val,"INR")
#
# convertor(20)

# num=int(input("Enter the number:"))

# def cal_sum(num):
#     if (num%2==0):
#         print("Even")
#     else:
#         print("Odd")
#
# cal_sum(3)


#recurssion

# def cal_sum(n):
#     if (n==0):
#         return 0
#     return cal_sum(n-1)+n
# sum=cal_sum(10)
# print(sum)

# def fact(n):
#     if (n==0 or n==1):
#         return  1
#     else:
#         return n*fact(n-1)
# print(fact(3))

#recursive function
# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n* fact(n-1)
#
# print(fact(2))

# f=open("E:\Pooja\Python\Sample.txt",'r')
# data=f.readline()
# # f.write("I am learning Python\n")
# # f.write("I am learning Java\n")
# # f.write("I am learning JavaScript")
# print(data)
# f.close()

# f=open("E:\Pooja\Python\Sample.txt",'r+')
# f.write("abc")
# f.close

# f=open("E:\Pooja\Python\Sample.txt",'a+')
# f.write("abc")
# f.close

# with open("E:\Pooja\Python\Sample.txt",'r') as f:
#     data=f.read()
#     print(data)

# with open("E:\Pooja\Python\Sample.txt",'w') as f:
#     f.write("new data")

# import os
# os.remove("E:\Pooja\Python\Sample.txt")

# f=open("E:\Pooja\Python\practice.txt","w")
# f.write("Hi Everyone\n we are learning file i/o\n using java\n i like programming in java")
# f.close

# f=open("E:\Pooja\Python\practice.txt","r")
# data=f.read()
# new_data=data.replace("java","Python")
# print(new_data)
# f.close
#
# with open("E:\Pooja\Python\practice.txt","w") as f:
#     f.write(new_data)


# word="learning"
# with open("E:\Pooja\Python\practice.txt",'r') as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")




















































































































































































































































































































































































































































































































































































































































































































