#keyword arguments can be passed to the function in any order
def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print(f"I have a pet {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='moose', animal_type='cat')