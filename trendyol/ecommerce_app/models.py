# ecommerce_app/models.py
from django.db import models

class Product(models.Model):
    product_no = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.product_no
