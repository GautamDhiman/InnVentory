from django.views.generic import View
import csv
from django.http import HttpResponse


from rooms.managers.room_inventory_manager import RoomInventoryManager

class ExportInventoryView(View):

    def __init__(self):
        self.room_inv_mng = RoomInventoryManager()

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="room_inventory.csv"'

        writer = csv.writer(response)

        writer.writerow(['Hotel ID', 'Hotel Name', 'Room ID', 'Date', 'Available'])

        room_inventory_objects = self.room_inv_mng.get_all_inventory()

        for room_inventory in room_inventory_objects:
            writer.writerow([
                room_inventory.hotel_id,
                room_inventory.hotel_name,
                room_inventory.room_id,
                room_inventory.date,
                room_inventory.available
            ])

        return response

