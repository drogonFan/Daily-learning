from random import random

def insertionSort(A):
    '''
    插入排序
    '''
    n = len(A)
    if n <= 1:
        return 
    for i in range(1, n):
        key_value = A[i]
        j = i - 1
        while j >= 0 and A[j] > key_value:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key_value
    

def bucketSort(A):
    '''
    桶排序，时间复杂度接近O(n)
    '''
    n = len(A)
    # 新建n个桶
    buckets = [[] for i in range(n)]

    # 将元素放入桶中
    for i in range(n):
        buckets[int(A[i] * n)].append(A[i])
    
    # 对每个桶进行插入排序
    for i in range(n):
        if len(buckets[i]) != 0:
            insertionSort(buckets[i])
            
    # 合并结果并返回
    return [num for bucket in buckets for num in bucket]

if __name__ == '__main__':
    A = [round(random(), 3) for i in range(200)]
    print(A)
    print(bucketSort(A))