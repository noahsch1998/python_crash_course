number = input("Give me a number and I will tell you if it is even or odd: ")
number = int(number)

# the modulo operator (%) returns the remainder of a division
if number % 2 == 0:
    print("EVEN")
else:
    print("ODD")