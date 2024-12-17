class Account:
    def __init__(self, num):
        self.amount = 0
        self.num = num
    
    def deposit(self, n):
        self.amount += n
    
    def withdraw(self, n):
        if self.amount - n < 0:
            print("Insufficient funds on the account")
            return
        
        self.amount -= n
    
    def display(self):
        print(f"Bank Account No.: {self.num}")
        print(f"Balance: PLN {self.amount}")

acc = Account("1" * 26)
acc.display()
acc.deposit(25.38)
acc.display()