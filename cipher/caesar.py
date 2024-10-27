alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = 3

def caesar(message):
    result = []
    for char in message:
        # Check if the character is and in the alphabet
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % len(alphabet)
            result.append(alphabet[new_index])
        else:
            # If it's not a  letter, add it as is
            result.append(char)
    return ''.join(result)

while True:
    print("Caesar cipher. What is your message?")
    message = input("Message: ")
    shifted_message = caesar(message)
    print(f"Caesar-fied! --> {shifted_message}")
    
    # Option to continue or exit
    option = input("Do you want to encode another message? (y/n): ").lower()
    if option != 'y':
        break
