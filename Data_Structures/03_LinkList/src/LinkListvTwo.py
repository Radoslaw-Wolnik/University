from src.Node import Node


class LinkListvTwo():

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = self.head  # jest 0 elementow wiec tail; = head wobec tego tail  wskazuje na head
        # self.head stanowi wyższą instancj, self.tail dziedziczy coz nie może być tail jeśli nie ma head

    def add_last(self, val):
        if self.size == 0:
            self.addFirst(val)
        else:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def del_last(self):
        if self.size == 0:
            return 'Nothing to do here'
        if self.size == 1:
            res = self.tail.item
            self.head = None
            self.tail = self.head
            self.size -= 1
            return res
        else:
            res = self.tail.item
            # self.tail = prev
            prev = None
            node = self.head
            while node.next != None:
                prev = node
                node = node.next
            self.tail = prev
            self.size -= 1
            return res

    def add_first(self, val):
        new = Node(val)
        x = self.head
        new.next = x
        self.head = new
        self.size += 1
        if self.size == 1:
            self.tail = self.head

    def del_first(self):
        if self.size == 0:
            return 'Nothing to do here'
        res = self.head.item
        x = self.head.next
        self.head = x
        self.size -= 1
        if self.size == 0:
            self.tail = self.head
        return res

    def __str__(self):
        print_val = self.head
        ret = []
        while print_val is not None:
            ret.append(print_val.item)
            print_val = print_val.next
        return str(ret)
