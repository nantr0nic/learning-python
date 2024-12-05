from gen import Sounds

while True:
    s = Sounds()
    print("Nonsense word generator!\nPick from the following list:")
    print("CV, VC, CCV, CVC, CCVC, CVCC, CCVCC.")
    print("Or Q to quit.")
    choice = input(" >> ").lower().strip()
    options = ["cv", "vc", "ccv", "cvc", "ccvc", "cvcc", "ccvcc"]
    if choice == "q":
        print("Thank you! Goodbye.")
        break
    elif choice not in options:
        print("That is not a valid option.\n")
    else:
        d = int(input('Include diphthongs like "oi", "aw", and "ou"? (1=yes, 0=no)\n >> '))
        t = int(input('Include vowel teams like "ai", "ea", and "ui"? (1=yes, 0=no)\n >> '))
        c = int(input('Include "th", "ch", and "sh"? (1=yes, 0=no)\n >> '))
        c_2 = int(input('Include "qu", "ph", and "kn"? (1=yes, 0=no)\n >> '))
        number = input("How many do you want to generate?\n >> ")
        method = getattr(s, choice)
        for i in range(0, int(number)):
            result = method(d, t, c, c_2)
            print(result)
