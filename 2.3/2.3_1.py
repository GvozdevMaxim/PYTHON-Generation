k = int(input())
d = {}
first = set()
second = set()
third = set()
fourth = set()


for i in range(k):
    x,y = map(int, input().split())
    d[i] = x, y
print(d)
for k,v in d.items():
    print(v)
    if v[0] != 0 and v[1] != 0:
        if v[0] > 0 and v[1] > 0:
            first.add(v)
        elif v[0] < 0 and v[1] > 0:
            second.add(v)
        elif v[0] < 0 and v[1] < 0:
            third.add(v)
        elif v[0] > 0 and v[1] < 0:
            fourth.add(v)

print(f"Первая четверть: {len(first)}")
print(f"Вторая четверть: {len(second)}")
print(f"Третья четверть: {len(third)}")
print(f"Четвертая четверть: {len(fourth)}")
