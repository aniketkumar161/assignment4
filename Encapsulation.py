
class BankAccount:
    def __init__(self, name, balance):
        self.name = name            # public
        self.__balance = balance    # private

    def get_balance(self):         # getter
        return self.__balance

    def set_balance(self, new_balance):  # setter
        self.__balance = new_balance

acc1 = BankAccount("Rahul", 50000)
print(acc1.get_balance())
acc1.set_balance(60000)
print(acc1.get_balance())