class Bank():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance 
        
    def deposit(self, depo):
        self.depo = depo 
        self.balance += self.depo
        
    def Withdrawals(self, amount):
        self.amownt = amount
        if self.amownt > self.balance:
            print("your balance does not have enough funds")
            while self.amownt > self.balance:
                a = int(input())
                self.balance = a
        else:
            print(f"there is still money left on the account {self.balance - self.amownt}")

p1 = Bank(input(),int(input()))
p2 = p1.deposit(int(input()))
p3 = p1.Withdrawals(int(input()))
p3.Withdrawals(int(input()))