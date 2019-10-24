def countingSort(A, k):
    n = len(A)
    B = [0 for i in range(n)]
    C = [0 for i in range(k + 1)]

    for j in A:
        C[j] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for j in A:
        B[C[j] - 1] = j
        C[j] = C[j] - 1

    return B
