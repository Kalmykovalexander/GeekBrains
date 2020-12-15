from itertools import groupby
from sys import argv

# 1
script_name, work_hours, salary_per_hour, bonus = argv

# work_hours = int(input('Введите полные отработанные часы сотрудника: '))
# salary_per_hour =int(input('Введите почасовую ставку сотрудника: '))
# bonus = int(input('Введите значение премии сотрудника: '))
# monthly_salary = (work_hours * salary_per_hour) + bonus
# return f'(work_hours * salary_per_hour) + bonus: {monthly_salary}'

print('Имя скрипта:', script_name)
print('Полные отработанные часы сотрудника:', work_hours)
print('Часовая ставка сотрудника:', salary_per_hour)
print('Полные отработанные часы сотрудника:', bonus)
print('Заработная оплата сотрудника в месяц:', (work_hours * salary_per_hour) + bonus)

# 2
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el-1]]
# print(new_list)

# 3
# my_list = [el for el in range(20, 240) if el % 21 == 0]
# print(my_list)

# 4
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list = []
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)
