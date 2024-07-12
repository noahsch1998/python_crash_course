# list to store orders
orders = ['club', 'pastrami', 'tuna', 'pastrami',
           'turkey', 'pastrami', 'italian']

# list for completed orders
completed = []

# pastrami is not available, remove it from the order
if 'pastrami' in orders:
    print("We are out of pastrami.")

# remove pastrami from orders
while 'pastrami' in orders:
    orders.remove('pastrami')

# while loop to move item from orders to completed
while orders:
    working = orders.pop()
    print(f"Working on your {working} sandwich.")
    completed.append(working)

print("\n\tORDER")
for sandwich in completed:
    print(sandwich)