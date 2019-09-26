"""
快速排序，’交换类排序‘，
使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，
然后递归地排序两个子序列
"""
import random
def quickSort(arr, low , high):
    if low < high:
        i, j = low, high
        pivot = arr[low] # 基准

        while i != j:
            while i < j and pivot < arr[j]: # 先从右往左比较
                j -= 1
            if i < j:
                arr[i] = arr[j] # 找到小于基准的数，将此数放在基准位置
                i += 1
            while i < j and pivot > arr[i]: # 再从左向右比较
                i += 1
            if i < j:
                arr[j] = arr[i] # 找到大于基准的数，放在之前j的位置
                j -= 1

        arr[i] = pivot # 一趟比较完成，及基准放在正确的位置，它左边的数都小于它，它右边的数都大于它

        quickSort(arr, low, i - 1)
        quickSort(arr, i + 1, high)

arr = [random.randint(1, 10000) for i in range(10000)]
quickSort(arr, 0, len(arr) - 1)
print(arr)
        