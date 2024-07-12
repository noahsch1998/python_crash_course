def make_pizza(*toppings):
    """Summarize the pizza we are making"""
    print("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('pepperoni', 'mushroom', 'onion')