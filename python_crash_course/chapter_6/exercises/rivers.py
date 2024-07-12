rivers = {
    'mississippi': 'United States',
    'amazon': 'brazil',
    'nile': 'egypt'
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\nRIVERS:")
for river in rivers.keys():
    print(river.title())

print("\nCOUNTRIES:")
for country in rivers.values():
    print(country.title())