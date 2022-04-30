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
        for _ in range(len(self.initaliser)):
                value = False
                for c in range(len(self.initaliser) - 1):
                    if AlgorithmDataPipeline.compare(self.initaliser[c].customer_name.lower().strip(), self.initaliser[c+1].customer_name.lower().strip()):
                        self.initaliser[c + 1], self.initaliser[c] = self.initaliser[c], self.initaliser[c+1]
                        value = True
                if value == False:
                    return self.initaliser



    def selection_sort(self, callback=None) -> list:
        for count in range(len(self.initaliser)):
            minimum = count
            for x in range(count, len(self.initaliser)):
                if AlgorithmDataPipeline.compare(self.initaliser[minimum].package_name,self.initaliser[x].package_name):
                    minimum = x
            self.initaliser[minimum], self.initaliser[count] = self.initaliser[count], self.initaliser[minimum]

    def insertion_sort(self, callback=None) -> list:
        pass

    def linear_search(self, callback=None) -> list:
        pass

    def binary_search(self, callback=None) -> list:
        pass

    def range_filter(self, callback=None) -> list:
        pass
