from django.contrib.auth.models import AbstractUser
from django.db import models

class SiteUser(AbstractUser):
    #email_address = models.EmailField(unique=True)
    shopping_cart = models.OneToOneField('ShoppingCart', null=True, blank=True, on_delete=models.CASCADE,default=None)
    #username = models.CharField(max_length=30, unique=True, default='')
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='siteuser_set',  # Use a custom related_name to avoid clashes
        related_query_name='siteuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='siteuser_set',  # Use a custom related_name to avoid clashes
        related_query_name='siteuser',
    )
    def __str__(self):
        return self.email_address

class GuestShoppingCart(models.Model):
    user_session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Guest Shopping Cart ({self.user_session_key})"

class UserAddress(models.Model):
    user_id = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    address_id = models.ForeignKey('Address', on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id.email_address}'s Address"


class Address(models.Model):
    unit_number = models.CharField(max_length=10, null=True, blank=True,default='')
    street_number = models.CharField(max_length=10, null=True, blank=True,default='')
    address_line1 = models.CharField(max_length=255,default='')
    address_line2 = models.CharField(max_length=255, null=True, blank=True,default='')
    city = models.CharField(max_length=100,default='')
    region = models.CharField(max_length=100, null=True, blank=True,default='')
    postal_code = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"{self.address_line1}, {self.city}"


class ShopOrder(models.Model):
    user_id = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    order_status_id = models.ForeignKey('OrderStatus', on_delete=models.PROTECT,default=None)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    shipping_address_id = models.ForeignKey(Address, on_delete=models.CASCADE,default=None)
    payment_method_id = models.ForeignKey('UserPaymentMethod', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"Order #{self.id} by {self.user_id.email_address}"


class MainCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    def __str__(self):
        return f'{self.name} ID : {self.id}'


class OrderStatus(models.Model):
    status = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.status


class OrderLine(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    order_id = models.ForeignKey(ShopOrder, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Order Line for {self.product_id.name} in Order #{self.order_id.id}"


class ShoppingCart(models.Model):
    user_id = models.OneToOneField(SiteUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Shopping Cart for {self.user_id.email_address}"

class ShoppingCartItem(models.Model):
    cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Shopping Cart Item for {self.cart_id.user_id.email_address}"

class PaymentType(models.Model):
    value = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.value

class UserPaymentMethod(models.Model):
    user_id = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255, default='')
    account_number = models.CharField(max_length=255, default='')
    expiry_date = models.DateField(default='1970-01-01')
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id.email_address}'s {self.provider} Payment Method"

class PromotionCategory(models.Model):
    category_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    promotion_id = models.ForeignKey('Promotion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category_id.category_name} Promotion Category"

class Promotion(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    start_date = models.DateField(default='1970-01-01')
    end_date = models.DateField(default='1970-01-01')

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    parent_category = models.ForeignKey(MainCategory, null=True, blank=True, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.parent_category}->{self.category_name} ID: {self.id}'

class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    product_image = models.ImageField(upload_to='product_images/', null=True, blank=True, default='')
    SKU = models.CharField(max_length=50, unique=True, default='')
    qty_in_stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.name} ID: {self.id}'

class Variation(models.Model):
    name = models.CharField(max_length=100, default='')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f"{self.name} - {self.product_id.name}"

class VariationOption(models.Model):
    value = models.CharField(max_length=100, default='')
    variation_id = models.ForeignKey(Variation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.value} - {self.variation_id.name}"

class ProductConfiguration(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    variation_option_id = models.ForeignKey(VariationOption, on_delete=models.CASCADE)
    def __str__(self):
        return f"Configuration for Product Item {self.product_id.id}"




