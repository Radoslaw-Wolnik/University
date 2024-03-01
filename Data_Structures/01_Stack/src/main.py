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
