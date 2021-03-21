file = open('task2.txt')
line = file.readline()
print(f'Строк {len(line)}')
file = open('task2.txt')
word = file.read()
word = word.split()
print(f'Слов {len(word)}')
file.close()

