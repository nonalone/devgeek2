with open('task5.txt', 'w+') as my_file:
    number = input('Введите число через пробел: ')
    my_file.writelines(number)
    my_num = number.split()
print(f'{sum(map(int, my_num))}')