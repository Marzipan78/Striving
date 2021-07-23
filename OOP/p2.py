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

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # def information(self):
    #     information = f"name = {self.name}, age ={self.age}, level = {self.level}"
    #     return information

    # d-under  methods
    def __str__(self):
        information = f"name = {self.name}, age ={self.age}, level = {self.level}"
        return information        
    
    def __eq__(self, other):    #comparing two objects by name and age, overwriting the default behaviour of Memory address
        return  self.name == other.name and self.age == other.age 
       

    #purposely omiting self

    @staticmethod # adding decorator to see effects

    def entry_salary(age):   # EXPECT TypeError: entry_salary() takes 1 positional argument but 2 were given 
        if age < 25:         # Self is automatically passed as the first argument
            return 4000      # however it can be passed to the class
        if age < 30:
            return 8000    

    def entry_salary_2(self,age):
        if age < 25:    
            return 4000
        if age < 30:
            return 8000

        

#instances 
se1 = SoftwareEngineer("Max", 26, "Junior", 7000) 
se2 = SoftwareEngineer("Sara", 20, "Junior", 4000)
se3 = SoftwareEngineer("Sara", 20, "Junior", 4000)

se1.code()
se1.code_in_language("Python")
# print(se1.information())
se2.code()
se2.code_in_language("C++")

#print(se2 == se3) # will never be the same as the Memory Address are different

#se1.entry_salary(24) # does not  work because of the arg error for omiting self
print(SoftwareEngineer.entry_salary(24))  # works because of self was ignored
print(se1.entry_salary(24)) # should work because of the decorator, note self is not passed, therefore will not work for a speqific instance    
se1.entry_salary_2(24) 