# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open('Task_3.txt', 'r') as f:
    employees = f.readlines()
    poor_employees = []
    sum_salary = 0
    for employee in employees:
        name, salary = employee.split(' : ')
        if int(salary) < 20000:
            poor_employees.append(name)
        sum_salary += int(salary)

print(f'Сотрудники, у которых оклад менн 20 тыс. руб.: {poor_employees}\n'
      f'Средняя заработная плата сотрудников: {round(sum_salary/len(employees))} тыс. руб.')
