import os
import sys
import psutil

log = input("Password!\n")

while log:
    if log == "password":
        print("Давайте поработаем\n")
        break
    else:
        log = input("Password!\n")

print("[0] - Выход;")
print("[1] - Выводить данные о системе;")
print("[2] - Выодить список процессов;")
print("[3] - Вывусти PID процессов.")

doing = 4
while doing:
    doing = int(input("Введите номер функции: "))

    if doing == 1:
        print("Платформа ОС " , sys.platform)
        print("Кодировка файловой системы ", sys.getdefaultencoding())
        print("Имя текущего директория " , os.getcwd())

    elif doing == 2:
        print(os.listdir())

    elif doing == 3:
        print(psutil.pids())

    elif not doing:
        print("EXIT!")
        break

    else:
        print("?")
