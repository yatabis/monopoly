from base64 import b64encode
from uuid import uuid4

import qrcode

from monopoly.settings import STATICFILES_DIRS
from .models import Room


def create_room(parent):
    pass


def set_new_room():
    room_id = str(b64encode(str(uuid4()).encode('utf-8')))[2:-1].lower()
    room_qr = qrcode.make(room_id)
    room_qr.save(f'{STATICFILES_DIRS[0]}/room/{room_id}.png')
    Room.objects.create(room_id=room_id)
    return room_id
