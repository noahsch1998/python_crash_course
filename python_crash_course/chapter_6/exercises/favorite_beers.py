favorite_beers = {
    'noah': ['McGolden', 'Busch Light'],
    'jack': ['McGolden', 'Foggy Geezer'],
    'travis': ['Coors Light']
}

for person, beers in favorite_beers.items():
    if len(beers) == 1:
        for beer in beers:
            print(f"\n{person.title()}'s favorite beer is {beer}.")
    else:
        print(f"\n{person.title()}'s favorite beers:")
        for beer in beers:
            print(f"\t{beer}")