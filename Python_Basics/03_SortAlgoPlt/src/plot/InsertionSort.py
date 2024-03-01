class InsertionSort:
    '''funkcja sortuje liste za pomoca algorytmu wstawiania
            przyjmuje liste
            jesli do funkcji przekazana będzie wartość Type != list to funkcja zwraca 'Not list'
            jesli do funkcji przekazana będzie wartość któej elementy nie mogą być porównane lub zamienione to funkcja
            zwróci 'Wrong type of element in list'
            jesli parametr jest właściwy zwraca posortowana liste'''

    def __init__(self):
        self.unsorted = None
        self.sorted = None

    def load_data(self, list_to_sort) -> None:
        """Overrides SortInterface.load_data()"""
        assert isinstance(list_to_sort, (tuple, list)), "Not list"
        assert all(isinstance(item, int) for item in list_to_sort), "Wrong type of element in list"
        self.unsorted = list_to_sort

    def execute(self) -> None:
        """Overrides SortInterface.execute()"""
        L = self.unsorted
        for marker in range(1, len(L)):
            for i in range(marker - 1, -1, -1):
                if L[i] > L[marker]:
                    L[i], L[marker] = L[marker], L[i]
                    marker -= 1
                else:
                    break
        return L

    def read_data(self):
        """Overrides SortInterface.read_data()"""
        return self.sorted

# tests:
# print(wstawienie_sort([5, 6, -1, 0, 4, 7, 2, 3, 102, 88]))
# print(wstawienie_sort([i for i in range(10)]))
# print(wstawienie_sort([i for i in range(10, 0, -1)]))
# print(wstawienie_sort('geografia'))
# print(wstawienie_sort([[1], [2]]))