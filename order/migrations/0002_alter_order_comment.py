# Generated by Django 3.2.4 on 2022-05-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
