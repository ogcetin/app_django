from django.contrib.auth.models import Group
from requests import Request, Response
from api.models import Activity, Customer, Data, User
from rest_framework import viewsets
from api.serializers import ActivitySerializer, UserSerializer, GroupSerializer, CustomerSerializer, DataSerializer
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

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    permission_classes = [IsAuthenticated]

def activityListByDataIDView(request, data_id):
    activity_list = Activity.objects.get(data_id=data_id)
    serializer = ActivitySerializer(activity_list)
    return Response(serializer.data)

def changePasswordFormView(request):
    return HttpResponse("Bıldırcın hurmalar sabriyi tırmalar")
