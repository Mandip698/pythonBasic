# x = 10
# y = 20
# z = 30
# # nested if else statement
# if x<y:
#     if x>z:
#         print('x is greater than y and z')
#     else:
#         print('z is greater than x and y')
# else:
#     if y>z:
#         print('y is greater than z')
#     else:
#         print('z is greater than x and y')


username = 'admin'
password = '12345'
if username == 'admin':
    if password == '12345':
        print('You are logged in')
    else:
        print('Wrong Password')
else:
    if password == '12345':
        if username == 'admin':
            print('You are logged in')
        else:
            print('Wrong username')
    else:
        print('Wrong username and password')
