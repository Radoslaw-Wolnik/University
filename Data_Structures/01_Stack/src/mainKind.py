from StackKind import StackKind as Stack
# all of this is implemented on some weird stack
# and the functions are like super long
# and im not sure if they aren't just poorly written functions from main
# because they seem to do the same thing


def check_expression(expression):
    stack_exp = Stack('ending')
    for character in expression:
        stack_exp.add(character)
    left = 0
    right = 0
    for _ in range(len(expression)):
        temp = stack_exp.get()
        if temp == '(':
            left += 1
        if temp == ')':
            right += 1
    if left == right:
        return True
    else:
        return False


def check_expression_all(expression):
    stack_exp = Stack('ending')
    for character in expression:
        stack_exp.add(character)
    curve = 0
    square = 0
    for _ in range(len(expression)):
        temp = stack_exp.get()
        if temp == '(':
            curve += 1
        if temp == ')':
            curve -= 1
        if temp == '[':
            square += 1
        if temp == ']':
            square -= 1

    if curve == 0 and square == 0:
        return True
    else:
        return False


def check_expression_all_v2(expression):
    stack_exp = Stack('ending')
    for character in expression:
        stack_exp.add(character)
    curve = 0
    square = 0
    prev = None
    for i in range(len(expression)):
        temp = stack_exp.get()
        if temp == '[':
            square += 1
        if temp == ']':
            if square == 0:
                break
            if curve > 0 and square == 0:
                break
            square -= 1
        if temp == '(':
            curve += 1
        if temp == ')':
            if curve == 0:
                break
            if square > 0 and curve == 0:
                break
            curve -= 1
        prev = temp

    if curve == 0 and square == 0:
        return True
    else:
        return i


def postfiksowe(exp):
    exp = [character for character in exp if character != ' ']  # del spacebars, change to list
    Exp_stack = Stack('ending')
    # print('expression:', exp)
    operators = [_ for _ in '+-/*']

    if '(' in exp or ')' in exp:  # condition of recursion
        curve = 0
        square = 0
        start = 0
        end = 0
        operation = ''
        op_i = 0
        for i in range(len(exp)):

            if exp[i] == '(':
                if curve == 0:
                    start = i
                curve += 1

            if exp[i] == ')':
                curve -= 1
                if curve == 0:
                    end = i

            if exp[i] in operators and curve == 0:  # jesli nie byla nawiasow ale jest operator np '41 + (2 * 3)'
                op_i = i
                operation = exp[i]
                Exp_stack.add(''.join(exp[:op_i]))
                Exp_stack.add(''.join(exp[op_i + 1:]))
                break

            if exp[i] in operators and end != 0:  # jesli sa nawiasy np '(41 * 2) +'
                operation = exp[i]
                op_i = i
                Exp_stack.add(''.join(exp[start:end + 1]))
                start = 0
                end = 0

            if operation != '' and end != 0:  # jesli to jest drugie wyrazeni z nawiasem np '(41 * 2) + (7 / 8)'
                Exp_stack.add(''.join(exp[start:end + 1]))

        left = Exp_stack.get()
        right = Exp_stack.get()
        # print('left: ', left, '  right: ', right, 'operator:', operation)
        if right == 'Stack is empty' and left != 'Stack is empty':  # jesli poierwsze wyrazenie ma nawiasy a drugie nie
            right = ''.join(exp[op_i + 1:])  # np '(2 * 3) + 41'

        if '(' in left and ')' in left:
            left = '(' + postfiksowe(left[1:-1]) + ')'
        if '(' in right and ')' in right:
            right = '(' + postfiksowe(right[1:-1]) + ')'
        Exp_stack.add(left)
        Exp_stack.add(right)
        Exp_stack.add(operation)

    elif sum([1 for character in exp if character in operators]) == 0:  # only number, exit recursion
        return exp

    else:  # exit recursion
        start = 0
        operation = ''
        for i in range(len(exp)):
            if exp[i] in operators and start == 0:
                operation = exp[i]
                end = i - 1
                Exp_stack.add(''.join(exp[start:end + 1]))
                start = i + 1
                break

        end = len(exp)
        Exp_stack.add(''.join(exp[start:end]))

        left = Exp_stack.get()
        right = Exp_stack.get()

        # return left + ';' + right + ';' + operation # for better notation to count anything uncomment here <---
        return left + ' ' + right + ' ' + operation  # and comment here

    left = Exp_stack.get()
    right = Exp_stack.get()
    operation = Exp_stack.get()
    # return left + ';' + right + ';' + operation # for better notation to count anything uncomment here <---
    return left + ' ' + right + ' ' + operation  # and comment here


def postfiksowe_better_notation(exp):
    exp = [character for character in exp if character != ' ']  # del spacebars, change to list
    Exp_stack = Stack('ending')
    # print('expression:', exp)
    operators = [_ for _ in '+-/*']

    if '(' in exp or ')' in exp:  # condition of recursion
        curve = 0
        square = 0
        start = 0
        end = 0
        operation = ''
        op_i = 0
        for i in range(len(exp)):

            if exp[i] == '(':
                if curve == 0:
                    start = i
                curve += 1

            if exp[i] == ')':
                curve -= 1
                if curve == 0:
                    end = i

            if exp[i] in operators and curve == 0:  # jesli nie byla nawiasow ale jest operator np '41 + (2 * 3)'
                op_i = i
                operation = exp[i]
                Exp_stack.add(''.join(exp[:op_i]))
                Exp_stack.add(''.join(exp[op_i + 1:]))
                break

            if exp[i] in operators and end != 0:  # jesli sa nawiasy np '(41 * 2) +'
                operation = exp[i]
                op_i = i
                Exp_stack.add(''.join(exp[start:end + 1]))
                start = 0
                end = 0

            if operation != '' and end != 0:  # jesli to jest drugie wyrazeni z nawiasem np '(41 * 2) + (7 / 8)'
                Exp_stack.add(''.join(exp[start:end + 1]))

        left = Exp_stack.get()
        right = Exp_stack.get()
        # print('left: ', left, '  right: ', right, 'operator:', operation)
        if right == 'Stack is empty' and left != 'Stack is empty':  # jesli poierwsze wyrazenie ma nawiasy a drugie nie
            right = ''.join(exp[op_i + 1:])  # np '(2 * 3) + 41'

        if '(' in left and ')' in left:
            left = '(;' + postfiksowe_better_notation(left[1:-1]) + ';)'
        if '(' in right and ')' in right:
            right = '(;' + postfiksowe_better_notation(right[1:-1]) + ';)'
        Exp_stack.add(left)
        Exp_stack.add(right)
        Exp_stack.add(operation)

    elif sum([1 for character in exp if character in operators]) == 0:  # only number, exit recursion
        return exp

    else:  # exit recursion
        start = 0
        operation = ''
        for i in range(len(exp)):
            if exp[i] in operators and start == 0:
                operation = exp[i]
                end = i - 1
                Exp_stack.add(''.join(exp[start:end + 1]))
                start = i + 1
                break

        end = len(exp)
        Exp_stack.add(''.join(exp[start:end]))

        left = Exp_stack.get()
        right = Exp_stack.get()

        return left + ';' + right + ';' + operation  # for better notation to count anything uncomment here <---
        # return left + ' ' + right + ' ' + operation  # and comment here

    left = Exp_stack.get()
    right = Exp_stack.get()
    operation = Exp_stack.get()
    return left + ';' + right + ';' + operation  # for better notation to count anything uncomment here <---
    # return left + ' ' + right + ' ' + operation  # and comment here


# Zadanie 6
# napisz program ktory sprawdza czy nawiasy sa dobrze a potem oblicza wyrazenie

# I'm not changing the postfiksowe function to be working with square brackets
# sorry

# check_expression - sprawdza nawiasy
# postfiksowe_better_notation - zmienia wyrazenie na postfixowy zapis z ';' jako rozdzielaniem czesci wyrazenia

def part(expression):  # dzieli na czesci wedlug nawiasow
    # print(expression, 'beginning')
    operation = expression[-1]
    expression = expression[:-1]
    part1 = ''
    part2 = ''
    parts = []
    brackets = 0
    start = 0
    end = 0
    # print(expression, 'list')

    if not ('(' in expression):  # dwie liczby
        part1 = expression[0]
        part2 = expression[1]

    else:  # dwa nawiasy lub nawias i jedna liczba
        for i in range(len(expression)):
            if expression[i] == '(':
                if brackets == 0:
                    start = i
                brackets += 1

            if expression[i] == ')':
                brackets -= 1
                if brackets == 0:
                    end = i
                    # print(expression[start+1:end])
                    parts.append(expression[start + 1:end])
    if len(parts) == 2:  # dwa nawiasy
        part1 = parts[0]
        part2 = parts[1]
    elif len(parts) == 1:  # jeden nawias i jedna liczba
        part1 = parts[0]
        part2 = expression[:start] + expression[end + 1:]
        part2 = part2[0]

    # print('part1: ', part1, 'part2:', part2)
    if isinstance(part1, (int, float)) and isinstance(part2, (int, float)):  # jesli obie czesci to liczby
        return count(part1, part2, operation)
    if isinstance(part1, (int, float)) or isinstance(part2, (int, float)):  # jesli jedna czesc to liczba
        if isinstance(part1, (int, float)):
            return count(part(part2), part1, operation)
        else:
            return count(part(part1), part2, operation)
    return count(part(part1), part(part2), operation)  # jesli zadna czesc nie jest liczba


def count(num1, num2, operation):
    # print(num1,num2,operation, 'count')
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    # if operation == '//':
    return num1 / num2


def count_value(expression):
    # check if expression is okay
    numbers = [_ for _ in '0123456789']
    operators = [_ for _ in '+-/*()']
    if sum(1 for _ in expression if _ in numbers) == 0:
        return 'You need numbers to count dear young human'
    if ']' in expression or '[' in expression:
        return "I don't like square brackets"
    if check_expression(expression) == False:
        return 'Your expression is written poorly :('

    # it's okay
    expression = postfiksowe_better_notation(expression)
    expression = expression.split(';')
    for i in range(len(expression)):
        if expression[i] in operators:
            pass
        else:
            expression[i] = int(expression[i])
    # print(expression)
    value = 0

    while not (isinstance(expression, (int, float))):
        if '(' in expression:
            expression = part(expression)

        else:
            expression = count(expression[0], expression[1], expression[2])

    return expression


if __name__ == "__mainKind__":
    print("Kind")
    # test StackKind
    Stack01 = Stack('ending')
    for el in [1, 2, 3, 4, 'Ania', 'Kasia', 'Jola', -1, 5]:
        Stack01.add(el)
    print(Stack01)
    for i in range(10):
        print(Stack01.get())

    print()
    print('-' * 10)
    print('-' * 10)
    print()

    Stack02 = Stack('beginning')
    for el in [1, 2, 3, 4, 'Ania', 'Kasia', 'Jola', -1, 5]:
        Stack02.add(el)
    print(Stack02)
    for i in range(10):
        print(Stack02.get())

    print('\n' + '-' * 10 + '\n')

    # wrong input
    # Stack03 = Stack('mandarynka')
    Stack03 = Stack('beginning')
    try:
        Stack03.add(('Kasia', 1))
    except Exception as e:
        print(e)

    # test check_expression function
    wyrazenie1 = '((()))'
    wyrazenie2 = '((()'
    wyrazenie3 = '(((((((())))))'

    print(check_expression(wyrazenie1))
    print(check_expression(wyrazenie2))
    print(check_expression(wyrazenie3))


    # test check_expression_all
    wyrazenie1 = '[((()))]'
    wyrazenie2 = '((](]))'
    wyrazenie3 = '(((((((([]))))))'
    wyrazenie4 = '[([(](])))'

    print(check_expression_all(wyrazenie1))
    print(check_expression_all(wyrazenie2))
    print(check_expression_all(wyrazenie3))
    print(check_expression_all(wyrazenie4))

    # test check_expression_all_v2
    exp1 = '(()('
    exp2 = 'foo(bar[i)'
    exp3 = '[()()]'
    exp4 = '([][])'

    print(check_expression_all_v2(exp1))  # okay
    print(check_expression_all_v2(exp2))  # okay
    print(check_expression_all_v2(exp3))  # okay
    print(check_expression_all_v2(exp4))  # okay

    # change expression to postfix notation tests
    expression0 = '41 * 2'  # 41 2 *
    expression1 = '(41 * 2) + (7 / 8)'  # (41 2 *) (7 8 /) +
    expression2 = '(2 * 3) + 41'  # ((2 3 *) 41 +)
    expression2_pol = '41 + (2 * 3)'  # (41 (2 3 *) +)
    expression3 = '(41 + (2 * 3)) / (2 + 1)'  # (4 (2 3 *) +) (2 1 +) /
    print(postfiksowe(expression0))  # works
    print(postfiksowe(expression1))  # works
    print(postfiksowe(expression2))  # works
    print(postfiksowe(expression2_pol))  # works
    print(postfiksowe(expression3))  # works

    # same but with ; witch I thought was apparently better
    expression0 = '41 * 2'  # 41 2 *
    expression1 = '(41 * 2) + (7 / 8)'  # (41 2 *) (7 8 /) +
    expression2 = '(2 * 3) + 41'  # ((2 3 *) 41 +)
    expression2_pol = '41 + (2 * 3)'  # (41 (2 3 *) +)
    expression3 = '(41 + (2 * 3)) / (2 + 1)'  # (4 (2 3 *) +) (2 1 +) /
    print(postfiksowe_better_notation(expression0))  # works
    print(postfiksowe_better_notation(expression1))  # works
    print(postfiksowe_better_notation(expression2))  # works
    print(postfiksowe_better_notation(expression2_pol))  # works
    print(postfiksowe_better_notation(expression3))  # works


    # idk what happens here

    expression0 = '41 * 2'  # 41 2 *
    expression1 = '(41 * 2) + (8 / 8)'  # (41 2 *) (7 8 /) +
    expression2 = '(2 * 3) + 41'  # ((2 3 *) 41 +)
    expression3 = '41 + (2 * 3)'  # (41 (2 3 *) +)
    expression4 = '(41 + (2 * 3)) / (2 + 1)'  # (4 (2 3 *) +) (2 1 +) /
    print(expression0)
    print(count_value(expression0))  # ok
    print(expression1)
    print(count_value(expression1))  # ok
    print(expression2)
    print(count_value(expression2))  # ok
    print(expression3)
    print(count_value(expression3))  # ok
    print(expression4)
    print(count_value(expression4))  # ok

    print('\n' + ('-' * 10 + '\n') * 2)

    # wrong input
    print(count_value('[[][][][]]'))
    print(count_value('[1]'))
    print(count_value('((1)'))

    expression1 = '(41 * 2) / (7 / 8)'
    expression2 = '(221 * 32) * (41 - 21)'
    expression3 = '41 + (2 * 3)'
    expression4 = '(41 + (2 * 3)) / ((2 + 1) * 7)'
    print(count_value(expression0))  # works
    print(count_value(expression1))  # works
    print(count_value(expression2))  # works
    print(count_value(expression3))  # works
    print(count_value(expression4))  # works

