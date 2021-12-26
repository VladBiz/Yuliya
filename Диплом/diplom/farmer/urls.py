from django.urls import path

from . import views

urlpatterns = [
    #path('', views.client),
    #path('menu/', views.ProductListAPI.as_view()),
    path('profile/', views.FarmerProfileAPI.as_view()),
    path('profile/pay/', views.FarmerPayAPI.as_view()),
    path('history/', views.FarmerHistoryAPI.as_view()),
    path('storages/', views.StorageAPI.as_view()),
    path('storages/edit/', views.StorageEditAPI.as_view()),
    path('products/', views.ProductListAPI.as_view()),
    path('products/add/', views.ProductAddAPI.as_view()),
    path('products/edit/', views.ProductEditAPI.as_view())

]