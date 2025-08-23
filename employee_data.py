class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self,hours_worked):
        if hours_worked>50:
            overtime_amount = (hours_worked-50)*(self.emp_salary/50)
        else:
            overtime_amount = 0
        return self.emp_salary+overtime_amount

    def emp_assign_department(self,new_emp_department):
        self.emp_department = new_emp_department

    def print_employee_details(self):
        print(f"Name: {self.emp_name}\nID: {self.emp_id}\nSalary: {self.emp_salary}\nDepartment: {self.emp_department}")

employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")

print("Employee details: ")
employee1.print_employee_details()

print(employee1.calculate_emp_salary(60))

employee1.emp_assign_department("FINANCE")

employee1.print_employee_details()
