# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def first_func(name, surname, year, city, email, telephone):
    return print(', '.join([name, surname, year, city, email, telephone]))


first_func(surname='Anp', name='Aleks', year='1991', city='SPb', email='ololo@mail.ru',
           telephone='8-999-777-66-66')
