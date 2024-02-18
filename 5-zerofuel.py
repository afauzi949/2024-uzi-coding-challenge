# UZI Coding Challenge
# 5/366
# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg*fuel_left:
        return True
    else:
        return False
    
print(zero_fuel(50,25,2))

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump / mpg <= fuel_left:
#         return True
#     else:
#         return False