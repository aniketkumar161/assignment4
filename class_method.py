class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type {cls.storage_type}")

    def get_info(self):  # instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

L1 = Laptop("16gb", "512gb")

Laptop.get_storage_type()
L1.get_info()
