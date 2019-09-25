# 素数判定

num = int(input('请输入一个正整数:'))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, '不是素数')
            print('因为', i, '*' , num // i, '=' , num)
            break
    else:
        print(num, '是素数')
else:
        print(num, '是素数')