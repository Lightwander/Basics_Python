# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Просим пользователя ввести число.
number = input('Введите число: ')
# Складываем числа в виде строк и переводим их в числовой тип. Суммируем числа.
sum_number = int(number) + int(number*2) + int(number*3)

print(sum_number)
