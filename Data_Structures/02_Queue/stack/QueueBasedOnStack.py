from stack.Stack import Stack


class QueueBasedOnStack:
    def __init__(self):
        self.One = Stack()
        self.Two = Stack()

    def enqueue(self, val):
        self.One.push(val)

    def dequeue(self):
        res = None
        while self.One.peak() != 'Stack is empty':
            self.Two.push(self.One.pop())
        res = self.Two.pop()
        while self.Two.peak() != 'Stack is empty':
            self.One.push(self.Two.pop())
        return res
