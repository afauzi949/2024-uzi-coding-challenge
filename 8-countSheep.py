# UZI Coding Challenge
# 8/366
# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python


def count_sheep(x):
    hasil = ""
    for i in range(1,x+1):
        hasil += str(i) + " sheep..."
    return hasil

print(count_sheep(5))

# def count_sheep(num):
#     result = ''
#     for i in range(1, num+1):
#         result += f'{i} sheep...'
#     return result

# print(count_sheep(5))