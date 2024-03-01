from LinkList import LinkList
from LinkListvTwo import LinkListvTwo
from TwoDirectionLinkList import TwoDirectionLinkList
from random import randint


def insertion_sort(LinkList):
    start = LinkList.head
    current = LinkList.head
    count = 0
    while current is not None:
        marker = start
        at = 0
        while marker != current:
            if current.item < marker.item:
                break
            marker = marker.next
            at += 1
        if at != count:
            LinkList.insert_at_position(current.item, at)
            LinkList.del_at_position(count)
        # print(count, current.item, at)
        # print(NodeList)
        current = current.next
        count += 1
    pass


if __name__ == '__main__':

    # test LinkList -----------------------------------------------------
    Lista01 = LinkList()
    Lista01.add_first('abc')
    Lista01.add_first('123')
    Lista01.add_first('zz')
    print(Lista01)
    Lista01.remove_first_el()
    print(Lista01)
    Lista01.del_last_el()
    print(Lista01)
    Lista01.add_first('12')
    Lista01.add_first('zz')
    print(Lista01)
    Lista01.insert_at_position('drugi', 1)
    print(Lista01)
    Lista01.del_at_position(1)
    print(Lista01)

    # test LinkList Two
    print('-' * 10 + '\n' * 2)
    link = LinkListvTwo()
    link.add_last('a')
    print(link)
    link.del_first()
    print(link)
    link.del_last()
    print(link)
    link.add_first('A')
    print(link)
    link.del_last()
    print(link)
    link.add_last('B')
    print(link)
    link.add_last('C')
    print(link)
    link.add_first('Z')
    print(link)
    link.del_last()
    print(link)

    link.del_first()
    print(link)

    # test Two direction LinkList
    link = TwoDirectionLinkList()
    link.add_last('a')
    print(link)
    link.del_first()
    print(link)
    link.del_last()
    print(link)
    link.add_first('A')
    print(link)
    link.del_last()
    print(link)
    link.add_last('B')
    print(link)
    link.add_last('C')
    print(link)
    link.add_first('A')
    print(link)
    link.del_last()
    print(link)
    link.del_first()
    print(link)

    # test insertion sort sort link list --------------------------------------------------------
    test01 = [-19, 12, 19, 14, -12, -13, 18, 3, -4, -7]
    test = [randint(-20, 20) for _ in range(10)]
    ToSort = LinkList()
    randSort = LinkList()

    for el in test01:
        ToSort.add_last(el)
    for el in test:
        randSort.add_last(el)

    print(ToSort)
    insertion_sort(ToSort)
    print(ToSort)
    print('\n-----------------------------------------\n')

    print(randSort)
    insertion_sort(randSort)
    print(randSort)
