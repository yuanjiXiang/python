# 插入排序

def insertSort(arr):
    for i in range(1, len(arr)):
        
        key = arr[i] # 待比较关键字
        j = i - 1 # 从关键字的上一个数开始比较
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

    return arr

arr = [12, 11, 13, 5, 6] 
print(insertSort(arr))
