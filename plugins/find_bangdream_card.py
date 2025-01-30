import os
import random
import mysql.connector
from botpy.ext.cog_yaml import read

config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "secret", "config.yaml"))
test_config = read(config_path)

def getDbSize():
    host = test_config["host"]
    user = test_config["user"]
    passwd = test_config["password"]
    database = test_config["dbName"]
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) FROM BanGDream_Card;")
    cardNums = cursor.fetchone()[0]
    return cardNums

def getCard(id:int):
    #如果正常返回，格式为["卡面命名",布尔数字:有无普通卡面,布尔数字:有无特训卡面，总卡面数]
    host = test_config["host"]
    user = test_config["user"]
    passwd = test_config["password"]
    database = test_config["dbName"]
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database
    )
    cursor = mydb.cursor()
    cardNums = getDbSize()
    if id <= 0 or id > cardNums:
        return []
    else:
        cursor.execute(f"SELECT * FROM BanGDream_Card where id = {id};")
        row = cursor.fetchone()
        return [f"{row[1]}{row[2]}",row[3],row[4],f"{cardNums}"]

def interface_find_bangdream_card(args):
    if (not args) or len(args) == 0:
        return interface_get_introduction()
    else:
        ans = []
        target = int(args[0])
        li = getCard(target)
        normal_url = ""
        after_url = ""
        if len(li) > 3:
            if li[1]:
                normal_url = f"https://bestdori.com/assets/cn/characters/resourceset/res{li[0]}_rip/card_normal.png"
                ans.append("特训前卡面")
                ans.append(normal_url)
            if li[2]:
                after_url = f"https://bestdori.com/assets/cn/characters/resourceset/res{li[0]}_rip/card_after_training.png"
                ans.append("特训后卡面")
                ans.append(after_url)
            return ans
        else:
            return interface_get_introduction()

def interface_get_introduction():
    return f"展示一张邦多利卡片，输入格式为/邦多利查卡 [卡面ID]，例:/邦多利查卡 947 。请注意输入的卡面ID应该满足大于0，小于等于{getDbSize()}"

def interface_get_name():
    return "邦多利查卡"

if __name__ == "__main__":
    print(interface_find_bangdream_card(["1779"]))
    print(getDbSize())