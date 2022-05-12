from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=200)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
