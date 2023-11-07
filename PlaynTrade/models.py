from django.db import models
class SiteUser(models.Model):
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class UserAddress(models.Model):
    user_id = models.ForeignKey('SiteUser', on_delete=models.CASCADE)
    address_id = models.ForeignKey('Address', on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)
class Address(models.Model):
    unit_number = models.CharField(max_length=10, blank=True, null=True)
    street_number = models.CharField(max_length=10)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
class OrderStatus(models.Model):
    status = models.CharField(max_length=50)

class ShopOrder(models.Model):
    user_id = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    payment_method_id = models.ForeignKey('UserPaymentMethod', on_delete=models.SET_NULL, null=True)

class ShoppingCartItem(models.Model):
    cart_id = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE)
    product_item_id = models.ForeignKey('ProductItem', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

class ShoppingCart(models.Model):
    user_id = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
class PaymentType(models.Model):
    value = models.CharField(max_length=50)

class UserPaymentMethod(models.Model):
    user_id = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    provider = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    expiry_date = models.DateField()
    is_default = models.BooleanField(default=False)

class PromotionCategory(models.Model):
    category_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    promotion_id = models.ForeignKey('Promotion', on_delete=models.CASCADE)

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class ProductCategory(models.Model):
    parent_category_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    category_name = models.CharField(max_length=100)

class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)

class Variation(models.Model):
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

class VariationOption(models.Model):
    value = models.CharField(max_length=100)
    variation_id = models.ForeignKey(Variation, on_delete=models.CASCADE)

class ProductItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    SKU = models.CharField(max_length=50, unique=True)
    qty_in_stock = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to='product_item_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ProductConfiguration(models.Model):
    product_item_id = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    variation_option_id = models.ForeignKey(VariationOption, on_delete=models.CASCADE)