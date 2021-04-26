class Addition() :
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s) :
        self.first = f
        self.second = s

    def result(self):
        print('Enter First No. : ', self.first)
        print('Enter second No.: ', self.second)
        print('After Addition: ', self.answer)

    def Calc(self) :
        self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
A = Addition(100, 200)
A.Calc()                # perform Addition
A.result()              # display result