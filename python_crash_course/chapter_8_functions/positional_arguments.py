# when using positional arguments, the arguments must be in the same order
# as the paremeters they are applied to
def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'moose')