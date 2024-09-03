from django.contrib import admin
from .models import Division
from .models import Employee

# Register your models here.
admin.site.register(Division)
admin.site.register(Employee)