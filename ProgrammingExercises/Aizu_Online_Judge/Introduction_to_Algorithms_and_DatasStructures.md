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

[Allocation](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_D)
```python
import sys
def slove(goods, carnum, P):
    # 一个二分查找
    tot_good = len(goods)
    cur_good = 0
    for _ in range(carnum):
        load = 0
        while cur_good < tot_good and goods[cur_good] <= P -load:
            load += goods[cur_good]
            cur_good += 1
    if cur_good == tot_good:
        return True
    else:
        return False

if __name__ == '__main__':

    datas = input().split(' ')
    good_num = int(datas[0])
    car_num = int(datas[1])
    goods = []
    for _ in range(good_num):
        goods.append(int(input()))

    left = 0
    right = sys.maxsize
    while left < right:
        mid = (left + right) // 2
        if slove(goods, car_num, mid):
            # 当前的P较大
            right = mid
        else:
            left = mid + 1
    print(right)
```

[Merge Sort](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B)
```python
import sys

def merge(A, left, mid, right):
    L = A[left: mid] + [sys.maxsize]
    R = A[mid: right] + [sys.maxsize]
    i = j = count = 0
    k = left
    while k < right:
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    return count

def merge_sort(A, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        lcost = merge_sort(A, left, mid)
        rcost = merge_sort(A, mid, right)
        tot = merge(A, left, mid, right)
        return tot + lcost + rcost
    else:
        return 0

if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    count = merge_sort(A, 0, n)
    print(str(A).replace(',', '').replace('[', '').replace(']', ''))
    print(count)
```

[Quick Sort](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_C)
```python
import copy
import sys

def partition(A, p, r):
    key = A[r][1]
    i = p
    for j in range(p, r):
        # 把小的放在左边
        if A[j][1] <= key:
            A[i], A[j] = A[j], A[i]
            i += 1
    # 最后交换key值
    A[r], A[i] = A[i], A[r]
    return i

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def merge(A, left, mid, right):
    L = A[left: mid] + [(0, sys.maxsize)]
    R = A[mid: right] + [(0, sys.maxsize)]
    i = j = 0
    k = left
    while k < right:
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

def merge_sort(A, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


if __name__ == '__main__':
    n = int(input())
    numlist = []
    for _ in range(n):
        datas = input().split(' ')
        numlist.append((datas[0], int(datas[1])))
    list2 = copy.deepcopy(numlist)
    quick_sort(numlist, 0, n - 1)
    merge_sort(list2, 0, n)
    # 利用稳定排序去验证是否稳定
    if list2 == numlist:
        print('Stable')
    else:
        print('Not stable')
    for c, num in numlist:
        print('%s %d' % (c, num))
```

[The Number of Inversions](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D)
**这道题直接求解的话时间复杂度是$O(n^2)$，但是可以采用分治的思想，将问题规模减小，这里采用了类似与归并排序的算法**
```python
import sys

def merge(numlist, left, mid, right):
    L = numlist[left:mid] + [sys.maxsize]
    R = numlist[mid:right] + [sys.maxsize]
    i = j = 0
    k = left
    inv = 0
    while k < right:
        if L[i] < R[j]:
            numlist[k] = L[i]
            i += 1
        else:
            inv += (mid - left - i)
            numlist[k] = R[j]
            j += 1
        k += 1
    return inv


def cal_inv(numlist, left, right):
    if right > left + 1:
        mid = (left + right) // 2
        linv = cal_inv(numlist, left, mid)
        rinv = cal_inv(numlist, mid, right)
        return linv + rinv + merge(numlist, left, mid, right)
    else:
        return 0
    

if __name__ == '__main__':
    n  = int(input())
    numlist = [int(num) for num in input().split(' ')]
    print(cal_inv(numlist, 0, n))
```

[Counting Sort](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_A)
**计数排序**
```python
def count_sort(numlist, n):
    C = [0 for i in range(n + 1)]
    B = [0 for i in range(len(numlist))]
    # store times that num has appear
    for num in numlist:
        C[num] += 1
    # cal index
    for i in range(1, n + 1):
        C[i] += C[i - 1]
    for n in range(len(numlist), 0, -1):
        C[numlist[n - 1]] -= 1
        B[C[numlist[n - 1]]] = numlist[n - 1]

    return B

if __name__ == '__main__':
    n = int(input())
    numlist = [int(num) for num in input().split(' ')]
    numlist = count_sort(numlist, max(numlist))
    print(str(numlist).replace(',', '').replace('[', '').replace(']', ''))
```

[Partition](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_B)
```python
def partition(A, p, r):
    key = A[r]
    i = p
    for j in range(p, r):
        # 把小的放在左边
        if A[j] <= key:
            A[i], A[j] = A[j], A[i]
            i += 1
    # 最后交换key值
    A[r], A[i] = A[i], A[r]
    return i


if __name__ == '__main__':
    n = int(input())
    numlist = [int(num) for num in input().split(' ')]
    index = partition(numlist, 0, len(numlist) - 1)
    out = str(numlist[0:index]).replace(',', '').replace('[', '').replace(']', '') \
        + ' [' + str(numlist[index]) + '] '\
        + str(numlist[index + 1:]).replace(',', '').replace('[', '').replace(']', '')
    print(out)
```

```python
# 又是一个超时答案，数据量太大了，性能是真的差，使用了标准的左孩子右兄弟的做法
class Node():
    def __init__(self, value):
        self.value = value
        self.deep = -1
        self.parent = None
        self.left = None
        self.right = None
        self.child = None
    
    def add_child(self, node):
        if self.child == None:
            self.child = node
            self.child.parent = self
        else:
            curnode = self.child
            while curnode.right != None:
                curnode = curnode.right
            curnode.right = node
            node.left = curnode
            node.parent = self

    def get_childs(self):
        childs = []
        if self.child != None:
            childs.append(self.child.value)
            curnode = self.child
            while curnode.right != None:
                childs.append(curnode.right.value)
                curnode = curnode.right
        return childs
    
    def set_deep(self, deep):
        self.deep = deep
        if self.child != None:
            curnode = self.child
            curnode.set_deep(deep + 1)
            while curnode.right != None:
                curnode.right.set_deep(deep + 1)
                curnode = curnode.right


if __name__ == '__main__':
    n = int(input())
    tree = {}
    for i in range(n):
        tree[i] = Node(i)

    for _ in range(n):
        datas = [int(num) for num in input().split(' ')]
        nodeid = datas[0]
        if datas[1] > 0:
            for cid in datas[2:]:
                tree[nodeid].add_child(tree[cid])

    for i in range(n):
        curnode = tree[i]
        if curnode.parent is None:
            # this is root
            curnode.set_deep(0)
            break
            
    
    for i in range(n):
        curnode = tree[i]
        if curnode.child == None:
            nodetype = 'leaf'
        else:
            nodetype = 'internal node'
        if curnode.parent == None:
            nodetype = 'root'
            parent = -1
        else:
            parent = curnode.parent.value
        
        
        childs = curnode.get_childs()
        print('node %d: parent = %d, depth = %d, %s, %s' % (i, parent,curnode.deep, nodetype, childs) )

# 想过只能走一些歪门邪道,这根本就不是算是一棵树
class Node():
    def __init__(self, value):
        self.value = value
        self.deep = -1
        self.parent = None
        self.left = None
        self.right = None
        self.childs = []

def setdeep(tree, i, deep):
    tree[i].deep = deep
    for child in tree[i].childs:
        tree[child].parent = i
        if child < len(tree):
            setdeep(tree, child, deep + 1)

if __name__ == '__main__':
    n = int(input())
    tree = {}

    for _ in range(n):
        datas = [int(num) for num in input().split(' ')]
        nodeid = datas[0]
        if nodeid not in tree.keys():
            tree[nodeid] = Node(nodeid)

        if datas[1] > 0:
            tree[nodeid].childs = datas[2:]
            for child in tree[nodeid].childs:
                if child not in tree.keys():
                    tree[child] = Node(child)
                tree[child].parent = nodeid


    for i in range(n):
        curnode = tree[i]
        if curnode.parent is None:
            # this is root
            setdeep(tree, i, 0)
            break
            
    
    for i in range(n):
        curnode = tree[i]
        if len(curnode.childs) == 0:
            nodetype = 'leaf'
        else:
            nodetype = 'internal node'
        if curnode.parent == None:
            nodetype = 'root'
            parent = -1
        else:
            parent = curnode.parent
        
        childs = curnode.childs
        print('node %d: parent = %d, depth = %d, %s, %s' % (i, parent,curnode.deep, nodetype, childs) )
```

[Binary Trees](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_B)
```python
class Node():
    def __init__(self, value):
        self.value = value
        self.deep = -1
        self.parent = None
        self.left = -1
        self.right = -1
        self.height = -1
        self.sib = -1

def setdeep(tree, i, deep):
    tree[i].deep = deep
    if tree[i].left != -1:
        setdeep(tree, tree[i].left, deep + 1)
    if tree[i].right != -1:
        setdeep(tree, tree[i].right, deep + 1)

def setheight(tree, i):
    if tree[i].height != -1:
        pass
    elif tree[i].left == -1 and tree[i].right == -1:
        tree[i].height = 0
    elif tree[i].left == -1:
        tree[i].height = setheight(tree, tree[i].right)
    elif tree[i].right == -1:
        tree[i].height = setheight(tree, tree[i].left)
    else:
        tree[i].height = max(setheight(tree, tree[i].right), setheight(tree, tree[i].left))
    return tree[i].height + 1

if __name__ == '__main__':
    n = int(input())
    tree = {}

    for _ in range(n):
        datas = [int(num) for num in input().split(' ')]
        nodeid = datas[0]
        if nodeid not in tree.keys():
            tree[nodeid] = Node(nodeid)
        tree[nodeid].left = left = int(datas[1])
        tree[nodeid].right = right = int(datas[2])
        if left != -1:
            if left not in tree.keys():
                tree[left] = Node(left)
            tree[left].parent = nodeid
            tree[left].sib = right
        if right != -1:
            if right not in tree.keys():
                tree[right] = Node(right)
            tree[right].parent = nodeid
            tree[right].sib = left

    for i in range(n):
        curnode = tree[i]
        if curnode.parent is None:
            # this is root
            setdeep(tree, i, 0)
            setheight(tree, i)
            break
            
    for i in range(n):
        curnode = tree[i]
        deg = 0
        if curnode.left == -1 and curnode.right == -1:
            nodetype = 'leaf'
            deg = 0
        else:
            if curnode.left != -1:
                deg += 1
            if curnode.right != -1:
                deg += 1
            nodetype = 'internal node'
        if curnode.parent == None:
            nodetype = 'root'
            parent = -1
        else:
            parent = curnode.parent
        print('node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, %s' \
            % (i, parent,curnode.sib, deg,  curnode.deep, curnode.height, nodetype) )
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

