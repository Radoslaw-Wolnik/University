from MyRange import MyRange
from RangeBase8 import RangeBase8
from pathlib import Path


# generator - funkcja zachowujaca sie jak iterator
def my_range(n):
    '''range(n)'''
    i = 0
    while i < n:
        yield i  # zwroc i i zatrzymaj kod
        i += 1


def range_odwrotnosc(n):
    '''range(1/n)'''
    i = 0
    while i < n:
        if i != 0:
            yield (1 / i)
        else:
            yield 0
        i += 1


def infinite_range():
    '''range(inf)'''
    i = 0
    while True:
        yield i
        i += 1


if __name__ == '__main__':
    root_folder = Path(__file__).parents[1]
    zen_file_path = root_folder / "resources/zen.txt"
    # operating on file - iterator
    i = 0
    for line in open(zen_file_path):
        print(i, line.strip())
        i += 1

    # ---- next cell ----
    cell_name = "Dos"
    print("\n" + f' : {cell_name} :' * 7 + "\n")
    L = [1, 2, 3]
    iL = L.__iter__()
    print(iL)
    iL = L.__iter__()
    print(iL)

    # ---- next cell ----
    cell_name = "Tres"
    print("\n" + f' : {cell_name} :' * 7 + "\n")
    iL2 = iter(L)
    print(iL2)
    print(next(iL2))
    print(iL2.__next__())
    print(next(iL2))

    # ---- next cell ----
    cell_name = "Quatro"
    print("\n" + f' : {cell_name} :' * 7 + "\n")
    iP = iter("Python")
    print(iP)
    print(iP.__next__())

    # ---- next cell ----
    cell_name = "Cinco"
    print("\n" + f' : {cell_name} :' * 7 + "\n")
    ### tuple
    iK = iter((-1, -2, -3))
    print(iK)
    print(iK.__next__())

    # ---- next cell ----
    cell_name = "Seis"
    print("\n" + f' : {cell_name} :' * 7 + "\n")
    # konsumpcja iteratora
    L = [1, 4, 9]
    iL = iter(L)
    print(iL)
    tuple(iL)  # tuple zbudowane na elementach przez ktore przechodzi iterator
    tuple(iL)  # iterator przeszedl przez wszystkie elementy wiec nie ma juz elementow
    # zeby tego uniknac mozna skonstruowac iterator zwracajacy iteratory

    # ---- next cell ----
    cell_name = "Siete"
    print("\n" + f' : {cell_name} :' * 7 + "\n")
    mr = MyRange(4)
    print(type(mr))
    print(iter(mr))

    try:
        print(next(mr))
        print(next(mr))
        print(next(mr))
        print(next(mr))
        print(next(mr))
    except StopIteration:
        print('StopIteration exception')
    except Exception as e:
        print(e)

    # ---- next cell ----
    for i in MyRange(5):
        print(i ** 2)

    # ---- next cell ----
    cell_name = "Ocho"
    print("\n" + f' : {cell_name} :' * 7 + "\n")
    il = MyRange(5)
    print(list(il))
    print(list(il))

    # ---- next cell ----
    cell_name = "Nueve"
    print("\n" + f' : {cell_name} :' * 7 + "\n")
    # using iterator based on 8 notation
    for i in RangeBase8(10):
        print(i)

    # using generator my_range
    mr = my_range(4)
    print(iter(mr))

    print(next(mr))
    print(next(mr))
    print(next(mr))
    print(next(mr))
    try:
        print(next(mr))
    except StopIteration:
        print('StopIteration Exception')

    # using range_odwrotnosc
    for i in range_odwrotnosc(4):
        print(i)

    # wyrażenie generujące
    L = [-2, 0, 2]

    kwadraty_L = [i ** 2 for i in L]
    print(kwadraty_L)

    kL = (i ** 2 for i in L)
    print(kL)

    print(kL.__iter__())

    print(kL.__next__())
    print(kL.__next__())
    print(kL.__next__())
    try:
        print(kL.__next__())
    except Exception as e:
        print(e)

    # generator nieskonczony liczb w systemie oct na podstawie inf generator:
    base_8 = (oct(i) for i in infinite_range())
