class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    def get_emp_info(self):
        return f"name - {self.name}, dob - {str(self.dob)}"
    def calculate_net_salary(self):
        tax = int(self.base_salary * 0.25)
        return self.base_salary - tax
    