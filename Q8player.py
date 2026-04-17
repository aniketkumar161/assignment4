
class Player:
    player_count = 0   # Class Variable

    def __init__(self, name, level):
        self.name = name
        self.level = level

        Player.player_count += 1

    def display(self):
        print("Player Name:", self.name)
        print("Player Level:", self.level)


# Object Creation
p1 = Player("Aniket", 5)
p2 = Player("Rahul", 8)
p3 = Player("Aman", 10)

# Display Player Details
p1.display()
print()

p2.display()
print()

p3.display()
print()

# Display Total Players Created
print("Total Players Created:", Player.player_count)
