from stack.QueueBasedOnStack import QueueBasedOnStack

if __name__ == '__main__':
    # test queue based on 2 stacks
    Kolejka = QueueBasedOnStack()
    Kolejka.enqueue('E')
    Kolejka.enqueue(1)
    Kolejka.enqueue(2)
    Kolejka.enqueue(3)
    print(Kolejka.dequeue())
    print(Kolejka.dequeue())
    print(Kolejka.dequeue())