# Generated by Django 3.2.5 on 2023-11-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_ide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ide',
            name='code',
            field=models.TextField(default=''),
        ),
    ]