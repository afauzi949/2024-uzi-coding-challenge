# UZI Coding Challenge
# 2/366
# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/solutions/python

# def reverse_seq(n):
#     data = [n]
#     while n > 1:
#         hasil = n - 1
#         data.append(hasil)
#         n = hasil
#     return data

# array1 = reverse_seq(5) 
# print(array1)


def reverse_seq(n):
    array = []
    for i in range(n):
        array.append(n)
        n -= 1
    return array

array = reverse_seq(5)
print(array)

# def reverse_seq(n):
#     return list(range(n, 0, -1))
