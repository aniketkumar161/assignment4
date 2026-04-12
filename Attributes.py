class Student:
    college = "ABC college"        # class attribute
    def __init__(self, name, gpa): # instance attributes
        self.name = name
        self.gpa = gpa

stu1 = Student("Rahul", 8.7)
stu2 = Student("Harshita", 9.4)

print(f"{stu1.name} studying in {stu1.college} has {stu1.gpa} cgpa.")

# class attributes can also be accessed with class name
print(f"{stu2.name} studying in {Student.college} has {stu2.gpa} cgpa.")