"""INHERITANCE

-> a child class is a class that inherits from the parent class (employee)
-> a child class can override the methods of the parent class
-> a child class can also add additional methods
"""

class Employee:   # parent class
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name}, is working...")        


class SoftwareEngineer(Employee):   # child class 
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    
        

class Designer(Employee):   # child class   
    pass


#se = SoftwareEngineer() # TypeError EXPECTED: __init__() missing 2 required positional arguments: 'name' and 'age',
                        # as it inhereted from Employee

se1 = SoftwareEngineer("John", 30, 5000, "Junior")	
print(se1.level)

d = Designer("Jane", 30, 6000)
d.work()