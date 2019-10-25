def quickSort1(array, left, right):
    '''
    用p和q从两边遍历数组
    '''
    if left >= right:
        return
    key_value = array[left]
    p = left
    q = right

    while p < q:
        while p < q and array[q] >= key_value:
            q -= 1
        array[p] = array[q]
        while p < q and array[p] < key_value:
            p += 1
        array[q] = array[p]
    array[p] = key_value
    quickSort1(array, left, p - 1)
    quickSort1(array, p + 1, right)


def quickSort2(array, p, r):
    '''
    算法导论上的快速排序，看起来比较简洁
    '''
    if p < r:
        q = partition(array, p, r)
        quickSort2(array, p, q - 1)
        quickSort2(array, q + 1, r)

def partition(array, left, right):
    x = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= x:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1