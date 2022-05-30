from django.contrib.auth.models import Group
from rest_framework import serializers
from api.models import User, Customer, Data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'status', 'auth']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name']

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['customer_id', 'name', 'phone', 'email']
