
from django import forms
from rooms.models.room_inventory import RoomInventory


class AdminRoomInventoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AdminRoomInventoryForm, self).__init__(*args, **kwargs)

        self.fields['created_by'].widget.attrs['readonly'] = True
        self.fields['created_by'].widget.attrs['disabled'] = True
        self.fields['updated_by'].widget.attrs['readonly'] = True
        self.fields['updated_by'].widget.attrs['disabled'] = True

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
        fields = '__all__'
