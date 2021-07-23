"""For SOFTWARE ENGINEER"""

# position, name, age, level, salary 



se1 = ["Software Engineer", "Sara", 20, "Junior", 4000]
se1 = ["Software Engineer", "Felix", 27, "Senior", 6000]

# Issues: not flexible, no error checking
# Solution: Use a class

# Class
class SoftwareEngineer:
    
    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

     


#instance
se1 = SoftwareEngineer("Max", 26, "Junior", 5000) 