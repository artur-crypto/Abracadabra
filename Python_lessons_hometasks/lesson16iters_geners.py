# Task 1


def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start+i, iterable[i]


party = ['beer', 'cigarettes', 'vodka']
enumerate_party = with_index(party, 10)

print(list(enumerate_party))


# Task 2

def in_range(start, end=None, step=1):

    if not end:
        start, end = 0, start

    while True:
        if step > 0 and start >= end:
            break
        elif step < 0 and start <= end:
            break
        elif step == 0:
            return

        yield start

        start += step


list_num = in_range(2, -10, 0)

for num in list_num:
    print('num', num)

# Task 3

class Iterable:
    def __init__(self, *arg):
        first, second = arg

        self.current = first - 1
        self.second = second

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.second:
            return self.current
        raise StopIteration


for i in Iterable(3, 9):
    print(i)


def iterable(first, second):
    current = first
    while current < second:
        yield current
        current += 1


for i in iterable(3, 9):
    print(i)