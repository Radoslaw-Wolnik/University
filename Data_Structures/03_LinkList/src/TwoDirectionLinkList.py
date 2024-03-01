# or two directional link list
from src.TwoDirectionNode import TwoDirectionNode as Node


class TwoDirectionLinkList():

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def add_last(self, val):
        if self.size == 0:
            self.addFirst(val)
        else:
            newNode = Node(val)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def del_last(self):
        if self.size == 0:
            return 'Nothing to do here'
        if self.size == 1:
            res = self.tail.item
            self.tail = None
            self.head = None
            self.size -= 1
            return res
        else:
            res = self.tail.item
            self.tail = self.tail.prev
            self.size -= 1
            return res

    def add_first(self, val):
        new = Node(val)
        if self.size == 0:
            self.head = new
            self.tail = self.head
        else:
            x = self.head
            new.next = x
            x.prev = new
            self.head = new
        self.size += 1

    def del_first(self):
        # res = None
        if self.size == 0:  # or self.head = None
            return 'Nothing to do here'
        elif self.size == 1:  # or self.head.next = None
            res = self.head.item
            self.head = None
            self.tail = None
        else:
            res = self.head.item
            x = self.head.next
            self.head = x
            self.head.prev = None
        self.size -= 1
        return res

    #    from first to last (also a way to check wheather all links work)
    #    def __str__(self):
    #        print_val = self.head
    #        ret = []
    #        while print_val != None:
    #            ret.append(print_val.item)
    #            print_val = print_val.next
    #        return str(ret)

    #   from last to first
    def __str__(self):
        print_val = self.tail
        ret = []
        while print_val is not None:
            ret.append(print_val.item)
            print_val = print_val.prev
        ret.reverse()
        return str(ret)