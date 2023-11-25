timur = str(input())
ruslan = str(input())

if ruslan == timur:
    print("ничья")
elif timur == 'камень' and (ruslan == "ножницы" or ruslan == "ящерица"):
    print("Тимур")
elif timur == "ножницы" and (ruslan == "бумага" or ruslan == "ящерица"):
    print("Тимур")
elif timur == 'бумага' and (ruslan == "камень" or ruslan == "Спок"):
    print("Тимур")
elif timur == "Спок" and (ruslan == "ножницы" or ruslan == "камень"):
    print("Тимур")
elif timur == "ящерица" and (ruslan == "Спок" or ruslan == "бумага"):
    print("Тимур")
else:
    print("Руслан")