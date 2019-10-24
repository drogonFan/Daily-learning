def shellSort(array):
    n = len(array)
    step = round(n / 2)
    while step > 0:
        for i in range(step):
            for i in range(0, n, step):
                j = i - step
                key = array[i]
                while j >= 0 and array[j] > key:
                    array[j + step] = array[j]
                    j -= step
                array[j + step] = key
        step = round(step/2)
    return array