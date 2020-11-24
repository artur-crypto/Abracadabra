def oops():
    number_list = list(range(1, 10))
    take_number = number_list[10]
    return take_number

def exception_oops():
    try:
        oops()
    except IndexError:
        print('no such index')

exception_oops()


# Task 2

print('****'*30)

def calcul():
    a = input('введите число: ')
    b = input('введите число: ')
    try:
        a = int(a)
        b = int(b)
        print(a ** 2 / b)
    except ZeroDivisionError:
        print('на ноль не делим')
    except ValueError:
        print('введен символ не соответственный')
    else:
        return (a ** 2 / b)

calcul()