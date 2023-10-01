from rest_framework import serializers
from django_apiapp.models import products,Order,OrderItem,Comment,Favorite,User,Category
class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = '__all__'
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = '__all__'
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'