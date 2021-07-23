"""Creating Functions"""

se1 = ["Software Engineer", "Sara", 20, "Junior", 4000]
d1 = ["Manager", "Bella", 24, "Senior", 6000]#

"""def code(se):
    print(f"{se[1]} is writing code...")
code(se1)
code(d1)
"""

# The main issue with a function like this is that it doesn't differentiate between the two lists. i.e. Manager / Software Engineer.	
# Manager may / may not be a Software Engineer or have coding skills





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

    #instance method, therefore we can access all the instance attributes defined above
    def code(self):
        print(f"{self.name} is writing code...")

#instances 
se1 = SoftwareEngineer("Max", 26, "Junior", 4000) 
se2 = SoftwareEngineer("Sara", 20, "Junior", 4000)

se1.code()
se2.code()