# Generated by Django 3.2.5 on 2023-12-01 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_ide_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ide',
            name='chat_room',
        ),
    ]