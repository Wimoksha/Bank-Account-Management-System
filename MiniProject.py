class BankAccount:
    def __init__(self,accountNo,initialDeposit):
        self.accountNo=accountNo
        self.balance=initialDeposit

    def deposit(self,amount):
        if amount<0:
            print("Deposit should be positive!")
            return False
        self.balance+=amount
        print("Deposited ",amount," into account ",self.accountNo)
        return True

    def withdraw(self,amount):
        if amount<0:
            print("Withdrwal should be positive!")
            return False
        if amount>self.balance:
            print("Balance is insufficient!")
            return False
        self.balance-=amount;
        print("Withdrew ",amount," from ",self.accountNo)
        return True
    
    def transfer(self,amount,receiver):
        if amount<0:
            print("Tranfer amount should be positive!")
            return False
        if amount>self.balance:
            print("Balance is insufficient!")
            return False
        self.balance-=amount
        receiver.balance+=amount
        print("Money has transferred ",amount," from account ",self.accountNo," to account ",receiver.accountNo)
        return True
    def checkBalance(self):
        print("Account ",self.accountNo," Balance ",self.balance)

def createAccount(accounts):
    accountNo=input("Enter account no : ")
    if accountNo in accounts:
        print("Account is available")
        return
    initialDeposit=float(input("Enter initial deposit amount : "))
    if initialDeposit<0:
        print("Deposit should be positive!")
        return
    accounts[accountNo]=BankAccount(accountNo,initialDeposit)
    print("Account ",accountNo," is created")

def depositMoney(accounts):
    accountNo=input("Enter account no : ")
    if accountNo not in accounts:
        print("Account does not exist.")
        return
    amount=float(input("Enter deposit amount : "))
    accounts[accountNo].deposit(amount)
    
def withdrawMoney(accounts):
    accountNo=input("Enter account no : ")
    if accountNo not in accounts:
        print("Account does not exist.")
        return
    amount=float(input("Enter withdrawal amount : "))
    accounts[accountNo].withdraw(amount)
    
def transferMoney(accounts):
    fromAccount=input("Enter sender's account no : ")
    toAccount=input("Enter receiver's account no : ")
    if fromAccount not in accounts or toAccount not in accounts:
        print("Account(s) does not exist")
        return
    amount=float(input("Enter transferring amount : "))
    accounts[fromAccount].transfer(amount,accounts[toAccount])
    
def checkBalance(accounts):
    accountNo=input("Enter account no : ")
    if accountNo not in accounts:
        print("Account does not exist.")
        return
    accounts[accountNo].checkBalance()

def main():
    accounts={}
    while True:
        print("\nBank Account Management System")
        print("1. Creating account")
        print("2. Depositing money")
        print("3. Withdrawing money")
        print("4. Transferring money")
        print("5. Checking balance")
        print("6. exit")
        choice=input("Enter your choice : ")
        if choice=='1':
            createAccount(accounts)
        elif choice=='2':
            depositMoney(accounts)
        elif choice=='3':
            withdrawMoney(accounts)
        elif choice=='4':
            transferMoney(accounts)
        elif choice=='5':
            checkBalance(accounts)
        elif choice=='6':
            print("Thank you!")
            break
        else:
            print("Invalid input! Enter again.")

if __name__ == "__main__":
    main()
