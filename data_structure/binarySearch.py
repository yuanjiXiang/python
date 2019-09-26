# 二分查找

def binarySearch(arr, h, r, x):
    """
    arr代表待查找数组，h表示数组的头尾下标，x表示待查找的数
    """
    if r >= h:
        mid = int((r + h) / 2)

        if arr[mid] == x:
            return mid
        elif arr[mid] >x:
            r = mid -1
            return binarySearch(arr, h, r, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1
# 测试数组
arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr) - 1, x)
print(result)
