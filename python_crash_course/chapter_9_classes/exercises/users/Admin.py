from User import User

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