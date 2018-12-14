from rest_framework import routers

from .views import RoomViewSets, PlayerViewSets

router = routers.DefaultRouter()
router.register('rooms', RoomViewSets)
router.register('players', PlayerViewSets)
