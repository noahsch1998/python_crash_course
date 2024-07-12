# make a list of short messages
# pass the messages through a function that displays them on screen
# and moves them to a list of sent messages

# function to send the messages
def send_messages(unsent, sent):
    while unsent:
        current_message = unsent.pop(0)
        show_message(current_message)
        sent.append(current_message)

# function to print the message
def show_message(message):
    print(message)

# list of messages
unsent_messages = ['Hello!', 'How are you?', 'Nice to meet you!']
sent_messages = []

# call the function to send the messages
send_messages(unsent_messages, sent_messages)

print(unsent_messages, sent_messages)