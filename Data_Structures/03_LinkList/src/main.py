from src.Queue import Queue
from LinkList import LinkList


if __name__ == '__main__':
    # test Queue -----------------------------------------------------
    Try01 = Queue()
    example = [1, 2, 3, 4, 5, 6, 7, 'a']

    for el in example:
        Try01.enqueue(el)
    print(Try01)
    print()

    while not Try01.empty():
        print(Try01.dequeue(), ' ', end='')  # end = ''
    print('\n')
    print(Try01)
    print()

    for el in example:
        Try01.enqueue(el)
    print(Try01)
    for _ in range(3):
        Try01.dequeue()
    print(Try01)

    # test Queue cd -----------------------------------------------------
    Try02 = Queue(2)

    example = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for el in example:
        print(Try02)
        Try02.enqueue(el)

    print(Try02, '\n')

    while not Try02.empty():
        print(Try02.dequeue(), ' ', end='')  # end = ''
    print('\n')
    print(Try02)

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
