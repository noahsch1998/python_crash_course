#create list
cities = ['rome', 'london', 'athens', 'sydney', 'paris']
#print list
print(cities)
#print list sorted alphabetically without modifying the list
print(sorted(cities))
#show list in original order
print(cities)
#print list in reverse alphabetical order without modifying the list
print(sorted(cities, reverse = True))
#change the list to reverse order and print new list
cities.reverse()
print(cities)
#sort the list in alphabetical order and print the list
cities.sort()
print(cities)
#sort the list in reverse alphabetical order and print
cities.sort(reverse = True)
print(cities) 