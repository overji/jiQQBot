import random


def interface_find_bangdream_card(args):
    if (not args) or len(args) == 0:
        picNum = 250  # 可以在这里修改表情包数量
        random_Pic = random.randint(1, picNum)
        file_url = f"http://112.124.43.86/bangdream_card/{random_Pic}.png"
    else:
        target = int(args[0])
        if (target > 0 and target <= 2640):
            file_url = f"http://112.124.43.86/bangdream_card/{target}.png"
        else:
            return "邦多利查卡功能介绍\n使用方法: /邦多利查卡 [卡面ID]\n示例: /邦多利查卡 1582\n请确保卡面ID是一个整数，并且这个数字应当大于0并小于2641，否则会返回本消息"
    return file_url

def interface_get_introduction():
    return "展示一张邦多利卡片"

def interface_get_name():
    return "邦多利查卡"