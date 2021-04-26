class Default() :
    def __init__(self) :        # default constructor
        self.country = 'India'

    def print_country(self):    # a method for printing data members
        print(self.country)

A = Default()                   # creating object of the class
A.print_country()               # calling the instance method using the object obj