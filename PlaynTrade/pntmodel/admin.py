from django.contrib import admin
from .models import (
    SiteUser,
    UserAddress,
    Address,
    OrderStatus,
    ShopOrder,
    ShoppingCartItem,
    ShoppingCart,
    PaymentType,
    UserPaymentMethod,
    PromotionCategory,
    Promotion,
    MainCategory,
    ProductCategory,
    Product,
    Variation,
    VariationOption,
    ProductItem,
    ProductConfiguration,
)

# Register your models in the admin interface
admin.site.register(SiteUser)
admin.site.register(UserAddress)
admin.site.register(Address)
admin.site.register(OrderStatus)
admin.site.register(ShopOrder)
admin.site.register(ShoppingCartItem)
admin.site.register(ShoppingCart)
admin.site.register(PaymentType)
admin.site.register(UserPaymentMethod)
admin.site.register(PromotionCategory)
admin.site.register(Promotion)
admin.site.register(MainCategory)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(VariationOption)
admin.site.register(ProductItem)
admin.site.register(ProductConfiguration)