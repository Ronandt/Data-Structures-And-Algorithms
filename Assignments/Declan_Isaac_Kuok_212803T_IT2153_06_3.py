from Declan_Isaac_Kuok_212803T_IT2153_06_2 import AbstractFilterMethods, AbstractSearchMethods, AbstractSortingMethods
from Declan_Isaac_Kuok_212803T_IT2153_06 import StaycationBookingRecord


class AlgorithmMethods(AbstractSortingMethods, AbstractFilterMethods, AbstractSearchMethods):

    def __init__(self, initaliser):
        self.initaliser = initaliser
    
    @property 
    def initaliser(self):
        return self._initaliser
    
    @initaliser.getter
    def initaliser(self):
        return self._initaliser

    @initaliser.setter
    def initaliser(self, initaliser):
        self._initaliser = initaliser
    
    @initaliser.deleter
    def initaliser(self):
        del self._initaliser

    
    def bubble_sort(self, callback) -> list:
        pass

    def selection_sort(self, callback) -> list:
        pass

    def insertion_sort(self, callback) -> list:
        pass

    def linear_search(self, callback) -> list:
        pass

    def binary_search(self, callback) -> list:
        pass

    def range_filter(self, callback) -> list:
        pass


class StaycationBookingRecordInitaliser(AlgorithmMethods):
    def __init__(self, initaliser = [StaycationBookingRecord("abcdefghij"[x], "abcdefghij"[x], x, x) for x in range(10)]):
        super().__init__(initaliser)
        print(self.initaliser)

class StaycationBookingRecordFactory():
    pass

StaycationBookingRecordInitaliser()