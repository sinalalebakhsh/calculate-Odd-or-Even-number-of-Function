
def import_os():
    import os
    os.system('cls')
import_os()

def check_even_in_list(list_number):
    count_even = 0
    for s in list_number:
        if int(s) % 2 == 0:
            count_even +=1
    return count_even

list_number = [1,2,3,4,5,6,7,8,9,10]

print(check_even_in_list(list_number))
