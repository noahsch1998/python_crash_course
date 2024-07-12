prompt = "We are very busy right now."
prompt += "\nHow many people are in your group? "

group = input(prompt)
group = int(group)

if group > 7:
    print("I am sorry, you will have to wait about 20 minutes")
else:
    print("We are getting your table ready now.")