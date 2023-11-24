m = float(input())
h = float(input())

imb = m / (h * h)
if imb < 18.5:
    print("Недостаточная масса")
elif 18.5 <= imb <= 25:
    print("Оптимальная масса")
elif imb > 25:
    print("Избыточная масса")