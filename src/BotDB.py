import os
from random import random, randint

import mysql.connector
from botpy.ext.cog_yaml import read
from botpy import logging

config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "secret", "config.yaml"))
test_config = read(config_path)

# _log = logging.get_logger()

class BotDB:
    def __init__(self):
        self.host = test_config["host"]
        self.user = test_config["user"]
        self.passwd = test_config["password"]
        self.database = test_config["dbName"]
        self.mydb = mysql.connector.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            database = self.database
        )
    def insert_group_if_not_exists(self,group_openid:str):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM groups WHERE group_openid=\"{group_openid}\";")
        res:list = mycursor.fetchall()
        if(len(res) != 0):
            print("已被注册了")
            # _log.info(f"群{group_openid}已被注册了")
        else:
            mycursor.execute(f"INSERT INTO groups (`group_openid`) VALUES (\"{group_openid}\");")
            self.mydb.commit()

    def delete_group_if_exists(self,group_openid:str):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM groups WHERE group_openid=\"{group_openid}\";")
        res: list = mycursor.fetchall()
        if (len(res) == 0):
            print("目标不存在")
            # _log.info(f"群{group_openid}目标不存在")
        else:
            mycursor.execute(f"DELETE FROM groups WHERE `group_openid`=\"{group_openid}\";")
            self.mydb.commit()
            mycursor.execute(f"SELECT * FROM groups;")
            newRes: list = mycursor.fetchall()
            for i in range(0,len(newRes)):
                mycursor.execute(f"UPDATE groups SET id = {i + 1} WHERE group_openid = \"{newRes[i][1]}\"")
            mycursor.execute(f"ALTER TABLE groups AUTO_INCREMENT = {len(newRes)}")
            self.mydb.commit()

    def get_all_groups(self)->list:
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT group_openid FROM groups;")
        return mycursor.fetchall()

    def insert_famousWords_if_not_exists(self,famousWords):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM famousWords WHERE sentence = \"{famousWords}\";")
        res: list = mycursor.fetchall()
        if (len(res) != 0):
            print("名言已被登记了")
            # _log.info(f"群{group_openid}已被注册了")
        else:
            mycursor.execute(f"INSERT INTO famousWords (`sentence`) VALUES (\"{famousWords}\");")
            self.mydb.commit()

    def delete_famousWords_if_exists(self, famousWords: str):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM famousWords WHERE sentence=\"{famousWords}\";")
        res: list = mycursor.fetchall()
        if (len(res) == 0):
            print("目标不存在")
            # _log.info(f"群{group_openid}目标不存在")
        else:
            mycursor.execute(f"DELETE FROM famousWords WHERE `sentence`=\"{famousWords}\";")
            self.mydb.commit()
            mycursor.execute(f"SELECT * FROM famousWords;")
            newRes: list = mycursor.fetchall()
            for i in range(0, len(newRes)):
                mycursor.execute(f"UPDATE famousWords SET id = {i + 1} WHERE sentence = \"{newRes[i][1]}\"")
            mycursor.execute(f"ALTER TABLE famousWords AUTO_INCREMENT = {len(newRes)}")
            self.mydb.commit()

    def get_all_famousWords(self)->list:
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT sentence FROM famousWords;")
        return mycursor.fetchall()

    def get_one_famousWords(self)->str:
        mycursor = self.mydb.cursor()
        choose = randint(1,1951)
        mycursor.execute(f"SELECT sentence FROM famousWords WHERE `id` = {choose}")
        return mycursor.fetchone()[0]



if __name__ == '__main__':
    db = BotDB()
    print(db.get_one_famousWords())
