class Employee:
    def employeeDetails(self):
        self.name = "Matthew"
        print("Name = ", self.name)
        age = 30
        print("Age =",age)

    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name:",self.name)
        print

employee = Employee()
employee.employeeDetails()