# Task 1

def task1():
    with open('myfile.txt', 'w') as myfile:
        myfile.write('Hello file world.\n')


def task1_part2():
    with open('myfile.txt', 'r') as myfile:
        read_myfile = myfile.read()
        print(read_myfile)
    try:
        with open('C:\\myfile.txt', 'r') as myfile2:
            read_myfile2 = myfile2.read()
            print(read_myfile2)
    except FileNotFoundError as filenotfound:
        print(f'File not found! {filenotfound}')


# Task 2

g

