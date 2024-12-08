class Dog:
    """Modeling a dog."""

    def __init__(self, name, age):
        """Initialize name and age atttributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate...rolling...over..."""
        print(self.name.title() + " rolled over!")


my_dog = Dog("Luz", 3)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {str(my_dog.age)} years old.")
print(my_dog)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Mendo", 6)
your_dog.sit()
your_dog.roll_over()
