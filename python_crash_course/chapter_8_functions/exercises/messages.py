# make a list of short messages
# pass the messages through a function that displays them on screen

# function to print the messages
def show_messages(messages):
    for message in messages:
        print(message)

# list of messages
messages = ['Hello!', 'How are you?', 'Nice to meet you!']

# call the function to print the messages
show_messages(messages)