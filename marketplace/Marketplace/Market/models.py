from django.db import models
from django.contrib.auth.models import User as AuthUser
my_choice = (
    ('seller', 'seller'),
    ('buyer', 'buyer'),
)


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    seller = models.ForeignKey(AuthUser , on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return f'{self.name} - {self.quantity}'


class Cart(models.Model):
    buyer = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products', blank=True)

    def __str__(self):
        return f'{self.buyer} - {self.products}'
