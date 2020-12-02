# Task 1

class Animal:
    def talk(self):
        return 'voice'

class Dog(Animal):
    def talk (self):
        return 'woof'

class Cat(Animal):
    def talk(self):
        return 'meow'

def do_voice(animal: Animal):
    animal.talk


do_voice(Dog())
do_voice(Cat())


 # Task 3



