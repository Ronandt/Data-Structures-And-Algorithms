from AlgorithmMethods import AlgorithmMethods
from StaycationBookingRecord import StaycationBookingRecord
from sys import exit


class StaycationBookingRecordInitaliser(AlgorithmMethods):
    def __init__(self, initaliser=[StaycationBookingRecord("".join(__import__("random").sample("abcdefghijk", 10)), "".join(__import__("random").sample("abcdefghijk", 10)), x, x) for x in range(10)]):
        super().__init__(initaliser)


class StaycationBookingRecordFactory:
    while 1:
        initalise = StaycationBookingRecordInitaliser()
        query = input(
            "Would you like to sort, search, filter or display (Enter 'exit' to quit): ").lower().strip()
        if query == "sort":
            types = input(
                "\n1. Bubble sort (Customer name) \n2. Insertion sort (Package name)\nWhat would you like to sort: ").strip()
            if types == "1":
                initalise.bubble_sort()
            elif types == "2":
                initalise.selection_sort()
            else:
                print("Not a value")
        elif query == "search":
            pass
        elif query == "filter":
            pass
        elif query == "display":
           [print(x) for x in initalise.initaliser]
        elif query == "exit":
            print("You have exited out.")
            exit()
        else:
            print("That is not a query")


if __name__ == "__main__":

    StaycationBookingRecordFactory()
