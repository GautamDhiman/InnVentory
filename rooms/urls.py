
from django.urls import path
from rooms.views.room_inventory_view import RoomInventoryView

urlpatterns = [
    path('', RoomInventoryView.as_view(), name='room_inventory'),
]