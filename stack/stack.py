class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(5)
s.push(10)
s.push(11)
print('Длинна стека =', s.size())

print(s.pop())
print(s.peek())


