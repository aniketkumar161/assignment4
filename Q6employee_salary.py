
from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        print("Intern Salary:", self.stipend)


class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print("Full Time Employee Salary:", self.monthly_salary)


class ContractEmployee(Employee):
    def __init__(self, hours_worked, rate_per_hour):
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        salary = self.hours_worked * self.rate_per_hour
        print("Contract Employee Salary:", salary)


# Object Creation
i1 = Intern(10000)
f1 = FullTimeEmployee(50000)
c1 = ContractEmployee(20, 500)

# Calling Methods
i1.calculate_salary()
f1.calculate_salary()
c1.calculate_salary()
