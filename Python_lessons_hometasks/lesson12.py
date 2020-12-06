# Task 1

class Animal:
    def __init__(self, name):
        self.name = name
        self._extended = 'ANIMAL'

    def voice(self):
        print(f'I am {self.name}')

    def voice_extended(self):
        print(f'EXTENDED {self.name}, {self._extended}')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(f'talk method {self.name}')

dog = Dog('Sharik')
dog.voice()
dog.voice_extended()



# Task 2

class Author:

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return f'Author("{self.name}", "{self.country}", "{self.birthday}")'

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __eq__(self, other):
        if not isinstance(other, Author):
            return False
        return self.name == other.name and \
               self.country == other.country and \
               self.birthday == other.birthday

class Book:
    def __init__(self, book_name, year, author: Author):
        self.book_name = book_name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'"book name: {self.book_name};' \
               f'year: {self.year};' \
               f'author: {self.author}"'

    def __str__(self):
        return str(f'"book name: {self.book_name};'
                   f'year: {self.year};'
                   f'author: {self.author}"')


class Library:

    TOTAL_BOOKS = 0

    def __init__(self, name: str = "Library"):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, book_name: str, year: int, author: Author):
        book = Book(book_name, year, author)
        self.books.append(book)
        self.authors.append(author)
        Library.TOTAL_BOOKS += 1
        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]


author1 = Author("Donald Trump", "USA", "14.06.1946")
author2 = Author("Nassim Nicholas Taleb", "Lebanon", "11.01.1960")
lib = Library()
lib.new_book("The Art of the Deal", 1987, author1)
lib.new_book("Never give up", 2010, author1)
lib.new_book("Fooled ba Randomness", 2001, author2)
lib.new_book("The Black Swan", 2007, author2)
print(lib.books)
print(lib.group_by_author(author2))
print(lib.group_by_year(2007))
print(lib)
print(Library.TOTAL_BOOKS)



# task 3

class Fraction:

     def __init__(self, fraction):
         if isinstance(fraction, str):
             raise Exception("pass a number")
         self.fraction = fraction

     def __add__(self, other):
         if not isinstance(other, Fraction):
             raise Exception("pass a Fraction")
         return round(self.fraction + other.fraction, 3)

     def __sub__(self, other):
         if not isinstance(other, Fraction):
             raise Exception("pass a Fraction")
         return round(self.fraction - other.fraction, 3)

     def __mul__(self, other):
         if not isinstance(other, Fraction):
             raise Exception("pass a Fraction")
         return round(self.fraction * other.fraction, 3)

     def __divmod__(self, other):
         if   not isinstance(other, Fraction):
             raise Exception("pass a Fraction")
         try:
             return round(self.fraction / other.__dict["fraction"], 3)
         except ZeroDivisionError:
             return "infinitely large number"


x = Fraction(1 / 2)
y = Fraction(1 / 4)
print(x + y)
print(x - y)
print(x * y)
print(x / y)







