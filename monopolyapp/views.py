from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import Room, Player
from .serializer import RoomSerializer, PlayerSerializer
from .functions import create_room, set_new_room, get_rooms
from .line import reply_text, push_text, HEADER

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
        title = "部屋を作成"
        room_id = set_new_room()
        return render(request, 'monopolyapp/make-room.html', {'title': title, 'room_id': room_id})
    elif request.method == 'POST':
        title = "部屋を作成"
        room_id = request.POST['room-id']
        line_id = request.POST['line-id']
        line_name = request.POST['line-name']
        created_room = Room.objects.filter(room_id=room_id)
        created_room.update(parent=line_id)
        if Player.objects.filter(line_id=line_id).exists():
            if Player.objects.filter(line_id=line_id).get().room_id == "":
                Player.objects.filter(line_id=line_id).update(
                    room_id=created_room.get(), position='parent', money=2000000, deal='free')
            else:
                push_text(line_id, "予期せぬエラーが発生しました。")
        else:
            Player.objects.create(line_id=line_id, line_name=line_name, room_id=created_room.get(), position='parent')
            push_text(line_id, f"ルーム{room_id[:6]}を作成しました。")
        return render(request, 'monopolyapp/room.html', {
            'title': title,
            'room_id': room_id,
            'parent': line_name,
        })


def join_room(request):
    if request.method == 'GET':
        title = "部屋に入る"
        room_id = request.GET['room']
        return render(request, 'monopolyapp/join-room.html', {'title': title, 'room_id': room_id, 'header': HEADER})
    elif request.method == 'POST':
        title = "部屋に入る"
        room_id = request.POST['room-id']
        line_id = request.POST['line-id']
        line_name = request.POST['line-name']
        Player.objects.create(line_id=line_id, line_name=line_name, room_id=room_id)
        push_text(line_id, f"ルーム{room_id[:6]}に入室しました。")
        return render(request, 'monopolyapp/joined.html', {'title': title, 'room_id': room_id})


# API
class RoomViewSets(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_fields = ('state',)


class PlayerViewSets(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_fields = ('room_id', 'line_id', 'position')


# test
def fetch_test(request):
    return render(request, 'monopolyapp/fetch-test.html')


def show_rooms(request):
    rooms = get_rooms()
    return render(request, 'monopolyapp/show-rooms.html', {'rooms': rooms})
