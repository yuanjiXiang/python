# 选择排序

"""
在未排序的序列中找到最小的元素，和第一个元素交换位置，第一次排序结束
再从剩余未排序的元素中找到最小的元素，放在已排序序列的末尾，以此类推
"""
import random
def selectSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [random.randint(1, 100) for i in range(100)]
selectSort(arr)
print(arr)
