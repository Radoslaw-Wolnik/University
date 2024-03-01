# dodawanie dwoch list dowiazanych
from src.LinkList import LinkList


class AddableLinkList(LinkList):

    def __add__(self, other):
        res = LinkList()
        a = self.head
        b = other.head

        smaller = self.size
        if other.size < smaller:
            smaller = other.size

        przeniesienie = 0
        for _ in range(smaller):
            assert isinstance(a.item, (int, float)) or isinstance(b.item, (int, float)), 'Blad'
            suma = a.item + b.item
            res.add_last(suma % 10 + przeniesienie)
            przeniesienie = suma // 10
            a = a.next
            b = b.next

        r = None
        if self.size > smaller:
            r = a
        elif other.size > smaller:
            r = b
        if self.size != other.size:
            while r != None:
                assert isinstance(r.item, (int, float)), 'Blad'
                res.add_last(r.item)
                r = r.next

        return res
