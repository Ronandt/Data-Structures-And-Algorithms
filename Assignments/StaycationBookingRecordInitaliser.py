from AlgorithmMethods import AlgorithmMethods
from StaycationBookingRecord import StaycationBookingRecord

class StaycationBookingRecordInitaliser(AlgorithmMethods):
    def __init__(self, initaliser=[StaycationBookingRecord("".join(__import__("random").sample("abcdefghijk", 10)), "".join(__import__("random").sample("abcdefghijk", 10)), x, x) for x in range(10)]):
        super().__init__(initaliser)
