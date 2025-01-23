from src.BotDB import BotDB


def interface_famous_sentence(args):
    mydb = BotDB()
    return mydb.get_one_famousWords()