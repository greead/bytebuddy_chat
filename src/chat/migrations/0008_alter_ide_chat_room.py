# Generated by Django 3.2.5 on 2023-11-27 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_ide_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ide',
            name='chat_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatroom', unique=True),
        ),
    ]