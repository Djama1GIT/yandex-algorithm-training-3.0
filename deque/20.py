class Heap:
    """
    max heap
    """

    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.rebuild()

    def extract(self):
        if len(self.heap) == 0:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self.sift()
        return item

    def rebuild(self):
        item_id = len(self.heap) - 1
        while item_id > 0 and self.heap[item_id] > self.heap[(item_id - 1) // 2]:
            self.heap[item_id], self.heap[(item_id - 1) // 2] = self.heap[(item_id - 1) // 2], self.heap[item_id]
            item_id = (item_id - 1) // 2

    def sift(self):
        item_id = 0

        while True:
            left_child_id = item_id * 2 + 1 if (len(self.heap) > (item_id * 2 + 1)) else None
            right_child_id = item_id * 2 + 2 if (len(self.heap) > (item_id * 2 + 2)) else None

            if left_child_id is None and right_child_id is None:
                break

            left_child = self.heap[left_child_id] if left_child_id is not None else float('-inf')
            right_child = self.heap[right_child_id] if right_child_id is not None else float('-inf')

            if max(left_child, right_child) <= self.heap[item_id]:
                break

            if left_child > right_child:
                self.heap[item_id], self.heap[left_child_id] = self.heap[left_child_id], self.heap[item_id]
                item_id = left_child_id
            else:
                self.heap[item_id], self.heap[right_child_id] = self.heap[right_child_id], self.heap[item_id]
                item_id = right_child_id


class HeapSort:
    def __init__(self, arr):
        self.sorted = []
        self.heap = Heap()
        for i in arr:
            self.heap.insert(i)

    def sort(self):
        while len(self.heap.heap):
            self.sorted += [self.heap.extract()]
        return list(reversed(self.sorted))


input()
print(*HeapSort(list(map(int, input().split()))).sort())
