def add_numbers(first_num, second_num):
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("I can only work with digits.")
    else:
        print(answer)


print("Give me two numbers and I will add them.")
print("To quit enter 'q'.")


while True:
    first_num = input("First number: ")
    if first_num == 'q':
        break

    second_num = input("Second number: ")
    if second_num == 'q':
        break

    add_numbers(first_num, second_num)