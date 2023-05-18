from rooms.models.base_model import BaseModel
from django.db import models

import datetime

class RoomInventory(BaseModel):
    """"""
    hotel_id = models.IntegerField()
    hotel_name = models.CharField(max_length=100)
    room_id = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
    available = models.IntegerField(default=0)

    def __str__(self):
        return self.hotel_name

    class Meta:
        app_label = 'rooms'
        db_table = 'room_inventory'
        unique_together = ('room_id', 'date',)