print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first = input("\nFirst number: ")
    if first == "q":
        break
    second = input("\nSecond number: ")
    if second == "q":
        break
    try:
        answer = float(first) / float(second)
    except ZeroDivisionError:
        print("Can't divide by 0.")
    except ValueError:
        print("Invalid input.")
    else:
        print(f"\nAnswer: {answer}")
