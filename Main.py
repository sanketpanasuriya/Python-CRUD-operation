from ValidateUser import Validation as V
from Database import Queries
class Employee :
    emp_no = ""
    phone = ""
    fname  =""
    lname = ""
    email = ""
    salary = 0
    field = ""

    def __init__(self):
        self.emp_no = input("Enter Employee number: ")
        self.fname = input("Enter first name: ")
        self.lname = input("Enter Last name: ")
        self.email = V.isEmail(self)
        self.phone = V.isPhone(self)
        self.salary = int(input("Enter Salary: "))
        self.field = input("Enter field: ")

print("1. Add Employee")
print("2. Display record of all Employee ")
print("3. Display record by first name")
print("4. Update salary using employee number")
print("5. Update all employee salary")
print("6. Delete Employee by Employee number")
print()
ch = int(input("Enter Choice: "))
if ch == 1:
    s = Employee()
    r = Queries()
    r.insert(s.emp_no,s.fname,s.lname,s.email,s.phone,s.salary,s.field)
elif ch == 2:
    r = Queries()
    r.DisplayAll()
elif ch == 3:
    r = Queries()
    r.DisplayFirst()
elif ch == 4:
    r = Queries()
    r.update_salary_by_emp_id()
elif ch == 5:
    r = Queries()
    r.update_All_employee_salary()
elif ch == 6:
    r = Queries()
    r.Delete()      
else :
    print("Please enter valid input.")
