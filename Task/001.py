# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from encodings import utf_8


path = 'text.txt'

dataTxt = ''
with open(path, 'r', encoding='utf_8') as file:
    dataTxt = file.read()
print(dataTxt)

dataTxt = dataTxt.split()
print(dataTxt)

findTxt = input('Введите текст для проверки: ')

resultTxt = []

for word in dataTxt:
    if findTxt not in word:
        resultTxt.append(word)
print(resultTxt)