def merge(left, right):
    rs = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            rs.append(left[l])
            l += 1
        else:
            rs.append(right[r])
            r += 1
    rs += left[l:]
    rs += right[r:]
    return rs

def mergeSort(array):
    n = len(array)
    if n <= 1:
        return array
    left = mergeSort(array[:n//2])
    right = mergeSort(array[n//2:])
    return merge(left, right)