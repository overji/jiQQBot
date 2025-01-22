from json import JSONDecodeError
from .log import log_info

import requests
import json

class jiLLM:
    def __init__(self):
        self.url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
        self.header = {
            "Authorization": "Bearer PUUDZpSeahQkkntuBDRm:TNChTOpFisAnmOiChuvQ"
        }

    def send_message(self,input_message:str):
        data = {"max_tokens": 4096, "top_k": 4, "temperature": 0.5, "messages": [
            {
                "role": "system",
                "content": "你是可爱学妹小锦，可以和用户聊天"
            },
            {
                "role": "user",
                "content": input_message
            }
        ], "model": "4.0Ultra", "stream": True}
        response = requests.post(self.url, headers=self.header, json=data, stream=True)
        returned_message = self.parse_response(response)
        log_info(f"返回的消息:{returned_message}，发送的消息:{input_message}")
        return returned_message

    def parse_response(self,response:requests.Response)->str:
        ans = ""
        response.encoding = "utf-8"
        for line in response.iter_lines(decode_unicode="utf-8"):
            try:
                lines = json.loads(line[6:].strip())
            except JSONDecodeError:
                continue
            if 'choices' in lines:
                choice = lines['choices'][0]
                if 'delta' in choice:
                    delta = choice['delta']
                    if 'content' in delta:
                        ans += delta['content']
        return ans




