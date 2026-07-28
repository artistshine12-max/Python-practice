#OOPS(Object oriented programming)
class Employee:
    language="Python" #this is a class attribute.
    salary=1200000

    def getInfo(self):
        print(f"The language is {self.language}. THe salary is {self.salary}")


harry= Employee()
harry.language="JavaScript" #Instance attribute
print(harry.language, harry.salary)
harry.getInfo()
