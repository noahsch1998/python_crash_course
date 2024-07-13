class Restaurant:
    """A class to define restaurants"""

    def __init__(self, name, cuisine):
        """Method to assign attributes to instance of restaurant"""
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

r_0 = Restaurant("Dom's", 'Italian')
r_1 = Restaurant("Ching's", "Chinese")
r_2 = Restaurant("Miko's", 'Greek')

r_0.describe_restaurant()
r_1.describe_restaurant()
r_2.describe_restaurant()