def import_os():
    import os
    os.system('cls')
import_os()

def find_length_string_list(exp_str):
    counter_char = 0
    for s in exp_str:
        counter_char += 1
    return counter_char

def find_even_number(list_number):
    even_number_list = []
    counter_even_number = 0
    for s in list_number:
        if s % 2 == 0:
            even_number_list.append(s)
            counter_even_number += 1
    return even_number_list, counter_even_number,find_length_string_list(list_number)

result_even_list , result_counting_even, length_orginal_list = find_even_number([1,2,3,4,5,6,7,8])

print(f'result even list:{result_even_list}')
print(f'result counting even number:{result_counting_even}')
print(f'length orginal list: {length_orginal_list}')


