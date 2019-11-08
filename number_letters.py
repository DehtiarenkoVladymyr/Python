import string

fam = 'dehtiarenko'

print('Номер букв в слове:', fam + ';', 'Количество букв:', len(fam))

# Узнаём общее количество букв в лове + порядковый номер каждой буквы.

for let in fam:
    c = ord(let)  # Узнаём номер символа в таблице символов
    a = ord('a')  # Узнаём номер пирвого символа
    n = c - a  # Вычитаем коды символов мы узнаем растоние между ними
    n = n + 1  # Что бы найи порядковый номер
    print(let, n, sep=' - ')

# Узнать сколько в слове есть одинаковых букв.
def let_num():
    letterCounts = {}
    for i in fam:
        letterCounts[i] = letterCounts.get(i, 0) + 1
    print (letterCounts)
let_num()

