class user():
    def __init__(self, login_name, password, full_name, department):
        self.login_name = login_name
        self.password   = password
        self.full_name  = full_name
        self.department = department
        print "User created"

    def get_login_name():
        return self.login_name

    def authenticate(self):
        return self.password == "cnffjbeg"

    def reset_password(self):
        self.password = "cnffjbeg"
        print "Password updated"

    def get_name(self):
        return self.full_name

    def change_name(self, new_name):
        self.full_name = new_name

    def get_department(self):
        return self.department

    def change_department(self, new_department):
        self.department = new_department

    def calculate_salary(self):
        salaries = {"HR": 25000, "Support": 18000, "IT": 40000}
        return salaries[self.department]

class IT_User(user):

    def __init__(self, login_name, password, full_name, department, skills):
        self.login_name = login_name
        self.password = password
        self.full_name = full_name
        self.department = department
        self.skills = skills

    def list_skills(self):
        print "Skills:"
        for s in self.skills:
            print s

    def fix_things(self):
        print "I am here because you broke something!"

new_it_user = IT_User("jbubb", "cnffjbeg", "James Bubb", "IT", ["Windows", "Linux", "MS Exchange", "FTP"])

print new_it_user.get_name()
new_it_user.list_skills()
