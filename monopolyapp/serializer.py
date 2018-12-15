from rest_framework import serializers

from .models import Room, Player


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_id', 'state')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('line_id', 'line_name', 'room_id', 'position', 'money', 'deal')
