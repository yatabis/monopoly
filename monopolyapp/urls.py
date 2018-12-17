from django.urls import path
from rest_framework import routers

from .views import line_callback
from .views import make_room, join_room, push_api, fetch_test, show_rooms
from .views import RoomViewSets, PlayerViewSets

urlpatterns = [
    path('callback/', line_callback, name='callback'),
    path('make-room/', make_room, name='make-room'),
    path('join-room/', join_room, name='join-room'),
    path('line/push', push_api, name='push-line'),
    path('debug/fetch-test/', fetch_test),
    path('debug/rooms/', show_rooms),
]

router = routers.DefaultRouter()
router.register('rooms', RoomViewSets)
router.register('players', PlayerViewSets)
