# empty dictionary to hold user inputs
responses = {}

#flag to indicate poll is still active
poll_active = True

#prompt for a poll response
while poll_active:
    name = input('\nWhat is your name?\n')
    team = input("\nWhat is your favorite football team?\n")

    # store the information in responses
    responses[name] = team

    # ask if there will be another response
    repeat = input("\nDo you want to add another response? (y/n)")
    if repeat == 'n':
        poll_active = False

# print poll results
print("\n\tRESULTS")
for name, team in responses.items():
    print(f"{name.title()}'s favorite team is the {team.title()}")