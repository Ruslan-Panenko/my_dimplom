from django.db import models

from shop.models import item


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE)
    product = models.ForeignKey(item, related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def got_cost(self):
        return self.price * self.quantity