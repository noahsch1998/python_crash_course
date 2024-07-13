from random import randint

class Die:
    """Clas to represent possible dice"""


    def __init__(self, sides):
        """Assign attributes to dice"""
        self.sides = sides

    def roll_dice(self):
        """Method to roll dice"""
        roll = randint(1, self.sides)
        print(f"You rolled a {roll}\n")

sides = input("How many sides does the die have?\n")
sides = int(sides)

die = Die(sides)
die.roll_dice()

while True:
    active = input("Roll again? (y/n)\n")
    if active == 'y':
        die.roll_dice()
    elif active == 'n':
        break
    else:
        print('Invalid input, try again\n')