class BankAccount:
    def __init__(self , account_number , owner_name , balance ):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self , amount):
        self.balance += amount
        print("deposet amount :",amount)

    def withdraw(self , amount):
        if amount<=self.balance:
            self.balance -= amount
            print("withdrow amount :", amount)

        else:
            print("insaficeant balance")
    def check_balance(self):
       print("Current Balance:", self.balance)

acc1 = BankAccount(233254252387, "aniket" ,50000)

acc1.deposit(2000)
acc1.withdraw(1500)
acc1.check_balance()