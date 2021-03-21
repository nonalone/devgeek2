dict_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('task4.txt', encoding='utf-8') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_list.append(dict_rus[i[0]] + ' ' + i[1])
    print(new_list)

with open('task4_dop.txt', 'w', encoding='utf-8') as my_file1:
    my_file1.writelines(new_list)