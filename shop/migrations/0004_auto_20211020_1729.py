# Generated by Django 3.2.4 on 2021-10-20 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211020_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_active_en',
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_active_fr',
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_active_ru',
        ),
    ]
