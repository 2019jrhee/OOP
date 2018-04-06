class Employee:
    def employeeDetails(self):
        self.name = "Ben"
    @staticmethod
    def welcome():
        print("Welcome")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcome()
