from logic import Logic
from interface import Interface

Interface.greetings()

while not Logic.comparison():
    Interface.print_main_interface()
    char = input('Введите возможную букву: ')
    if  Logic.len_check(char) and Logic.ord_check(char) :
        Logic.check_input(char)
        print(Logic.word_lst)
        if Logic.word_lst == Logic.word_try_lst:
            print("Поздравляю, вы победили! ")
            break
    else:
        print('\n')
        print('Вы ввели неправильный символ, используйте кириллицу ')
    
   

if Logic.comparison():
    print('Вы проиграли :(')
    Logic.print_word()