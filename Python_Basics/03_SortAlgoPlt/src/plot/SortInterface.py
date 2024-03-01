import abc


class SortInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'execute') and
                callable(subclass.execute) and
                hasattr(subclass, 'read_data') and
                callable(subclass.read_data))


class ExampleSortInterfaceImplementation:
    """Sorts list of arguments"""

    def __init__(self):
        self.unsorted = None
        self.sorted = None

    def load_data(self, list_to_sort):
        """Overrides SortInterface.load_data()"""
        assert isinstance(list_to_sort, (tuple, list)), "given data is not a list or tuple"
        assert all(isinstance(item, int) for item in list_to_sort), "given list doesn't consist of only int type"
        self.unsorted = list_to_sort

    def execute(self):
        """Overrides SortInterface.execute()"""
        pass

    def read_data(self):
        """Overrides SortInterface.read_data()"""
        return self.sorted
