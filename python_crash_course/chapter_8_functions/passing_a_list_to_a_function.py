def greet(names):
    """Print a greeting to each name in names"""
    for name in names:
        print(f"Hello, {name.title()}!")

usernames = ['noah', 'jack', 'travis', 'caleb']
greet(usernames)