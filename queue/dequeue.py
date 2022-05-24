class Dequeue:
    """класс ограниченной (кольцевой) двусторонней очереди - n"""
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n      # максимально возможное количество элементов в очереди
        self.head = 0       # индекс, по которому нужно извлекать элемент, если очередь не пустая
        self.tail = 0       # индекс, по которому нужно добавлять элемент, если в очереди есть место
        self.size = 0       # размер очереди

    def is_empty(self):
        """возвращает True если очередь пустая"""
        return self.size == 0

    def push_back(self, x):
        """добавление элемента в конец очереди"""
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def push_front(self, x):
        """добавление элемента в начало очереди"""
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = x
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        """возвращение и удаление первого добавленного элемента"""
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        """возвращение и удаление последнего добавленного элемента"""
        if self.is_empty():
            return 'error'
        x = self.queue[self.tail-1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x


q = Dequeue(10)
q.push_back(10)
q.push_back(12)
q.push_back(5)
q.push_back(8)
print(q.queue)

print('pop_back:', q.pop_back())
print(q.queue)

q.push_back(23)
q.push_back(28)
print(q.queue)

print('pop_back:', q.pop_back())
print('pop_front:', q.pop_front())
print(q.queue)

q.push_back(11)
q.push_back(12)
print(q.queue)

print('push_front')
q.push_front(5)
print(q.queue)

print('push_front')
q.push_front(10)
print(q.queue)

print('push_front')
q.push_front(25)
print(q.queue)

print('pop_back:', q.pop_back())
print(q.queue)

print('pop_front:', q.pop_front())
print(q.queue)

