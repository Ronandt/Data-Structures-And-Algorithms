from abc import ABC, abstractmethod
class StaycationBookingRecord:
    def __init__(self, package_name: str, customer_name: str, number_of_pax: int, package_cost_per_pax: float):
        self._package_name = package_name
        self._customer_name = customer_name
        self._number_of_pax = number_of_pax
        self._package_cost_per_pax = package_cost_per_pax

    @property
    def package_name(self) -> str:
        return self._package_name

    @package_name.getter
    def package_name(self) -> str:
        return self._package_name

    @package_name.setter
    def package_name(self, package_name: str) -> None:
        self._package_name = package_name

    @package_name.deleter
    def package_name(self) -> None:
        del self._package_name

    @property
    def customer_name(self) -> str:
        return self._customer_name

    @customer_name.getter
    def customer_name(self) -> str:
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name: str) -> None:
        self._customer_name = customer_name

    @customer_name.deleter
    def customer_name(self) -> None:
        del self._customer_name

    @property
    def number_of_pax(self) -> int:
        return self._number_of_pax

    @number_of_pax.getter
    def number_of_pax(self) -> int:
        return self._number_of_pax

    @number_of_pax.setter
    def number_of_pax(self, number_of_pax: int) -> None:
        self._number_of_pax = number_of_pax

    @number_of_pax.deleter
    def number_of_pax(self) -> None:
        del self._number_of_pax

    @property
    def package_cost_per_pax(self) -> float:
        return self._package_cost_per_pax

    @number_of_pax.getter
    def package_cost_per_pax(self) -> float:
        return self._package_cost_per_pax

    @number_of_pax.setter
    def package_cost_per_pax(self, package_cost_per_pax: int) -> None:
        self._package_cost_per_pax = package_cost_per_pax

    @number_of_pax.deleter
    def package_cost_per_pax(self) -> None:
        del self._package_cost_per_pax
    
    def __str__(self) -> str:
        return f"Package name: {self._package_name}, Customer name: {self._customer_name}, Number of pax: {self._number_of_pax}, Package cost per pax: {self._package_cost_per_pax}"

    def __repr__(self) -> str:
        return f"Package name: {self._package_name}, Customer name: {self._customer_name}, Number of pax: {self._number_of_pax}, Package cost per pax: {self._package_cost_per_pax}"
    
    def __eq__(self, __o: object) -> bool:
        for x in [c for c in dir(self) if not c.startswith("__")]:
            if getattr(__o, x) != getattr(self, x):
                return False
        return True




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
        elif query == "exit":
            exit()
        else:
            print("That is not a query")

StaycationBookingRecordFactory()