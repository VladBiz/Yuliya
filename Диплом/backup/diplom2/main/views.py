from database.models import PersonalData
from database.models import Farmer
from database.models import Client
from .forms import NameForm
from django.http import HttpResponseRedirect
from django.db.models import query
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django.contrib.auth import get_user_model
# Uses= get_user_model()
from django.contrib.auth.models import User
from database import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



class UserApi(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    # serializers.UserSerializer(queryset.objects.all())
    def get(self, request):
        return Response(self.get_serializer(self.get_queryset(), many = True).data)

    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'status':'error', 'message':'no args', 'user':request.data['username'], 'pass':request.data['password']}, status= 400)
        createUser = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'], is_active = True)
        
        userData = PersonalData.objects.create(user = createUser, isFarmer = request.data['is_farmer'], phoneNumber = request.data['phone_number'], money = 0)
        
        try:
            user = User.objects.get(username = request.data['username'])
        except:
            return Response({'user':'user not found'}, status= 401)
        result = self.get_serializer(user).data
        result2 = serializers.PersonalDataSerializer(userData).data
        result.update(result2)
        if request.data['is_farmer'] == True:
            farmer = Farmer(personalData = userData)
            farmer.save()
        elif request.data['is_farmer'] == False:
            print(request.data)
            client = Client(personalData = userData, addres = request.data['addres'])
            client.save()
        
        createUser.save()
        userData.save()
        #return Response(self.get_serializer(result, many = False).data)
        #return Response(result)
        return render(request, 'welcome.html')
        #return redirect('http://127.0.0.1:8000/')





class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


def get_name(request):
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = NameForm(request.POST)
    #     # check whether it's valid:
    #     print('1')
    #     print(form.data)
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         #a = UserApi()
    #         #a.post(form)
    #         print('2')
    #         # if 'is_farmer' not in form.data:
    #         #     user = form.data
    #         #     s = {'if_farmer':'False'}
    #         #     user.update(s)
    #         #     print(user, "user")
    #         print(form.data)
    #         # redirect to a new URL:
    #         #UserApi.post(form)
    #         return HttpResponseRedirect('/')
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     print('3')
    #     form = NameForm()


    return render(request, 'main.html')#, {'form': form})