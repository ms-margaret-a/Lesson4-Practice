# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами

from sys import argv

name, hours, pay, bonus = argv
try:
    hours = int(hours)
    pay = int(pay)
    bonus = int(bonus)
    calculation = hours * pay + bonus
    print(f'Ваша зарплата:  {calculation}')
except ValueError:
    print('Введите число')