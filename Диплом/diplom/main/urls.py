from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserAPI.as_view()),
    path('main/', views.main),
    path('hello/', views.HelloView.as_view())
    

]