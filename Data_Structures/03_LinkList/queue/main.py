from queue.Queue import Queue

if __name__ == '__main__':
    test = Queue()
    example = [1, 2, 3, 4, 5, 6, 7, 'a']

    for el in example:
        test.enqueue(el)
        print(test)
    print()

    while not test.is_empty():
        print(test.dequeue(), ' ', end='')  # end = ''
    print('\n')
    print(test)
    print()

    for el in example:
        test.enqueue(el)
    print(test)
    for _ in range(3):
        test.dequeue()
    print(test)
