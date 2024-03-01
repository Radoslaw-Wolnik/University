from src.TwoDirectionLinkList import TwoDirectionLinkList as LinkList


class Queue():

    def __init__(self):
        self.core = LinkList()

    def __str__(self):
        return str(self.core)

    def dequeue(self):
        return self.core.del_last()

    def enqueue(self, item):
        self.core.add_first(item)

    def is_empty(self):
        return self.core.size == 0

