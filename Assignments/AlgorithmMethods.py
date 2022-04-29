from AbstractClasses import AbstractFilterMethods, AbstractSearchMethods, AbstractSortingMethods
from AlgorirthmDataPipeline import AlgorithmDataPipeline


class AlgorithmMethods(AbstractSortingMethods, AbstractFilterMethods, AbstractSearchMethods):
    
    def __init__(self, initaliser):
        self.initaliser = initaliser

    @property
    def initaliser(self) -> list:
        return self._initaliser

    @initaliser.getter
    def initaliser(self) -> list:
        return self._initaliser

    @initaliser.setter
    def initaliser(self, initaliser : list) -> None:
        self._initaliser = initaliser

    @initaliser.deleter
    def initaliser(self) -> None:
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
