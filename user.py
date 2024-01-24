class User:
    """ this class defines users"""
    def __init__(self, first_name, last_name, field, where):
        """ assigning users a range of attributes"""
        self.first = first_name
        self.last = last_name
        self.field = field
        self.where = where
        self.login_attempts = 0
                
    def describe_user(self):
        """ describe the user using attributes created"""
        print(f"{self.first} {self.last} from {self.where} is majored in {self.field}.")
            
    def greet_user(self):
        """ greet the user"""
        print(f"Hello, {self.first}, how are you?")
        
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        print(f"You've tried {self.login_attempts} attempt in total.")
        
    def reset_login_attempt(self):
        self.login_attempts = 0
        print("Login attempts have been reset to 0.")
