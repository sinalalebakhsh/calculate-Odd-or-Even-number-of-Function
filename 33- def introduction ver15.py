from operator import truediv


def import_os():
    import os
    os.system('cls')
import_os()

def find_even(number):
    if number % 2 == 0:
        return True
    return False

def find_odd(number):
    if number % 2 != 0:
        return True
    return False


def finder(list_number):
    list_even = []
    list_odd = []
    for s in list_number:
        if find_even(s):
            list_even.append(s)
        elif find_odd(s):
            list_odd.append(s)
    return list_even, list_odd

list_of_number = [1,2,3,4,5,6,7,8,9,10]

finded_even, finded_odd = finder(list_of_number)

print(f'list of even: {finded_even}')
print(f'list of  odd: {finded_odd}')
