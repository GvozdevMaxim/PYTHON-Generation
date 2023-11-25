inp = list(map(int, input().split()))
res = []
res.append(inp[-1])
res += inp[:-1]
print(*res)
