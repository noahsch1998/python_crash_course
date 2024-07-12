players = {
    9: {
        'first': 'JJ',
        'last': 'McCarthy',
        'position': 'quarterback',
        'age': 21,
        'college': 'Michigan'
    },

    18: {
        'first': 'Justin',
        'last': 'Jefferson',
        'position': 'wide receiver',
        'age': 25,
        'college': 'LSU'
    },

    22: {
        'first': 'Harrison',
        'last': 'Smith',
        'position': 'safety',
        'age': 35,
        'college': 'Notre Dame'
    }
}

print("Minnesot Vikings 2024 Roster")
for number, info in players.items():
    print(f"#{number}")
    name = f"{info['first']} {info['last']}"
    position = info['position']
    age = info['age']
    college = info['college']
    print(f"\tName: {name.title()}")
    print(f"\tPosition: {position.title()}")
    print(f"\tAge: {age}")
    print(f"\tCollege: {college.title()}\n")