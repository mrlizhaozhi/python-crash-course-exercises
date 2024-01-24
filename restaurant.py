class Restaurant:
    """ this class describes restaurants """
    def __init__(self, name, type):
        """ the __init__ method provides attributes"""
        self.name = name
        self.type = type
        self.number = 0
        
    def describe_restaurant(self):
        """ this method describes restaurants"""
        print(f"{self.name} is a {self.type} restaurant.")
        
    def open_restaurant(self):
        """ this method indicates the restuarant is open"""
        print(f'{self.name}, the {self.type} restaurant, is open.')
        
    def set_number_served(self, number):
        self.number = number
        print(f"{self.name}, the {self.type} restuarant, has served {self.number} customers.")
        
    def increment_number(self, number):
        self.number += number
        print(f"As of now, that number has increased to {self.number} customers.")
  
