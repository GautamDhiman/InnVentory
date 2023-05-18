
from django.contrib import admin
from rooms.models.room_inventory import RoomInventory
from rooms.forms.admin_room_inventory_form import AdminRoomInventoryForm


@admin.register(RoomInventory)
class AdminRoomInventory(admin.ModelAdmin):

    form = AdminRoomInventoryForm
    list_per_page = 20
    ordering = ['hotel_name']
    list_display = ['hotel_name', 'room_id', 'date', 'available']
    list_filter = ['hotel_name', 'room_id', 'date', 'available']

    def get_form(self, request, obj=None, **kwargs):
        form = super(AdminRoomInventory, self).get_form(request, obj, **kwargs)
        form.request = request
        return form

    def has_delete_permission(self, request, obj=None):
        """Removing delete permission."""
        return False
