# 99乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{} * {} = {}\t'.format(j, i, j * i), end = '')
    print()