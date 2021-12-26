from django.db.models import fields
from database.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        exclude = ['personalData']


class FarmerPersonalDataStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'


class FarmerStorageSerializer(serializers.ModelSerializer):
    personalData = FarmerPersonalDataStorageSerializer()
    class Meta:
        model = Farmer
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer): # Узнать почему я не могу взять тут PersonalDataSerializer или FarmerProfileSerializer
    farmer = FarmerStorageSerializer()
    class Meta:
        model = Storage
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    storage = StorageSerializer()
    class Meta:
        model = Stock
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    stock = StockSerializer()
    class Meta:
        model = Product
        fields = '__all__'
    

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class TypeOfPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfPayment
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class TypeOfDeliverySerializer(serializers.ModelSerializer): 
    class Meta:
        model = TypeOfDelivery
        fields = '__all__'


class DeliveryCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCompanies
        fields = '__all__'
        


class PersonalDataSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer()
    class Meta:
        model = PersonalData
        exclude = ['user']





class FarmerProfileSerializer(serializers.ModelSerializer):
    personaldata = PersonalDataSerializer()
    
    class Meta:
        model = User
        fields = '__all__'

class FermerPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'






class FarmerHistorySerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    client = ClientSerializer()
    farmer = FarmerSerializer()
    purchase = PurchaseSerializer()
    typeOfPayment = TypeOfPaymentSerializer(many = False)
    payment = PaymentSerializer()
    typeOfDelivery = TypeOfDeliverySerializer()
    deliveryCompany = DeliveryCompanySerializer()
    class Meta:
        model = Trade
        fields = '__all__'


class ProductAddSerializer(serializers.ModelSerializer):
    stock = StockSerializer()
    class Meta:
        model = Product
        fields = '__all__'


class ProductEditSerializer(serializers.ModelSerializer):
    stock = StockSerializer()
    class Meta:
        model = Product
        fields = '__all__'