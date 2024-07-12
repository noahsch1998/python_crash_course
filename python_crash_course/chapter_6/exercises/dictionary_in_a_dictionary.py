# nesting dictionaries within dictionaries can be useful
# but it is often complicated

# create a dictionary of users with a dictionary to store their info
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeston',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{info['first']} {info['last']}"
    location = info['location']
    print(f"Name: {full_name.title()}")
    print(f"Location: {location.title()}")
