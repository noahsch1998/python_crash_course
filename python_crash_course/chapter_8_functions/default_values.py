# you can set a default value for a parameter
def describe_pet(pet_name, animal_type = 'cat'):
    print(f"\nI have a pet {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('moose')

# you can still change the argument of the default parameter
describe_pet(pet_name='louie', animal_type='dog')