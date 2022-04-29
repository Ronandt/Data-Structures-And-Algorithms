from AlgorithmMethods import AlgorithmMethods
from StaycationBookingRecord import StaycationBookingRecord
from sys import exit




class StaycationBookingRecordInitaliser(AlgorithmMethods):
    def __init__(self, initaliser=[StaycationBookingRecord("abcdefghij"[x], "abcdefghij"[x], x, x) for x in range(10)]):
        super().__init__(initaliser)
        print(self.initaliser)


class StaycationBookingRecordFactory:
    while 1:
        StaycationBookingRecordInitaliser()
        query = input(
            "Would you like to sort, search or filter (Enter 'exit' to quit): ").lower().strip()
        if query == "sort":
            pass
        elif query == "search":
            pass
        elif query == "filter":
            pass
        elif query == "display":
            pass
        elif query == "exit":
            print("You have exited out.")
            exit()
        else:
            print("That is not a query")

if __name__ == "__main__":
        StaycationBookingRecordFactory()
  
