# coding=utf-8
# Домашка за 3-й урок medium
import random
def ranlist():
    return [random.randint(1, 20) for a in range(1, 20)]

# Возвращает скписок из чисел фибоначи с n по m элемент
def  fibonacci(n, m):
    fib = [1, 1]
    for i in range(1, m):
        new = fib[i - 1] + fib[i]
        fib.append(new)
    return fib[n:]


# функция сортировка от мин к макс
def sort_to_max(list):
    for i in range(0, len(list)):
        for j in range(0, len(list)-1):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
    return list


# функция работает как фильтр

def myfilter(define, list):
    new_list = []
    for i in list:
        if define(i):
            new_list.append(i)

    return new_list

# принимает список из кортежей с координатами точек, возвращает True если эти точки - вершины паралелограмма

def isparal(point_list):

    result = False
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0

    for a in point_list:
        if a[0] > max_x:
            max_x = a[0]
        if a[1] > max_y:
            max_y = a[1]
        if a[0] <= min_x:
            min_x = a[0]
        if a[1] <= min_y:
            min_y = a[1]

    center_x = (max_x + min_x) / 2
    center_y = (max_y + min_y) / 2
    center = tuple([center_x, center_y])

    for i in point_list:
        for j in point_list:
            x = (i[0] + j[0])/2
            y = (i[1] + j[1])/2
            maybe_list = tuple([x, y])
            if maybe_list == center:
                result = True

    return result

