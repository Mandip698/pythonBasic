class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Child(Parent):
    def __init__(self, fname, lname, age):
        Parent.__init__(self, fname, lname)
        # super().__init__(fname, lname)
        self.printage = age

    # def welcome(self):
    #     print('Congratulations', self.firstname, self.lastname, f'for your {x.printage}th birthday')


x = Child('Mandeep', 'Panta', 20)
x.printname()
print('Age :', x.printage)
# x.welcome()
