from src.Stack import Stack


def count_postfix(exp):
    operators = ['+', '-', '*', '/']
    result = Stack()
    exp = exp.split()

    for el in exp:
        if el in operators:
            if not result.is_empty():
                b = result.get()
                a = result.get()
                if el == '+':
                    a = a + b
                elif el == '-':
                    a = a - b
                elif el == '/':
                    a = a / b
                elif el == '*':
                    a = a * b
                result.add(a)
        else:
            result.add(float(el))

    return result.get()


def infix_to_postfix(exp):
    operators = ['+', '-', '*', '/']
    res = ''
    stos = Stack()
    exp = exp.split(' ')
    for element in exp:
        if element == '(':
            pass
            # nothing?

        elif element == ')':
            if not stos.is_empty():
                res += stos.get() + ' '

        elif element in operators:
            stos.add(element)

        else:
            res += element + ' '

    return res


def postfix_to_infix(exp):
    operators = ['+', '-', '*', '/']
    Stos = Stack()
    exp = exp.split(' ')[:-1]
    for element in exp:
        if element in operators:
            b = Stos.get()
            a = Stos.get()
            Stos.add('(' + a + element + b + ')')
        else:
            Stos.add(element)
    return Stos.get()


def infix_bracket_check(exp):
    operators = ['+', '-', '*', '/']
    result = Stack()
    exp = exp.split()

    for el in exp:
        if el == '(':
            pass
        elif el in operators:
            result.add(el)
        elif el == ')':
            b = result.get()
            operation = result.get()
            a = result.get()
            if operation == '+':
                a = a + b
            elif operation == '-':
                a = a - b
            elif operation == '/':
                a = a / b
            elif operation == '*':
                a = a * b
            result.add(a)

        else:
            result.add(float(el))

    return result.get()


# without Stack
def system_repr(system, number):
    representation = []
    while number > 0:
        representation.append(number%system)
        number = number//system
    return representation


# with Stack
def system_repr_stack(system, number):
    representation = Stack()
    while number > 0:
        representation.add(number%system)
        number = number//system
    return representation


def decode(text):
    stos = Stack()
    for el in text:
        if el in [str(x) for x in range(0, 10)]:
            stos.push(int(el))
        elif el == ']':
            temp = [stos.pop()]
            while stos.peak() != '[':
                temp.append(stos.pop())
            stos.pop()  # usuwanie [
            multiplier = stos.pop()
            temp.reverse()
            stos.push(''.join(temp) * multiplier)
        else:
            stos.push(el)
    res = []
    while not stos.isEmpty():
        res.append(stos.pop())
    res.reverse()
    return ''.join(res)


if __name__ == '__main__':
    x = "20 10 + 75 45 - *"
    temp = count_postfix(x)
    print("equation: " + x + f"\nsolved: {temp}")

    x = '( 10 + 2 )'
    y = '( ( 10 + 2 ) * 3 )'
    z = '( ( 10 + 2 ) * ( 2 + 3 ) )'
    print(infix_to_postfix(x))
    print(infix_to_postfix(y))
    print(infix_to_postfix(z))

    x = '10 2 + '
    y = '10 2 + 3 * '
    z = '10 2 + 2 3 + * '
    print(postfix_to_infix(x))
    print(postfix_to_infix(y))
    print(postfix_to_infix(z))

    tryEquation = '( 11 + ( ( 22 + 3 ) * ( 44 - 52 ) ) )'  # -189
    print(infix_bracket_check(tryEquation))


    # representing numbers in different base systems
    print(system_repr(2, 8))
    print(system_repr_stack(2, 8))
    print(system_repr_stack(3, 8))

    # decode
    s1 = '3[a]2[bc]'
    s2 = '3[a2[c]]'
    s3 = '2[abc]3[cd]ef'

    print(s1)
    print(decode(s1))
    print(s2)
    print(decode(s2))
    print(s3)
    print(decode(s3))
