from click import get_app_dir
from AbstractClasses import AbstractFilterMethods, AbstractSearchMethods, AbstractSortingMethods, AbstractBonusMethods
from AlgorirthmDataPipeline import AlgorithmDataPipeline


class AlgorithmMethods(AbstractSortingMethods, AbstractFilterMethods, AbstractSearchMethods, AbstractBonusMethods):

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
    
    def cocktail_sort(self):
        not_swap = True
        start, end = 0, len(self.initaliser) - 1
        for _ in range(len(self.initaliser)):
            for x in range(start, end):
                if self.initaliser[x].package_cost_per_pax > self.initaliser[x+1].package_cost_per_pax:
                    self.initaliser[x], self.initaliser[x+1] = self.initaliser[x+1], self.initaliser[x]
                    not_swap = False
            end-=1 #-1 as we don't want to scan through the same thing
      
    
            for x in range(end-1, start -1 , -1): #-1 because we have +1 here so it compensates, start-1 to compensate for range stop
                if self.initaliser[x].package_cost_per_pax > self.initaliser[x+1].package_cost_per_pax:
                    self.initaliser[x], self.initaliser[x+1] = self.initaliser[x+1], self.initaliser[x] 
                    not_swap = False
            start += 1 # don't scan the same thing
            if not_swap:
                break
        return "List has been sorted!"

    def comb_sort(self):

        n = len(self.initaliser)
        gap = n
        swapped = True
        while gap>1 or swapped:
            gap = min((gap * 10)//3, 1)
            swapped = False
            for i in range(0, n-gap):
                if self.initaliser[i].package_cost_per_pax > self.initaliser[i + gap].package_cost_per_pax:
                    self.initaliser[i], self.initaliser[i + gap] = self.initaliser[i + gap], self.initaliser[i]
                    swapped = True

    def shell_sort(self):
        marcin_curia_gap_sequence =  [701, 301, 132, 57, 23, 10, 4, 1]
        for gap in marcin_curia_gap_sequence:
            j = gap #e.g 4
            while j < len(self.initaliser): #Check gap until ends to the array
                i = j-gap #0 then plus plus plus
                while i>=0: #check when it goes down
                    if self.initaliser[i + gap].number_of_pax > self.initaliser[i].number_of_pax:
                        break
                    else: #if wrong pos
                        self.initaliser[i + gap], self.initaliser[i] = self.initaliser[i], self.initaliser[i+gap]
                    i -=gap #go backwards if it doesn't compare
                j += 1 #displace +1 to 5 to move on
        
        return "List has been sorted"

    def heapify(self, n, i):
        largest = i #2*i is a sibling, assume i is the largest first
        l = i * 2 + 1 #Next to those is a parent
        r = 2 * i + 2
        if l < n and self.initaliser[i].number_of_pax < self.initaliser[l].number_of_pax: #l < n/ r < n is an existing node
            print(self.initaliser[l])
            largest = l
        if r < n and self.initaliser[largest].number_of_pax < self.initaliser[r].number_of_pax:
            print(self.initaliser[i])
            largest = r
        if largest != i:
            self.initaliser[i], self.initaliser[largest] = self.initaliser[largest], self.initaliser[i]
            self.heapify(n, largest) #check again


    def heap_sort(self):
        length = len(self.initaliser)
        for i in range(length//2, -1, -1): #All the nodes
            self.heapify(length, i)
        for i in range(length-1, 0, -1):
            self.initaliser[i], self.initaliser[0] = self.initaliser[0], self.initaliser[i]
            self.heapify(i, 0)
        return "List has been sorted"



        
