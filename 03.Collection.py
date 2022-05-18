# Variable holds 1 value at a time.
# Collection is used to store more than 1 value at a time.
# Different types of Collection are: List, Tuple, Set, Dictionary.
x = [1, 3, 5, 6, 7, 8]
# This is a list . It is enclosed in a square bracket.
print(x)
print(x[2])
x.append(10)
# Append adds value in the end of the list.
print(x)
x.insert(0, 20)
# Insert is used to add value in between the list.
print(x)
x.remove(20)
print(x)
print(len(x))
y = x.copy()
print(y)
name = "Mandeep"
age = 25
print(f"My name is {name} age {age}")
