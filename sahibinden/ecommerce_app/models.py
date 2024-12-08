from django.db import models

class Product(models.Model):
    product_no = models.CharField(max_length=10)
    name = models.CharField(max_length=255, default='Ürün Adı')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=50, default='İstanbul')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.product_no:
            last_product = Product.objects.all().order_by('product_no').last()
            if last_product:
                last_product_no = int(last_product.product_no[1:]) + 1
                self.product_no = f"P{last_product_no:03d}"
            else:
                self.product_no = "P001"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
# to generate product number automatically 
