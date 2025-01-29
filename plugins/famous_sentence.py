from src.BotDB import BotDB


def interface_famous_sentence(args):
    mydb = BotDB()
    return mydb.get_one_famousWords()

def interface_get_introduction():
    return "返回一句名言"

def interface_get_name():
    return "小锦一言"