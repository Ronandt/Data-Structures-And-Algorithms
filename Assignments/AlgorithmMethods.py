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
                    if AlgorithmDataPipeline.compare(self.initaliser[c].customer_name.lower().replace(" ", ""), self.initaliser[c+1].customer_name.lower().replace(" ", "")):
                        self.initaliser[c + 1], self.initaliser[c] = self.initaliser[c], self.initaliser[c+1]
                        value = True
                if value == False:
                    return self.initaliser



    def selection_sort(self, callback=None) -> list:
        for count in range(len(self.initaliser)):
            minimum = count
            for x in range(count, len(self.initaliser)):
                if AlgorithmDataPipeline.compare(self.initaliser[minimum].package_name.lower().replace(" ", ""),self.initaliser[x].package_name.lower().replace(" ", "")):
                    minimum = x
            self.initaliser[minimum], self.initaliser[count] = self.initaliser[count], self.initaliser[minimum]
        return self.initaliser


    def insertion_sort(self, callback=None) -> list:
        for x in range(1, len(self.initaliser)):
                count = 0
                while self.initaliser[x- count - 1].package_cost_per_pax * self.initaliser[x- count - 1].number_of_pax > self.initaliser[x - count].package_cost_per_pax * self.initaliser[x - count].number_of_pax and x-count != 0: #if 0, stop comparing with negative index\
                    self.initaliser[x- count - 1], self.initaliser[x - count] = self.initaliser[x - count], self.initaliser[x- count - 1]
                    count += 1
        return self.initaliser

    def linear_search(self, target, callback=None):
        for x in self.initaliser:
            if x.customer_name == target:
                return AlgorithmDataPipeline.updateRecord(x)
        return "Can't find result"

    def binary_search(self, target):
        def binary_search_def(target, pointer1 = None, pointer2 = None, callback=None):
            if pointer2 >= pointer1:
                mid = (pointer1 + pointer2 )//2 #assuming simply taking the length
                if self.initaliser[mid].package_name == target:
                    return AlgorithmDataPipeline.updateRecord(self.initaliser[mid])
                elif AlgorithmDataPipeline.compare(self.initaliser[mid].package_name, target):
                    return binary_search_def(target, pointer1, mid - 1)
                else:
                    return binary_search_def(target, mid + 1, pointer2)
            else:
                return "Can't find result"
        return binary_search_def(target, pointer1 = 0, pointer2 = len(self.initaliser) - 1)

    def range_filter(self, ranges, callback=None) -> str:
        range_list = [float(x) for x in ranges.split("-")]
        if len(range_list) == 1:
            range_list.append(range_list[0])
        if range_list[0] > range_list[1]:
            range_list[0], range_list[1] = range_list[1], range_list[0]
        list_of_objects = [str(x) for x in self.initaliser if range_list[0] <= x.package_cost_per_pax <= range_list[1]]
        return "\n".join(list_of_objects) if len(list_of_objects) > 0 else "No records found"

