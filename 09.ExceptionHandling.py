# print(10/0)

# try:
#     print(10/0)
# except Exception as e:
#     print('Exception', e)
#
# finally:
#     print('Finally')


def add(x, y):
    if y == 0:
        raise ZeroDivisionError('y cannot be zero')
    return x + y


try:
    print(add(10, 0))
except ZeroDivisionError as e:
    print('Exception', e)

