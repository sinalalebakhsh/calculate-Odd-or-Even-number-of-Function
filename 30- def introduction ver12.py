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

input_text = input('Write your text: ')

input_text = input_text.split(' ')

list_number = []

for s in input_text:
    list_number.append(len(s))

print(check_even_in_list(list_number))
