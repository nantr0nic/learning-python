# Lists but also NUMBERS

import os

os.system("cls")
print("\n\n\n")
print("█ ▄▄  █▄▄▄▄ ▄█ █▀▄▀█ ▄███▄          ▄     ▄   █▀▄▀█ ███   ▄███▄   █▄▄▄▄ ")
print("█   █ █  ▄▀ ██ █ █ █ █▀   ▀          █     █  █ █ █ █  █  █▀   ▀  █  ▄▀ ")
print("█▀▀▀  █▀▀▌  ██ █ ▄ █ ██▄▄        ██   █ █   █ █ ▄ █ █ ▀ ▄ ██▄▄    █▀▀▌  ")
print("█     █  █  ▐█ █   █ █▄   ▄▀     █ █  █ █   █ █   █ █  ▄▀ █▄   ▄▀ █  █  ")
print(" █      █    ▐    █  ▀███▀       █  █ █ █▄ ▄█    █  ███   ▀███▀     █   ")
print("  ▀    ▀         ▀               █   ██  ▀▀▀    ▀                  ▀    ")
print("                                                                        ")
print("▄████  ▄█    ▄   ██▄   ▄███▄   █▄▄▄▄                                    ")
print("█▀   ▀ ██     █  █  █  █▀   ▀  █  ▄▀                                    ")
print("█▀▀    ██ ██   █ █   █ ██▄▄    █▀▀▌                                     ")
print("█      ▐█ █ █  █ █  █  █▄   ▄▀ █  █                                     ")
print(" █      ▐ █  █ █ ███▀  ▀███▀     █                                      ")
print("  ▀       █   ██                ▀                                       \n\n")

print("Pick the range you'd like to find prime numbers in.")
low = int(input("Minimum: "))
high = int(input("Maximum: ")) + 1
primes = []

for i in range(low, high):
    if all(i % j != 0 for j in range(2, i)):
        print(str(i) + " <-- prime number")
        primes.append(i)

print(len(primes))
