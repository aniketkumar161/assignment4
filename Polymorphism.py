# Polymorphism

# Example - Operator Overloading
print(1 + 2)    # adds 2 numbers
print("1" + "2") # concatenates 2 strings

# Function Overriding
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
dog = Dog()

a.sound()  # Some generic sound
dog.sound()  # Bark

# Duck Typing
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

class Robot:
    def speak(self):
        print("Beep Boop")

def make_it_speak(entity):
    entity.speak()  # doesn’t care about type

d = Dog()
c = Cat()
r = Robot()

for e in [d, c, r]:
    make_it_speak(e)