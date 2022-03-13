from django.shortcuts import render
from user_app.models import *
from rest_framework.generics import *
from user_app.serializers import AccountSerial
# Create your views here.


class UserCreateList(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerial

class UserGetDeleteUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerial