# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

path = "text.txt"

dataTxt = ""

with open('text.txt', 'r', encoding='utf_8') as file:
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




# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')