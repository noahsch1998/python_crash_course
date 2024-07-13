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

# create a new instance of Car
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 1 modify odometer reading directly
my_new_car.odometer_reading = 12
my_new_car.read_odometer()

# 2 modify the odometer reading using a method
my_new_car.update_odometer(19)
my_new_car.read_odometer()

# 3 increment the odometer using a method
my_new_car.increment_odometer(13)
my_new_car.read_odometer()