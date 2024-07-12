topping = ''
pizza = []
available_toppings = ('pepperoni', 'sausage', 'bacon', 'onion', 'onions',
                      'mushroom', 'mushrooms', 'green pepper', 'green peppers',
                      'extra cheese')
messenge = "What topping would you like to add to your pizza?"
messenge += "\nWhen you are done adding toppings type 'quit': "

while True:
    topping = (input(messenge))
    if topping.lower() in available_toppings:
        print(f"\nAdding {topping} to your pizza.\n")
        pizza.append(topping.lower())
    elif topping == 'quit':
        break
    else:
        print(f"\nI'm sorry, we can't add {topping} to your pizza.\n")

print("You ordered a pizza with the following toppings:")

for topping in pizza:
    print(f"\t{topping}")