# Task 1

class Person():
    def __init__(self, _first_name, _last_name, _age: int):
        self._first_name = _first_name
        self._last_name = _last_name
        self._age = _age

    def talk(self):
        print('Hello my name is ' + self._first_name +' '+ self._last_name +' im '+ self._age +' years old')

p1 = Person('Carl', 'Johnson', '25')
p1.talk()


# Task 2

class Dog():
    def dog_factor(self, dog_factor: int):
        self.dog_factor = dog_factor
        dog_factor = 7

    def __init__(self, dog_age: int):
        self.dog_age = dog_age
        dog_age = 10

    def human_age(self):
        return





