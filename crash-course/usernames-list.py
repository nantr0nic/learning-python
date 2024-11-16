# Username thing
import os

os.system("cls")

usernames = []

print("Welcome to the username program!\n")

while True:
    menu = (
        input(
            "\nWould you like to (a)dd a new username, (b) view all usernames, or (c) exit? "
        )
        .strip()
        .lower()
    )
    if menu == "a":
        add = input("\nWhat username do you want to add? >> ").lower().strip()
        if add not in usernames:
            usernames.append(add)
            print("Username added!")
        elif add in usernames:
            print("Username exists. Try again.")
    elif menu == "b":
        for name in usernames:
            print(name)
    elif menu == "c":
        break
    else:
        print("That's not a valid option.")
