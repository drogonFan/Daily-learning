#基本的冒泡排序
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

#冒泡排序的优化方法一：某一趟如果没有数据交换，则说明已经排好序，因此不用在进行迭代
def bubbleSort_1(array):
    n = len(array)
    for i in range(n):
        flag = 1            #标记
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 0
        if flag == 1:       #排好顺序
            break
    return array

#冒泡排序优化二：记录上次最后的交换位置，这个位置之后的数一定是有序的
def bubbleSort_2(array):
    n = len(array)
    k = n - 1
    for i in range(n):
        flag = 1
        for j in range(k):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                k = j           #最后一次交换的位置
                flag = 0
        if flag == 1:
            break
    return array