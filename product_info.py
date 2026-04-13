class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")


# object creation
p1 = Product("phone", 10000)
p2 = Product("laptop", 50000)
p3 = Product("pen", 10)

# method call
p1.get_info()
p2.get_info()
p3.get_info()
