class Person :
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, My name is:', self.name)

p=Person('Anirudh')
p.say_hi()