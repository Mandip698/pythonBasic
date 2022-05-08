# WAP to create a collection of username and password.
# If username and password are input correctly by user according to the collected list print welcome.
# Else print Username and password incorrect.
import sys

users = [
    ['user1', '12345'],
    ['user2', '123456'],
    ['user3', '1234567'],
    ['user4', '12345678'],
]
count = 0
username = input("Enter Username: ")
password = input("Enter Password: ")

for user in users:
    if username == user[0]:
        if password == user[1]:
            print('Welcome')
            sys.exit()
        else:
            print('Wrong Password')
            sys.exit()
    else:
        if password == user[1]:
            if username == user[0]:
                print('Welcome')
                sys.exit()
            else:
                print('Wrong username')
                sys.exit()

print('Wrong username and password')



