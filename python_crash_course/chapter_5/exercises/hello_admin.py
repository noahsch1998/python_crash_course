users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello Admin. Would you like to see a status report?")
        else:
            print(f"Hello {user.title()}. Welcome to your account page.")
else:
    print("There are no active users.")