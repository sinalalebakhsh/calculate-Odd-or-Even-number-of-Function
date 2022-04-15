def import_os():
    import os
    os.system('cls')
import_os()

def list_builder():
    user_input = input('Write your word:')
    list_words = []
    while user_input != 'finish':     
        list_words.append(user_input)
        user_input = input('Write your word:')
    return list_words
    
def average_calculator(list_exp):
    all_words = 0
    for word in list_exp:
        all_words += len(word)
    return all_words / len(list_exp)

user_input_words = list_builder()

print(average_calculator(user_input_words))

#محاسبه گر میانگین با استفاده از تعریف تابع
