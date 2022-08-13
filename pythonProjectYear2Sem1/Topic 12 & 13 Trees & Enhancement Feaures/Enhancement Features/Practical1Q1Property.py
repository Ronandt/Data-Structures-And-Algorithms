#@Property is the proper way to have getters and setters in python ahd the most pythonic and proper way to do it in python
'''
. It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.
'''
class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._balance = 0
        self._bank = bank
        self._account = account
        self._limit = limit

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer (self, customer):
        self._customer = customer
    
    
    @property
    def bank(self):
        return self._bank
    
    @bank.setter
    def bank (self, bank):
        self._bank = bank

    @property
    def account(self):
        return self._account
    

    @account.setter
    def account(self, account):
        self._account = account

    @property
    def limit(self):
        return self._limit

        
    @limit.setter
    def limit (self, limit):
        self._limit = limit

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance (self, balance):
        self._balance = balance
        
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
        print("Customer =", wallet[c].customer)
        print("Bank = ", wallet[c].bank)
        print("Account = ", wallet[c].account)
        print("Limit = ", wallet[c].balance)
        while wallet[c].balance > 100:
            wallet[c].make_payment(100)
            print("new balance =", wallet[c].balance)
        print()