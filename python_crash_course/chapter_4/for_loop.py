# define list named cars
cars = ['mazda', 'toyota', 'nissan']

# create for loop to print all names in cars
for car in cars:
    print(f"{car.title()} is a Japanese car brand.")
    print(f"{car.title()} makes reliable cars.\n")

# once a line is not indented python knows that it is not part of the loop
print('Japanese cars are known to be safe.')

# python creates a new variable called car
# for each item in cars, python assigns the item to the variable
# then runs through the for loop for that item