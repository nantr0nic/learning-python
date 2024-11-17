import json

filename = "username.json"


def get_stored_username():
    """Get stores username if available."""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Gets a new username is file doesn't exist."""
    username = input("What is your name? >>")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        if not verify_user(username):
            username = get_new_username()
            print(f"We'll remember you, {username}.")
        else:
            print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you, {username}.")


def verify_user(username):
    """Verifies username."""
    verity = input(f"Is your username {username}? (y/n) >> ")
    if verity == "y":
        return True
    elif verity == "n":
        return False
    else:
        print("That's not y/n.")


greet_user()
