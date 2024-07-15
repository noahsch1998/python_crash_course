def format_city(city, country, population = None):
    if population:
        location = f"{city}, {country} - Population: {population}"
        return location.title()
    else:
        location = f"{city}, {country}"
        return location.title()