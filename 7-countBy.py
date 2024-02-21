# UZI Coding Challenge
# 7/366
# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

def countBy(x, n):
    z = []
    for i in range(1, n+1):
        z.append(i * x)
    return z

print(countBy(2, 5))
print(countBy(3, 9)
