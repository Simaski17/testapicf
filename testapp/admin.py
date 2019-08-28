from django.contrib import admin
from testapp.models import Employee
from testapp.models import Users


# Register your models here.
class EmpleyeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']

class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'username', 'password','image_profile','email','telefono','rut','accepterms']



admin.site.register(Employee, EmpleyeeAdmin)
admin.site.register(Users, UsersAdmin)
