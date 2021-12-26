from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import *
from django.db.models import Prefetch

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

class ProductAPI(generics.GenericAPIView):
    serializer_class=ProductSerializer
    queryset = Product.objects.all()

    def get(self, request):
        print(request.META)
        if 'category' in request.GET:
            name = Category.objects.filter(name=request.GET['category'])
            if name.count() == 1:
                temp = CategorySerializer(Category.objects.get(name=name[0])).data
                return Response(self.get_serializer(self.get_queryset().filter(category = name[0]), many=True).data, status=200)
            else:
                return Response({'status': 'error', 'message': 'category does not exists'}, status=404)
        if 'brand' in request.GET:
            brand = Brand.objects.filter(brandName=request.GET['brand'])
            if brand.count() == 1:
                return Response(self.get_serializer(self.get_queryset().filter(brand=brand[0]), many=True).data, status=200)
            else:
                return Response({'status': 'error', 'message': 'brand does not exists'}, status=404)
        return Response(self.get_serializer(self.get_queryset(), many=True).data, status=200)

class CategoryAPI(generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
        except Exception as e:
            print(e)
        return Response(serializer.data, status=200)

class BrandAPI(generics.GenericAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def get(self, request):
        return Response(self.get_serializer(self.get_queryset(), many=True).data, status=200)

class ProjectAPI(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request):
        return Response(self.get_serializer(self.get_queryset(), many=True).data, status=200)