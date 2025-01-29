import random


def interface_random_galgame_emoji(args):
    picNum = 10  # 可以在这里修改表情包数量
    random_Pic = random.randint(1, picNum)
    file_url = f"http://112.124.43.86/gal/{random_Pic}.jpg"
    return file_url

def interface_get_introduction():
    return "随机发送旮旯给木表情包"

def interface_get_name():
    return "旮旯给木表情包"