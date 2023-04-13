class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance =  balance
        
    def getBalance(self):
        return self.balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdrawal(self, amount):
         self.balance = self.balance - amount
    
    def bankFees(self):
        return self.balance * 1.05
    
    def display(self):
        print('Name - ', self.name)
        print('Account Number - ', self.accountNumber)
        
banckaccount = BankAccount('025078890', 'Nurbolat', 250)
banckaccount.deposit(500)
print('Balance - ', banckaccount.getBalance())
banckaccount.withdrawal(500)
print('Balance - ' ,banckaccount.bankFees())
banckaccount.display()

    