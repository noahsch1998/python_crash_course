# python always interprets user input as a string unless you say not to
age = input("How old are you? ")

#use the isnumeric method to verify age is numeric
if age.isnumeric():
    age = int(age)
    print(age >=18)
else:
    print("That is not a valid age.")
# the int function changes age from a string to an integer