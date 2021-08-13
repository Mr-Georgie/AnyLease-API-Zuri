from django.db.models import fields
from rest_framework import serializers
from .models import Category, Product
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=5)
    username = serializers.CharField(max_length =50, min_length=5)
    password = serializers.CharField(max_length=150, write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)






class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'title'
    
    ]
        model = Category

class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
    class Meta:
        fields = [
            'name',
            'category',
            'description',
            'price',
            'quantity',
            'image_upload',
            'created_by',
            'status',
            'date_created',
    ]
        model = Product

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'products'
            ]
