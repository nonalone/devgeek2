f = open('task6.txt', encoding='utf-8')
D2 = {}
for lines in f:
    string = lines.split(':')
    key = string[0]
    value = string[1].rstrip()
    D2[key] = value
print('D2 = ', D2)
f.close()