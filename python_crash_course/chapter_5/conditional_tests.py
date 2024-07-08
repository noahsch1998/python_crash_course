# simple tests

car = 'ford'
food = 'chicken'
number = 65
team = 'vikings'

print("Is car == 'mazda'? I predict False.")
print(car == 'mazda')
print("Is food == 'chicken'? I predict True.")
print(food == 'chicken')
print("Is number < 50? I predice False")
print(number < 50)
print("Is team == vikings? I predict True.")
print(team == 'vikings')

# more complicated tests

menu = ['Salad', 'Chicken', 'Burger']
menu_lower = [item.lower() for item in menu]
print("Is 'salad' in menu? I predict True.")
if 'salad' in menu_lower:
    print("True")
else:
    print("False")

print("Are 'chicken' and 'burger' on the menu? I predict True.")
if 'chicken' in menu_lower and 'burger' in menu_lower:
    print("True")
else:
    print("False")

print("Are 'salmon' or 'steak' on the menu? I predict False.")
if 'salmon' in menu_lower or 'steak' in menu_lower:
    print("True")
else:
    print("False")