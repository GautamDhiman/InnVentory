from rooms.models import RoomInventory

class RoomInventoryManager(object):

    def __init__(self):
        super(RoomInventoryManager, self).__init__()
    def get_all_inventory(self):
        return RoomInventory.objects.all()

    def get_all_inventory_by_hotel(self, hotel_id):
        return RoomInventory.objects.filter(hotel=hotel_id)

    def create_inventory(self, hotel_id, hotel_name, room_id, date, available):
        success = failed = 0
        try:
            status = RoomInventory.objects.update_or_create(
                hotel_id=hotel_id,
                hotel_name=hotel_name,
                room_id=room_id,
                date=date,
                defaults={'available': available}
            )

            if status:
                success += 1
        except Exception as e:
            failed += 1

        return {'success': success, 'failed': failed}
