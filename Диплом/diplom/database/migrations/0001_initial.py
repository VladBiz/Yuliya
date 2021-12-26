# Generated by Django 3.2 on 2021-05-18 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.CharField(max_length=50, verbose_name='client_addres')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='company_name')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='company_priceForKM')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='farmer_money')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfPayment', models.DateTimeField(verbose_name='payment_date')),
                ('sum', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='payment_sum')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.client')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='user_name')),
                ('surname', models.CharField(max_length=30, verbose_name='user_surname')),
                ('phoneNumber', models.CharField(max_length=13, verbose_name='user_phoneNumber')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='product_name')),
                ('unitOfMeasure', models.CharField(max_length=30, verbose_name='product_uom')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfRequest', models.DateTimeField(verbose_name='sale_RequestDate')),
                ('dateOfPurchase', models.DateTimeField(verbose_name='sale_RequestDate')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='purchase_amount')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.client')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='typeOfDelivery_name')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='payment_type')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='trade_priceOfProduct')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='trade_amountOfProduct')),
                ('distance', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='trade_distanceOfDelivery')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.client')),
                ('deliveryCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.deliverycompanies')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.farmer')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.purchase')),
                ('typeOfDelivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.typeofdelivery')),
                ('typeOfPayment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.typeofpayment')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.CharField(max_length=50, verbose_name='storage_addres')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountOfProduct', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='stock_amountOfProduct')),
                ('dateOfHarvest', models.DateTimeField(verbose_name='product_harvestDate')),
                ('shelfLife', models.DateTimeField(verbose_name='product_shelfLife')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='product_price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.storage')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfRequest', models.DateTimeField(verbose_name='sale_RequestDate')),
                ('dateOfHarvest', models.DateTimeField(verbose_name='sale_productHarvestTime')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='sale_amountOfProduct')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='sale_priceOfGrowingHarvest')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.farmer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.sale'),
        ),
        migrations.AddField(
            model_name='payment',
            name='typeOfPayment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.typeofpayment'),
        ),
        migrations.AddField(
            model_name='farmer',
            name='personalData',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.personaldata'),
        ),
        migrations.AddField(
            model_name='client',
            name='personalData',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.personaldata'),
        ),
    ]
