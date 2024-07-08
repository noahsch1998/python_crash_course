# you can search within a list using the "in" keyword

toppings = ['pepperoni', 'onions', 'mushrooms']
if 'mushrooms' in toppings:
    print("This pizza has mushrooms.")
else:
    print("This pizza does not have mushrooms.")

if 'peppers' in toppings:
    print("This pizza has peppers.")   
else:
    print("This pizza does not have peppers.")

# you can use "not in" to check if a item is not in a list

topping = 'olives'
if topping not in toppings:
    print(f"This pizza does not have {topping}.")