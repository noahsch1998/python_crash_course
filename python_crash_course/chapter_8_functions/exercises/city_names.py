def city(city, country):
    """Return the name of a called city as a string"""
    city_name = f"{city.title()}, {country.title()}"
    return city_name

destination = city('rome', 'italy')
print(destination)

destination = city('barcelona', 'spain')
print(destination)

destination = city('moscow', 'russia')
print(destination)