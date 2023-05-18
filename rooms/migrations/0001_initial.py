# Generated by Django 4.2.1 on 2023-05-18 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_by', models.CharField(max_length=100)),
                ('created_by_id', models.PositiveIntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('hotel_id', models.IntegerField()),
                ('hotel_name', models.CharField(max_length=100)),
                ('room_id', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('available', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'room_inventory',
                'unique_together': {('room_id', 'date')},
            },
        ),
    ]
