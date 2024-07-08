availible_toppings = ['pepperoni', 'saussage', 'extra cheese', 'mushrooms',
                      'peppers', 'onions']

request = ['pepperoni', 'extra cheese', 'french fries']

for topping in request:
    if topping in availible_toppings:
        print(f"Adding {topping} to your pizza.")
    else:
        print(f"Sorry, we don't have {topping}.")

print("\nYour pizza is finished.")