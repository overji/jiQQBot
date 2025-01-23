import random


def interface_roll_dice(self, args):
    return f"掷骰子的结果是:{str(random.randint(1, 6))}"