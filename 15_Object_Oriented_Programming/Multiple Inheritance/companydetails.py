class company:
    def __init__(self, dept, role, cname):
        self.dept = dept
        self.role = role
        self.cname = cname

    def display_company_details(self):
        print("===== Company Details =====")
        print(f"Department: {self.dept} Role: {self.role} Company: {self.cname}")