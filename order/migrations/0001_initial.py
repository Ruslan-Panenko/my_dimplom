# Generated by Django 3.2.4 on 2022-05-09 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0008_remove_item_bottom_photo_xxl2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('city', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('comment', models.CharField(max_length=1000)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='shop.item')),
            ],
        ),
    ]