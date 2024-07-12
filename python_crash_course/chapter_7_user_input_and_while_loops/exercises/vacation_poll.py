# empty dictionary to hold results
results = {}

# flag variable
active = True

# while loop to get user input and add it to results
while active:
    name = input("What is your name?\n")
    destination = input("What is your dream vacation destination?\n")
    results[name] = destination

    # determine if they want to add another result
    repeat = input('Would you like to add another response? (y/n)\n')
    if repeat == 'n':
        active = False

print("\n\tRESULTS")
for name, destination in results.items():
    print(f"{name.title()} wants to visit {destination.title()}")