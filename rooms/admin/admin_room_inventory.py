
from django.contrib import admin
from functools import update_wrapper
from django.urls import re_path
from rooms.models.room_inventory import RoomInventory
from rooms.forms.admin_room_inventory_form import AdminRoomInventoryForm


@admin.register(RoomInventory)
class AdminRoomInventory(admin.ModelAdmin):

    form = AdminRoomInventoryForm
    change_list_template = 'room_inventory.html'
    list_per_page = 20
    ordering = ['hotel_name']
    search_fields = ['hotel_name']
    list_display = ['hotel_name', 'room_id', 'date', 'available']
    list_filter = ['hotel_name', 'room_id', 'date', 'available']

    def get_form(self, request, obj=None, **kwargs):
        form = super(AdminRoomInventory, self).get_form(request, obj, **kwargs)
        form.request = request
        return form

    def get_urls(self):
        """Overriding for add some urls."""
        def wrap(view):
            """Add more urls."""
            def wrapper(*args, **kwargs):
                """Default wrapper."""
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        urls = super(AdminRoomInventory, self).get_urls()

        from rooms.views.export_inventory_view import ExportInventoryView
        from rooms.views.import_inventory_view import ImportInventoryView

        my_urls = [
            re_path(r'^export/', ExportInventoryView.as_view(), name='export_inventory'),
            re_path(r'^import/', ImportInventoryView.as_view(), name='import_inventory')
        ]

        return my_urls + urls

    def has_delete_permission(self, request, obj=None):
        """Removing delete permission."""
        return False
