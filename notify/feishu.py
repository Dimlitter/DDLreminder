import json
import os
import requests


def feishu_bot(title: str, content: str) -> None:
    """
    使用 飞书机器人 推送消息。
    """
    if not os.getenv("FSKEY"):
        pass
        return
    print("飞书 服务启动")

    url = f'https://open.feishu.cn/open-apis/bot/v2/hook/{os.getenv("FSKEY")}'
    data = {"msg_type": "text", "content": {"text": f"{title}\n\n{content}"}}
    response = requests.post(url, data=json.dumps(data)).json()

    if response.get("StatusCode") == 0:
        print("飞书 推送成功！")
    else:
        print("飞书 推送失败！错误信息如下：\n", response)