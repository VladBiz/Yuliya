from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserApi.as_view()),
    path('main/', views.get_name),
    path('hello/', views.HelloView.as_view())
    

]