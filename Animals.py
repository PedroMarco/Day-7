class Animal:
    def __init__(self, name = 'pepe'):    # Constructor of the class. Defined self as "name". Pepe would be the name if no name is defined
        self.name = name

class Cat(Animal):  # This will mean that what we enter instead of "animal" will be taken as "name"
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat(),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

for whatever in animals: # I say whatever because is just a name for the range in for - in defined in the animals list
    print ((whatever.name), ': ', whatever.talk())

# prints the following:
#
# Missy: Meow!
# Mr. Mistoffelees: Meow!
# Lassie: Woof! Woof!
