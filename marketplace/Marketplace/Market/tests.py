from django.test import TestCase
from .models import *
from django.contrib.auth.models import User as AuthUser


class AppTest(TestCase):
    def setUp(self):
        auth_user = AuthUser.objects.create_user(
            username='seller',
            password='password',
            email='1@1.com', )
        self.product_valid = Product.objects.create(
            name='test_valid',
            description='Valid product',
            price=5,
            quantity=10,
            seller=auth_user,
            image='https://shorturl.at/ixW35'
        )

        self.product_negative_price = Product.objects.create(
            name='test_negative_price',
            description='Negative price product',
            price=-5,
            quantity=10,
            seller=auth_user,
            image='https://shorturl.at/ixW35'
        )

        self.product_no_quantity = Product.objects.create(
            name='test_no_quantity',
            description='No quantity product',
            price=5,
            quantity=0,
            seller=auth_user,
            image='https://shorturl.at/ixW35'
        )

        self.product_zero_quantity = Product.objects.create(
            name='test_zero_quantity',
            description='Zero quantity product',
            price=5,
            quantity=0,
            seller=auth_user,
            image='https://shorturl.at/ixW35'
        )
        self.product_Negative_quantity = Product.objects.create(
            name='test_Negative_quantity',
            description='Negative quantity product',
            price=5,
            quantity=-10,
            seller=auth_user,
            image='https://shorturl.at/ixW35'
        )

    def test_valid_product(self):
        self.assertTrue(self.product_valid.is_valid_product())

    def test_negative_price_invalid_product(self):
        self.assertFalse(self.product_negative_price.is_valid_product())

    def test_no_quantity_invalid_product(self):
        self.assertFalse(self.product_no_quantity.is_valid_product())

    def test_zero_quantity_invalid_product(self):
        self.assertFalse(self.product_zero_quantity.is_valid_product())

    def test_negative_quantity_invalid_product(self):
        self.assertFalse(self.product_Negative_quantity.is_valid_product())
