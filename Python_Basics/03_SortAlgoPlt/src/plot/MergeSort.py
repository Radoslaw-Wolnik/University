class MergeSort:
    """Sorts list of arguments"""

    # pesymistycznie O(nlogn)
    #
    # optymistycznie O(nlogn)

    def __init__(self):
        self.unsorted = None
        self.sorted = None

    def load_data(self, list_to_sort) -> None:
        """Overrides SortInterface.load_data()"""
        assert isinstance(list_to_sort, (tuple, list)), "given data is not a list or tuple"
        assert all(isinstance(item, int) for item in list_to_sort), "given list doesn't consist of only int type"
        self.unsorted = list_to_sort

    @staticmethod
    def merge(left, right):
        result = []
        # print(left)
        # print(right)
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                del right[0]
            else:
                result.append(left[0])
                del left[0]

        result += left + right
        # print(result)
        return result

    def merge_sort(self, L):
        '''funkcja sortuje liste za pomoca algorytmu scalenia
        przyjmuje liste'''

        if len(L) > 1:
            mid = len(L) // 2
            left = L[:mid]
            right = L[mid:]
            left = self.merge_sort(left)
            right = self.merge_sort(right)
            return self.merge(left, right)
        else:
            return L

    def execute(self) -> None:
        """Overrides SortInterface.execute()"""
        self.sorted = self.merge_sort(self.unsorted)

    def read_data(self):
        """Overrides SortInterface.read_data()"""
        return self.sorted

# tests:
# print(merge_sort([3 ,5 ,-1 ,2 ,7 ,4]))
# print(merge_sort([-3 ,4 ,5 ,7 ,2 ,4 ,-8 ,0 ,-3]))
# print(merge_sort([5, 6, -1, 0, 4, 7, 2, 3, 102, 88]))
# print(merge_sort([i for i in range (10)]))
# print(merge_sort([i for i in range (10 ,0 ,-1)]))
