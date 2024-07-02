#Create motorcycles list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Replace "honda" with "ducati"

motorcycles[0] = 'ducati'
print(motorcycles)

#Add honda to the end of the list

motorcycles.append('honda')
print(motorcycles)

#Delete yamaha from list

del motorcycles[1]
print(motorcycles)

#Add yamaha back in its original place

motorcycles.insert(1, 'yamaha')
print(motorcycles)

#Pop honda from the end of the list

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Pop items from various spots in the list and use them. Print the empty list.

last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
second_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}. The first motorcycle I owned was a {first_owned.title()}. After that I owned a {second_owned.title()}.")
print(motorcycles)

#create new motorcycles list and use remove() method

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()} is too expensive for me.")