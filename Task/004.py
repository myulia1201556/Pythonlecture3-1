# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

with open("RLE1_decoded.txt", "r") as data:
    text = data.read()

def encode_rle(alf):
    str_code = ""
    prev_char = ""
    count = 1
    for char in alf:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = encode_rle(text)
print(str_code)

with open("RLE2_encoded.txt", "r") as data:
    text2 = data.read()

def decoding_rle(alf:str):
    count = ""
    str_decode = ""
    for char in alf:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ""
    return str_decode

str_decode = decoding_rle(text2)
print(str_decode)