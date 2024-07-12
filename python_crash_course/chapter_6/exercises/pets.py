pet_0 = {
    'name': 'louie',
    'age': 12,
    'breed': 'german shorthair pointer',
    'owner': 'megan'
}

pet_1 = {
    'name': 'rook',
    'age': 4,
    'breed': 'black cat',
    'owner': 'jack'
}

pet_2 = {
    'name': 'moose',
    'age' : 13,
    'breed': 'ragdoll',
    'owner': 'noah'
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    name = pet['name']
    age = pet['age']
    breed = pet['breed']
    owner = pet['owner']
    print(f"{name.title()} is a {age} year old {breed.title()}."
          f"\n {name.title()}'s best friend is {owner.title()}.\n")