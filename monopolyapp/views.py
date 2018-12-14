from django.shortcuts import render

from .models import Player
from .functions import create_room, set_new_room
from .line import reply_text, get_line_id

# Create your views here.


def line_callback(request):
    events = request.json['events']
    for event in events:
        reply_token = event.get('replyToken')
        if event['type'] == 'message' and event['message']['type'] == 'text':
            if event['source']['type'] == 'user':
                user_id = event['source']['userId']
                text = event['message']['text']
                if "部屋" in text and "作る" in text:
                    create_room(user_id)
                else:
                    reply_text(reply_token, "メッセージの返答には対応していません。")
            else:
                reply_text(reply_token, "メッセージの返答には対応していません。")


def make_room(request):
    title = "部屋を作成"
    room_id = set_new_room()
    parent = get_line_id(request.body)
    Player.objects.create(room_id=room_id, position='parent')
    return render(request, 'monopolyapp/room.html', {
        'title': title,
        'room_id': room_id,
        'parent': parent
    })
