# to return a value from a function to a program use the return statement
def format_name(first, last):
    name = f'{first} {last}'
    return name.title()

person = format_name('justin', 'jefferson')
print(person)