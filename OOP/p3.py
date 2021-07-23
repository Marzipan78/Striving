"""INHERITANCE

-> a child class is a class that inherits from the parent class (employee)
-> a child class can override the methods of the parent class
-> a child class can also add additional methods
"""

class Employee:   #parent class
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class SoftwareEngineer(Employee):   # child class 
    pass


class Designer(Employee):   # child class   
    pass
