"""For SOFTWARE ENGINEER"""

#       position,name, age, level, salary 
se1 = ["Software Engineer", "Sara", 20, "Junior", 4000]
se2 = ["Software Engineer", "Felix", 27, "Senior", 6000]

# Issues: not flexible, no error checking

# Solution: Use a class

# Class
class SoftwareEngineer:

    #class atributes
    alias = "Keyboard Tech"
    
    def __init__(self, name, age, level, salary):
        # instance attributes belong to only the object created
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

     


#instance
se1 = SoftwareEngineer("Max", 26, "Junior", 4000) 
se2 = SoftwareEngineer("Sara", 20, "Junior", 4000)
print(se1.name, se1.age, se1.level, se1.salary)  # here we refer to the instance attribute (self.name etc) and not the init arugments
print(se1.alias, se2.alias)    # we can access the class attributes using the instance name
print(SoftwareEngineer.alias) # we can access the class attributes using the class name