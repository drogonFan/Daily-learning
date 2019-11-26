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

[Bubble Sort](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A)

```python
def bubbleSort(numlist):
    n = len(numlist)
    swaptime = 0
    for i in range(n):
        for j in range(n - 1, i, -1):
            if numlist[j] < numlist[j - 1]:
                swaptime += 1
                numlist[j], numlist[j - 1] = numlist[j - 1], numlist[j]
    return swaptime

def print_numlist(numlist):
    if len(numlist) == 1:
        print(numlist[0])
    else:
        for i in range(0, len(numlist) - 1):
            print(numlist[i], end = ' ')
        print(numlist[-1])

if __name__ == '__main__':
    n = int(input())
    numlist = [int(i) for i in input().replace('\n', '').split(' ')]
    swapnum =  bubbleSort(numlist)

    print_numlist(numlist)
    print(swapnum)
```

[Selection Sort](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B)

```python
def selectionSort(numlist):
    n = len(numlist)
    swaptime = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numlist[j] < numlist[min_index]:
                min_index = j
        if min_index != i:
            numlist[i], numlist[min_index] = numlist[min_index], numlist[i]
            swaptime += 1
    return swaptime

def print_numlist(numlist):
    if len(numlist) == 1:
        print(numlist[0])
    else:
        for i in range(0, len(numlist) - 1):
            print(numlist[i], end = ' ')
        print(numlist[-1])

if __name__ == '__main__':
    n = int(input())
    numlist = [int(i) for i in input().replace('\n', '').split(' ')]
    swapnum =  selectionSort(numlist)

    print_numlist(numlist)
    print(swapnum)
```

[Stable Sort](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C)

```python
def bubbleSort(numlist):
    n = len(numlist)
    flag = True
    for i in range(n):
        if flag is False:
            break
        flag = False
        for j in range(n - 1, i, -1):
            if numlist[j][1] < numlist[j - 1][1]:
                numlist[j], numlist[j - 1] = numlist[j - 1], numlist[j]
                flag = True

def selectionSort(numlist):
    n = len(numlist)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numlist[min_index][1] > numlist[j][1]:
                min_index = j
        
        if min_index != i:
            numlist[min_index], numlist[i] = numlist[i], numlist[min_index]

def print_numlist(numlist):
    if len(numlist) == 1:
        print(numlist[0])
    else:
        n = len(numlist)
        for i in range(n - 1):
            print(numlist[i], end=' ')
        print(numlist[-1])

if __name__ == '__main__':
    n = int(input())
    numlist = [num for num in input().replace('\n', '').split(' ')]
    numlist2 = numlist.copy()
    bubbleSort(numlist)
    print_numlist(numlist)
    print('Stable')
    selectionSort(numlist2)
    print_numlist(numlist2)
    flag = True
    for i in range(len(numlist)):
        if numlist[i] != numlist2[i]:
            flag = False
            break
    if flag:
        print('Stable')
    else:
        print('Not stable')
```

[Stack](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A)

```python
def isOp(c):
    if c in ('+', '-', '*', '/'):
        return True
    return False

def cal(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    else:
        return num1 / num2

if __name__ == '__main__':
    infos = input().split(' ')
    stack = []
    for f in infos:
        if isOp(f):
            num2 = stack.pop(-1)
            num1 = stack.pop(-1)
            stack.append(cal(num1, num2, f))
        else:
            stack.append(int(f))
    print(stack.pop())
```

[Queue](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B)
```python
if __name__ == '__main__':
    args = input().split(' ')
    n = int(args[0])
    t = int(args[1])

    queue = []

    prolist = {}
    finish = []
    for i in range(n):
        datas = input().split(' ')
        prolist[datas[0]] = int(datas[1])
        # add to queue by order
        queue.append(datas[0])
    
    tottime = 0
    while len(queue) > 0:
        name = queue.pop(0)
        if prolist[name] == 0:
            pass
        else:
            if prolist[name] > t:
                # has some task unfinish
                prolist[name] -= t
                tottime += t
                queue.append(name)
            else:
                # finish all task, quit
                finish.append('%s %d' %(name, tottime + prolist[name]))
                tottime += prolist[name]
                prolist[name] = 0
    
    for info in finish:
        print(info)
```

[Doubly Linked List](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C)
```python

```