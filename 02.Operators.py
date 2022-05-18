# Arithmetic operators : +,-,*,/,//.**
# x = 5
# y = 2
# x += 2
# z = x % y  # Modulus operator gives Remainder value
# print(x)
# print(z)
# print(100/0)
# print(2**4)
# print(28/5)
# print(28//5)

# Assignment Operator
x = 10
x += 20
print(x)

# Logical Operators : and,or,not

# Comparison Operators : ==,<=,>=,!=
print(5 < 10)

# Bitwise Operators : &,|,!,^

# Special Operators
# Identity Operators : is,is not
# Membership Operators : in,not in
x = 5
y = 20
z = x
print(x is y)
print(x is not y)
print(x is z)

print(id(x))
print(id(y))
print(id(z))

# name = 'Mandeep'
# print('a' in name)
# print('x' in name)
# print('e' not in name)

# p=int(input("Enter value of p: "))
# t=int(input("Enter value of t: "))
# r=int(input("Enter value of r: "))
# s=p*t*r
# print(s)

name = input("Enter name of Student: ")
nep = int(input("Enter score of Nepali Subject: "))
eng = int(input("Enter score of English Subject: "))
math = int(input("Enter score of Math Subject: "))
sci = int(input("Enter score of Science Subject: "))
sco = int(input("Enter score of Social Subject: "))
total = nep + eng + math + sci + sco
percentage = (total / 5)
print(total)
print(percentage)
