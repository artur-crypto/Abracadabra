class Person():
    def __init__(self, _first_name, _last_name, _age: int):
        self._first_name = _first_name
        self._last_name = _last_name
        self._age = _age

    def talk(self):
        print('Hello my name is ' + self._first_name +' '+ self._last_name +' im '+ self._age +' years old')

p1 = Person('Carl', 'Johnson', '25')
p1.talk()




