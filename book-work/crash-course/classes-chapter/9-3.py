class User:
    def __init__(self, f_name, l_name, age):
        """Defines the first name, last name, and age of a user."""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def describe_user(self):
        print(f"User: {self.l_name}, {self.f_name}. Age: {self.age}")

    def greet_user(self):
        print(f"Wassup, {self.f_name}!")


user_list = [
    User("Andy", "K.", 33),
    User("AP", "R.", 10),
    User("Heather", "Sheppard", 40),
]

for user in user_list:
    user.describe_user()
    user.greet_user()
