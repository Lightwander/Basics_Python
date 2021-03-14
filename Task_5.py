# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce


def numerator():
    try:
        numbers = input('Введите числа через пробел: ')
        with open('Task_5.txt', 'w+') as f:
            f.writelines(numbers)

        with open('Task_5.txt', 'r') as f:
            some_num = [float(el) for el in f.readline().split(' ')]
        print(f" Сумма введенных чисел = {reduce((lambda a, b: a + b), some_num)}")
    except ValueError:
        print('Вместе с числами введены строки!')


numerator()
