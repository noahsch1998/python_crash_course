# create a program that allows the user to create a sandwich
# allow them to select a type of bread and the toppings

#function to make the sandwich
def make_sandwich(bread, ingredients):
    print(f"\nMaking a sandwich on {bread} bread with the following toppings:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

#create a list for toppings
toppings = []

# collect user input for the desired sandwich
bread = input("What kind of bread would you like?\n")

print('\nWhen you are done adding toppings, enter "done"')
while True:
    topping = input("What would you like to add to the sandwich?\n")
    if topping.lower() == 'done':
        break
    else:
        toppings.append(topping)

# call the function to make the sandwich
make_sandwich(bread, toppings)