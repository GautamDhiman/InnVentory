# Generated by Django 4.2.1 on 2023-05-18 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roominventory',
            name='created_by_id',
        ),
    ]
