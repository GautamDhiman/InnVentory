
from django import forms
from rooms.models.room_inventory import RoomInventory


class AdminRoomInventoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AdminRoomInventoryForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AdminRoomInventoryForm, self).save(commit=False)

        if self.request is not None:
            if not instance.created_by:
                instance.created_by = self.request.user.email
            instance.updated_by = self.request.user.email

        if commit:
            instance.save()

        return instance

    class Meta:
        model = RoomInventory
        fields = ['hotel_id', 'hotel_name', 'room_id', 'date', 'available']
