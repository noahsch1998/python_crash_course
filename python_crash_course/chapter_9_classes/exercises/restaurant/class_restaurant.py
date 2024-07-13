class Restaurant:
    """A class to define restaurants"""

    def __init__(self, name, cuisine):
        """Method to assign attributes to instance of restaurant"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

    def set_number_served(self, customers):
        """Method to manually set the number of customer served"""
        self.number_served = customers

    def increment_number_served(self, increment):
        self.number_served += increment