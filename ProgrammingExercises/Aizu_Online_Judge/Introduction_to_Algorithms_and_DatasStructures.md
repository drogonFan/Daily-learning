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