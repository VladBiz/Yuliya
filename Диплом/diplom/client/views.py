from database.models import PersonalData
from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import *

class ProductListAPI(generics.GenericAPIView):

    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

    def get(self, request):
        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 


class ClientProfileAPI(generics.GenericAPIView): # Тут нужно сделать что бы возвращало только одного юзера

    serializer_class = ClientProfileSerializer
    queryset = User.objects.all()

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)

    
    def post(self, request):

        return 



class ClientPayAPI(generics.GenericAPIView):

    serializer_class = ClientPaySerializer
    queryset = Purchase.objects.all()


    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)

    
    def post(self, request):

        return 


class ClientHistoryAPI(generics.GenericAPIView):

    serializer_class = ClientTradeSerializer
    queryset = Trade.objects.all()

    def get(self, request):


        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 


class ClientBinAPI(generics.GenericAPIView):

    serializer_class = ClientBinSerializer
    queryset = Purchase.objects.all()

    def get(self, request):


        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 

class ClientBuyAPI(generics.GenericAPIView): #

    serializer_class = ClientBuySerializer
    queryset = Purchase.objects.all()

    def get(self, request):


        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 



class TypeOfDeliveryAPI(generics.GenericAPIView):

    serializer_class = ClientDeliverySerializer
    queryset = TypeOfDelivery.objects.all()

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 