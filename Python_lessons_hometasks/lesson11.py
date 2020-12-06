# task 1

class Person():
    def __init__(self, first_name, last_name, birthday, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.phone = phone
        self.email = email

    def add_teacher(self):
        pass

    def add_students(self):
        pass

class Student(Person):
    pass
class Teacher(Person):
    def __init__(self, salary):
        self.salary = salary
    def add_salary(self):
        pass


# Task 2

class Mathematician:

    def square_num(self, numbers):
        return [num ** 2 for num in numbers]

    def remove_positives(self, numbers):
        return [num for num in numbers if num < 0]

    def filter_leaps(self, years):
        return [year for year in years if years % 4 == 0]

m = Mathematician()
m.square_num(7, 11, 5, 4)
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

Mathematician.filter_leaps()
Mathematician.remove_positives()
Mathematician.square_num()


# task 3
class Product:

    def __init__(self, type_of_product, name, price):
        self.type = type_of_product
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __hash__(self):
        return hash(f'{self.type}-{self.name}')

    def __eq__(self, other):
        return self.name == other.name \
               and self.type == other.type == self.price == other.price

class ProductStore:

    def __init__(self):
        self._products = dict()
        self._prices = dict()
        self._discount_by_name = dict()
        self._discount_by_type = dict()
        self._earn = 0
        self.__products = set()

    def add(self, product: Product, amount: int):

        current_amount = self._products.get(f'{product.type}-{product.name}', 0)
        self._products[f'{product.type}-{product.name}'] = current_amount + amount
        current_price = self._prices.get(f'{product.type}-{product.name}')

        if not current_price:
            self._prices[f'{product.type}-{product.name}'] = amount * 1.3
        self.__products.add(product)

    def set_discount(self, name_or_type, percent, identifier_type = 'name'):
        if identifier_type == 'name':
            self._discount_by_name[name_or_type] = percent
        else:
            self._discount_by_type[name_or_type] = percent

    def sell_product(self, type_of_product, name, amount):

        product_key = f'{type_of_product}-{name}'

        if product_key not in self._products:
            raise Exception('Такого продукта нет')
        if amount > self._products[product_key]:
            raise Exception(f'Недостаточно продуктов, имеется: {self._products[product_key]} штук')

        discount_by_name = self._discount_by_name.get(name, 0)
        discount_by_type = self._discount_by_type.get(type_of_product, 0)
        discount = discount_by_name or discount_by_type or 2
        total_price = self._prices[product_key] * amount
        total_price = total_price - total_price * discount / 100
        self._earn += total_price
        return total_price

    def get_income(self):
        return self._earn

    def get_all_products(self):
        return [
            (product, self._products[f'{product.type}-{product.name}'])
            for product in self.__products
        ]

    def get_product_info(self, type_of_product, name):
        amount = self._products.get(f'{type_of_product}-{name}')
        return type_of_product, name, amount


p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)
p3 = Product("Sport", "Rasd", 23)
product_store = ProductStore()
product_store.add(p, 10)
product_store.add(p2, 300)
product_store.add(p3, 20)



# task 4

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__()
        with open('logs.txt', 'a') as f:
            f.write(f'{msg}\n')