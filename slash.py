# coding=utf-8
# функция считывает строку и решает уравнение заданного вида



def take_drob(exp):

    in_num = False
    count_space = 1
    expl = ['']
    num_expl = 0
    ceil = False
    exp = list(exp)

    for i in exp:

        if in_num:
            if i == ' ' or i == '+':
                if ceil or count_space > 1:
                    in_num = False
                    num_expl += 1
                    expl.append('')

                else:
                    ceil = True
                    count_space += 1
                    expl[num_expl] += i


            elif i == "/":
                count_space = 0
                ceil = True
                expl[num_expl] += i

            else:
                count_space = 0
                expl[num_expl] += i

        else:
            if i.isalnum() or i == '-':
                in_num = True
                ceil = False
                expl[num_expl] += i
                count_space = 0
            else:
                pass
    return expl


# функция завписывающая из целой части в обычную дробь
def trans(listi):
    listl = list(listi)
    sign = 1
    ceil = 0
# если минус то надо его вытащить
    if '-' in listl:
        sign *= -1
        for i in listl:
            if i == '-':
                listl.remove(i)
#если есть целая часть есть и пробел
    if ' ' in listl:
        listC = ''.join(listl)

        listC = listC.split(" ")
        ceil = listC[0]
        drob = listC[1]

    else:
        drob = ''.join(listl)

    drobL = drob.split('/')

    drobL[0] = (int(drobL[0]) + int(drobL[1]) * int(ceil)) * sign
    drobL[1] = int(drobL[1])

    print(drobL)
    return tuple(drobL)


# функция сложения
def sum_drob(list):
    num = 1
    chisl = 0

    for i in list:
        print(i)
        chislit = i[0]
        if num != i[1]:
            chislit *= num
            num *= i[1]
            chisl = chisl * i[1] + chislit
        else:
            num = i[1]
            chisl += chislit

    result = (chisl, num)
    print(result)

    return result


# функция которая превращает получивгшийся картеж  в дробь
def print_drob(tupleD):
    z = 1

    delit = 1
    while(z <= tupleD[1] and z >= 1):
         if tupleD[0] % z == 0 and tupleD[1] % z == 0 and tupleD[1] / z >= 2 and tupleD[0] != 1:
             delit = z
         z += 1

    drob_low = tupleD[1]/delit
    drob_up = tupleD[0]/delit

    if drob_up / drob_low > 1:
        celi = str(int(drob_up/drob_low))
        drob_up = drob_up % drob_low
        result = celi + ' ' + str(int(drob_up)) + '/' + str(int(drob_low))
    else:
        result = str(int(drob_up)) + '/' + str(int(drob_low))
    return result

#print(trans(input()))
#print(sum_drob([(-7, 3), (1, 2)]))



drobs = input("Введите дробьи\n")

rez = take_drob(drobs)
rezalt = []

for i in rez:
    rezalt.append(trans(i))

print(print_drob(sum_drob(rezalt)))













