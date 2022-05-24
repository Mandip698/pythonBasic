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


x = Child('Mandeep', 'Panta', 10)
x.printname()
print(x.printage)
