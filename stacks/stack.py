class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.is_empty():
            raise BaseException('stacks is empty')
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
