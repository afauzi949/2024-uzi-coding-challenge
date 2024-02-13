# UZI Coding Challenge
# 3/366
# https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python

# 1 naga butuh 2 peluru


def hero(bullets,dragons):
    return bullets >= dragons * 2

def hero(bullets, dragons):
    if bullets >= 2 * dragons:
        return True
    else:
        return False
    
tes1 = hero(1500,751)
tes2 = hero(10,5)
print(f"Tes 1 = {tes1}, Tes 2 = {tes2}")


# def hero(bullets,dragon):
#     if bullets / 2 >= dragon:
#         return True
#     else: 
#         return False
    
