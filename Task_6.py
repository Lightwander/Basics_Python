# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


def generator_integer(start, stop):
    try:
        for el in count(int(start)):
            if el > int(stop):
                break
            else:
                print(el)
    except ValueError:
        print('Введено не число!')


generator_integer(input('Введите число, с которого стартуем:'),
                  input('Введите число, на котором закончим: '))


def cycle_mod(some_list, count_of_iterations):
    iteraion = 0
    for el in cycle(some_list):
        if iteraion >= count_of_iterations:
            break
        else:
            print(el)
            iteraion += 1


cycle_mod([1, 'fkfkd', 12, 'ew'], 3)
