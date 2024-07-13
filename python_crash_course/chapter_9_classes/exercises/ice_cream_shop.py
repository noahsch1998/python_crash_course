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



class IceCreamStand(Restaurant):
    """Child class for a specific type of restaurant called ice cream stand"""

    def __init__(self, name, cuisine):
        """Initialize the class with the attributes of an ice cream stand"""
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'rocky road']

    def get_flavors(self):
        """Print the list of flavors available"""
        print(f"\nIce Cream Flavors")

        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream = IceCreamStand('scoops', 'ice cream')
ice_cream.get_flavors()