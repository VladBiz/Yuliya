from database.serializers import UserSerializer
import client
from django.db.models import fields
from database.models import *
from rest_framework import serializers
from django.contrib.auth.models import User




class FarmerPersonalDataSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = PersonalData
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FarmerSerializer(serializers.ModelSerializer):
    personalData = FarmerPersonalDataSerializer()
    class Meta:
        model = Farmer
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['personalData']


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
    client = ClientSerializer()
    class Meta:
        model = PersonalData
        exclude = ['user']


class ClientProfileSerializer(serializers.ModelSerializer):
    personaldata = PersonalDataSerializer()
    
    class Meta:
        model = User
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer()
    product = ProductSerializer()
    class Meta:
        model = Sale
        fields = '__all__'
    



class ClientBuySerializer(serializers.ModelSerializer):
    sale = SaleSerializer()
    class Meta:
        model = Purchase
        fields = '__all__'



class ClientTradeSerializer(serializers.ModelSerializer):
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


class ClientDeliverySerializer(serializers.ModelSerializer): # Вот тут нужно придумать как сделать нормальный сериалайзер без onetoone field
    trade = ClientTradeSerializer()
    class Meta:
        model = TypeOfDelivery
        fields = '__all__'



class ClientBinSerializer(serializers.ModelSerializer):

    client = ClientSerializer()
    sale = SaleSerializer()
    class Meta:
        model = Purchase
        fields = '__all__'


class ClientPaySerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    sale = SaleSerializer()
    class Meta:
        model = Purchase
        fields = '__all__'