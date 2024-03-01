# kolejka Fifo in lista cykliczna
class QueueCycle():

    def __init__(self, n=10):
        self.items = n * [None]
        self.size = 0
        self._size = n
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self._size == self.size

    def enqueue(self, item):
        if self.isFull():
            raise ValueError('Fifo is Full')
        self.items[self.tail] = item
        self.size += 1
        if self.tail == self._size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Fifo is Empty')
        res = self.items[self.head]
        self.items[self.head] = None
        self.size -= 1
        if self.head == self._size - 1:
            self.head = 0
        else:
            self.head += 1
        return res

    def __str__(self):
        return str(self.items)