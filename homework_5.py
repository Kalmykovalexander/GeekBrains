import re
import json

#1
with open('text.txt', 'a') as f:
    f.write(input('Введите сюда текст: '))

#2
with open("homework_5_task2.txt") as f:
    content = f.readlines()
    print(f'Количество строк состовляет: {len(content)}')
    for id, item in enumerate(content):
        print(f'Количество слов в {id+1} строке состовляет: {len(item.split())}')

#3
with open('homework_5_task3.txt', 'r') as f:
    staff_dict = {el.split()[0]: int(el.split()[1]) for el in f}
    print(f'Средний оклад сотрудников: {sum(staff_dict.values()) / len(staff_dict.values())}\n'
          f'Фамилия сотрудника чей оклад менее 20к: {[key for key, value in staff_dict.items() if value < 20000]}')

#4
with open('homework_5_task4.txt') as f:
    ru_numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open('new_text.txt', 'w') as new_f:
        for i in f:
            if i.split()[0] in ru_numerals.keys():
                new_f.write(i.replace(i.split()[0], ru_numerals.get(i.split()[0])))

#5
with open('homework_5_task5.txt', 'r+') as f:
    f.write(' '.join(map(str, [el for el in range(1, 16)])))
    with open('homework_5_task5.txt') as f:
        b = sum([int(i) for i in f.read().split()])
        print(b)

#6
with open('homework_5_task6.txt', encoding='utf-8') as f:
    content = f.readlines()
    numeral_dict = {}
    for line in content:
        num = re.findall(r'[0-9]+', line)
        numeral_dict[line.split(':')[0]] = sum([int(i) for i in num])
    print(numeral_dict)

#7
with open('homework_5_task7.txt', encoding='utf-8') as f:
    a = {}
    profit = {'average profit': 0}
    losses = {'losses': 0}
    for line in f.readlines():
        a[line.split()[0]] =int(line.split()[2]) - int(line.split()[3])

    positive = [i for i in a.values() if i > 0]
    negative = [i for i in a.values() if i < 0]

    profit['average profit'] = round(sum(positive) / len(positive), 2)
    losses['losses'] = sum(negative)

    unique_list = [a, profit, losses]
    print(unique_list)
    with open("my_file.json", "w") as write_f:
        json.dump(unique_list, write_f)




