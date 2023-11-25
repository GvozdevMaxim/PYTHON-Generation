n = int(input())
d = []
result = []
# dadafafafaafafafaf
for i in range(n):
    x = str(input())
    if 5 <= len(x) <= 100:
        d.append(x)

for k, x in enumerate(d):
    if "a" in x and "n" in x and "t" in x and "o" in x and "n" in x:
        A = x.index("a")
        if x.find("n", A) != -1:
            N = x.index("n", A)
        else:
            continue
        if x.find("t", N) != -1:
            T = x.index("t", N)
        else:
            continue
        if x.find("o", T) != -1:
            C = x.index("o", T)
        else:
            continue
        if x.find("n", C) != -1:
            Z = x.index('n', C)
        else:
            continue
        if A < N < T < C < Z:
            result.append(k+1)

print(*result)


