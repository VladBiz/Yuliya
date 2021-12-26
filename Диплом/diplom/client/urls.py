from django.urls import path

from . import views

urlpatterns = [
    #path('', views.),
    path('menu/', views.ProductListAPI.as_view()),
    path('profile/', views.ClientProfileAPI.as_view()),
    path('profile/pay/', views.ClientPayAPI.as_view()),
    path('history/', views.ClientHistoryAPI.as_view()),
    path('bin/', views.ClientBinAPI.as_view()),
    path('buy/', views.ClientBuyAPI.as_view()),
    path('buy/delivery', views.TypeOfDeliveryAPI.as_view())

]