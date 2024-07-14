from pathlib import Path
import json

def get_user_info():
    """Function to get a user to input their information"""
    username = input("What is your name?: ")
    age = input("How old are you?: ")
    location = input("Where are you located?: ")
    user_info = {'username': username, 'age': age, 'location': location}
    return user_info

def save_info(user_info):
    """Save the user info in a .json file"""
    contents = json.dumps(user_info)
    path.write_text(contents)

def show_new_message(username):
    """Print a message telling the user that their name is saved"""
    print(f"We'll remember you when you come back, {username}.")

def retrieve_user_info():
    """Retrieve the username from the .json file"""
    contents = path.read_text()
    user_info = json.loads(contents)
    return user_info

def show_returning_message(username):
    """Print message to welcome existing user back"""
    print(f"Welcome back, {username}!")

def welcome_user():
    """Welcome the user back if their profile exists"""
    user_info = retrieve_user_info()
    show_returning_message(user_info['username'])
    print(user_info['age'])
    print(user_info['location'])
    

def make_user():
    """Make a new user profile"""
    user_info = get_user_info()
    save_info(user_info)
    show_new_message(user_info['username'])

def verify_user():
    user_info = retrieve_user_info()
    verify = input(f"Is {user_info['username']} your username? (y/n)\n")
    if verify == 'y':
        return True
    else:
        return False


path = Path('saving_user_data/username.json')
if path.exists():
    current_user = verify_user()
    if current_user:
        welcome_user()
    else:
        make_user()
else:
    make_user()