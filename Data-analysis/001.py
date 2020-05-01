# birth_year = input('Birth year:')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# weight_lbs = input('Weight (lbs):')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

#string
# course = "Python's Course for Beginnners"
# print(course)

# course = '''
# 哈哈哈，你好呀
#    甜豆儿今天去打疫苗了
# '''
# print(course)

# course = "Python's Course for Beginnners"
# another = course[:]
# print(another)
# print(another[1:-1])

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg)

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('o'))
# print(course.replace('Beginners','Absolute Beginners'))
# print('python' in course)
# print(course.title())

# x = 2.9
# print(round(2.9))
# print(abs(-x))

# import math
# print(math.floor(2.9))

# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a cold day")
#     print("wear warm clothes")
# elif is_cold:
#     print("It's a hot day")
#     print("Drink plenty of water")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# has_high_income = False
# has_good_credit = True
# if has_good_credit and not has_high_income:
#     print("Eligible for loan")

# temperature = 35
# # if temperature >30:
# #     print("It's a hot day")
# # else:
# #     print("It's not a hot day")

# weight = int(input("Weight:"))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} lbs")

# i = 1
# # while i<=5:
# #     print(i)
# #     i=i+1
# # print("Done")
# while i<=5:
#     print('*'*i)
#     i=i+1
# print("Done")

#猜数字
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#    guess = int(input('Guess: '))
#    guess_count += 1
#    if guess == secret_number:
#        print("You win!")
#        break
# else:
#     print("Sorry,You are failed")

#for loop
# for item in ['Python','John','dangdang']:
#     print(item)
# for item in range(5,10):
#     print(item)

# prices = [10,20,39]
# total = 0
# for price in prices:
#     total += price
# print(f"Total:{total}")

#Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

# numbers = [5,2,5,2,2]
# for x_count in numbers:
#     print('x' * x_count)

#List
# names = ['John','BOb','Mosh']
# print(names[-1])

# numbers = [3,6,2,8,4,10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

#2DList
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][1])

#list method
# numbers = [5,3,2,34,4]
# numbers.insert(0,10)
# numbers.append(10)
# print(50 in numbers)
# print(numbers.count(2))
# print(numbers.sort())
# numbers.reverse()
# print(numbers)

# numbers = [2,2,4,6,3,4,6,1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

#Tuples(元组)不可再分割
# numbers = (1,2,3)
#numbers[0]=3   出错
# print(numbers[0])

#unpacking(开箱)
# coordinates = (1,2,3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x,y,z=coordinates
# print(x)

#dictionary
# customer = {
#     "name":"John Smith",
#     "age":30,
#     "is_verified":True
# }
# print(customer["name"])
# customer["name"] = "Jack Smith"
# print(customer.get("birthday","1996-09-10"))

# phone = input("Phone: ")
# digits_mapping = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }
# output = ""
# for ch in phone:
#     #数字字典中没有的用！来代替
#     output += digits_mapping.get(ch,"!")+" "
# print(output)

#emoji converter 表情 windows下无法打印表情包
# message = input(">")
# words = message.split(' ')

#Functions
# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard')
# print('Start')
# greet_user()
# print('Finish')

#Funtions and Parameters
# def greet_user(name):
#     print(f'Hi {name}!')
#     print('Welcome aboard')
# print("Start")
# greet_user("John")
# greet_user()

#keyword argument
# def spare(number):
#     return number * number
#     return None
# print(spare(3))

#class
# class Point:
#     def move(self):
#        print("move")
#     def draw(self):
#         print("draw")
# point1 = Point()
# point1.x=1
# point1.draw()
# print(point1.x)

#Constructor
# class problem:
#     name = 'dangdang'
#     price = 18
#     def add(self,x,y):
#         print(self.name)
#         result = x + y
#         print(result)
#     def minus(self,x,y):
#         result = x - y
#         print(result)

# class Person:
#     def talk(self):
#         print("talk")
# john = Person()
# john.talk()

# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.n = name
#     def talk(self):
#         print("Hi,I am %s" % self.n)
#         print(f"Hi,I am {self.name}")
# bob = Person("李小康")
# print(bob.talk())

#继承
# class Mammal:
#     def walk(self):
#         print("walk")
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
# class Cat(Mammal):
#     pass
# dog1 = Dog()
# dog1.walk()
# dog1.bark()


# from converter import lbs_to_kg,kg_to_lbs
# kg_to_lbs(29)
# print(kg_to_lbs(40))

# numbers = [10,2,3,7,8]
# # print(max(numbers))

#引入模块
# import ecommerce.shipping as es
# es.calc_shipping()

# from ecommerce.shipping import  calc_shipping
# calc_shipping()

#Generating Random Value
#随机数
# import random
# for i in range(3):
#      print(random.randint(10,20))

# import random
# members = ['John','Mary','Bob']
# leader = random.choice(members)
# print(leader)

# import random
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first,second
# dice = Dice()
# print(dice.roll())

#Files and Directories
from pathlib import Path
#Absolute path
#relative path
#s是否是路径
#path = Path("fr")
#print(p ath.mkdir())

# path = Path()
# for file in path.glob('*.py'):
#     print(file)

path = Path()
for file in path.glob('*.py'):
    print(file)