# 最大公约数 greast common divisor

def cal_gcd(x, y):
    if x <= y:
        smaller = x
    else:
        smaller = y
    
    for i in range(1, smaller + 1):
        if(x % i == 0 and y % i == 0):
            gcd = i
    return gcd

num1 = int(input('第一个数：'))
num2 = int(input('第二个数：'))

print('最大公约数：', cal_gcd(num1, num2))