from stack.Stack import Stack


if __name__ == '__main__':
    test = Stack()
    example = [1, 2, 3, 4, 5, 6, 7, 'a']

    for el in example:
        test.push(el)
        print(test)
    print()

    while not test.is_empty():
        x = test.pop()
        print(f'pop = {x}, test = {test}')
    print('\n')
    print(test)
    print()

    for el in example:
        test.push(el)
    print(test)
    for _ in range(3):
        test.pop()