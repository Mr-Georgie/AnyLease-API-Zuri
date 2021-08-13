from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer, UserSerializer, RegistrationSerializer
from rest_framework import permissions 
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import serializers
from rest_framework import parsers
import uuid

# Create your views here.

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        
       # serializer.is_valid(raise_exception = True)
       # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                 "Requestid": str(uuid.uuid4()),
                 "Message": "User created successfully",

                 "User": serializer.data}, status=status.HTTP_201_CREATED 
            )
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)






class ListCategory(generics.ListCreateAPIView):
    permisssion_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permisssion_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProduct(generics.ListCreateAPIView):
    permisssion_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permisssion_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListUser(generics.ListCreateAPIView):
    permisssion_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permisssion_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
