# Generated by Django 4.2.6 on 2023-11-14 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20231107_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='/images/basicProfile.png', upload_to='images/'),
        ),
    ]