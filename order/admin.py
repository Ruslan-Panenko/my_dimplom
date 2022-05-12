from django.contrib import admin

from order.models import OrderItem, Order


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    save_on_top = True

    list_display = ['id', 'first_name', 'email',
                    'address', 'city', 'paid']
    list_filter = ['paid']
    inlines = [OrderItemInLine]