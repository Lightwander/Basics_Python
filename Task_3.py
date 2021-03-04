# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

list_seasons = [
    ['Зима', ['12', '1', '2']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]

dict_seasons = dict()
for season, months in list_seasons:
    dict_seasons.update({season: months})

while True:
    month = input('Введите номер месяца: ')
    if month not in sum(dict_seasons.values(), []):
        print('Неправильный месяц!')
        continue
    break

for season, months in list_seasons:
    if month in months:
        print(f'{month}-й месяц года - это {season}')

for season, months in dict_seasons.items():
    if month in months:
        print(f'{month}-й месяц года - это {season}')
