prompt = "Tell me something and I will repeat it back to you"
prompt += '\nTo quit the program enter "quit": '

#active is a 'flag' variable. if any condition makes the flag change to 'False'
#the while loop stops running
active = True
message = ' '
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)