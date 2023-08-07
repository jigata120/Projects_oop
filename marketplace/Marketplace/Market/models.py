from django.db import models

my_choice = (
    ('seller', 'seller'),
    ('buyer', 'buyer'),
)


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100, choices=my_choice)

    def __str__(self):
        return f'{self.username} - {self.role}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return f'{self.name} - {self.quantity}'


class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return f'{self.buyer} - {self.products}'
