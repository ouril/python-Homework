import os
import sys
import psutil # модуль для управлением процессами (внешний, требует установки)
import shutil   # модуль для манипуляией с файлами

# функции для дальнейшей программы которые не обращаются к переменным модуля

def help_list():
    # словарь с инструкциями
    help_list = {
                'q   ': 'выход',
                's   ': 'данные о системе',
                'ls  ': 'содержимое текущей папки',
                'pd  ': 'список процессов',
                'c   ': 'копирование файла',
                'd   ': 'улаление файла',
                'help': 'справка'
    }
    # цикл для пербора ключей
    for key in help_list.keys():
        print("{0} - {1}".format(key, help_list[key]))

def ls():
    for i in os.listdir():
        print(i)

def mycopy():
    ls()
    target = str(input("Введите имя файла для копирования: "))
    name_new = str(input("Имя нового файла: "))
    shutil.copy(target, name_new)
    ls()

def mydel():
    ls()
    target = str(input("Введите имя удаляемого файла: "))
    os.remove(target)
    ls()

# сама программа

log = input("Password!\n")

while log:
    if log == "password":
        print("Давайте поработаем\n")
        break
    else:
        log = input("Password!\n")
help_list()

doing = 'a'

# цикд самой программы
while doing:

    doing = str(input("\nВведите команду\n>> "))
    print()

    if doing == "s":
        print("Платформа ОС " , sys.platform)
        print("Кодировка файловой системы ", sys.getdefaultencoding())
        print("Имя текущего директория " , os.getcwd())
    elif doing == "ls":
        ls()
    elif doing == "pd":
        print(psutil.pids())
    elif doing == "q":
        print("EXIT!")
        break
    elif doing == "c":
        mycopy()
    elif doing == "d":
        mydel()
    elif doing == "help":
        help_list()
    else:
        print("?")
