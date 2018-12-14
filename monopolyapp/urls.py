from django.urls import path

from .views import line_callback
from .views import make_room

urlpatterns = [
    path('callback/', line_callback, name='callback'),
    path('make-room/', make_room, name='make-room'),
    path('make-room/<str:room_id>', make_room, name='make-room')
]
