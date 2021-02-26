# Cпортсмен занимается ежедневными пробежками.
# В первый день его результат составил A километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее B километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22

a, b = 3, 4

Day = 1

while True:
    print(f'{Day}-й день: {a:.2f}')
    if a >= b:
        break
    else:
        a *= 1.1
        Day += 1