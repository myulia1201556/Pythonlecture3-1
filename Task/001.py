# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# решена на семинаре, удаляются слова с задаными символами из текста
# сохранённого в txt файле

# path = "text.txt"

# data_txt = ""

# with open("text.txt", "r", encoding="utf_8") as file:
#     data_txt = file.read()
# print(data_txt)

# data_txt = data_txt.split()
# print(data_txt)

# find_txt = input("Введите текст для проверки: ")

# result_txt = []

# for word in data_txt:
#     if find_txt not in word:
#         result_txt.append(word)
# print(result_txt)


text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_some_words(text):
    text = list(filter(lambda x: "абв" not in x, text.split()))
    return " ".join(text)

text = del_some_words(text)
print(text)
