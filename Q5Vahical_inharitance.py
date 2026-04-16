class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_car(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Number of Seats:", self.seats)


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_bike(self):
        print("Bike Brand:", self.brand)
        print("Bike Model:", self.model)
        print("Engine CC:", self.engine_cc)


# Object Creation
car1 = Car("Toyota", "Fortuner", 7)
bike1 = Bike("Yamaha", "R15", 155)

# Calling Methods
car1.display_car()
print()
bike1.display_bike()
