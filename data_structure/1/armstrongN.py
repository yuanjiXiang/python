# 阿姆斯特朗数

num = int(input('请输入一个数：'))

# 指数
n = len(str(num))

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print(num, '是阿姆斯特朗数')
else:
    print(num, '不是阿姆斯特朗数')