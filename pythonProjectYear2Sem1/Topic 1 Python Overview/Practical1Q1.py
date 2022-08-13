class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._balance = 0
        self._bank = bank
        self._account = account
        self._limit = limit

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("John Lee", "DBS", "5391 0375 9387 5309", 2500))
    wallet.append(CreditCard('John Lee', 'OCBC',
                             '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Lee', 'Maybank',
                             '5391 0375 9387 5309', 5000))
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print("Account = ", wallet[c].get_account())
        print("Limit = ", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("new balance =", wallet[c].get_balance())
        print()