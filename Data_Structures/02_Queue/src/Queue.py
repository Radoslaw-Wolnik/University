from copy import deepcopy


class Queue:
    # self.data structure
    # self.len length of structure
    # self.size number of elements in structure
    # self.front position of first element in queue

    def __init__(self, length=10):
        self.len = length
        self.data = [None] * self.len
        self.size = 0
        self.front = 0

    def set_len(self, val):
        assert isinstance(val, int), 'Length of structure have to be an integer value'
        self.len = val

    def make_all_null(self):
        self.data = [None] * self.len
        self.size = 0

    def front(self):
        return self.data[self.front]

    def empty(self):
        if sum([1 for el in self.data if el is not None]) == 0:
            return True
        return False

    def enqueue(self, val):  # adds element to structure; add at the end
        position = (self.front + self.size) % self.len
        if self.data[position] is not None:
            self.resize()
            position = (self.front + self.size) % self.len
        self.data[position] = val
        self.size += 1

    def dequeue(self):  # returns element from structure; returns the element that was on structure longest time
        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.len
        self.size -= 1
        return val

    def resize(self):
        temp = deepcopy(self)
        self.set_len(self.len * 2)
        self.make_all_null()
        while not temp.empty():
            self.enqueue(temp.dequeue())

    def resize_new(self):
        temp = self.data
        walk = self.front
        self.set_len(self.len * 2)
        self.make_all_null()
        for i in range(len(temp)):
            self.enqueue(temp[walk])
            walk = (walk + 1) % len(temp)

    def __str__(self):
        return f'front: {self.front} size: {self.size} length: {self.len}\n' + f'{self.data}'
