filename = "guest.txt"

while True:
    name = input("What is your name? (q for quit) >> ").strip()
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
            print("Welcome to the party, " + name)
