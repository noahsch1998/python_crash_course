favorite_teams = {
    'noah': 'vikings',
    'brad': 'commanders',
    'ethan': 'bears',
    'casey': 'packers',
    'jay': 'vikings',
    }

# To loop through all of the key/value pairs use a for loop with two
# variables and the items method.

for name, team in favorite_teams.items():
    print(f"{name.title()}'s favorite team is the {team.title()}")

# You can loop through all of the keys using one variable and the keys method

nfc_north = ['brad', 'noah', 'casey']

for name in favorite_teams.keys():
    print(f"Hi, {name.title() }")
    if name in nfc_north:
        team = favorite_teams[name].title()
        print(f"\tYou're a fan of {team.title()}. That makes us rivals.")

# Use not in to determine if a key is in your dictionary

if 'jack' not in favorite_teams.keys():
    print("We do not know Jack's favorite team.")

# Use the sorted function to loop through the keys in order

for name in sorted(favorite_teams.keys()):
    print(name.title())

# Use the values method to separate the valuse from their keys

print("TEAMS")
for team in favorite_teams.values():
    print(team.title())

#Use the set function to avoid repeats

print("\nTEAMS")
for team in set(favorite_teams.values()):
    print(team.title())