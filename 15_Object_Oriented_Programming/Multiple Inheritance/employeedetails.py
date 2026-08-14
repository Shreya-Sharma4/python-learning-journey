from personaldetails import person
from companydetails import company


class employee(person, company):
    def __init__(self, name, city, age, dept, role, cname, salary):
        person.__init__(self, name, city, age)
        company.__init__(self, dept, role, cname)
        self.salary = salary

    def display_employee_details(self):
        self.display_personal_details()
        self.display_company_details()