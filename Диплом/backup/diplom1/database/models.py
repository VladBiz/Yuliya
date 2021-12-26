from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# class User(models.Model):
#     login = models.CharField('user_login', max_length= 40, unique= True)
#     password = models.CharField('user_password', max_length= 20)

class PersonalData(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    # user = models.ForeignKey(User, on_delete= models.CASCADE)
    # name = models.CharField('user_name', max_length = 20)
    # surname = models.CharField('user_surname', max_length = 30)
    isFarmer = models.BooleanField(default= False)
    phoneNumber = models.CharField('user_phoneNumber', max_length = 13)

class Client(models.Model):
    #user = models.ForeignKey(User, on_delete= models.CASCADE)
    personalData = models.ForeignKey(PersonalData, on_delete = models.CASCADE)
    addres = models.CharField('client_addres', max_length = 50)
    

class Farmer(models.Model):
    #user = models.ForeignKey(User, on_delete= models.CASCADE)
    personalData = models.ForeignKey(PersonalData, on_delete = models.CASCADE)
    money = models.DecimalField('farmer_money', max_digits= 10, decimal_places= 3)

class TypeOfPayment(models.Model):
    name = models.CharField('payment_type', max_length= 20)

class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete= models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete= models.CASCADE)
    typeOfPayment = models.ForeignKey(TypeOfPayment, on_delete=models.CASCADE)
    dateOfPayment = models.DateTimeField('payment_date', auto_now=False, auto_now_add=False)
    sum = models.DecimalField('payment_sum', max_digits= 10, decimal_places= 3)

class DeliveryCompanies(models.Model):
    name = models.CharField('company_name', max_length= 40)
    price = models.DecimalField('company_priceForKM', max_digits= 10, decimal_places= 3)

class TypeOfDelivery(models.Model):
    name = models.CharField('typeOfDelivery_name', max_length= 30)

class Product(models.Model):
    name = models.CharField('product_name', max_length= 30)
    unitOfMeasure =  models.CharField('product_uom', max_length= 30)

class Storage(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete= models.CASCADE)
    addres = models.CharField('storage_addres', max_length = 50)

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete= models.CASCADE)
    amountOfProduct = models.DecimalField('stock_amountOfProduct', max_digits= 10, decimal_places= 3)
    dateOfHarvest = models.DateTimeField('product_harvestDate', auto_now=False, auto_now_add=False)
    shelfLife = models.DateTimeField('product_shelfLife', auto_now=False, auto_now_add=False)
    price = models.DecimalField('product_price', max_digits= 10, decimal_places= 3)

class Sale(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    dateOfRequest = models.DateTimeField('sale_RequestDate', auto_now=False, auto_now_add=False)
    dateOfHarvest = models.DateTimeField('sale_productHarvestTime', auto_now=False, auto_now_add=False)
    amount = models.DecimalField('sale_amountOfProduct', max_digits= 10, decimal_places= 3)
    price = models.DecimalField('sale_priceOfGrowingHarvest', max_digits= 10, decimal_places= 3)


class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete= models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete= models.CASCADE)
    dateOfRequest = models.DateTimeField('sale_RequestDate', auto_now=False, auto_now_add=False)
    dateOfPurchase = models.DateTimeField('sale_RequestDate', auto_now=False, auto_now_add=False)
    amount = models.DecimalField('purchase_amount', max_digits= 10, decimal_places= 3)


class Trade(models.Model):
    client = models.ForeignKey(Client, on_delete= models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete= models.CASCADE)
    typeOfPayment = models.ForeignKey(TypeOfPayment, on_delete= models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete= models.CASCADE)
    typeOfDelivery = models.ForeignKey(TypeOfDelivery, on_delete= models.CASCADE)
    deliveryCompany = models.ForeignKey(DeliveryCompanies, on_delete= models.CASCADE)
    price = models.DecimalField('trade_priceOfProduct', max_digits= 10, decimal_places= 3)
    amount = models.DecimalField('trade_amountOfProduct', max_digits= 10, decimal_places= 3)
    distance = models.DecimalField('trade_distanceOfDelivery', max_digits= 10, decimal_places= 3)
    
