from src.Queue import Queue
from src.QueueCycle import QueueCycle


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

    # test queue cycle ------------------------------------------
    Try03 = QueueCycle(10)
    example = [1, 2, 3, 4, 5, 6, 7, 'a']

    for el in example:
        Try03.enqueue(el)
    print(Try03)
    print()

    while not Try03.is_empty():
        print(Try03.dequeue(), ' ', end='')  # end = ''
    print('\n')
    print(Try03)
    print()

    for el in example:
        Try03.enqueue(el)
    print(Try03)
    for _ in range(3):
        Try03.dequeue()
    print(Try03)

    print('\n' * 2)

    Try04 = QueueCycle(2)
    example = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for el in example:
        print(Try04)
        Try04.enqueue(el)
