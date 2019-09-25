# 约瑟夫死者小游戏

'''
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
'''

crews = [i for i in range(1, 31)]
for crew in crews:
    print(crew, end = ' ')
    if (crews.index(crew) + 1) % 9 == 0:
        print()
print()
crews_down = []

while len(crews_down) < 15:

    # 每次首先获取数组中要删除元素的个数
    i = 1
    while i * 9 < len(crews):
        i += 1
    i -= 1

    # 根据规则确定待删除数的下标
    c_indexs = [9 * j -1 for j in range(1, i + 1)]

    # 将删除的数保存在一个数组中，并将原数组的这些数置为0，以便过滤
    for ind in c_indexs:
        crews_down.append(crews[ind])
        crews[ind] = 0

    # 将数组按照规则重新排序  
    crews = crews[c_indexs[-1] + 1:] + crews[: c_indexs[-1] + 1:]

    # 将0元素剔除
    crews = [crew for crew in crews if crew != 0]
   
print(crews_down)
    







