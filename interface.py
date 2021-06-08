from logic import *
import os

path = os.getcwd()+'\\figures\\'
    
class Interface:
    
    @classmethod
    def greetings(cls):
        print('Давай поиграем в игру "Виселица"? Надо угадать слово.\nУ тебя есть 7 попыток, постарайся не стать виновным в смерти человека :)')

    @classmethod
    def print_main_interface(cls):
        out = " ".join(Logic.word_try_lst)
        print('Слово: '+ out )
        Interface.print_visilica()
        print(f'Ошибки ({Logic.num_of_errors}): {Logic.error_list}')
        print(f"У вас осталось ошибок: {Logic.error_last}")

    @classmethod
    def print_visilica(cls):
        file = open(path+str(Logic.num_of_errors)+'.txt','r')
        visilica = file.read()
        file.close()
        print(visilica)


        