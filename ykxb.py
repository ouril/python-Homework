# функция считывает строку и решает уравнение заданного вида
exp = input("Введите уравнение в виде y = kx + b, где k и b - числа:\n")
x = float(input("Введите x:\n"))

k = ''
b = ''
kcount = 0

# цикл читает выражение и находит k и b
for i in exp:
    # пропускаем у = , пробелы и +
    if i == 'y' or i == '=' or i == ' ' or i == '+':
        pass
    # если мы нашли х то значит к найден, отмечаем это в kcount
    elif i == 'x':
        kcount += 1

    else:
        if kcount > 0:
            b = str(b) + str(i)
        else:
            k = str(k) + str(i)

# если к не изменилось, то записать его как 1
if k == '':
    k = 1

y = x * float(k) + float(b)

print(y)