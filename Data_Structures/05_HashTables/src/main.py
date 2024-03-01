from src.HashTableChain import HashTableChain
from src.HashTableOpenAdress import HashTableOpenAdress

if __name__ == '__main__':
    print('hash table')
    BD = [(266602, 'Asembler'), (236872, 'Basic'), (384392, 'Cobol'), (478236, 'Fortran'), (347298, 'Go'),
          (126738, 'Haskell'), (671388, 'Java')]

    ab = HashTableChain(4)
    print(ab)

    for el in BD:
        ab.add(el[0], el[1])
    print(ab)
    ab.delete(126738)
    ab.delete(671388)
    print(ab)

    # test open address Hash table

    BD = [(266602, 'Asembler'), (236872, 'Basic'), (384392, 'Cobol'), (478236, 'Fortran'), (347298, 'Go')]
    ob_table = HashTableOpenAdress(9)
    for pair in BD:
        ob_table.insert(pair)

    print(ob_table)
    print('-' * 30)

    ob_table.insert((671388, 'Java'))
    print(ob_table)

    print('-' * 30)

    # print(ob_table.search(126738)) nie ma takiego elementu
    print(ob_table.search(671388))

    print('-' * 30)

    # print(ob_table.delete(126738)) nie ma takiego elementu
    print(ob_table.delete(671388))
    print()
    print(ob_table)