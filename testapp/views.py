from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee, Users
from testapp.serializers import EmployeeSerializer, UsersSerializer

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UsersCRUDCBV(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer