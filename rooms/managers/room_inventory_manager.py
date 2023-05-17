from rooms.models import RoomInventory

class RoomInventoryManager(object):

    def __init__(self):
        super(RoomInventoryManager, self).__init__()
    def get_all_inventory(self):
        return RoomInventory.objects.all()

    def get_all_inventory_by_hotel(self, hotel_id):
        return RoomInventory.objects.filter(hotel=hotel_id)