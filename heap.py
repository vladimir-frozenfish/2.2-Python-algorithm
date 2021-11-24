"""структура данных Куча - Heap"""


class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):  # O(log(n))
        """Поднимает последний элемент на верх кучи"""
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2
            # меняем местами

    def extract_min(self):  # O(log(n))
        """Достает минимум из кучи"""
        if not self.size:  # если куча пустая
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.shift_down(0)
        return tmp

    def shift_down(self, i):  # O(log(n))
        """Переместить первый новый элемент вниз"""
        while 2 * i + 1 < self.size:
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j:
                break  # нет смысла смотреть вниз
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j
            # обмен 2х значений


def heapify(arr):
    heap = Heap()
    for item in arr:
        heap.insert(item)
    return heap


def get_get_sorted_arr(heap):
    arr = []
    while heap.size:
        arr.append(heap.extract_min())
    return arr


def heap_heapify_fast(arr):
    heap = Heap()
    heap.values = arr[:]
    heap.size = len(arr)
    for c in reversed(range(heap.size // 2)):
        heap.shift_down(c)
    return heap
