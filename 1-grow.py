# UZI Coding Challenge
# 1/366
# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

def grow(arr):
    hasil = 1
    for i in arr:
        hasil *= i
    return hasil

test1 = grow([1,2,3])
test2 = grow([4,1,1,1,4])
test3 = grow([2,2,2,2,2,2])
print(test1)
print(test2)
print(test3)