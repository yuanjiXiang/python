# 堆排序

import random
def heapSort(arr):
    new_arr = []
    while len(arr) > 1:
        for i in range(len(arr) - 1, -1, -1):
            if 2 * i + 1 < len(arr) and arr[i] < arr[2 * i + 1]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
            if 2 * i + 2 < len(arr) and arr[i] < arr[2 * i + 2]:
                arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
        # 一次比较完,头尾交换位置,最大的元素在末尾
        arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
        # 将最后一个元素添加进新列表
        new_arr.append(arr.pop())

    return new_arr

test_arr = [random.randint(1, 100) for i in range(100)]
print(test_arr)
conf_arr = heapSort(test_arr)
conf_arr.reverse()
print(conf_arr)

