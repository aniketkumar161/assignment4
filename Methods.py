class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM):
        self.RAM = RAM

    def get_info(self):   # Instance Method
        print(f"Laptop has {self.RAM} RAM & storage type is {self.storage_type}")

    @classmethod          # Class Method
    def get_storage_type(cls):
        print(f"storage type is {cls.storage_type}")

    @staticmethod         # Static Method
    def cal_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"final price = {final_price}")

l1 = Laptop("16 GB")

l1.get_info() 
Laptop.get_storage_type()
l1.cal_discount(40_000, 10)