# Types of functions:
# 1. Inbuilt functions
# 2. User-defined function

# Inbuilt functions:
# 1.abs()
# 2.pow()
# 3.max()
# 4.min()
# 5.round()

# print(dir(__builtins__))

# User-defined function:
# def my_function():
#     print('Hello World!')  # function body
#
#
# my_function()
# my_function()  # call function


# parameters example:
# def users(name, age, address):
#     print('Hello', name)
#     print('You are', age, 'years old')
#     print('You live in', address)
#
#
# users('John', 32, 'NewYork')


# def add(x,y):
#     print(x+y)
#
#
# add(40,50)
# add(70,80)


# Optional parameters
# def add(x, y=10):
#     print(x + y)
#
#
# add(40)


# *args and **kwargs are array arguments and keyword arguments
# def users(*names, **data):
#     print(names)
#     print(data)
#
#
# users("John", "Mary", "Peter", name="John", age=30, address="NewYork")


# def test():
#     print("Hello World!")
#
#
# def get():
#     test()
#
#
# get()


# Return type function
# def add(x, y):
#     return x + y
#
#
# print(add(20, 30))


# def add(x, y):
#     return x + y
#     return x - y
#
#
# print(add(20, 30))


# def users():
#     pass
#
#
# print(users())


# def add_sub(x, y):
#     add = x + y
#     sub = x - y
#     return [add, sub]
#
#
# print(add_sub(30, 20))


# x = 10
#
#
# def test():
#     global x
#     x += 30
#     print(x)
#
#
# test()
# print(x)


# incline function:
# a = lambda x, y: x + y
# print(a(20, 30))
#
# Both give same output
# def a(x, y):
#     return x + y
#
#
# a(20, 30)


# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
#
#
# print(fac(5))
# 5-1:4 =20
# 4-1:3 =60
# 3-1:2 =120


# Recursive function
# def fac(n):
#     if n==1:


# Nested Function:
# def users():
#     def name():
#         return "I am Mandeep"
#
#     return name
#
#
# a = users()
# print(a())


# def users():
#     def name(new_name):
#         return f"I am {new_name}"
#
#     return name
#
#
# a = users()('Mandeep')
# print(a)
# print(users()("ram"))
# a = users()
# print(a())
# print(type(a))


# def users():
#     yield 'ram'
#     yield 'shyam'
#     yield 'hari'
#
#
# a = users()
# print(a.__next__())
# print(a.__next__())
# for i in a:
#     print(i)

#
# def connection():
#     """
#     This is a connection function used to connect to the database
#     """
#     return True
#
#
# print(connection.__doc__)


# Inbuilt functions
# print()
# len()
# id()
# type(): int,list,dict,str,tuple,set,frozenset,bool,float,complex
# help()
# input()
# dir()
# range()
# globals()

# print(dir(__builtins__))

# zip()

data = [12, 34, 56, 67, 99]
data1 = [67, 364, 566, 667, 'ram']
d1 = list(zip(data, data1))
print(d1)
# for a in d1:
#     print(a)
# print(type(d1))
# print(data+data1)
