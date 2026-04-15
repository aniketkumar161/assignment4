class Teacher:             
    def __init__(self, salary):
        self.salary = salary

class Student():     
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):    
    def __init__(self, name, salary, gpa):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta = TA("Rahul", 50_000, 7.5)

print(ta.name, ta.salary, ta.gpa)