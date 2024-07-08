toppings = []

# when the name of a list is the only thing in an if statement
# python returns "True" if the list is populated and "Fales" if it is not

if toppings:
    for topping in toppings:
        print(f"Adding {topping}")
    print("\n Your pizza is finished.")
else:
    print("Are you sure you want a plain pizza?")