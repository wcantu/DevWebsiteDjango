# Generated by Django 4.1 on 2023-11-13 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.CharField(blank=True, max_length=10, null=True)),
                ('street_number', models.CharField(max_length=10)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('parent_category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pntmodel.maincategory')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('SKU', models.CharField(default='123456', max_length=50, unique=True)),
                ('qty_in_stock', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.01, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('parent_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pntmodel.maincategory')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='pntmodel.shoppingcart')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='VariationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('variation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.variation')),
            ],
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.PositiveIntegerField()),
                ('comment', models.TextField()),
                ('ordered_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.orderline')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.siteuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=100)),
                ('expiry_date', models.DateField()),
                ('is_default', models.BooleanField(default=False)),
                ('payment_type_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pntmodel.paymenttype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.siteuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_default', models.BooleanField(default=False)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.address')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.siteuser')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.shoppingcart')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pntmodel.product')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.siteuser'),
        ),
        migrations.CreateModel(
            name='ShopOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pntmodel.orderstatus')),
                ('payment_method_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pntmodel.userpaymentmethod')),
                ('shipping_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pntmodel.address')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.siteuser')),
            ],
        ),
        migrations.CreateModel(
            name='PromotionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.productcategory')),
                ('promotion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.promotion')),
            ],
        ),
        migrations.CreateModel(
            name='ProductConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pntmodel.product')),
                ('variation_option_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.variationoption')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.productcategory'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pntmodel.shoporder'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pntmodel.product'),
        ),
    ]
