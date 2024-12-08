class User:
    def __init__(self, f_name, l_name, age):
        """Defines the first name, last name, and age of a user."""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"User: {self.l_name}, {self.f_name}. Age: {self.age}. Login attempts: {self.login_attempts}"
        )

    def greet_user(self):
        print(f"Wassup, {self.f_name}!")

    def increment_login(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print Admin privileges"""
        print(f"This user has the following privileges: ")
        for item in self.privileges:
            print(f"\t{item}")


class Admin(User):
    """Subclass of User. Inherits attributes and adds privileges."""

    def __init__(self, f_name, l_name, age):
        super().__init__(f_name, l_name, age)
        self.privileges = Privileges()

user_list = [
    User("Andy", "K.", 33),
    User("AP", "R.", 10),
    User("Heather", "Sheppard", 40),
]

adm = user_list[0]
first_admin = Admin(adm.f_name, adm.l_name, adm.age)
first_admin.describe_user()
first_admin.privileges.show_privileges()
