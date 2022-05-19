# # Declare a class
# class Introduction:
#     # Body part of class
#     x = 10
#
#     def test(self):
#         pass
#
#
# # Declare an object: instance of the class
# obj = Introduction()
# # access the object
# print(obj.x)
# print(obj.test())
#
#
# class Students:
#     pass
#
#
# obj = Students()
# obj.name = 'John'
# obj.age = 10
#
# print(obj.name)
# print(obj.age)


# class Students:
#     def name(self, name):
#         print(f'Student name is {name}')
#
#     def age(self, age):
#         print(f'Student age is {age}')
#
#
# obj = Students()
# obj.name = 'John'
# obj.age = 10
# obj.name = 'Sita'
# obj.age = 12


# class User:
#     name = 'Sophia'
#
#     def get_name(self):
#         print(self.name)
#         print(self.age)
#
#     def age(self):
#         return 15
#
# obj = User()
# obj.get_name()


class Introduction:
    total = 0

    def __init__(self, name, age):
        print(name, age)
        self.total += 1


obj = Introduction('John', 20)
obj1 = Introduction('Sita', 20)
obj2 = Introduction('Gita', 20)
obj3 = Introduction('Hari', 20)

print(obj3.total)
