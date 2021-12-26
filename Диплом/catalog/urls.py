from django.urls import include, path
from .views import *

urlpatterns = [
    path('api/product/', ProductAPI.as_view()),
    path('api/category/', CategoryAPI.as_view()),
    path('api/brand/', BrandAPI.as_view()),
    path('api/project/', ProjectAPI.as_view()),
]
