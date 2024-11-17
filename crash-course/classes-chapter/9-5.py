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


user_list = [
    User("Andy", "K.", 33),
    User("AP", "R.", 10),
    User("Heather", "Sheppard", 40),
]

for user in user_list:
    user.describe_user()

user_list[0].increment_login()
user_list[0].increment_login()
user_list[1].increment_login()
user_list[2].increment_login()
user_list[2].increment_login()
user_list[2].increment_login()

for user in user_list:
    user.describe_user()

for user in user_list:
    user.reset_login_attempts()
    user.describe_user()
