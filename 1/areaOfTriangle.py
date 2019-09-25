# 三角形面积

a = float(input('第一条边:'))
b = float(input('第二条边:'))
c = float(input('第二条边:'))

# 三角形的半周长
s = (a + b + c) / 2

# 面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('面积为:', area)