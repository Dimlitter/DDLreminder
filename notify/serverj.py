import os
import requests

def serverJ(title: str, content: str) -> None:
    """
    通过 serverJ 推送消息。
    """
    if not os.getenv("PUSH_KEY"):
        pass
        return
    print("serverJ 服务启动")

    data = {"text": title, "desp": content.replace("\n", "\n\n")}
    if os.getenv("PUSH_KEY").index("SCT") != -1:
        url = f'https://sctapi.ftqq.com/{os.getenv("PUSH_KEY")}.send'
    else:
        url = f'https://sc.ftqq.com/${os.getenv("PUSH_KEY")}.send'
    response = requests.post(url, data=data).json()

    if response.get("errno") == 0 or response.get("code") == 0:
        print("serverJ 推送成功！")
    else:
        print(f'serverJ 推送失败！错误码：{response["message"]}')
