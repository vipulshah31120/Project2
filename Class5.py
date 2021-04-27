
# parent class
class Person(object) :
    def __init__(self, name, idnumber) :            # __init__ is known as the constructor
        self.name = name
        self. idnumber = idnumber

    def display(self) :
        print(self.name)
        print(self.idnumber)

#child class
class Employee(Person) :
    def __init__(self, name, idnumber, salary, post) :
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

A = Employee('Andrew', 55875, 700000, 'Technical Head')     #creation of object
A.display()                                                 #calling a function of class