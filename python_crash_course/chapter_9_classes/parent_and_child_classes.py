# parent class 'car'
class Car:
    """Class to define a car"""


    def __init__(self, make, model, year):
        """Initialize attributes to a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Return a formated description of the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    

    def read_odometer(self):
        """Print a statment showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")


# method to update the odometer reading
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer")


    def increment_odometer(self, miles):
        """Add the given amount of miles to the odometer reading"""
        self.odometer_reading += miles


# child class 'ElectricCar'
class ElectricCar(Car):
    """Represents the attributes of a car specific to electric car"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class
        Then initialize attributes specific to electric cars"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}kWh battery")

my_tesla = ElectricCar('tesla', 'model 3', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()