# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input('Введите сумму чисел X и Y:  '))
P = int(input('Введите произведение чисел X и Y:  '))
for x in range(S):
    for y in range(P):
        if S == x + y and P == x * y:
            print(f'Искомые числа: X = {x}, Y = {y}')