class HashTableChain:
    ''' Hash Table wit collision solved by chaining'''

    def __init__(self, m):
        self.set_m(m)
        self.build()

    def set_m(self, m):
        if type(m) == int:
            self.m = m

    def get_m(self):
        return self.m

    def build(self):
        self.lancuch = [[] for _ in range(self.m)]

    def add(self, index, name):
        if len(self.lancuch[index % self.m]) == 0:
            self.lancuch[index % self.m].append((index, name))
        else:
            if self.lancuch[index % self.m][0][0] > index:  # jesli index jest mniejszy niz pierwszy index
                self.lancuch[index % self.m].insert(0, (index, name))
            elif self.lancuch[index % self.m][-1][0] < index:  # jesli index jest wiekszy niz ostatni index
                self.lancuch[index % self.m].append((index, name))
            else:  # jesli index jest gdzies pomiedzy pierwszym i ostatnim
                for i in range(1, len(self.lancuch[index % self.m]) - 1):
                    if self.lancuch[index % self.m][i - 1][0] < index and self.lancuch[index % self.m][i + 1][
                        0] > index:
                        self.lancuch[index % self.m].insert(i + 1, (index, name))
                        break

    def search(self, index):
        s_id = index % self.m
        if len(self.lancuch[s_id]) == 1:
            return 0
        else:
            res = -1
            up = len(self.lancuch[s_id])
            down = 0
            while (up - down) > 0:
                half = (down + up) // 2
                if index > self.lancuch[s_id][half][0]:
                    down = half
                if index < self.lancuch[s_id][half][0]:
                    up = half
                if index == self.lancuch[s_id][half][0]:
                    res = half
                    break
            return res

    def delete(self, index):
        scnd_id = self.search(index)
        del self.lancuch[index % self.m][scnd_id]
        return True

    def __repr__(self):
        r = ''
        for el in self.lancuch:
            r += str(el) + '\n'
        return r

    def __str__(self):
        return self.__repr__()
