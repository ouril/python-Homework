import random

#функция возвращает лист с  10-ю рендомными ислами от 1 до 10
def ranlist():
    return [random.randint(1, 10) for a in range(1, 10)]

first = ranlist()
second = ranlist()
print(a)
print(b)


def rem_list(a, b):
    for i in b:
        while i in a:
            a.remove(i)

rem_list(first, second)

print(a)
