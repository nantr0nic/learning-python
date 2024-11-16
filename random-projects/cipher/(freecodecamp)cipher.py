#############################################
## Crypt project shit from freecodeacademy ##
#############################################


def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


# encryption = encrypt(text, custom_key)
# decryption = decrypt(text, custom_key)

# def ui(choice, message, key):
#     print('(1) Encrypt or (2) Decrypt?\n')
#     choice = input("1 or 2: ")
#    # if choice != '1' or '2':
#    #    print("Fuck you lol i said 1 or 2")
#    #    exit()
#     print("What is the message?")
#     message = input("Message: ")
#     print("What is the key?")
#     key = input("Key: ")
#     return choice, message, key

while True:
    print("(1) Encrypt or (2) Decrypt?\n")
    choice = input("1 or 2: ")
    #  if choice not in ['1','2']:
    #      print('using set')
    if choice != "1" and choice != "2":
        print("boooooobs")
        break
    print("What is the message?")
    message = input("Message: ")
    print("What is the key?")
    key = input("Key: ")
    if choice == "1":
        print(encrypt(message, key))
        print("Done!")
        break
    elif choice == "2":
        print(decrypt(message, key))
        print("Done!")
        break
