from src.LinkList import LinkList


class ReversibleLinkList(LinkList):

    def reverse_self(self):
        prev = None
        current = self.head
        while current.next is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        current.next = prev
        self.head = current

    def reverse_one(self):
        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # current.next = prev
        self.head = prev

    def reverse_recursive(self):
        pass
        # pomyslec jak zapisac
