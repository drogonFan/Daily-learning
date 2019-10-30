[ALDS1_1_A Insertion Sort](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A)

```python
def print_list(numlist):
    n = len(numlist)
    for i in range(n):
        if i == n - 1:
            print(numlist[i])
        else:
            print(numlist[i], end=' ')
        
if __name__ == '__main__':
    n = int(input())
    numlist = [int(num) for num in input().split(' ')]
    
    print_list(numlist)
    for i in range(1, n):
        key_value = numlist[i]
        j = i - 1
        while j >= 0 and numlist[j] > key_value:
            numlist[j + 1] = numlist[j]
            j -= 1
        numlist[j + 1] = key_value
        print_list(numlist)
```

[Greatest Common Divisor](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B)

```python
def greatestc(a, b):
    if a < b:
        a, b = b, a

    c = a % b    
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

if __name__ == '__main__':
    a, b = input().split(' ')

    print(greatestc(int(a), int(b)))
```

[Prime Numbers](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C)

```python 
import math

def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    nump = 0
    for i in range(n):
        num = int(input())
        if isPrime(num):
            nump += 1
    
    print(nump)
```

