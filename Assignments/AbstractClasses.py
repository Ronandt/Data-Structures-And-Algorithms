
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
