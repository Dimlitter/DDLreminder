<div align="center">


# 浙江大学DDL提醒小助手
![avatar](./pic/logo.png)
![GitHub Repo stars](https://github.com/Dimlitter/DDLremider)
![GitHub forks](https://github.com/Dimlitter/DDLremider)

</div>

<div align="center">

<font size="5">朋友！你是否因为某些原因错过了该死的DDL？你是否曾经低声下气的请求助教小哥哥小姐姐们给你一个补交作业的机会？</font>

<font size="5">好消息，好消息！浙江大学DDL提醒小助手已经上线！有了它，你就可以更加轻松的提醒自己的DDL了！你再也不用提心吊胆地担心错过最后期限啦！</font>

</div>

## 简介

- 模拟学在浙大平台登录

- 通过发送简单的GET请求获取DDL信息

- 多样化的推送提醒渠道

- 支持github action 部署，无需服务器

## 使用方法

1、fork本项目

2、配置github secret

3、开启github action推送

<font size="4">需要的secrets：</font>

## 参数配置

> 必须配置的内容

```bash
ZJU_USERNAME : 'username',
ZJU_PASSWORD : 'password',
```

> 可选配置内容

<font size="3">钉钉机器人的推送</font>

```bash
'DD_BOT_SECRET': '',      # 钉钉机器人的 DD_BOT_SECRET，加签密钥
'DD_BOT_TOKEN' : '',      # 钉钉机器人的 DD_BOT_TOKEN, access_token后一段
```

<font size="3">飞书推送</font>

```bash
'FSKEY': '',              # 飞书机器人的 FSKEY
 ```

<font size="3">push+ 微信推送</font>

```bash
'PUSH_PLUS_TOKEN': '',    # push+ 微信推送的用户令牌
'PUSH_PLUS_USER': '',     # push+ 微信推送的群组编码
```

<font size="3">server酱微信推送</font>

```bash
'PUSH_KEY': '',           # server 酱的 PUSH_KEY，兼容旧版与 Turbo 版
```

<font size="3">telegrame机器人推送</font>

```bash
'TG_BOT_TOKEN': '',       # tg 机器人的 TG_BOT_TOKEN
'TG_USER_ID': '',         # tg 机器人的 TG_USER_ID
'TG_API_HOST': '',        # tg 代理 api
'TG_PROXY_AUTH': '',      # tg 代理认证参数
'TG_PROXY_HOST': '',      # tg 机器人的 TG_PROXY_HOST
'TG_PROXY_PORT': '',      # tg 机器人的 TG_PROXY_PORT
```

## 自定义运行时间

> <font size="3">修改`.github/workflows/run.yml`文件中的自定义运行时间</font>

```yml
watch:
    types: [ started ]
  schedule:
    - cron: 45 22 * * *
```

- 注意，cron表达式时间为UTC时间，与北京时间相差八小时

## 参考

- 推送模块参考 [qinglong](https://github.com/whyour/qinglong)
- 模拟登录类参考 [When_Coding_in_ZJU](https://github.com/Freedomisgood/When_Coding_in_ZJU)


## 声明

本项目为Python学习交流的开源非营利项目，仅作为程序员之间相互学习交流之用。

严禁用于商业用途，禁止使用本项目进行任何盈利活动。

使用者请遵从相关政策。对一切非法使用所产生的后果，我们概不负责。

本项目对您如有困扰请联系我们删除。

## 交流群组

<font size="3">

欢迎加入[群聊](t.me/zjuers)共同交流


</font>