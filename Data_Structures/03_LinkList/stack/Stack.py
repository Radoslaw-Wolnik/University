# Stack based on linkList
from src.LinkList import LinkList


class Stack():

    def __init__(self):
        self.core = LinkList()

    def __str__(self):
        return str(self.core)

    def pop(self):
        return self.core.remove_first_el()

    def push(self, item):
        self.core.add_first(item)

    def is_empty(self):
        return self.core.size == 0
