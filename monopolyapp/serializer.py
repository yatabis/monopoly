from rest_framework import serializers

from .models import Room, Player


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        field = ('room_id', 'state')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        field = ('line_id', 'line_name', 'room_id', 'money', 'deal')
