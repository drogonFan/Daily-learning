from random import randint

def radixSort(A, d):
    # 进行n轮排序
    for r in range(0, d):
        # 根据当前位上的数字进行稳定排序(这里使用插入排序)
        for i in range(1, len(A)):
            key_value = A[i]
            j = i - 1
            while j >= 0 and radix_of_num(A[j], r + 1) > radix_of_num(key_value, r + 1):
                A[j + 1] = A[j]
                j -=1
            A[j + 1] = key_value

def radix_of_num(num, d):
    '''
    获取一个数字某位上的数字
    '''
    return num % (10 ** d) // (10 ** (d - 1))

if __name__ == '__main__':
    A = [randint(0, 9999) for i in range(20)]
    radixSort(A, 4)
    print(A)