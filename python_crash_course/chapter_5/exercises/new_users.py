current_users = ['Jets18', 'VikesFan84', 'Skol28']
current_users_l = [user.lower() for user in current_users]

new_users = ['JJtoJJ', 'Skol28', 'DT15']

for user in new_users:
    user_l = user.lower()
    if user_l in current_users_l:
        print(f"{user} is already taken. Please try a different username.")
    else:
        current_users.append(user)
        print(f"Welcome to the forum, {user}")