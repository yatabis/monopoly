from django.urls import path

from .views import line_callback
from .views import make_room, join_room

urlpatterns = [
    path('callback/', line_callback, name='callback'),
    path('make-room/', make_room, name='make-room'),
    path('join-room/', join_room, name='join-room'),
]
