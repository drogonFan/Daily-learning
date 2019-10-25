class MinHeap(object):
    def __init__(self, numlist):
        self._list = numlist
        self._size = len(numlist)

    def min_heapify(self, i):
        '''
        向下维护最小堆的性质,时间复杂都为O(n)
        '''
        left = 2 * i + 1
        right = 2 * i + 2
        min_index = i

        if left < self._size and self._list[left] < self._list[i]:
            min_index = left
        
        if right < self._size and self._list[right] < self._list[min_index]:
            min_index = right

        if min_index != i:
            self._list[i], self._list[min_index] = self._list[min_index], self._list[i]
            self.min_heapify(min_index)

    def build_heap(self):
        '''
        构建最小堆，时间复杂度为O(nlgn)
        '''
        i = self._size // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1
    
    def heapSort(self):
        '''
        堆排序，时间复杂都为O(nlgn)
        '''
        n = self._size - 1
        for i in range(n, 1, -1):
            self._list[i], self._list[0] = self._list[0], self._list[i]
            self._size -= 1
            self.min_heapify(0)

    def getlist(self):
        return self._list

if __name__ == '__main__':
    A = [16,14,10,8,7,9,3,2,4,1]
    mheap = MinHeap(A)
    mheap.build_heap()
    mheap.heapSort()
    print(mheap.getlist())