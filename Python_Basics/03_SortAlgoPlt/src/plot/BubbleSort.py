class BubbleSort:
    """funkcja sortuje liste L za pomoca aglgorytmu bubble sort
    funkcja przyjmuje liste
    jesli do funkcji przekazana będzie wartość Type != list to funkcja funkcja zwraca 'Not list'
    jesli do funkcji przekazana będzie wartość któej elementy nie mogą być porównane lub zamienione to funkcja
    zwróci 'Wrong type of element in list'
    jeśli zostanie przekazany dobry typ funkcja zwróci posortowana liste"""

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
        sortowanie = True
        licznik = 1
        while sortowanie:
            sortowanie = False
            for i in range(len(L) - licznik):
                if L[i + 1] < L[i]:
                    L[i + 1], L[i] = L[i], L[i + 1]
                    sortowanie = True
            licznik += 1
        self.sorted = L

    def read_data(self):
        """Overrides SortInterface.read_data()"""
        return self.sorted

# tests:
# lista = [5, 6, -1, 0, 4, 7, 2, 3]
# print(sort_bubble(lista))
# print(sort_bubble([i for i in range (10)]))
# print(sort_bubble([i for i in range (10,0,-1)]))
# print(sort_bubble(['v', 'd', 's', 'h', 'a', 'i']))
# print(sort_bubble('vdshai'))
# print(sort_bubble(['vd','aa','ccc']))
# print(sort_bubble([[1],[2]]))
