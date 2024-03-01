from src.Node import Node


class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_last(self, item):
        new = Node(item)
        if self.is_empty():
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
        self.size += 1

    # nie dziala dlatego ze usuwa referencje do miejsca w pamieci a nie wezel
    # def delLast(self):
    #     lastNode = self.head
    #     while lastNode is not None:
    #         lastNode = lastNode.next
    #     del lastNode

    def del_last_el(self):
        last_node = self.head
        prev_node = None
        while last_node.next is not None:
            prev_node = last_node
            last_node = last_node.next
        prev_node.next = None
        self.size -= 1
        return last_node

    def add_first(self, item):
        new = Node(item)
        x = self.head
        new.next = x
        self.head = new
        self.size += 1

    def remove_first_el(self):
        res = self.head.item
        x = self.head.next
        self.head = x
        self.size -= 1
        return res

    def insert_at_position(self, val, position):
        if position > self.size or position == -1:
            self.add_last(val)
        elif position == 0:
            self.add_first(val)
        else:
            new_node = Node(val)
            iterator = 0
            current_node = self.head
            prev_node = None  # ?? there was no this line and i don't know how it did get to prev_node outside of if
            while True:
                if iterator == position:
                    new_node.next = current_node
                    prev_node.next = new_node
                    break
                prev_node = current_node
                current_node = current_node.next
                iterator += 1
        self.size += 1

    def del_at_position(self, position):
        if position > self.size or position == -1:
            self.size -= 1
            return self.del_last_el()
        elif position == 0:
            self.size -= 1
            return self.remove_first_el()
        else:
            res = None
            iterator = 0
            prev_node = None
            current_node = self.head
            while True:
                if iterator == position:
                    res = current_node
                    prev_node.next = current_node.next
                    break
                prev_node = current_node
                current_node = current_node.next
                iterator += 1
            self.size -= 1
            return res

    def __str__(self):
        print_val = self.head
        ret = []
        while print_val is not None:
            ret.append(print_val.item)
            print_val = print_val.next
        return str(ret)
