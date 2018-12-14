from django.urls import path
from rest_framework import routers

from .views import line_callback
from .views import make_room, join_room
from .views import RoomViewSets, PlayerViewSets

urlpatterns = [
    path('callback/', line_callback, name='callback'),
    path('make-room/', make_room, name='make-room'),
    path('join-room/', join_room, name='join-room'),
]

router = routers.DefaultRouter()
router.register('rooms', RoomViewSets)
router.register('players', PlayerViewSets)
