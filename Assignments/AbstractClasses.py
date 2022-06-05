#Declan, 212803T, IT2153-06

from abc import ABC, abstractmethod


class AbstractSortingMethods(ABC):
   
    @abstractmethod
    def bubble_sort(self):
        pass

  
    @abstractmethod
    def selection_sort(self):
        pass


    @abstractmethod
    def insertion_sort(self):
        pass


class AbstractSearchMethods(ABC):
  
    @abstractmethod
    def linear_search(self):
        pass
    
    @abstractmethod
    def binary_search(self):
        pass


class AbstractFilterMethods(ABC):
 
    @abstractmethod
    def range_filter(self):
        pass

class AbstractBonusMethods(ABC):
    @abstractmethod
    def cocktail_sort(self):
        pass

    @abstractmethod
    def comb_sort(self):
        pass

    @abstractmethod
    def heap_sort(self):
        pass

    @abstractmethod
    def shell_sort(self):
        pass

