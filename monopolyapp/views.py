from django.shortcuts import render

from .models import Room, Player
from .functions import create_room, set_new_room
from .line import reply_text

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
    if request.method == 'GET':
        room_id = set_new_room()
        return render(request, 'monopolyapp/make-room.html', {'room_id': room_id})
    elif request.method == 'POST':
        title = "部屋を作成"
        line_id = request.POST['line-id']
        room_id = request.POST['room-id']
        Player.objects.create(line_id=line_id, room_id=room_id, position='parent')
        Room.objects.filter(room_id=room_id).update(parent=line_id)
        return render(request, 'monopolyapp/room.html', {
            'title': title,
            'room_id': room_id,
            'parent': line_id,
        })
