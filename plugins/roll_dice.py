import random


def interface_roll_dice(args):
    start = 1
    end = 6
    if(len(args) == 2):
        start = int(args[0])
        end = int(args[1])
    elif(len(args) == 1):
        end = int(args[0])
    else:
        pass
    return f"掷骰子的结果是:{str(random.randint(start,end))}"