# import introduction
#
# print(introduction.test())
# print(introduction.get_students())


# import introduction as intro
#
# print(intro.test())
# print(intro.get_students())
# print(dir(intro) )


# from introduction import get_students, test
# print(test())
# print(get_students())


# from introduction import *  # * means all modules
# print(test())


# def run():
#     import introduction
#     print(introduction.get_students())
#
#
# run()


# print(__file__)
#
# print(__name__)
#


# import introduction
# if __name__ == '__main__':
#     print('main')


# import lib.demo
#
# print(lib.demo.get_demo())


# from lib.demo import get_demo
#
# print(get_demo())

from lib import *

print(demo.get_demo())
print(db.connection())
