import itchat
from itchat.content import *
import requests


bot_url = 'http://localhost:5000/say'

def get_reply(text):
    payload = {"text": text}
    response = requests.get(bot_url, params=payload)
    return response.text


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    return get_reply(msg.text)


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        reply = get_reply(msg.text)
        msg.user.send(u'@%s\u2005  %s' % (msg.actualNickName, reply))


itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()