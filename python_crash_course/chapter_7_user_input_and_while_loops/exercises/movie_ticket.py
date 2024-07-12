age = input("How old are you?\n")

while age.isnumeric() != True:
    age = input("Please enter a valid age\n")

age = int(age)

if age < 3:
    price = 'free'
elif age < 13:
    price = '$10'
else:
    price = '$15'

print(f"Your ticket is {price}.")