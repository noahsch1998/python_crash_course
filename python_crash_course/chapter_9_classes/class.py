# define a class called 'dog' from scratch
class Dog:    
    """A simple attempt to model a dog"""

# write a method to create a new instance of the dog class
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

# method to tell the dog to sit
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

# method to tell the dog to roll over
    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over.")

# instances of Dog
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"{your_dog.name} is {your_dog.age} years old.")
your_dog.sit()