# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Решить задачу двумя способами: с помощью re и без.


line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


list_ans = []
j = -1
isFind = False
for i in range(0, len(line)-1):
    if isFind:
        if line[i].islower():
            isFind = False
        elif line[i].isupper():
            list_ans[j] += line[i]

    elif not isFind:
        if line[i].isupper():
            isFind = True
            j += 1
            list_ans.append('')
            list_ans[j] += line[i-1]
            list_ans[j] += line[i]


print(j)
print(list_ans)


import re

p = re.compile(r'[a-z][A-Z]+')
g = p.findall(line)

print(g)



# Задача-2:
# Напишите скрипт заполняющий указанный файл (самомстоятельно задайте имя файла) произвольными целыми
# цифрами, в результате в файле должно быть 2500-значное произвольное число
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле

import os
import random

path = os.path.join('data', 'randomfile')
with open(path, 'w', encoding="UTF-8") as file:
    for i in range(2500):
        file.write(str(random.randint(1, 9)))

with open(path, 'r', encoding="UTF-8") as file:
    line_for_search = file.read()

answer = []
buf = 0
in_collect = False
j = -1


for i in line_for_search:
    if i == buf and not in_collect:
        answer.append("")
        j += 1
        answer[j] += str(i) + str(buf)
        in_collect = True
    elif i == buf and in_collect:
        answer[j] += str(i)
    else:
        in_collect = False
    buf = i
best = [0, 0]
for i in answer:
    if len(i) >= best[0]:
        best[0] = len(i)
        best[1] = i[0]
print(best)


# Задание-3:
# Найдите наибольшее произведение пяти последовательных цифр в
# 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
716362695618826704282524836008"""

def fifth(list):
    buf = 1
    result = 0
    for i in list:
        if i.isdigit():
            result = int(i)* buf
            buf = int(i)
    return result

rezaltnew = [0, 0]

for i in range(len(number)):
    rez = fifth(number[i:i+5])
    if rez > rezaltnew[0]:
        rezaltnew[0] = rez
        rezaltnew[1] = i

print(rezaltnew)




