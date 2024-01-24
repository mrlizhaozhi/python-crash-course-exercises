# need to review!

from user import User

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        print("An administrator account has the following privileges: ")
        for privilege in self.privileges:
            print(privilege.capitalize())
            
class Admin(User):
    def __init__(self, first_name, last_name, field, where):
        super().__init__(first_name, last_name, field, where)
        self.privileges = Privileges()

