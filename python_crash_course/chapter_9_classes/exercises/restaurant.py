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

print(r_0.name)
print(r_0.cuisine)

r_0.describe_restaurant()
r_0.open_restaurant()