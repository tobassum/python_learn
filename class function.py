class Employee():
    
    empcount = 0
    
    # self as a intences and name and salary as parameters
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1
        
    def displaycount(self):
        print("Total Employee %d" % Employee.empcount)
        
    def displayEmployee(self):
        print("Name: ", self.name, "  salary: ", self.salary)
        

emp1 = Employee(input("Enter the name of Employee: "), 20000)
emp2 = Employee(input("Enter the name of Employee: "), 50000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee are %d" % Employee.empcount)
    
    