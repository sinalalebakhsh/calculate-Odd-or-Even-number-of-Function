from traceback import print_tb


def import_os():
    import os
    os.system('cls')
import_os()

def addition_of_numbers(*args):
    result_numbers = 0
    for s in args:
        result_numbers += s
    return result_numbers

print(addition_of_numbers(1,2,3,4,5,6,7,8,9,10))