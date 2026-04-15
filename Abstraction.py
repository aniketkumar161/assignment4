from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("Roar!")


class Cow(Animal):
    def make_sound(self):
        print("Moo!")


class Dog(Animal):
    def make_sound(self):
        print("Bark!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Elephant(Animal):
    def make_sound(self):
        print("Trumpet!")


class Horse(Animal):
    def make_sound(self):
        print("Neigh!")


class Goat(Animal):
    def make_sound(self):
        print("Baa!")


class Duck(Animal):
    def make_sound(self):
        print("Quack!")


class Snake(Animal):
    def make_sound(self):
        print("Hiss!")


lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()

elephant = Elephant()
elephant.make_sound()

horse = Horse()
horse.make_sound()

goat = Goat()
goat.make_sound()

duck = Duck()
duck.make_sound()

snake = Snake()
snake.make_sound()
