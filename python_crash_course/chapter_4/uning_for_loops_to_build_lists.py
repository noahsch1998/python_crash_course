# the purpose of this program is to show how to use a for loop
# to create a new list

squares = []
for number in range(1, 11):
    square = number ** 2
    squares.append(square)

print(squares)

# the same function can be completed using fewer lines

multiples = []
for number in range(1, 11):
    multiples.append(number * 10)

print(multiples)