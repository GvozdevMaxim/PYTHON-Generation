str_inp = list(map(int, input().split()))
lst_count = []
print(str_inp)
for i in range(len(str_inp) - 1):
    if lst_count == []:
        if str_inp[i+1] > str_inp[i]:
            lst_count.append(1)
    elif str_inp[i+1] > str_inp[i]:
        lst_count.append(1)
print(len(lst_count))