from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    parent_category_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    category_name = models.CharField(max_length=100)
class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)


