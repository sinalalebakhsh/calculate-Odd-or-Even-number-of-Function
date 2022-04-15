def import_os():
    import os
    os.system('cls')
import_os()

def check_min_max_list(list_number):
    min_list = min(list_number)
    max_list = max(list_number)
    return min_list, max_list

list_numberssss = [1, 2, 3, 4, 5, 6, 7, 8]

minimom_number, maximom_number = check_min_max_list(list_numberssss)

print(minimom_number)
print(maximom_number)
