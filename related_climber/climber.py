import os
import time
import requests
import mysql.connector
from botpy.ext.cog_yaml import read
from lxml import etree


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'}
# url = "https://bestdori.com/assets/cn/characters/resourceset/res001003_rip/card_after_training.png"
dir = "./bangdream_card"
TEST_SIZE = 50 * 1024
CNT = 1
config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "secret", "config.yaml"))
test_config = read(config_path)
host = test_config["host"]
user = test_config["user"]
passwd = test_config["password"]
database = test_config["dbName"]
mydb = mysql.connector.connect(
    host = host,
    user = user,
    passwd = passwd,
    database = database
)

def get_pic(target:str):
    global CNT
    after_url = f"https://bestdori.com/assets/cn/characters/resourceset/res{target}_rip/card_after_training.png"
    normal_url = f"https://bestdori.com/assets/cn/characters/resourceset/res{target}_rip/card_normal.png"
    print(f"now getting {target}")
    after_r = requests.get(after_url,headers=header)
    if after_r.status_code == 200:
        if len(after_r.content) > TEST_SIZE:
            with open(f'./bangdream_card/{CNT}.png', 'wb') as f:
                f.write(after_r.content)
            CNT += 1
    else:
        print(f"cannot find after of {target}")

    normal_r = requests.get(normal_url, headers=header)
    if normal_r.status_code == 200:
        if len(normal_r.content) > TEST_SIZE:
            with open(f'./bangdream_card/{CNT}.png', 'wb') as f:
                f.write(normal_r.content)
            CNT += 1
    else:
        print(f"cannot find normal of {target}")

def get_pic_url(target:str):
    global CNT
    after_url = f"https://bestdori.com/assets/cn/characters/resourceset/res{target}_rip/card_after_training.png"
    print(f"now getting {target}")
    after_r = requests.get(after_url, headers=header)
    if after_r.status_code == 200:
        if len(after_r.content) > TEST_SIZE:
            print(f"get {target} at url {after_url}")
            send_to_db(after_url,target[0:3],target[3:6])
    else:
        print(f"cannot find after of {target}")

def send_to_db(url:str,characterName:str,cardName:str):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM bangDreamCardUrl WHERE url = \"{url}\";")
    res: list = mycursor.fetchall()
    if (len(res) != 0):
        print("url已被登记了")
    else:
        mycursor.execute(f"INSERT INTO bangDreamCardUrl (`url`,`characterName`,`cardId`) VALUES (\"{url}\",\"{characterName}\",\"{cardName}\");")
        mydb.commit()
        print(f"已经登记{url},characterName:{characterName},cardName:{cardName}")


if __name__ == '__main__':
    for role in range(1,41):
        new_role = ""
        if (role <= 9 and role >= 1):
            new_role = f"00{role}"
        else:
            new_role = f"0{role}"

        for card in range(1,100):
            if(card <= 9 and card >= 1):
                new_card = f"00{card}"
            else:
                new_card = f"0{card}"

            get_pic_url(new_role + new_card)
            time.sleep(0.1)











