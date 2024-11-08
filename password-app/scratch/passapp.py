import os
import string
import random

# Setting all options to 'on' and length to 12
letters = True
digits = True
punctuation = True
letters_enabled = False
digits_enabled = False
punctuation_enabled = False
length = 12

# Password generator function
def genpass(length):
    options = []
    if letters == True:
        letters_enabled = string.ascii_letters
        options.append(letters_enabled)
    if digits == True:
        digits_enabled = string.digits
        options.append(digits_enabled)
    if punctuation == True:
        punctuation_enabled = string.punctuation
        options.append(punctuation_enabled)
    elif letters == False and digits == False and punctuation == False:
        print("You must have at least 1 option enabled!")
        return
    generated = ''
    for i in range(0,length):
        if any(option in options for option in options): # lol it works but not really
            generated += random.choice()
    print(f"Password: {generated}")
    # heuristic shit
    print(f"Letters = {letters} / digits = {digits} / punc = {punctuation}")
    print(f"{letters_enabled} / {digits_enabled} / {punctuation_enabled} ")
    return

# Checkbox function for main interface loop
def checkbox(text, checked):
    if checked:
        checked_str = "[X] {}".format(text)
    else:
        checked_str = "[ ] {}".format(text)
    return checked_str

# Main loop
while True:
    os.system('cls')
    print(" # # # # # # # # # # #\n--> Password Generator <--\n # # # # # # # # # # #")
    print("Choose password options.")
    print(checkbox('[L]etters', letters))
    print(checkbox('[D]igits', digits))
    print(checkbox('[P]unctuation', punctuation))
    print(f"Password L[e]ngth: {length}")
    print("Type G to [G]enerate or X to E[x]it!")
    
    choice = input(">> ").lower().strip()
    
    # Input loop
    while True:
        if choice == 'l':
            letters = not letters
            break
        elif choice == 'd':
            digits = not digits
            break
        elif choice == 'p':
            punctuation = not punctuation
            break
        elif choice == 'e':
            print("How many characters long do you want the password to be?")
            length = int(input(">> ").strip())
            break
        elif choice == 'g':
            genpass(length)
            input("Press any key to continue!")
            break
        elif choice == 'x':
            break
        else:
            print("Not a valid option.")
            break
    if choice == 'x':
        break