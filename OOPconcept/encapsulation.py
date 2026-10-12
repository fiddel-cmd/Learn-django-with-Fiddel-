class wallet():
    def __int__(self ,balance):
        self.balance = balance

    def deposit(self , amount):
        if amount > 0:
            self. _balance += amount
    def withdraw( self , amoutn):
        if 0 < amoutn <= self. _balance:
            self. _balance -= amoutn
        

person = wallet()
print(person._balance)