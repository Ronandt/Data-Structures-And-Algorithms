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
    def initaliser(self, initaliser: list) -> None:
        self._initaliser = initaliser

    @initaliser.deleter
    def initaliser(self) -> None:
        del self._initaliser

    def bubble_sort(self, callback=None) -> list:
        for _ in range(len(self.initaliser)):
            value = False
            for c in range(len(self.initaliser) - 1):
                if AlgorithmDataPipeline.compare(self.initaliser[c].customer_name.lower(), self.initaliser[c+1].customer_name.lower()):
                    self.initaliser[c +1], self.initaliser[c] = self.initaliser[c], self.initaliser[c+1]
                    value = True
            if value == False:
                
                return "List has been sorted!"

    def selection_sort(self, callback=None) -> list:
        for count in range(len(self.initaliser)):
            minimum = count
            for x in range(count, len(self.initaliser)):
                if AlgorithmDataPipeline.compare(self.initaliser[minimum].package_name.lower(), self.initaliser[x].package_name.lower()):
                    minimum = x
            if minimum != count:
                self.initaliser[minimum], self.initaliser[count] = self.initaliser[count], self.initaliser[minimum]
        return "List has been sorted!"

    def insertion_sort(self, callback=None) -> list:
        
        for x in range(1, len(self.initaliser)):
            target = self.initaliser[x]
            target_minus = x - 1
            while target_minus >= 0 and target.package_cost_per_pax * target.number_of_pax < self.initaliser[target_minus].package_cost_per_pax * self.initaliser[target_minus].number_of_pax:
                self.initaliser[target_minus + 1] = self.initaliser[target_minus]

                target_minus -= 1
            self.initaliser[target_minus + 1] = target


        return "List has been sorted!"

    def linear_search(self, target, callback=None):
        for x in range(len(self.initaliser)):
            if self.initaliser[x].customer_name.strip().lower() == target.strip().lower():
                targets = [x]
                current_index_positive = x
                while current_index_positive < (len(self.initaliser) + 1) and self.initaliser[current_index_positive + 1].customer_name.lower().strip() == target:
                    current_index_positive += 1
                    targets.append(current_index_positive)
                if len(targets) > 1:
                    print("\nPackage Selection: ")
                elif len(targets) == 1:
                    print("\nYou Have Selected: ")
                [print(
                        f"({x}) {self.initaliser[x]}") for x in targets]
                index = targets[0]
                if len(targets) > 1:
                    while 1:
                        try:
                            index = int(input("Choose your selected Booking Record: "))
                            if index not in targets:
                                print("That is not in the list of what you've searched")
                                continue
                            break
                        except ValueError:
                            print("Plesze choose a proper Booking Record by index")
                return AlgorithmDataPipeline.updateRecord(self.initaliser[index])
        return "Can't find result"

    def binary_search(self, target):
        self.selection_sort(self.initaliser)

        def binary_search_def(target, pointer1=None, pointer2=None, callback=None):
            target = target.lower().strip()
            if pointer2 >= pointer1:
                # assuming simply taking the length
                mid = (pointer1 + pointer2)//2
                if self.initaliser[mid].package_name.lower().strip() == target:
                    indexes = [mid]
                    current_index_minus = current_index_positive = mid
    
                    while current_index_minus-1 < 0 and self.initaliser[current_index_minus - 1].package_name.lower().strip() == target:
                        current_index_minus -= 1
                        indexes.append(current_index_minus)
     
                 
                    while current_index_positive + 1 < (len(self.initaliser)) and self.initaliser[current_index_positive + 1].package_name.lower().strip() == target:
                        current_index_positive += 1
                        indexes.append(current_index_positive)
                         
                    if len(indexes) > 1 :
                        print('\nPackage Selection: ')
                    elif len(indexes) == 1:
                        print("\nYou Have Selected: ")
                    [print(
                        f"({x}) {self.initaliser[x]}") for x in indexes]
                    index = indexes[0]
                    if len(indexes) > 1:
                        while 1:
                            try:
                                index = int(input(
                                    "Choose your selected Booking Record: "))
                                if index not in indexes:
                                    print(
                                        "That is not in the list of what you've searched!")
                                    continue
                                break
                            except ValueError:
                                print(
                                    "Please choose a proper Booking Record by index")

                    return AlgorithmDataPipeline.updateRecord(self.initaliser[index])
                elif AlgorithmDataPipeline.compare(self.initaliser[mid].package_name.lower().strip(), target.lower().strip()):
                    return binary_search_def(target, pointer1, mid - 1)
                else:
                    return binary_search_def(target, mid + 1, pointer2)
            else:
                return "Can't find result"
        bin_s = binary_search_def(
            target, pointer1=0, pointer2=len(self.initaliser) - 1)
        return bin_s

    def range_filter(self, ranges, callback=None) -> str:
        range_list = [float(x) for x in ranges.split("-")]
        if len(range_list) == 1:
            range_list.append(range_list[0])
        if range_list[0] > range_list[1]:
            range_list[0], range_list[1] = range_list[1], range_list[0]
        list_of_objects = [str(x) for x in self.initaliser if range_list[0]
                           <= x.package_cost_per_pax <= range_list[1]]
        return "\n".join(list_of_objects) if len(list_of_objects) > 0 else "No records found"
