151115_q3.py

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary updated to {new_salary}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} added to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name}: {total}")

    def display_all_employees(self):
        print(f"Employees in {self.department_name}:")
        for employee in self.employees:
            employee.display_details()

# Interactive example
dept = Department("Engineering")
emp1 = Employee("Alice", "E001", 60000)
emp2 = Employee("Bob", "E002", 55000)

dept.add_employee(emp1)
dept.add_employee(emp2)
dept.display_all_employees()
dept.calculate_total_salary_expenditure()
