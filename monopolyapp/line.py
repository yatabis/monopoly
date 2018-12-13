import json
import os
import requests

REPLY_EP = "https://api.line.me/v2/bot/message/reply"
CAT = os.environ.get('CHANNEL_ACCESS_TOKEN')
HEADER = {'Content-Type': 'application/json', 'Authorization': f"Bearer {CAT}"}


def reply_text(token, text):
    body = {'replyToken': token, 'messages': [{'type': 'text', 'text': text}]}
    requests.post(REPLY_EP, json.dumps(body, ensure_ascii=False).encode('utf-8'), headers=HEADER)


def get_line_id(req):
    return req['source']['userId']
