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

[Tree Walk](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_C)
使用递归实现，比较简单：

+ 前序遍历：根左右
+ 中序遍历：左根右
+ 后序遍历：左右根
```python
class Node():
    def __init__(self, value):
        self.value = value
        self.parent = -1
        self.left = -1
        self.right = -1

def preorder(tree, root):
    if root == -1:
        pass
    else:
        print(' %d' % root, end='')
        preorder(tree, tree[root].left)
        preorder(tree, tree[root].right)

def inorder(tree, root):
    if root == -1:
        pass
    else:
        inorder(tree, tree[root].left)
        print(' %d' % root, end='')
        inorder(tree, tree[root].right)

def postorder(tree, root):
    if root == -1:
        pass
    else:
        postorder(tree, tree[root].left)
        postorder(tree, tree[root].right)
        print(' %d' % root, end='')

if __name__ == '__main__':
    n = int(input())
    tree = {}
    root = -1
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
        if right != -1:
            if right not in tree.keys():
                tree[right] = Node(right)
            tree[right].parent = nodeid

    for i in range(n):
        if tree[i].parent == -1:
            # this is root
            root = i
            break
            
    print('Preorder')
    preorder(tree, root)
    print()

    print('Inorder')
    inorder(tree, root)
    print()

    print('Postorder')
    postorder(tree, root)
    print()
```

[Reconstruction of a Tree](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_D)
根据前序遍历和中序遍历确定一棵树
```python
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder(root, out):
    if root == None:
        pass
    else:
        postorder(root.left, out)
        postorder(root.right, out)
        out.append(root.value)

def build_tree(pres, ins):
    if len(pres) < 1:
        return None
    else:
        node = Node(pres[0])
        index = 0
        for i in range(len(ins)):
            if ins[i] == pres[0]:
                index = i
                break
        
        node.left = build_tree(pres[1:1+index], ins[0:index])
        node.right = build_tree(pres[1+index:], ins[1+index:])
        return node


if __name__ == '__main__':
    n = int(input())
    pres = [int(num) for num in input().split(' ')]
    ins = [int(num) for num in input().split(' ')]
    root = build_tree(pres, ins)
    out = []
    postorder(root, out)
    print(str(out).replace(',', '').replace('[', '').replace(']', ''))

```

[Binary Search Tree I](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_A)
```python
class Node():
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            parentnode = curnode = self.root
            while curnode != None:
                parentnode = curnode
                if curnode.value > value:
                    curnode = curnode.left
                else:
                    curnode = curnode.right
            if value > parentnode.value:
                parentnode.right = Node(value)
            else:
                parentnode.left = Node(value)

    def preorder(self, root):
        if root == None:
            pass
        else:
            print(' %d' % root.value, end='')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root == None:
            pass
        else:
            self.inorder(root.left)
            print(' %d' % root.value, end='')
            self.inorder(root.right)

if __name__ == '__main__':
    n = int(input())
    binarytree = BinaryTree()
    for _ in range(n):
        common = input()
        if common[0] == 'i':
            binarytree.insert(int(common[7:]))
        else:
            binarytree.inorder(binarytree.root)
            print()
            binarytree.preorder(binarytree.root)
            print()
```

[Binary Search Tree II](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_B)
```python
class Node():
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            parentnode = curnode = self.root
            while curnode != None:
                parentnode = curnode
                if curnode.value > value:
                    curnode = curnode.left
                else:
                    curnode = curnode.right
            if value > parentnode.value:
                parentnode.right = Node(value)
            else:
                parentnode.left = Node(value)

    def find(self, value):
        curnode = self.root
        while curnode != None:
            if curnode.value == value:
                return True
            elif curnode.value < value:
                curnode = curnode.right
            else:
                curnode = curnode.left
        return False

    def preorder(self, root):
        if root == None:
            pass
        else:
            print(' %d' % root.value, end='')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root == None:
            pass
        else:
            self.inorder(root.left)
            print(' %d' % root.value, end='')
            self.inorder(root.right)

if __name__ == '__main__':
    n = int(input())
    binarytree = BinaryTree()
    for _ in range(n):
        common = input()
        if common[0] == 'i':
            binarytree.insert(int(common[7:]))
        elif common[0] == 'f':
            if binarytree.find(int(common[5:])):
                print('yes')
            else:
                print('no')
        else:
            binarytree.inorder(binarytree.root)
            print()
            binarytree.preorder(binarytree.root)
            print()
```

[Binary Search Tree III]()
二叉树删除的时候的三种情况（z为被删除结点）：

+ 当z没有子节点时，直接删除z
+ 当z有一个子节点时，将z的子节点直接提升
+ 当z有两个子节点时，选取**中序遍历在z后面的结点**替代z，即右结点的最左边的结点

```python
class Node():
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            parentnode = curnode = self.root
            while curnode != None:
                parentnode = curnode
                if curnode.value > value:
                    curnode = curnode.left
                else:
                    curnode = curnode.right
            if value > parentnode.value:
                parentnode.right = Node(value)
            else:
                parentnode.left = Node(value)

    def find(self, value):
        c, _ = self.findvalue(value)
        if c is None:
            return False
        else:
            return True

    def findvalue(self, value):
        parentnode = curnode = self.root
        while curnode != None:
            if value == curnode.value:
                return curnode, parentnode
            parentnode = curnode
            if value > curnode.value:
                curnode = curnode.right
            else:
                curnode = curnode.left
        return None, None
    
    def replace_child(self, parentnode, childnode, newnode):
        if parentnode == self.root:
            self.root = newnode
        elif parentnode.value > childnode.value:
            parentnode.left = newnode
        else:
            parentnode.right = newnode
    
    def delete(self, value):
        curnode, parentnode = self.findvalue(value)
        if curnode is None:
            # 没有找到这个结点，无法删除
            return False
        if curnode.left == None and curnode.right == None:
            # 被删除结点的左右子树都为空，直接将当前结点删除
            self.replace_child(parentnode, curnode, None)
        elif curnode.right == None:
            # 右子树为空，使用左子树代替
            self.replace_child(parentnode, curnode, curnode.left)
        elif curnode.left == None:
            # 左子树为空，使用右子树代替
            self.replace_child(parentnode, curnode, curnode.right)
        else:
            # 左右子树都存在的话， 找到一个代替结点
            p = curnode
            r = curnode.right
            while r.left != None:
                p = r
                r = r.left
            curnode.value = r.value
            self.replace_child(p, r, r.right)
        return True

    def preorder(self, root):
        if root == None:
            pass
        else:
            print(' %d' % root.value, end='')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root == None:
            pass
        else:
            self.inorder(root.left)
            print(' %d' % root.value, end='')
            self.inorder(root.right)

if __name__ == '__main__':
    n = int(input())
    binarytree = BinaryTree()
    for _ in range(n):
        common = input()
        if common[0] == 'i':
            binarytree.insert(int(common[7:]))
        elif common[0] == 'f':
            if binarytree.find(int(common[5:])):
                print('yes')
            else:
                print('no')
        elif common[0] == 'd':
            binarytree.delete(int(common[7:]))
        else:
            binarytree.inorder(binarytree.root)
            print()
            binarytree.preorder(binarytree.root)
            print()
```

[Treap](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_D)
Treap:
+ **binary-search-tree property**. If v is a left child of u, then v.key<u.key and if v is a right child of u, then u.key<v.key
+ **heap property**. If v is a child of u, then v.priority<u.priority
```python

```

[Complete Binary Tree](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_A)
```python
def slove(nodelist):
    for i in range(len(nodelist)):
        out = 'node %d: key = %d, ' % (i + 1, nodelist[i])
        if i > 0:
            # 注意计算父结点的时候，是向下取整(i - 1)//2
            out += 'parent key = %d, ' % (nodelist[(i - 1)//2])
        if 2 * i + 1 < len(nodelist):
            out += 'left key = %d, ' % (nodelist[2 * i + 1])
        if 2 * i + 2 < len(nodelist):
            out += 'right key = %d, ' % (nodelist[2 * i + 2])
        print(out)

if __name__ == '__main__':
    n = input()
    nodelist = [int(num) for num in input().split(' ')]
    slove(nodelist)
```

[Maximum Heap](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_B)
```python
class Heap():
    def __init__(self, numlist):
        self.datas = numlist
        self.size = len(numlist)
        self.buildMaxHeap()

    def maxHeapify(self, i):
        # 构建最大堆
        if i > self.size:
            return
        
        l = i * 2 + 1
        r = i * 2 + 2
        max_index = i

        if l < self.size and self.datas[l] > self.datas[max_index]:
            max_index = l
        if r < self.size and self.datas[r] > self.datas[max_index]:
            max_index = r
        
        if max_index != i:
            self.datas[max_index], self.datas[i] = self.datas[i], self.datas[max_index]
            self.maxHeapify(max_index)
    
    def buildMaxHeap(self):
        index = self.size // 2
        while index >= 0:
            self.maxHeapify(index)
            index -= 1

    def show(self):
        print(' ' + str(self.datas).replace(',', '').replace('[', '').replace(']', ''))


if __name__ == '__main__':
    n = input()
    numlist = [int(num) for num in input().split(' ')]
    maxheap = Heap(numlist)
    maxheap.show()
```

[Priority Queue](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C)
```python
class PriorityQueue():
    def __init__(self, numlist):
        self.datas = numlist
        self.size = len(numlist)
        self.buildMaxHeap()

    def minHeapify(self, i):
        if i > self.size:
            return
        
        l = i * 2 + 1
        r = i * 2 + 2
        min_index = i

        if l < self.size and self.datas[l] > self.datas[min_index]:
            min_index = l
        if r < self.size and self.datas[r] > self.datas[min_index]:
            min_index = r
        
        if min_index != i:
            self.datas[min_index], self.datas[i] = self.datas[i], self.datas[min_index]
            self.minHeapify(min_index)
    
    def buildMaxHeap(self):
        index = self.size // 2
        while index >= 0:
            self.minHeapify(index)
            index -= 1

    def heapIncreaseKey(self, i):
        while (i - 1) // 2 >= 0 and self.datas[i] > self.datas[(i - 1) // 2]:
            self.datas[i], self.datas[(i - 1) // 2] = self.datas[(i - 1) // 2], self.datas[i]
            i = (i - 1) // 2

    def insert(self, value):
        self.datas.append(value)
        self.heapIncreaseKey(self.size)
        self.size += 1
    
    def heapExtractMax(self):
        if self.size < 1:
            return None
        else:
            maxnum = self.datas[0]
            self.datas[0] = self.datas[self.size - 1]
            self.datas.pop(-1)
            self.size -= 1
            self.minHeapify(0)
            return maxnum
    

    def show(self):
        print(' ' + str(self.datas).replace(',', '').replace('[', '').replace(']', ''))


if __name__ == '__main__':
    maxheap = PriorityQueue([])
    while True:
        common = input()
        if common[0] == 'i':
            maxheap.insert(int(common[7:]))
        elif common == 'extract':
            print(maxheap.heapExtractMax())
        else:
            break
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


[Graph](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_A)
邻接矩阵法表示图
```python
if __name__ == '__main__':
    n = int(input())
    graph = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):
        datas = [int(num) for num in input().split(' ')]
        if datas[1] > 0:
            for j in datas[2:]:
                graph[datas[0] - 1][j - 1] = 1

    for row in graph:
        print(str(row).replace(',', '').replace('[', '').replace(']', ''))
```

[Depth First Search](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B)
这简直是我写的最差的DFS，自己看着都觉得恶心
```python


if __name__ == '__main__':
    n = int(input())
    graph = [[0 for i in range(n)] for _ in range(n)]
    frist = [0 for _ in range(n)]
    end = [0 for _ in range(n)]
    visit = [False for _ in range(n)]
    # get the group
    for i in range(n):
        datas = [int(num) for num in input().split(' ')]
        if datas[1] > 0:
            for j in datas[2:]:
                graph[datas[0] - 1][j - 1] = 1

    visit[0] = True
    frist[0] = s = 1
    stack = [0]

    while len(stack) != 0:
        point = stack.pop(-1)
        flag = False
        for i in range(n):
            if graph[point][i] == 1 and visit[i] is False:
                visit[i] = True
                flag = True
                s += 1
                frist[i] = s
                stack.append(point)
                stack.append(i)
                break
        if flag is False:
            s += 1
            end[point] = s
        
        if len(stack) == 0:
            for i in range(n):
                if visit[i] is False:
                    visit[i] = True
                    s += 1
                    frist[i] = s
                    stack.append(i)
                    break
            
    for i in range(n):
        print('%d %d %d' % (i+1, frist[i], end[i]))
```

[Breadth First Search](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C)
同样也是写的最烂的BFS
```python
if __name__ == '__main__':
    n = int(input())
    graph = [[0 for i in range(n)] for _ in range(n)]
    # get the group
    for i in range(n):
        datas = [int(num) for num in input().split(' ')]
        if datas[1] > 0:
            for j in datas[2:]:
                graph[datas[0] - 1][j - 1] = 1

    queue = [0]
    visit = [False for _ in range(n)]
    visit[0] = True
    depths = [0 for _ in range(n)]
    while len(queue) != 0:
        point = queue.pop(0)
        for i in range(n):
            if graph[point][i] == 1 and visit[i] is False:
                queue.append(i)
                visit[i] = True
                depths[i] = depths[point] + 1
        if len(queue) == 0:
            for i in range(n):
                if visit[i] is False:
                    queue.append(i)
                    depths[i] = -1
                    visit[i] = True

    for i in range(n):
        print('%d %d' % (i + 1, depths[i]))
```

[Connected Components](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_D)
无向图求连通分量：使用BFS或者并查集，感觉BFS没有并查集效率高

随后进行了尝试，发现即便是并查集，在几百万的测试数据下还是速度很慢
```python
if __name__ == '__main__':
    m, n = [int(num) for num in input().split(' ')]
    # 邻接表方法存储链表
    graph = [[] for _ in range(m)]
    visit = [False for _ in range(n)]
    # get the group
    for i in range(n):
        datas = [int(num) for num in input().split(' ')]
        graph[datas[0]].append(datas[1])
        graph[datas[1]].append(datas[0])

    # DFS
    stack = []
    visit = [False for _ in range(m)]
    color = [0 for _ in range(m)]
    c = 1

    stack.append(0)
    visit[0] = True

    while len(stack) > 0:
        point = stack[-1]
        flag = False
        for p in graph[point]:
            if visit[p] is False:
                flag = True
                visit[p] = True
                color[p] = color[point]
                stack.append(p)
                break
        if flag is False:
            stack.pop(-1)
        
        if len(stack) == 0:
            for i in range(m):
                if visit[i] is False:
                    visit[i] = True
                    color[i] = color[point] + 1
                    stack.append(i)
                    break
    o = int(input())
    for _ in range(o):
        p, q = [int(num) for num in input().split(' ')]
        if color[p] == color[q]:
            print('yes')
        else:
            print('no')

# 并查集
class Union():
    def __init__(self, n):
        self.pre = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def union(self, a, b):
        aroot = self.find(a)
        broot = self.find(b)
        if aroot == broot:
            return
        if self.rank[aroot] > self.rank[broot]:
            self.pre[broot] = self.pre[aroot]
            self.rank[broot] += self.rank[aroot]
        else:
            self.pre[aroot] = self.pre[broot]
            self.rank[aroot] += self.rank[broot]


    def find(self, n):
        while self.pre[n] != n:
            n = self.pre[n]
        return n

    def issame(self, a, b):
        if self.find(a) == self.find(b):
            return True
        return False

if __name__ == '__main__':
    m, n = [int(num) for num in input().split(' ')]
    union = Union(m)

    for _ in range(n):
        datas = [int(num) for num in input().split(' ')]
        union.union(datas[0], datas[1])

    o = int(input())
    for _ in range(o):
        p, q = [int(num) for num in input().split(' ')]
        if union.issame(p, q):
            print('yes')
        else:
            print('no')


# 效率更高的并查集
import sys
class Union():
    def __init__(self, n):
        self.pre = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def union(self, a, b):
        aroot = self.find(a)
        broot = self.find(b)
        if aroot == broot:
            return
        if self.rank[aroot] < self.rank[broot]:
            aroot, broot = broot, aroot
        self.pre[broot] = self.pre[aroot]
        if self.rank[aroot] == self.rank[broot]:
            self.rank[aroot] += 1

    def find(self, n):
        while self.pre[n] != n:
            n = self.pre[n]
        return n

    def issame(self, a, b):
        if self.find(a) == self.find(b):
            return True
        return False

if __name__ == '__main__':
    m, n = map(int, sys.stdin.readline().split())
    union = Union(m)

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        union.union(a, b)

    o = int(input())
    for _ in range(o):
        p, q = map(int, sys.stdin.readline().split())
        if union.issame(p, q):
            print('yes')
        else:
            print('no')
```