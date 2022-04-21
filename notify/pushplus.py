import json
import os
import requests

def pushplus_bot(title: str, content: str) -> None:
    """
    通过 push+ 推送消息。
    """
    if not os.getenv("PUSH_PLUS_TOKEN"):
        pass
        return
    print("PUSHPLUS 服务启动")

    url = "http://www.pushplus.plus/send"
    data = {
        "token": os.getenv("PUSH_PLUS_TOKEN"),
        "title": title,
        "content": content,
        "topic": os.getenv("PUSH_PLUS_USER"),
    }
    body = json.dumps(data).encode(encoding="utf-8")
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, data=body, headers=headers).json()

    if response["code"] == 200:
        print("PUSHPLUS 推送成功！")

    else:

        url_old = "http://pushplus.hxtrip.com/send"
        headers["Accept"] = "application/json"
        response = requests.post(url=url_old, data=body, headers=headers).json()

        if response["code"] == 200:
            print("PUSHPLUS(hxtrip) 推送成功！")

        else:
            print("PUSHPLUS 推送失败！")