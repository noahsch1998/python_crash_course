class User:
    """A class to assign attributes to a user"""


    def __init__(self, first, last, membership_level):
        """Initialize user and assign attributes"""
        self.first = first
        self.last = last
        self.membership_level = membership_level
        self.login_attempts = 0
        self.full_name = f"{self.first} {self.last}"


    def describe_user(self):
        """Print the description of a user"""
        print(f"\nName: {self.full_name}")
        print(f"Membership Level: {self.membership_level}")


    def welcome_message(self):
        """Print a message to a user"""
        print(f"\nHello, {self.first}. Thank you for being a "
              f"{self.membership_level} member!")


    def increment_login_attempts(self):
        """Increase login attempts by one when login attempt fails"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Reset the count of login attempts when login attempt is successful"""
        self.login_attempts = 0
        


class Privelages():
    """Assign attributes to privelages"""


    def __init__(self, privelages = ['delete post', 
                                     'delete comment', 
                                     'ban user']):
        """Initialize privelages with attributes"""
        self.privelages = privelages

    def show_privelages(self):
        """Print admin privelages"""
        print("Admin Privelages:")
        for privelage in self.privelages:
            print(f"- {privelage}")


class Admin(User):
    """Class to assign attributes to an admin account"""

    def __init__(self, first, last, membership_level):
        """Initialize Admin class with Admin attributes"""
        super().__init__(first, last, membership_level)
        self.privelages = Privelages()
        

    def show_privelages(self):
        """Print admin privelages"""
        print("Admin Privelages:")
        for privelage in self.privelages:
            print(f"- {privelage}")



admin_0 = Admin('Admin', 'Admin', 'Admin')
user_0 = User('Noah', 'Schlottman', 'diamond')
user_1 = User('Brad', 'Lacoume', 'silver')
user_2 = User('Jack', 'Schneewind', 'gold')

admin_0.privelages.show_privelages()