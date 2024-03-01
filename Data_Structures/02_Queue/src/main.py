from src.Queue import Queue
from src.QueueBasedOnStack import QueueBasedOnStack


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

    # test queue based on 2 stacks
    Kolejka = QueueBasedOnStack()
    Kolejka.enqueue('E')
    Kolejka.enqueue(1)
    Kolejka.enqueue(2)
    Kolejka.enqueue(3)
    print(Kolejka.dequeue())
    print(Kolejka.dequeue())
    print(Kolejka.dequeue())