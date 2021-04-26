# program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

class Dog :
    animal = 'dog'

    def __init__(self, breed, color) :
        self.breed = breed
        self.color = color

Jackie = Dog('Huskey', 'White')
Dany = Dog('Shepard', 'Brown')

print('Jackie\'s Details: ')
print('Jackie is a: ',Jackie.animal)
print('Jackie\'s Breed: ',Jackie.breed)
print('Jackie\'s color: ', Jackie.color)

print('\nDany\'s Details: ')
print('Dany is a: ', Dany.animal)
print('Dany\'s Breed: ', Dany.breed)
print('Dany\'s color: ', Dany.color)

print('\nAccessing Class Variables using Class Name')
print(Dog.animal)
