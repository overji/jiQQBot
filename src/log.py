import datetime
import os

def log_info(text:str,type=0):
    # type为0表示信息，1表示错误

    # Get the current date
    current_date = datetime.datetime.now()

    # Format the date as YYYY-MM-DD
    formatted_date = current_date.strftime("%Y-%m-%d")
    formatted_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    final_info = ""
    if type == 0:
        final_info = f"{formatted_time} [INFO] {text}"
    else:
        final_info = f"{formatted_time} [ERROR] {text}"
    logPath = f"../logs/{formatted_date}-jilog.log"
    os.makedirs(os.path.dirname(logPath), exist_ok=True)
    with open(logPath, 'a', encoding="utf-8") as f:
        f.write(final_info)
    print("Ji log:" + final_info)



