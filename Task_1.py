# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

result_list = [1, 1.2, 'Какой-то текст', True, ['Список', 'в', 'списке'], ('К', 'О', 'Р', 'Т', 'Е', 'Ж')]

for el in result_list:
    print(f'{el} - {type(el)}')
