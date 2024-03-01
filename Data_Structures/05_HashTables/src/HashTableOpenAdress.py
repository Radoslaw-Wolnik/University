def h2_iter(key, mod):
    '''dwuargumentowa funkcja skrotu w formie iteratora'''
    i = 0
    while i < mod:
        yield (key + i) % mod
        i += 1


class HashTableOpenAdress():
    '''Tablica haszujaca wykorzystujaca adresowanie otwarte i iterator jako funkcje skrotu'''

    def __init__(self, m):
        self.set_m(m)
        self.build()

    def set_m(self, m):
        if type(m) == int:
            self.m = m

    def get_m(self):
        return self.m

    def build(self):
        self.table = [None for _ in range(self.m)]

    def insert(self, para):
        key, val = para
        for idx in h2_iter(key, self.m):
            if self.table[idx] == None:
                self.table[idx] = para
                return idx
        raise IndexError('Nie ma juz miejsca w tablicy')

    def delete(self, key):
        for idx in h2_iter(key, self.m):
            if self.table[idx][0] == key:
                self.table[idx] = None
                return True
        raise IndexError('Nie ma elementu do usuniecia')

    def search(self, key):
        for idx in h2_iter(key, self.m):
            if self.table[idx] != None:
                if self.table[idx][0] == key:
                    return idx
        raise IndexError('Nie ma takiego elementu')

    # nie moj kod
    def __repr__(self):
        r = ''
        for el in self.table:
            r += str(el) + '\n'
        return r

    def __str__(self):
        return self.__repr__()
