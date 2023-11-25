inp = list(map(int, input().split()))

for k in range(len(inp)):
    if k + 1 <= len(inp) - 1:
        if k % 2 == 0:
            inp[k], inp[k+1] = inp[k+1], inp[k]
print(inp)
