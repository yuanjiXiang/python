# 最小公倍数 least common multiple

def cal_lcm(x, y):
    if x >= y:
        greater = x
    else:
        greater = y

    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break      
        greater += 1
    return lcm

num1 = int(input('Number 1:'))
num2 = int(input('Number 2:'))

print('Least common multiple:', cal_lcm(num1, num2))