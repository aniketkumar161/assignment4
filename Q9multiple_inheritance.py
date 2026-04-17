class Herbivore:
    def eat_plants(self):
        print("Herbivore eats plants")


class Carnivore:
    def eat_meat(self):
        print("Carnivore eats meat")


class Omnivore:
    def eat_both(self):
        print("Omnivore eats both plants and meat")


class Bear(Herbivore, Carnivore, Omnivore):
    def bear_info(self):
        print("Bear can eat plants and meat")


# Object Creation
b1 = Bear()

# Calling Methods
b1.eat_plants()
b1.eat_meat()
b1.eat_both()
b1.bear_info()
