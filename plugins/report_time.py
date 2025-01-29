import datetime


def interface_report_time(args):
    nowTime = "现在是 "
    youbi = datetime.datetime.now().weekday() + 1
    if (youbi == 1):
        nowTime += "星期一 "
    elif (youbi == 2):
        nowTime += "星期二 "
    elif (youbi == 3):
        nowTime += "星期三 "
    elif (youbi == 4):
        nowTime += "星期四 "
    elif (youbi == 5):
        nowTime += "星期五 "
    elif (youbi == 6):
        nowTime += "星期六 "
    elif (youbi == 7):
        nowTime += "星期日 "

    nowTime += datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return nowTime

def interface_get_introduction():
    return "报时功能，返回当前时间"

def interface_get_name():
    return "报时"