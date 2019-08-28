from testapp.models import Employee, Users
from rest_framework.serializers import ModelSerializer


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
