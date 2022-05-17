# WAP to create a collection of username and password.
# If username and password are input correctly by user according to the collected list print welcome.
# Else print Username and password incorrect.
# import sys
# users = [
#     ['user1', '12345'],
#     ['user2', '123456'],
#     ['user3', '1234567'],
#     ['user4', '12345678'],
# ]
# username = input("Enter Username: ")
# password = input("Enter Password: ")
#
# for user in users:
#     if username == user[0]:
#         if password == user[1]:
#             print(f'Welcome {username}')
#             sys.exit()
#         else:
#             print('Wrong Password')
#             sys.exit()
#     else:
#         if password == user[1]:
#             if username == user[0]:
#                 print(f'Welcome {username}')
#                 sys.exit()
#             else:
#                 print('Wrong username')
#                 sys.exit()
#
# print('Wrong username and password')

# -------Sir Method-------

# users = [
#     ['user1', '12345'],
#     ['user2', '123456'],
#     ['user3', '1234567'],
#     ['user4', '12345678'],
# ]
# username = input("Enter Username: ")
# password = input("Enter Password: ")
# total_users=len(users)
# i=0
# login_success=False
# while i<total_users:
#     uname=users[i][0]
#     upass=users[i][1]
#     if username == uname and password == upass:
#         login_success = True
#     i+=1
#
# if login_success:
#     print(f'Welcome {username}')
# else:
#     print('Username and password incorrect')

