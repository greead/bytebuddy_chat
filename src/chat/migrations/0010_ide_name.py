# Generated by Django 3.2.5 on 2023-12-01 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_alter_ide_chat_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='ide',
            name='name',
            field=models.CharField(default='AAA', max_length=128),
            preserve_default=False,
        ),
    ]