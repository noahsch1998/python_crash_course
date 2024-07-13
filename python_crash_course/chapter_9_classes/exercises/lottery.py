from random import choice

balls = [int for int in range(1, 11)]
tries = 0
winning_numbers = []
my_numbers = [1, 4, 6, 9]

while winning_numbers != my_numbers:
    count = 4
    winning_numbers = []

    while count > 0:
        number = choice(balls)
        winning_numbers.append(number)
        count = count - 1

    winning_numbers.sort()
    tries = tries + 1

print(tries)