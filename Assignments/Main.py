from AbstractClasses import AbstractFilterMethods, AbstractSearchMethods, AbstractSortingMethods
from StaycationBookingRecord import StaycationBookingRecord
from sys import exit


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

    def bubble_sort(self, callback=None) -> list:
        pass

    def selection_sort(self, callback=None) -> list:
        pass

    def insertion_sort(self, callback=None) -> list:
        pass

    def linear_search(self, callback=None) -> list:
        pass

    def binary_search(self, callback=None) -> list:
        pass

    def range_filter(self, callback=None) -> list:
        pass


class StaycationBookingRecordInitaliser(AlgorithmMethods):
    def __init__(self, initaliser=[StaycationBookingRecord("abcdefghij"[x], "abcdefghij"[x], x, x) for x in range(10)]):
        super().__init__(initaliser)


class StaycationBookingRecordFactory():
    while 1:
        query = input(
            "Would you like to sort, search or filter (Enter 'exit' to quit): ").lower().strip()
        if query == "sort":
            pass
        elif query == "search":
            pass
        elif query == "filter":
            pass
        elif query == "display":
            pass
        elif query == "exit":
            print("You have exited out.")
            exit()
        else:
            print("That is not a query")


StaycationBookingRecordFactory()
