from django.contrib.auth.models import Group
from api.models import Customer, Data, User
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, CustomerSerializer, DataSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    permission_classes = [IsAuthenticated]

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    permission_classes = [IsAuthenticated]


def changePasswordFormView(request):
    return HttpResponse("Bıldırcın hurmalar sabriyi tırmalar")
