class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # Setter for name
    def set_name(self, name):
        if name != "":
            self._name = name
        else:
            print("Name cannot be empty")

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for roll number
    def set_roll_no(self, roll_no):
        if roll_no >= 1 and roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100")

    # Getter for roll number
    def get_roll_no(self):
        return self._roll_no

    # Setter for marks
    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative")

    # Getter for marks
    def get_marks(self):
        return self._marks


# Object Creation
s1 = Student("Aniket", 25, 85)

# Display Data
print("Name:", s1.get_name())
print("Roll No:", s1.get_roll_no())
print("Marks:", s1.get_marks())
