from json import JSONDecodeError
from .log import log_info

import requests
import json

class jiLLM:
    def __init__(self):
        self.background_prompt = "你是《常轨脱离Creative》的錦あすみ，对你的简介是:与智宏在公园相遇的学妹。喜欢吃肉包。在遇见智宏前很少来学校上学。背地里是拥有着20w粉丝的超人气Vtuber“雪景四季”（民汉译名：雪景式）的中之人。"
        "父（锦京太郎/锦响太郎，知名钢琴家）母（锦贵乃/KINO，知名作曲家）因为音乐相关工作长期在海外出差。"
        "在父母的影响下，自幼便对音乐产生了兴趣。"
        "在成为Vtuber前曾作为VOITO P主“miasuP”活动过，在此期间创作了播放量500w以上的名曲《Whitetip》。"
        "因为自身天使般的性格和可爱的外表而被智宏称为“小天使”。"
        "请你以这样的身份和用户聊天，注意你多轮对话的轮数为10轮，超过10轮后会清空对话记录。"
        self.messages = [
            {
                "role": "system",
                "content": self.background_prompt
            }
        ]
        self.url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
        self.header = {
            "Authorization": "Bearer PUUDZpSeahQkkntuBDRm:TNChTOpFisAnmOiChuvQ"
        }

    def send_message(self,input_message:str):
        self.messages.append({
            "role": "user",
            "content": input_message
        })
        data = {"max_tokens": 4096, "top_k": 4, "temperature": 0.5, "messages": self.messages, "model": "4.0Ultra", "stream": True}
        response = requests.post(self.url, headers=self.header, json=data, stream=True)
        returned_message = self.parse_response(response)
        self.messages.append({
            "role": "assistant",
            "content": returned_message
        })
        self.check_messages()
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

    def check_messages(self):
        if(len(self.messages) > 10):
            self.clear_message()

    def clear_message(self):
        self.messages = [
            {
                "role": "system",
                "content": self.background_prompt
            }
        ]




