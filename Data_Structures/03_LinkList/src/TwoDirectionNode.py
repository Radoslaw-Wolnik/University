class TwoDirectionNode():
    def __init__(self, item = None):
        self.prev = None
        self.item = item
        self.next = None
    def __str__(self):
        return f'prev: {self.prev is not None}, item: {self.item}, next: {self.next is not None}'
