from database.models import PersonalData
from django.db.models import query
from django.http import HttpResponse
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
    def get(self, request):
        return Response(self.get_serializer(self.get_queryset(), many = True).data)

    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data or 'first_name' not in request.data or 'last_name' not in request.data:
            return Response({'status':'error', 'message':'no args', 'user':request.data['username'], 'pass':request.data['password']}, status= 400)
        #user = {'username':request.data['username'], 'password':request.data['password'], 'email':request.data['email']}
        #createUser = serializers.UserSerializer(data = user)
        createUser = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'], is_active = True)
        createUser.save()
        userData = PersonalData()
        newUser = createUser.save()
        return Response(self.get_serializer(newUser, many = False).data)




class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)