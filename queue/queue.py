class Queue:
    """класс ограниченной очереди - n"""
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n      # максимально возможное количество элементов в очереди
        self.head = 0       # индекс, по которому нужно извлекать элемент, если очередь не пустая
        self.tail = 0       # индекс, по которому нужно добавлять элемент, если в очереди есть место
        self.size = 0       # размер очереди

    def is_empty(self):
        """возвращает True если очередь пустая"""
        return self.size == 0

    def push(self, x):
        """добавление элемента в конец очереди"""
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        """удаление первого добавленного элемента"""
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        """возвращает последний добавленный элемент"""
        return None if self.is_empty() else self.queue[self.tail - 1]


q = Queue(10)
print(q.peek())

q.push(5)
q.push(3)
q.push(10)
print(q.peek())
print(q.queue)
q.pop()
print(q.queue)
