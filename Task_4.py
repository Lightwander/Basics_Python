# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

ru_numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_lesson_4 = []
with open('Task_4.txt', 'r') as f:
    for line in f:
        line = line.split(' ', 1)
        new_lesson_4.append(ru_numbers[line[0]] + ' ' + line[1])

with open('New_task_4.txt', 'w') as f:
    f.writelines(new_lesson_4)
