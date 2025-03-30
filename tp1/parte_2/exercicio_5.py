class HeapIndexOperations:
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

heap_ops = HeapIndexOperations()

print(heap_ops.parent(2)) 
print(heap_ops.left_child(1)) 
print(heap_ops.right_child(1))  
