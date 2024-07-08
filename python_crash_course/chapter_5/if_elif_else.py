age = 12
if age < 4:
    price = 'free'
elif age < 18:
    price = '$10'
elif age < 60:
    price = '$25'
else:
    price = '$20'

print(f"Admission is {price}.")

# to avoid invalid data the else statement can be another specific elif

age = 60
if age < 4:
    price = 'free'
elif age < 18:
    price = '$10'
elif age < 60:
    price = '$25'
elif age >= 60:
    price = '$20'

print(f"Admission is {price}.")