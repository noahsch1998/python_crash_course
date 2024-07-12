# start with a list of uncomfirmed users
# and an empty list for confirmed users
unconfirmed_users = ['joe', 'mike', 'bob']
confirmed_users = []

# verify each user until there are no unconfirmed users
while unconfirmed_users:
    currrent_user = unconfirmed_users.pop()

    print(f"Verifying user: {currrent_user.title()}")
    confirmed_users.append(currrent_user)

# print the list of confirmed users
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())