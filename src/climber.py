import os
import time
import requests
from lxml import etree


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'}
# url = "https://bestdori.com/assets/cn/characters/resourceset/res001003_rip/card_after_training.png"
dir = "./bangdream_card"
TEST_SIZE = 50 * 1024
CNT = 1

if not os.path.exists(dir):
    os.mkdir(os.path.join(os.path.dirname(__file__),"bangdream_card"))

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

        get_pic(new_role + new_card)
        time.sleep(0.1)











