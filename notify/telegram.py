import os
import requests

def telegram_bot(title: str, content: str) -> None:
    """
    使用 telegram 机器人 推送消息。
    """
    if not os.getenv("TG_BOT_TOKEN") or not os.getenv("TG_USER_ID"):
        pass
        return
    print("tg 服务启动")

    if os.getenv("TG_API_HOST"):
        url = f"https://{os.getenv('TG_API_HOST')}/bot{os.getenv('TG_BOT_TOKEN')}/sendMessage"
    else:
        url = (
            f"https://api.telegram.org/bot{os.getenv('TG_BOT_TOKEN')}/sendMessage"
        )
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "chat_id": str(os.getenv("TG_USER_ID")),
        "text": f"{title}\n\n{content}",
        "disable_web_page_preview": "true",
    }
    proxies = None
    if os.getenv("TG_PROXY_HOST") and os.getenv("TG_PROXY_PORT"):
        if os.getenv("TG_PROXY_AUTH") is not None and "@" not in os.getenv(
            "TG_PROXY_HOST"
        ):
            os.getenv["TG_PROXY_HOST"] = (
                os.getenv("TG_PROXY_AUTH")
                + "@"
                + os.getenv("TG_PROXY_HOST")
            )
        proxyStr = "http://{}:{}".format(
            os.getenv("TG_PROXY_HOST"), os.getenv("TG_PROXY_PORT")
        )
        proxies = {"http": proxyStr, "https": proxyStr}
    response = requests.post(
        url=url, headers=headers, params=payload, proxies=proxies
    ).json()

    if response["ok"]:
        print("tg 推送成功！")
    else:
        print("tg 推送失败！")