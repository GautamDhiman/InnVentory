
from django.contrib import admin
from rooms.models.room_inventory import RoomInventory


@admin.register(RoomInventory)
class AdminRoomInventory(admin.ModelAdmin):

    list_per_page = 20
    ordering = ['hotel_id']
    list_display = ['hotel_id', 'room_id', 'date', 'available']
    list_filter = ['hotel_id', 'room_id', 'date', 'available']

    def has_delete_permission(self, request, obj=None):
        """Removing delete permission."""
        return False
