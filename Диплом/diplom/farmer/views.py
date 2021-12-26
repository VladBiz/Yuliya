from rest_framework.response import Response
from .serializers import *
from django.http import HttpResponse
from rest_framework import generics

# class ProductListAPI(generics.GenericAPIView):

#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

#     def get(self, request):
#         return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


class FarmerProfileAPI(generics.GenericAPIView): 

    serializer_class = FarmerProfileSerializer
    queryset = User.objects.all()

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)

    
    def post(self, request):

        return 

###

class FarmerPayAPI(generics.GenericAPIView): # Нужно сделать вывод только текущего

    serializer_class = FermerPaySerializer
    queryset = PersonalData.objects.all()


    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 

##

class FarmerHistoryAPI(generics.GenericAPIView):

    serializer_class = FarmerHistorySerializer
    queryset = Trade.objects.all()

    def get(self, request):


        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 
 
##

class StorageAPI(generics.GenericAPIView):

    serializer_class = StorageSerializer
    queryset = Storage.objects.all()

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 


##

class StorageEditAPI(generics.GenericAPIView): # Нужно узнать, нужен ли отдельный сериалайзер

    serializer_class = StorageSerializer
    queryset = Storage.objects.all()

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 
        


class ProductListAPI(generics.GenericAPIView):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 


##



class ProductAddAPI(generics.GenericAPIView):

    serializer_class = ProductAddSerializer
    queryset = Product.objects.all()

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 


##



class ProductEditAPI(generics.GenericAPIView):

    serializer_class = ProductEditSerializer
    queryset = Product.objects.all()

    def get(self, request):

        return Response(self.get_serializer(self.get_queryset(), many = True).data, status = 200)


    def post(self, request):

        return 


