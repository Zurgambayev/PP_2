class Bank():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance 
    def deposit (other,depo):
        other.depo = depo 
        other.balance += other.depo
    def Withdrawals (self, amount):
        self.amownt = amount
        if self.amownt > self.balance:
            print("your balance does not have enough funds")
            while self.amownt > self.balance:
                a = int(input())
                self.balance = a
        else:
            print(f"there is still money left on the account {self.balance - self.amownt}")

p1 = Bank(input(),int(input()))
p2 = Bank(int(input()))
p3 = Bank(int(input()))
p3.Withdrawals(int(input()))