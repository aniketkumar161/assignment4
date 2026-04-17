class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        
        if self.age is not None:
            print("Age:", self.age)
            
        if self.address is not None:
            print("Address:", self.address)

        print()


# Object with name only
p1 = Person("Aniket")

# Object with name and age
p2 = Person("Rahul", 21)

# Object with name, age and address
p3 = Person("Aman", 22, "Jamshedpur")

# Calling Method
p1.display()
p2.display()
p3.display()
