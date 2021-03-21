with open('task3.txt', encoding='utf-8') as my_file:
    min_salary = []
    work = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            work.append(i[0])
        min_salary.append(i[1])
print(f'Оклад меньше 20.000 {work}, средний оклад {sum(map(int, min_salary)) / len(min_salary)}')
