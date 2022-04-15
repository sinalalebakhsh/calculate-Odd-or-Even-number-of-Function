
def import_os():
    import os
    os.system('cls')
import_os()

def calc_odd_even_num(number):
    result = number % 2 == 0
    return result
    
input_number = int(input('Enter Your number: '))

print(calc_odd_even_num(input_number))


