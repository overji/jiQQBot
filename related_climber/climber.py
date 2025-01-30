import os
import time
import requests
import mysql.connector
from botpy.ext.cog_yaml import read
from lxml import etree


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'}
# url = "https://bestdori.com/assets/cn/characters/resourceset/res001003_rip/card_after_training.png"
dir = "./bangdream_card"
TEST_SIZE = 25 * 1024
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
    normal_url = f"https://bestdori.com/assets/cn/characters/resourceset/res{target}_rip/card_normal.png"
    after_url = f"https://bestdori.com/assets/cn/characters/resourceset/res{target}_rip/card_after_training.png"
    print(f"now getting {target}")
    normal_exist:bool = False
    after_exist:bool = False
    normal_r = requests.get(normal_url,headers=header)
    after_r = requests.get(after_url, headers=header)
    if after_r.status_code == 200:
        if len(after_r.content) > TEST_SIZE:
            print(f"get normal {target} at url {after_url}")
            after_exist = True
    else:
        print(f"cannot find after of {target}")

    if normal_r.status_code == 200:
        if len(normal_r.content) > TEST_SIZE:
            print(f"get normal {target} at url {normal_url}")
            normal_exist = True
    else:
        print(f"cannot find normal of {target}")

    if normal_exist or after_exist:
        send_to_db(target[0:3],target[-3:],normal_exist,after_exist)
        return True
    else:
        return False


def send_to_db(characterName:str,cardName:str,hasNormal:bool,hasAfter:bool):
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO BanGDream_Card(characterName, cardId, hasNormal, hasAfter) VALUES(\"{characterName}\",\"{cardName}\",{hasNormal},{hasAfter})")
    print(f"已经登记{characterName}{cardName},characterName:{characterName},cardName:{cardName}")
    mydb.commit()


if __name__ == '__main__':
    for role in range(1,41):
        new_role = ""
        spaceCnt = 0
        if (role <= 9 and role >= 1):
            new_role = f"00{role}"
        else:
            new_role = f"0{role}"

        for card in range(1,200):
            if(card <= 9 and card >= 1):
                new_card = f"00{card}"
            else:
                new_card = f"0{card}"

            if get_pic_url(new_role + new_card):
                spaceCnt = 0
            else:
                spaceCnt += 1
                if spaceCnt > 10:
                    break
            time.sleep(0.1)











