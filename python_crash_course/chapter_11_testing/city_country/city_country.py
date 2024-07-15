from function_city_country import format_city

city = input("Name a city: ")
country = input("What country is your city in?: ")

location = format_city(city, country)
print(location)