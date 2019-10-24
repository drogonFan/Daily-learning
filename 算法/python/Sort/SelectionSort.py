def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array 