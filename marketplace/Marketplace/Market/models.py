from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    seller = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return f'{self.name} - {self.quantity} X ${self.price}'

    def is_valid_product(self):
        return 999 > self.quantity > 0 and self.price > 0


class Cart(models.Model):
    buyer = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products', blank=True)

    def __str__(self):
        return f'{self.buyer} - {self.products.count()}'
