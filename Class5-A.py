#Multiple Inheritance
class Base1(object) :
    def __init__(self) :
        self.str1 = 'Samsung'
        print('Base1')


class Base2(object) :
    def __init__(self) :
        self.str2 = 'Apple'
        print('Base2')


class Derived(Base1, Base2) :
    def __init__(self) :

        Base1.__init__(self)        #Calling Constructors of Base1 and Base2
        Base2.__init__(self)
        print('Derived')


    def printstr(self) :
        print(self.str1, self.str2)


ob = Derived()
ob.printstr()