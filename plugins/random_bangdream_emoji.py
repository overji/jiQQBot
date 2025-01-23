import random


def interface_random_bangdream_emoji(self,args):
        picNum = 6#可以在这里修改表情包数量
        random_Pic = random.randint(1,picNum)
        file_url = f"http://112.124.43.86/bangDream/{random_Pic}.jpg"
        return file_url