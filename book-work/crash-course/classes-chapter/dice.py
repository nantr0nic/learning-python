from random import randint

class Dice():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        x = randint(1, self.sides)
        print(f"Rolling a {self.sides}-sided die: {x}")

six_d = Dice()
ten_d = Dice(10)
twenty_d = Dice(20)

six_d.roll_dice()
six_d.roll_dice()
six_d.roll_dice()
six_d.roll_dice()
ten_d.roll_dice()
ten_d.roll_dice()
ten_d.roll_dice()
ten_d.roll_dice()
twenty_d.roll_dice()
twenty_d.roll_dice()
twenty_d.roll_dice()
twenty_d.roll_dice()