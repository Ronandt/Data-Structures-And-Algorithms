from CreditCard import CreditCard
class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit,)
        self.apr = apr #qn2
        self.charge_counter = 0 #qn3
        #Create a new predatory credit card instance.
    def charge(self, price):
        self.charge_counter+=1#qn 3
        print(f'Charge number {self.charge_counter}')#qn 3
        if self.charge_counter >10:#qn 3
            self.balance += 1#qn 3
            print("After 10 transaction charged 1$ fee") #qn 3

        success = super().charge(price)#qn2 call inherited method
        if not success:#qn2
            self.balance +=5#qn2
            print("charge $5 penalty")#qn2
        return success #qn 2
        # if price + self.balance > self.limit:
        #     price_charged = 5
        #     return price_charged, False
        # else:
        #     self.balance+=price
        #     return True
        # Charge given price to the card, assuming sufficient credit limit.
        # Return True if charge was processed.
        # Return False and assess $5 fee if charge is denied.

    def process_month(self):
        self.charge_counter += 0#qn3
        monthly_factor =  pow(1 + self.apr, 1/12)#qn2
        self.balance *=monthly_factor #qn2
        # Assess monthly interest on outstanding balance.

if __name__ == '__main__': #testing code
    wallet = []
    wallet.append(PredatoryCreditCard('John Lee', 'DBS',
    '5391 0375 9387 5309', 2000, 0.0825) )

    print('Customer =', wallet[0].get_customer())
    print('Bank =', wallet[0].get_bank())
    print('Account =', wallet[0].get_account())
    print('Limit =', wallet[0].get_limit())
    print('Balance =', wallet[0].get_balance())

    for val in range(1, 17):
        wallet[0].charge(200)
        print('New balance =', wallet[0].get_balance())
    print()

