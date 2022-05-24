class Node:
    """класс односвязного списка"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class QueueNodeList:
    """класс очереди построенной на связном списке"""
    def __init__(self):
        self.head = None
        self.size = 0       # размер очереди

    def is_empty(self):
        """возвращает True если очередь пустая"""
        return self.size == 0

    def put(self, x):
        """добавление элемента в конец очереди"""
        if self.head is None:
            self.head = Node(x)
            self.size = 1
            self.end = self.head
        else:
            self.new_node = Node(x)
            self.end.next = self.new_node
            self.end = self.new_node
            self.size += 1

    def get(self):
        """возвращает первый добавленный элемент очереди и
        удалет его из связного списка"""
        if self.is_empty():
            return 'error'
        self.value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return self.value

    def print_queue(self):
        self.current = self.head
        while self.current:
            print(self.current.value, end=" -> ")
            self.current = self.current.next
        print("None")


q = QueueNodeList()
q.put(10)
q.print_queue()

q.put(5)
q.print_queue()

q.put(7)
q.print_queue()

q.put(25)
q.print_queue()

print(q.get())
q.print_queue()

print(q.get())
q.print_queue()

print(q.get())
print(q.get())
print(q.get())



