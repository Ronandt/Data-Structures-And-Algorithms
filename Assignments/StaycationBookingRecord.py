
#Declan, 212803T, IT2153-06
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

    @package_cost_per_pax.getter
    def package_cost_per_pax(self) -> float:
        return self._package_cost_per_pax

    @package_cost_per_pax.setter
    def package_cost_per_pax(self, package_cost_per_pax: float) -> None:
        self._package_cost_per_pax = package_cost_per_pax

    @package_cost_per_pax.deleter
    def package_cost_per_pax(self) -> None:
        del self._package_cost_per_pax
    
    def __str__(self) -> str:
        return f"Package name: {self.package_name}, Customer name: {self.customer_name}, Number of pax: {self.number_of_pax}, Package cost per pax: {self.package_cost_per_pax}"

    def __repr__(self) -> str:
        return f"PackageName: {self.package_name}, CustomerName: {self.customer_name}, NumberOfPax: {self.number_of_pax}, PackageCostPerPax: {self.package_cost_per_pax}"
    
    def __eq__(self, __o: object) -> bool:
        for x in [c for c in dir(self) if not c.startswith("__")]:
            if getattr(__o, x) != getattr(self, x):
                return False
        return True

    



    
    
