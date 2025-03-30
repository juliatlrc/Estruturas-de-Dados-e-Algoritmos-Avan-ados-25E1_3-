class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        while index > 0 and self.heap[self._parent(index)] > self.heap[index]:
            self.heap[self._parent(index)], self.heap[index] = self.heap[index], self.heap[self._parent(index)]
            index = self._parent(index)

    def _heapify_down(self, index):
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

# Testando a MinHeap
min_heap = MinHeap()

min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(15)
min_heap.insert(2)
min_heap.insert(8)

print("Heap após inserções:", min_heap.heap)

print("Removendo o menor elemento:", min_heap.pop())  
print("Heap após remoção:", min_heap.heap)
