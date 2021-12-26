from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserApi.as_view()),
    path('hello/', views.HelloView.as_view())

]