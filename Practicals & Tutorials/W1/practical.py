class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self.__customer = customer
        self.__balance = 0
        self.__bank = bank
        self.__account = account
        self.__limit = limit
  
    def get_customer(self):
        return self.__customer

    def get_bank(self):
        return self.__bank

    def get_account(self):
        return self.__account
    def get_limit(self):
        return self.__limit
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def charge(self, price):
        if price + self.__balance> self.__limit:
            return False
        else:
            self.__balance += price
            return True

    def make_payment(self, amount):
        self.__balance -= amount

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self.__apr = apr
        self.__charge_no = 0
      
    

    def charge(self, price):
        self.__charge_no += 1
        if price + self.get_balance() > self.get_limit():
            self.make_payment(5)
            return False
        else:
            self.set_balance(5)
            return True

    def process_month(self):
        self.__apr = 0
        return ((self.__apr + 1)**(1/12)) + max(0, self.__charge_no - 10) * 1


if __name__ == "__main__":
    print("PREDATORY CARD TEST CASES")
    wallet = []
    wallet.append(CreditCard("John Lee", "DBS", "2032839232", 2500))
    wallet.append(CreditCard('John Lee', 'OCBC',
    '3485 0399 3395 1954', 3500) )
    wallet.append(CreditCard('John Lee', 'Maybank',
    '5391 0375 9387 5309', 5000) )
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

    print("PREDATORY CREDIT CARD TEST CASES")
    wallet = []
    wallet.append(PredatoryCreditCard("John Lee", "DBS", "2032839232", 5, 1))
    wallet.append(PredatoryCreditCard('John Lee', 'OCBC',
    '3485 0399 3395 1954', 3500, 1) )
    wallet.append(PredatoryCreditCard('John Lee', 'Maybank',
    '5391 0375 9387 5309', 5000, 1) )
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)
    
    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print("Account = ", wallet[c].get_account())
        print("Balance = ", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("new balance =", wallet[c].get_balance())
        print()