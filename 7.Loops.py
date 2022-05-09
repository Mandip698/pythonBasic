# While Loop : Indefinite Loop
# Print numbers from 1 to 10
# x = 1
# while x < 10:
#     print(x)
#     x += 1
# Also
# x = 1
# while x < 10:
#     print(x, end=',')
#     x += 1

# Print name 5 times
# x = 0
# while x < 5:
#     print('Mandeep')
#     x += 1

# WAP to print even and odd sum
# total_even = 0
# total_odd = 0
# i = 1
# num = int(input("Enter number: "))
# while i <= num:
#     if i % 2 == 0:
#         total_even += i
#     else:
#         total_odd += i
#     i += 1
# print(f"Total even: {total_even}")
# print(f"Total odd: {total_odd}")

# While loop :Definite Loop
# data = ['ram', 'sita', 'hari', 'laxmi']
# x = 0
# while x < len(data):
#     print()
#     x += 1

# For loop
# for a in data:
#     print(a)

# Print 1 to 10 in descending order
# a = 10
# while a > 0:
#     print(a)    #print(a, end=" ")
#     a -= 1

# Stop iteration : break, continue
# break
# x = 1
# while x <= 10:
#     if x == 5:
#         break
#
#     print(x, end=" ")
#     x += 1

# continue
# x = 1
# while x <= 10:
#     x += 1
#     if x == 5:
#         continue
#
#     print(x, end=" ")

# print 1 to 10 except 1,4, and 9.
# x = 1
# while x < 10:
#     x += 1
#     if x == 1 or x == 4 or x == 9:
#         continue
#
#     print(x, end=" ")

#

num = int(input("Enter no. of students: "))
i = 1
students_name = []
while i <= num:
    name = input("Enter name: ")
    students_name.append(name)
    i += 1

print(students_name)
