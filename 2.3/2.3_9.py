inp = str(input())
counter_P = []
len_res = []
res = []
for i, x in enumerate(inp):
    if x == "Р":
        counter_P.append(x)
    elif x == "О":
        if counter_P != []:
            len_res.append(len(counter_P))
            counter_P.clear()
len_res.append(len(counter_P))
print(max(len_res))