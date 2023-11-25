import math
k = int(input())
lst_nums = []
temp = None
for i in range(k):
    x = int(input())
    lst_nums.append(x)
the_number = int(input())
for x, el in enumerate(lst_nums):
    for y, el2 in enumerate(lst_nums):
        if el * el2 == the_number and x != y:
            temp = el * el2
            break

print("ДА" if temp is not None else "НЕТ")