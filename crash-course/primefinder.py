# Lists but also NUMBERS
 
import os

os.system('cls')
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
high = int(input("Maximum: "))
primes1 = []
primes2 = []

# why +1? obviously required
for i in range(low,high):
    if all(i % j != 0 for j in range(2,int(i**0.5) + 1)):
        print(str(i) + " <-- prime number")
        primes1.append(i)

print(len(primes1))
print(sum(primes1))

for i in range(low,high):
    if all(i % j != 0 for j in range(2,int(i**0.5))):
        print(str(i) + " <-- prime number")
        primes2.append(i)

print(len(primes2))
print(sum(primes2))

# Convert lists to sets
set1 = set(primes1)
set2 = set(primes2)

# Find the symmetric difference (elements in either set but not in both)
diff1 = set1 - set2  # Elements in list1 that are not in list2
diff2 = set2 - set1  # Elements in list2 that are not in list1

# Combine and print the differences
differences = diff1.union(diff2)
print("Elements that don't match:", differences)   