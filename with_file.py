# coding=utf-8
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"


#Решение : взять часы из одного файла , сравнить с нормой и записать во второй.

import os
import os.path
import decimal

# хороший кроссплатформенный метод указания пути
path = os.path.join('data', "hours_of")
hourLines = []
with open(path, 'r', encoding='UTF-8') as f:
    print(f.read())
with open(path, 'r', encoding='UTF-8') as f:
    hourLines = f.readlines()

HW = {}

norm_of_hours = float(input("Введите норму трудочасов:\n>"))
money_for_full = float(input("Стоимость рабочего часа:\n>"))
for line in hourLines:
    hour_worker = line[:-1].split("\t\t")
    res_hours = float(hour_worker[1])

    if  res_hours < norm_of_hours:
        HW[hour_worker[0]] = str(round(res_hours * money_for_full / norm_of_hours, 2)).split('.')
    elif res_hours > norm_of_hours:
        HW[hour_worker[0]] =  str(round(money_for_full + (res_hours - norm_of_hours) * 2 * money_for_full/norm_of_hours, 2)).split('.')
    else:
        HW[hour_worker[0]] = str(money_for_full).split('.')

path = os.path.join('data', "workers")

with open(path, 'w', encoding='UTF-8') as f:
    for k, v in HW.items():
        f.write("{0}\t\t{1} руб {2} коп \n".format(k, v[0], v[1]))

# Считываем всю информацию из файла в виде списка строк

with open(path, 'r', encoding='UTF-8') as f:
    print(f.read())





