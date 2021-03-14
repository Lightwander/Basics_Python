# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

from itertools import count

with open('Task_2.txt', 'r') as f:
    line = f.readlines()
    print(f'Всего строк в файле: {len(line)}')
    for line_number, text in enumerate(line):
        print(f'В строке {line_number+1} содержится {len(text.split())} слов')
