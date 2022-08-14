from Practical1Q1 import CreditCard


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr
        self._balance = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            print("Limit for this month reached, additional $5 charge")
            self._balance += 5

        else:
            self._balance += price

    def process_month(self):
        return ((1 + self._apr) ** (1 / 12)) * self.get_balance()


if __name__ == "__main__":
    wallet = []
    wallet.append(PredatoryCreditCard("John Lee", "DBS", "5391 0375 9387 5309", 2500, 0.0825))

    print('Customer =', wallet[0].get_customer())
    print("Bank =", wallet[0].get_bank())
    print("Account =", wallet[0].get_account())
    print("Limit =", wallet[0].get_limit())
    print("Balance =", wallet[0].get_balance())

    for val in range(1, 17):
        wallet[0].charge(200)
        print("charge")
        print("Transaction number", val)
        print(f": Charge $200 Balance = ${wallet[0].get_balance()}")
    processmonth = wallet[0].process_month()
    print(f"After Process Month ${processmonth:.2f}")
