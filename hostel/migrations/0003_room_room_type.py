# Generated by Django 4.2.2 on 2024-02-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_remove_message_recipient_remove_message_sender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.CharField(default='single', max_length=8),
            preserve_default=False,
        ),
    ]
