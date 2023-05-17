from django.views.generic import View
from django.shortcuts import render

from rooms.managers.room_inventory_manager import RoomInventoryManager

class RoomInventoryView(View):

    def __init__(self):
        self.room_inv_mng = RoomInventoryManager()

    def get(self, request):
        room_inventory = self.room_inv_mng.get_all_inventory()
        return render(request, "list_room_inventory.html", {"room_inventory": room_inventory})