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




# creating a new class called 'battery'
# 'battery' will be an attribute in 'ElectricCar'
# "composition" allows you to simplify classes

class Battery():
    """"Represents the battery in an instance of ElectricCar"""


    def __init__(self, battery_size = 40):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}kWh battery")

    
    def get_range(self):
        """Print a statement about this battery's range"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go {range} miles on a full charge")


    def upgrade_battery(self):
        if self.battery_size == 65:
            print("Your battery is already upgraded.")
        else:
            self.battery_size = 65
            print("Upgrading battery")





# child class 'ElectricCar'
class ElectricCar(Car):
    """Represents the attributes of a car specific to electric car"""
    

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class
        Then initialize attributes specific to electric cars"""
        super().__init__(make, model, year)
        self.battery = Battery()



my_tesla = ElectricCar('tesla', 'cybertruck', 2024)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()