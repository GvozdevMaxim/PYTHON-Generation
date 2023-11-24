int_inp = int(input())
if len(str(int_inp)) == 5:
    print(str(int_inp)[::-1].lstrip('0'))
elif len(str(int_inp)) == 6:
    res = str(int_inp)[0] + str(int_inp)[1:len(str(int_inp))][::-1].lstrip('0')
    print(res)
