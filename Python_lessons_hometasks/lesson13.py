# Task 1
def local_var_num_detect(*args, **kwargs):
    b = 2
    c = 3

    return len(locals())


local_var_num_detect(1, 2, 3, 4, 5, 6, 7)

print(local_var_num_detect.__code__.co_nlocals)


# Task 2

def simple_function():
    msg = 'whats good?'

    def inner_function():
        print(msg)

    inner_function()


simple_function()

# Task 3


def choose_func(numbers: list, func1, func2):
    if all(num > 0 for num in numbers):
        return func1(numbers)
    else:
        return func2(numbers)


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, -2, 3, -4, 5]


def square_numbers(numbers):
    return [number ** 2 for number in numbers]


def remove_negatives(numbers):
    return [number for number in numbers if number > 0]


assert choose_func(numbers1, square_numbers, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(numbers2, square_numbers, remove_negatives) == [1, 3, 5]