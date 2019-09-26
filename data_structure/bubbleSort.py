# 冒泡排序

import random
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1): # 一次排序，最大的元素已经在末尾
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [random.randint(1, 100) for i in range(100)]
bubbleSort(arr)
print(arr)
            