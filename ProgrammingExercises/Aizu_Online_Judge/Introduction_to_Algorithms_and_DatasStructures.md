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
class Node():
    def __init__(self, value=0, pre=None, nex=None):
        self.value = value
        self.pre = pre
        self.next = nex

class DoubleLinkList():
    def __init__(self):
        self.head = Node()
        self.head.pre = self.head
        self.head.next = self.head

    def insert(self, value):
        newNode = Node(value, self.head, self.head.next)
        self.head.next.pre = newNode
        self.head.next = newNode

    def delete(self, x):
        curnode = self.head
        while curnode.next != self.head:
            if curnode.next.value == x:
                # delete node
                curnode.next.next.pre = curnode
                curnode.next = curnode.next.next
                break
            curnode = curnode.next

    def deleteFirst(self):
        if self.head.next == self.head:
            pass
        else:
            delnode = self.head.next
            self.head.next = delnode.next
            delnode.next.pre = self.head

    def deleteLast(self):
        if self.head.pre == self.head:
            pass
        else:
            delnode = self.head.pre
            delnode.pre.next = self.head
            self.head.pre = delnode.pre

    def show(self):
        curnode = self.head
        out = ''
        while curnode.next != self.head:
            out += str(curnode.next.value)
            out += ' '
            curnode = curnode.next
        out = out[:-1]
        print(out)

if __name__ == '__main__':
    n = int(input())
    link = DoubleLinkList()
    for i in range(n):
        com = input()
        if com[0] == 'i':
            link.insert(int(com[7:]))
        elif com[0] == 'd' and com[6] == ' ':
            link.delete(int(com[7:]))
        elif com == 'deleteFirst':
            link.deleteFirst()
        elif com == 'deleteLast':
            link.deleteLast()

    link.show()
```

[Areas on the Cross-Section Diagram](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_D)
```python
def cal_water(floods):
    # 保存地形
    fstack = []
    # 保存一段地形的面积
    astack = []
    i = 0
    for flood in floods:
        if flood == '\\':
            fstack.append(i)
        elif flood == '/' and len(fstack) > 0:
            # 出现右边的/，计算面积，并且观察是否有可以合并的地方
            s = fstack.pop(-1)
            area = (i - s) * 1
            while len(astack) > 0 and astack[-1][0] > s:
                _, a = astack.pop(-1)
                area += a
            astack.append((s, area))   
        else:
            pass
        i += 1
    
    tot = 0
    tot_area = 0
    out = ''
    while len(astack) > 0:
        _, area = astack.pop()
        tot += 1
        tot_area += area
        out = ' ' + str(area) + out
    
    print(tot_area)
    print(str(tot) +  out)

if __name__ == '__main__':
    floods = input()
    cal_water(floods)
```

[Linear Search](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A)
```python
def linear_search(num, numlist):
    # 设置一个标记位，可以加快搜索效率
    # 原因是可以省略循环终止条件的判断
    # 相比与不加的时候可以减少比较次数
    numlist.append(num)
    index = 0
    while numlist[index] != num:
        index += 1
    numlist.pop(-1)
    if index == len(numlist):
        return False
    else:
        return True

if __name__ == '__main__':
    n = input()
    numlist1 = [int(num) for num in input().split()]
    m = input()
    numlist2 = [int(num) for num in input().split()]

    tot = 0
    for num in numlist2:
        if linear_search(num, numlist1):
            tot += 1
    print(tot)
```

[Binary Search](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B)
```python
def binary_search(num, numlist):
    # 二叉搜索
    left = 0
    right = len(numlist)
    while left < right:
        mid = (left + right) // 2
        if numlist[mid] == num:
            return mid
        elif numlist[mid] < num:
            left = mid + 1
        else:
            right = mid
    return -1

if __name__ == '__main__':
    n = input()
    numlist1 = [int(num) for num in input().split()]
    m = input()
    numlist2 = [int(num) for num in input().split()]

    tot = 0
    for num in numlist2:
        if binary_search(num, numlist1) >= 0:
            tot += 1
    print(tot)
```

[Dictionary](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C)
```python
if __name__ == '__main__':
    n = int(input())
    worddict = {}
    for _ in range(n):
        common, word = input().split(' ')
        if common == 'insert':
            worddict[word] = 1
        else:
            if word in worddict.keys():
                print('yes')
            else:
                print('no')
```


[Exhaustive Search](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A)
```python
# 解法一：穷举搜索，时间复杂度为O(2^n)
def solve(i: int, A: list, m: int):
    if m == 0:
        return True
    elif m < 0 or i >= len(A):
        return False
    else:
        return solve(i + 1, A, m - A[i]) or solve(i + 1, A, m)

if __name__ == '__main__':
    n = int(input())
    A = [int(num) for num in input().split(' ')]
    m = int(input())
    mlist = [int(num) for num in input().split(' ')]

    for num in mlist:
        if solve(0, A, num):
            print('yes')
        else:
            print('no')

# 解法二：动态规划，使用记忆化递归,使用nm的空间辅助，时间复杂度为O(nm)
def solve(i: int, A: list, meolist: list, m: int):
    if m == 0:
        return True
    elif m in meolist[i].keys():
        return meolist[i][m]
    
    if i >= len(A):
        meolist[i][m] = False
    elif solve(i + 1, A, meolist, m - A[i]) is True:
        meolist[i][m] = True
    elif solve(i + 1, A, meolist, m) is True:
        meolist[i][m] = True
    else:
        meolist[i][m] = False

    return meolist[i][m]

if __name__ == '__main__':
    n = int(input())
    A = [int(num) for num in input().split(' ')]
    m = int(input())
    mlist = [int(num) for num in input().split(' ')]

    # Memory array, store the num already cal
    meolist = [{} for i in range(n + 1)]

    for num in mlist:
        if solve(0, A, meolist, num):
            print('yes')
        else:
            print('no')
```

[Fibonacci Number](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A)
```python
# 暴力求解，时间复杂为O(2^n)，求解第44项需要1 134 903 170次计算
def fib(n):
    if n == 0 or n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    n = int(input())
    print(fib(n))

# 动态规划，使用一个数组存储计算结果
def fib(n: int, meolist: dict):
    if n == 0 or n == 1:
        meolist[n] = 1
        return 1
    elif n in meolist.keys():
        return meolist[n]
    
    meolist[n] = fib(n - 1, meolist) + fib(n - 2, meolist)
    return meolist[n]

if __name__ == '__main__':
    n = int(input())
    meolist = {}
    print(fib(n, meolist))
```

